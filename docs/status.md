# Project Status

**DMATS (Drag Modulation Apogee Targeting System) never deployed in flight.**
It was planned for two rockets, Hyperion at the 2024 Spaceport America Cup
and Hyperion II in 2025, and did not fly as a working system on either.
The project is inactive.

Every statement below cites a path in this repository (at commit `99d8a5c`
unless another commit is named), a commit, a linked repository, or the
owner's statement of 2026-11-05.

## Why it never flew

| Year | Rocket | What happened | Source |
| --- | --- | --- | --- |
| 2024 | Hyperion (SAC 2024) | Finishing the airframe ran into the first days of launches at the competition, "which also led to the airbrakes and payload becoming non-functional". The same note says the last-minute airframe changes added weight and drag, which made the airbrakes unnecessary anyway. | [`flight_sims/configs.py`](../flight_sims/configs.py) line 263, commit `7dff387` (2024-06-22) |
| 2024 | Hyperion (SAC 2024) | The TeleMega log peaks at 2728 m AGL (about 8950 ft), short of the 10,000 ft target, so there was no excess apogee for airbrakes to remove. | [`flight_sims/Prometheus_flight_data/2024-06-21-serial-6583-flight-0004.csv`](../flight_sims/Prometheus_flight_data/2024-06-21-serial-6583-flight-0004.csv), commit `99d8a5c`: maximum of the `height` column is 2728.02 |
| 2025 | Hyperion II | The design summary lists airbrakes in the drogue chute bay, and a lookup table was generated for them (commits from 2025-08-07 to 2025-11-24). The airbrakes still did not deploy, because of time constraints and external factors in the wider rocket build. | [burnoutlabs/Hyperion-II `DSS.md`](https://github.com/burnoutlabs/Hyperion-II/blob/main/DSS.md); [werocketry/airbrakes-lookuptable-generator](https://github.com/werocketry/airbrakes-lookuptable-generator); owner statement, 2026-11-05 |

## State reached, by subsystem

| Subsystem | State reached | Evidence |
| --- | --- | --- |
| Mechanical | Three-flap lead-screw and push-rod design, modelled in SolidWorks. A 3D-printed prototype was assembled and held the maximum expected flap loads. | [`mechanical/CAD/airbrakes_CAD_V5_0_0/`](../mechanical/CAD/airbrakes_CAD_V5_0_0/); [`docs/prod_test.md`](prod_test.md), Loaded Testing |
| Airframe section | A body tube with flap cutouts failed at 2.37 kN in compression, against 11.16 kN for a tube without cutouts. The required load is 1547 N, a factor of safety of 1.53. | [`docs/prod_test.md`](prod_test.md), Tube Crushing; raw export [`mechanical/strength_testing/mar_8_2024_compression_test/MAR0824 tube with cutouts.1348`](<../mechanical/strength_testing/mar_8_2024_compression_test/MAR0824 tube with cutouts.1348>) (peak 2373.9 N) |
| Flaps | The forged carbon-fibre flaps failed. The design moved to flaps cut from woven carbon-fibre tube. | Design Day presentation, slide 19 ([PDF](<MME 4499 2023-2024 Group 13 Design Day Presentation.pdf>)); [`docs/detailed_design.md`](detailed_design.md), Carbon Fiber Parts |
| Actuation | A full stroke took 1.51 s unloaded. Under load the motor stalled at mid-stroke and could only drive the upper and lower ~30% of the lead screw. A larger motor was ordered; there is no record that it was tested. | [`docs/prod_test.md`](prod_test.md), Actuation Testing |
| Electrical, functional prototype | Hand-wired modules: Portenta H7 (ABX00042), Nicla Sense ME, L298N driver, 12 V gearmotor with encoder, Hall-effect end stops, 3S 18650 pack. | [`docs/plan_prod.md`](plan_prod.md), Electrical Prototype Development; [`docs/detailed_design.md`](detailed_design.md), Electrical Design |
| Electrical, production prototype | Schematic and PCB layout with the A4957 discrete MOSFET driver: 37 footprints, 205 track segments, 27 vias. No fabrication outputs. Never manufactured or tested. | [`electrical/dmats_hw_v2_0/`](../electrical/dmats_hw_v2_0/); [`electrical/README.md`](../electrical/README.md), Future Work |
| Electrical, `dmats_hw_v1_0` | Schematic of the functional prototype (L298N). Its PCB holds 2 footprints and no tracks. | [`electrical/dmats_hw_v1_0/`](../electrical/dmats_hw_v1_0/) |
| Software | Bench sketches only. `dmat_comain.ino` and `flight_comp_main.ino` are byte-identical: serial-command PID motor tuning (`KP=`, `KI=`, `KD=`, `MOVE=`, `MAXPWM=`) plus an altitude-estimator print block gated by `printFlag`, which is initialised `false` and never set `true`. There is no flight state machine, no lookup-table use, no end-stop handling and no fail-safe. | [`software/src/`](../software/src/); `cmp` of the two sketches reports no difference |
| Flight computer | Planned as a customised HPR-Rocket-Flight-Computer. The report says the core "still requires significant development and testing before flight". That code is not in this repository. | [`docs/detailed_design.md`](detailed_design.md), Flight Computer; [`docs/plan_prod.md`](plan_prod.md), Software Prototype Development |
| Simulations | Custom controller simulation, lookup-table and sensitivity scripts, kept current through SAC 2024. The 2025 lookup-table work continued in a separate repository. | [`flight_sims/`](../flight_sims/), commits `650ef27` and `7dff387`; [werocketry/airbrakes-lookuptable-generator](https://github.com/werocketry/airbrakes-lookuptable-generator) |

## Validation plan items

The Design Day validation plan (slide 18) lists three tests. None has a
result in this repository.

| Test | Planned | Outcome |
| --- | --- | --- |
| Algorithm testing on simulated data | Early April 2024 | No record that it ran |
| Integration with airframe (fit test) | Early to mid April 2024 | No record that it ran |
| Wind tunnel testing | Mid to late April 2024 | No record that it ran; slide 16 says it was delayed because the rocket exterior was not finished. See [#20](https://github.com/burnoutlabs/airbrakes-SR/issues/20). |
| Upsized motor | Ordered after the loaded test | No record that it ran |

## Open questions

These need the owner's answer and are not resolved here.

- Did the wind tunnel test ([`aero_cfd/wind_tunnel/wind_tunnel_plan.md`](../aero_cfd/wind_tunnel/wind_tunnel_plan.md)) ever happen? Tracked in [#20](https://github.com/burnoutlabs/airbrakes-SR/issues/20).
- Was the upsized motor ever tested? Tracked in [#16](https://github.com/burnoutlabs/airbrakes-SR/issues/16).
- Where is the Hyperion II airbrake hardware now?
