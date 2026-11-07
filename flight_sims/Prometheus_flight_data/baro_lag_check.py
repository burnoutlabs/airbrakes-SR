# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Check the "0.8 s barometric lag" hypothesis against the AltOS flight logs.

flight_sims/README.md attributes the ~1000 ft sim-vs-flight gap around motor
burnout to the pressure inside the rocket lagging the outside pressure by about
0.8 s. This script compares, for each log in this directory:

  * h_baro: altitude from the logged pressure (ISA troposphere, relative to the
    median pad pressure before t = 0), and
  * h_acc: altitude from integrating the logged axial `acceleration` twice from
    launch (t = 0, v = 0, h = 0). AltOS zeroes this channel on the pad, so in
    near-vertical flight it is the vertical kinematic acceleration.

If the barometer lagged by tau, h_baro(t) would track h_acc(t - tau). Three
estimates of tau:

  1. peak-velocity lag: time of the peak of the barometric vertical velocity
     (a least-squares slope over a +/-0.25 s window) minus the time of the peak
     of the accelerometer-integrated velocity (= burnout);
  2. best shift: the tau in [-0.5, 2.0] s minimising the RMS of
     h_baro(t) - h_acc(t - tau) over launch + 0.5 s to burnout + 3 s;
  3. the altitude gap h_acc - h_baro at burnout, and the lag it would imply at
     the burnout velocity (gap / v_burnout).

Standard library only. Run from the repository root:

    uv run flight_sims/Prometheus_flight_data/baro_lag_check.py
    # or: python3 flight_sims/Prometheus_flight_data/baro_lag_check.py
