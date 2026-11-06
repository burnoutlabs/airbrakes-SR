# software-controls

Drag Modulation Apogee Targeting System (DMATS)

Bench-test Arduino sketches for the airbrakes controller, plus helper
scripts. There is no flight software here: no flight state machine, no
lookup-table use, no end-stop handling and no fail-safe. See
[docs/status.md](../docs/status.md).

None of these sketches has been compiled as part of this documentation;
the notes on building them come from reading the source.

## Sketches (`src/`)

| Sketch | Board | What it does |
| --- | --- | --- |
| [`flight_comp_main/flight_comp_main.ino`](src/flight_comp_main/flight_comp_main.ino) | Portenta H7 (host) | PID position control of the gearmotor through DCMotorServo, tuned over the serial monitor with the commands `KP=`, `KI=`, `KD=`, `MOVE=` and `MAXPWM=`. Reads the Nicla Sense ME over ESLOV and runs the AltitudeEstimation filter; its print block is gated by `printFlag`, which is initialised `false` and never set `true`. Includes [`altitude_eqn/altitude_eqn.h`](src/flight_comp_main/altitude_eqn/altitude_eqn.h), a barometric pressure-altitude helper. |
| [`dmat_comain/dmat_comain.ino`](src/dmat_comain/dmat_comain.ino) | Portenta H7 | Byte-identical to `flight_comp_main.ino` (`cmp` reports no difference). It includes `altitude_eqn/altitude_eqn.h`, which exists only under `flight_comp_main/`, so it will not find that header as laid out. |
| [`sense_app/sense_app.ino`](src/sense_app/sense_app.ino) | Nicla Sense ME (client) | The manufacturer's unaltered example that makes the Nicla act as a client to an external host over ESLOV or BLE. |

## Scripts (`scripts/`)

| Script | What it does |
| --- | --- |
| [`sensor_std_devs/std_devs.ino`](scripts/sensor_std_devs/std_devs.ino) | Portenta H7 sketch that samples the Nicla's accelerometer, gyroscope and barometer and prints their standard deviations, the noise inputs to the altitude estimator. |
| [`data_parser/`](scripts/data_parser/) | Python plotting scripts for flight, telemetry and bench-test files from the HPR flight computer, written by SparkyVT (`@author: Sparky`). They import `win32gui` and `win32con`, so they run on Windows only. See [`scripts/README.md`](scripts/README.md). |

## External libraries

None is vendored or pinned. Install them with the Arduino library manager
or from source:

| Include | Library |
| --- | --- |
| `Arduino_BHY2Host.h` (host sketches), `Arduino_BHY2.h` (`sense_app`) | Arduino BHY2Host / Arduino BHY2, for the Nicla Sense ME |
| `altitude.h` | [juangallostra/AltitudeEstimation](https://github.com/juangallostra/AltitudeEstimation) |
| `Encoder.h` | [PaulStoffregen/Encoder](https://github.com/PaulStoffregen/Encoder) |
| `PID_v1.h` | [br3ttb/Arduino-PID-Library](https://github.com/br3ttb/Arduino-PID-Library) |
| `DCMotorServo.h` | [feastorg/dcmotorservo](https://github.com/feastorg/dcmotorservo) |

The capstone repository carried DCMotorServo as a git submodule; this
repository dropped the submodule when it was split out (commit `2a644e5`).
