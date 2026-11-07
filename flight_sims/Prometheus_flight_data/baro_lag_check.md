# Is the barometer 0.8 s late at burnout?

`flight_sims/README.md` explains the roughly 1000 ft gap between the simulation
and the Prometheus flight data near motor burnout as a barometric lag: the
pressure inside the rocket takes "on the order of 0.8 s" to equalise with the
outside, so the logged altitude trails the real one. This note tests that
against the logs in this directory.

**Result: the gap is real, but a 0.8 s delay does not explain it.** At burnout
on the 2022 Prometheus flight, the barometric altitude is about 360 m (about
1180 ft) below the altitude from the accelerometer. Two independent loggers on
that flight agree. The way the gap opens and closes does not fit a time delay of
0.8 s or any other value. The mechanism is not identified here.

## Method

[`baro_lag_check.py`](baro_lag_check.py) uses the standard library only. From
the repository root, run either
`uv run flight_sims/Prometheus_flight_data/baro_lag_check.py` or `python3` on
the same path.

For each AltOS log it compares two altitudes:

- **Barometric altitude**: the logged `pressure` converted with the ISA
  troposphere formula, relative to the median pad pressure before t = 0. It
  matches the logger's own `height` column to within 0.3 m on all three logs.
- **Accelerometer altitude**: the logged axial `acceleration` integrated twice
  from launch (t = 0, v = 0). AltOS zeroes this channel on the pad, so for
  near-vertical flight it is the vertical acceleration. Duplicated timestamps
  are averaged.

If the barometer were simply late by τ, barometric altitude at time t would
equal accelerometer altitude at t − τ. The script estimates τ three ways:

1. the time between the peak accelerometer velocity (burnout) and the peak
   barometric velocity (a least-squares slope over ±0.25 s);
2. the shift that best fits barometric altitude to the accelerometer altitude
   from 0.5 s to 3 s after burnout;
3. the altitude gap at burnout, divided by the burnout velocity.

It also prints both velocities and the gap at fixed times, next to the gap a
0.8 s delay would produce.

## Results

Output of the command above (rc = 0), condensed:

| Log | Burnout t, v (accel) | Peak baro velocity | τ from peaks [1] | Best-fit τ [2] | Gap at burnout | τ from gap [3] |
| --- | --- | --- | --- | --- | --- | --- |
| 2022-06-24 TeleMetrum 5115 | 4.76 s, 315.5 m/s | 373.4 m/s at 4.97 s | +0.21 s | +1.07 s | +362.5 m (+1189 ft) | +1.15 s |
| 2022-06-24 TeleMega 6583 | 4.69 s, 316.6 m/s | 370.6 m/s at 4.90 s | +0.21 s | +1.05 s | +358.5 m (+1176 ft) | +1.13 s |
| 2024-06-21 TeleMega 6583 | 2.92 s, 267.9 m/s | 258.5 m/s at 3.78 s | +0.86 s | +0.12 s | +13.7 m (+45 ft) | +0.05 s |

The 2022 logs are the Prometheus flight. The 2024 log was added in `99d8a5c`
("addition of Hyperion flight data") and `data_processing.py` reads it as
`telemega_Hyperion`. It is a different flight, very likely a different airframe,
and is shown here for contrast only.

The 2022 TeleMega, over time. The TeleMetrum's velocities are within 13 m/s
of these and its gaps within 7 m, up to 6 s:

| t | v accel | v baro | gap (accel − baro) | gap from a 0.8 s delay |
| --- | --- | --- | --- | --- |
| 1 s | 79.1 | 43.6 | 10.5 m | 37.8 m |
| 2 s | 159.6 | 73.6 | 77.9 m | 102.2 m |
| 3 s | 232.1 | 116.6 | 177.8 m | 163.3 m |
| 4 s | 292.4 | 170.3 | 297.6 m | 215.8 m |
| 5 s | 310.1 | 358.0 | 337.8 m | 250.4 m |
| 6 s | 286.5 | 310.9 | 308.8 m | 236.5 m |
| 10 s | 212.5 | 218.9 | 238.0 m | 175.3 m |

## Reading the numbers

- **The gap is real and about the size the README describes.** On the 2022
  flight both loggers put the barometer about 360 m (1180 ft) behind the
  accelerometer at burnout. A barometric error of that size could account for
  the "about 1000 ft" gap between sim and data. The sim itself was not re-run
  here.
- **It does not behave like a delay:**
  - A delayed signal cannot rise faster than the real one. Yet after burnout the
    barometric velocity reaches 358–373 m/s against a peak of about 316 m/s from
    the accelerometer, only 0.2 s after burnout.
  - During boost the barometric velocity is roughly half the accelerometer's (for
    example 116.6 against 232.1 m/s at 3 s). That is lower than even a 1 s delay
    would give: the accelerometer velocity 1 s earlier was 159.6 m/s.
  - The three estimates of τ disagree: 0.2 s, 1.06 s and 1.14 s.
- **The pattern looks more like an altitude error that grows with speed**: the
  barometer reads too low while the rocket is fast, then recovers quickly as it
  slows after burnout. A rough estimate puts the 2022 burnout speed of about
  316 m/s near Mach 0.9–0.95, assuming a speed of sound of 335–345 m/s from the
  24 °C ground temperature that `data_processing.py` uses. That is the transonic
  range, where static-port pressure errors are known to occur. These logs
  cannot separate that from other causes, such as the port location or vent
  sizing, so it remains a candidate and is not demonstrated.
- **The 2024 log shows no boost-phase lag at all.** The gap is −7 to +17 m up to
  3 s at speeds up to about 268 m/s, and the best-fit shift is 0.12 s. Its
  0.86 s peak-velocity estimate comes from one short peak in the barometric
  velocity and is not borne out by the altitudes. Whatever affected the 2022 barometer did not show up on
  this flight.

## Limits

- **The accelerometer altitude assumes vertical flight and an accurate
  accelerometer scale.** Tilt and scale errors build up over time. That is why
  the comparison concentrates on boost and the first few seconds after burnout:
  the gap on the 2024 log grows steadily through coast, and both 2022
  accelerometer apogees overshoot the barometric ones by 87–202 m. Over the
  boost phase the two independent 2022 accelerometers agree to within about
  1% on velocity and within 8 m on altitude at burnout.
- **Burnout is taken as the peak accelerometer velocity, not from motor data.**
  AltOS's own boost-to-coast transition (4.96 s and 4.85 s in 2022) falls close
  to it.
- **No sensor or vent geometry was checked**, and no wind-tunnel or reference
  data were used.

## Conclusion

**Not supported as stated.** A barometer that is late by about 0.8 s does not
reproduce the 2022 logs: the barometric velocity overshoots the true peak, and
the delay estimates disagree with each other. The discrepancy at burnout is
real, at about 360 m (1180 ft) on Prometheus, so treating the sim mismatch as a
barometric artefact rather than a sim error remains plausible. The mechanism is
**inconclusive** from these logs; a speed-dependent pressure error fits better
than a delay. For the airbrakes, any barometric altitude near burnout at this
speed should not be trusted on its own. Fusing it with the IMU, as the bench
sketch does, needs to allow for an error of several hundred metres near
Mach 1, not just a fixed delay.