"""

from __future__ import annotations

import csv
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGS = sorted(HERE.glob("*-serial-*-flight-*.csv"))

P0_PA = 101325.0
FT_PER_M = 1 / 0.3048
SLOPE_HALF_WINDOW_S = 0.25
FIT_START_S = 0.5
FIT_AFTER_BURNOUT_S = 3.0
LAG_HYPOTHESIS_S = 0.8
TIMELINE_S = (1, 2, 3, 4, 5, 6, 8, 10, 15)


def isa_alt_m(p_pa: float) -> float:
    t0, lapse, g0, r = 288.15, 0.0065, 9.80665, 287.05287
    return (t0 / lapse) * (1.0 - (p_pa / P0_PA) ** (r * lapse / g0))


def load(path: Path) -> tuple[list[float], list[float], list[float], list[float]]:
    """Return (t, accel, pressure, logged height), duplicate timestamps averaged."""
    with open(path, newline="") as fh:
        rows = csv.reader(fh)
        header = [h.strip().lstrip("#") for h in next(rows)]
        it, ia, ip, ih = (header.index(k) for k in ("time", "acceleration", "pressure", "height"))
        groups: dict[float, list[tuple[float, float, float]]] = {}
        for r in rows:
            if len(r) <= max(it, ia, ip, ih):
                continue
            try:
                t, a, p, h = float(r[it]), float(r[ia]), float(r[ip]), float(r[ih])
            except ValueError:
                continue
            groups.setdefault(round(t, 3), []).append((a, p, h))
    t = sorted(groups)
    mean = lambda vals, k: statistics.fmean(v[k] for v in vals)  # noqa: E731
    return (t, [mean(groups[x], 0) for x in t], [mean(groups[x], 1) for x in t], [mean(groups[x], 2) for x in t])


def integrate(t: list[float], a: list[float]) -> tuple[list[float], list[float]]:
    """Trapezoidal v and h from launch (t = 0); zero before launch."""
    v, h = [0.0] * len(t), [0.0] * len(t)
    for i in range(1, len(t)):
        if t[i] <= 0:
            continue
        dt = t[i] - max(t[i - 1], 0.0)
        a_prev = a[i - 1] if t[i - 1] >= 0 else a[i]
        v[i] = v[i - 1] + 0.5 * (a_prev + a[i]) * dt
        h[i] = h[i - 1] + 0.5 * (v[i - 1] + v[i]) * dt
    return v, h


def slope(t: list[float], y: list[float], i: int, half: float) -> float:
    idx = [j for j in range(len(t)) if abs(t[j] - t[i]) <= half]
    tm = statistics.fmean(t[j] for j in idx)
    ym = statistics.fmean(y[j] for j in idx)
    den = sum((t[j] - tm) ** 2 for j in idx)
    return sum((t[j] - tm) * (y[j] - ym) for j in idx) / den


def interp(t: list[float], y: list[float], x: float) -> float:
    if x <= t[0]:
        return y[0]
    lo, hi = 0, len(t) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if t[mid] <= x:
            lo = mid
        else:
            hi = mid
    f = (x - t[lo]) / (t[hi] - t[lo])
    return y[lo] + f * (y[hi] - y[lo])


def analyse(path: Path) -> dict:
    t, a, p, h_logged = load(path)
    p_pad = statistics.median(pi for ti, pi in zip(t, p) if ti < 0)
    z_pad = isa_alt_m(p_pad)
    h_baro = [isa_alt_m(pi) - z_pad for pi in p]
    v_acc, h_acc = integrate(t, a)

    # Restrict to the powered and early coast phase (before apogee).
    i_apo = max(range(len(t)), key=lambda i: h_baro[i])
    i_bo = max(range(i_apo), key=lambda i: v_acc[i])  # accel-integrated peak velocity
    t_bo = t[i_bo]
    win = [i for i in range(len(t)) if 0 <= t[i] <= t_bo + FIT_AFTER_BURNOUT_S]
    v_baro = {i: slope(t, h_baro, i, SLOPE_HALF_WINDOW_S) for i in win}
    i_vb = max(v_baro, key=v_baro.get)

    fit = [i for i in win if t[i] >= FIT_START_S]
    best = None
    for k in range(-50, 201):
        tau = k / 100
        rms = (statistics.fmean((h_baro[i] - interp(t, h_acc, t[i] - tau)) ** 2 for i in fit)) ** 0.5
        if best is None or rms < best[1]:
            best = (tau, rms)
    rms0 = (statistics.fmean((h_baro[i] - h_acc[i]) ** 2 for i in fit)) ** 0.5
    rms08 = (statistics.fmean((h_baro[i] - interp(t, h_acc, t[i] - LAG_HYPOTHESIS_S)) ** 2 for i in fit)) ** 0.5

    gap = h_acc[i_bo] - h_baro[i_bo]
    return {
        "log": path.name,
        "height_vs_isa_max_abs_m": max(abs(x - y) for x, y in zip(h_logged, h_baro)),
        "t_burnout_s": t_bo,
        "v_burnout_acc_mps": v_acc[i_bo],
        "t_peak_v_baro_s": t[i_vb],
        "v_peak_baro_mps": v_baro[i_vb],
        "lag_peak_velocity_s": t[i_vb] - t_bo,
        "lag_best_shift_s": best[0],
        "rms_at_best_m": best[1],
        "rms_at_0_m": rms0,
        "rms_at_0p8_m": rms08,
        "h_acc_burnout_m": h_acc[i_bo],
        "h_baro_burnout_m": h_baro[i_bo],
        "gap_burnout_m": gap,
        "lag_implied_by_gap_s": gap / v_acc[i_bo],
        "gap_if_0p8_lag_m": h_acc[i_bo] - interp(t, h_acc, t_bo - LAG_HYPOTHESIS_S),
        "apogee_baro_m": h_baro[i_apo],
        "apogee_acc_m": max(h_acc[: i_apo + 1]),
        "timeline": [
            (x, v_acc[i], slope(t, h_baro, i, SLOPE_HALF_WINDOW_S), h_acc[i] - h_baro[i],
             h_acc[i] - interp(t, h_acc, x - LAG_HYPOTHESIS_S))
            for x in TIMELINE_S
            for i in [min(range(len(t)), key=lambda j: abs(t[j] - x))]
        ],
    }


def main() -> int:
    if not LOGS:
        print(f"no logs found in {HERE}", file=sys.stderr)
        return 1
    for path in LOGS:
        r = analyse(path)
        print(f"== {r['log']}")
        print(f"  logged height vs ISA(pressure), max |diff|: {r['height_vs_isa_max_abs_m']:.2f} m")
        print(f"  burnout (peak accel-integrated velocity):  t = {r['t_burnout_s']:.2f} s, v = {r['v_burnout_acc_mps']:.1f} m/s")
        print(f"  peak barometric velocity:                  t = {r['t_peak_v_baro_s']:.2f} s, v = {r['v_peak_baro_mps']:.1f} m/s")
        print(f"  [1] lag from peak velocity:                {r['lag_peak_velocity_s']:+.2f} s")
        print(f"  [2] best-fit shift, h_baro(t) ~ h_acc(t - tau): tau = {r['lag_best_shift_s']:+.2f} s "
              f"(RMS {r['rms_at_best_m']:.1f} m; at 0 s {r['rms_at_0_m']:.1f} m; at 0.8 s {r['rms_at_0p8_m']:.1f} m)")
        print(f"  [3] at burnout: h_acc {r['h_acc_burnout_m']:.1f} m, h_baro {r['h_baro_burnout_m']:.1f} m, "
              f"gap {r['gap_burnout_m']:+.1f} m ({r['gap_burnout_m'] * FT_PER_M:+.0f} ft) -> implied lag {r['lag_implied_by_gap_s']:+.2f} s")
        print(f"      a 0.8 s lag would give a gap of {r['gap_if_0p8_lag_m']:.1f} m ({r['gap_if_0p8_lag_m'] * FT_PER_M:.0f} ft)")
        print(f"  apogee: baro {r['apogee_baro_m']:.1f} m, accel-integrated {r['apogee_acc_m']:.1f} m")
        print("  timeline:   t   v_acc  v_baro   gap h_acc-h_baro   gap a 0.8 s lag predicts")
        for x, va, vb, gap, pred in r["timeline"]:
            print(f"           {x:>3} s {va:6.1f} {vb:7.1f} {gap:9.1f} m {pred:20.1f} m")
    return 0


if __name__ == "__main__":
    sys.exit(main())
