# Flight Analysis

Flight simulations, analysis of Prometheus' flight data

- **Alignment of Sim Data with Experimental Data:** 
  - About 1000 ft off around motor burnout.
  - try taking data to motor burnout and simulating remainder of flight to see congruence with experimental data
    - just run sim as is and set deployment angle to 0 for the entire flight
  - this isn't a real problem; it's caused by the delay in barometric sensor data. The rocket should have been just about where the sim says it would be at motor burnout, it's just a delay on the order of 0.8s in the pressure in the rocket getting to equilibrate with the pressure outside the rocket that causes the discrepancy.
  - Note that if wanting to simulate airbrakes using Prometheus experimental data as the data till burnout, the flight data has no vertical vs horizontal velocity data, so would need to use the speed and change of height with time to separate them out. Possibly use the velocity not being 0/the acceleration not being -g at apogee to help determine the horizontal motion then too. Not a priority at all.

## Status of the TODOs in this directory

**Superseded; not to be worked on here.** These scripts were kept current
through SAC 2024 (commits `650ef27`, `7dff387`) and are frozen as a record
of that work. The simulator itself lives in
[werocketry/RocketFlightSim](https://github.com/werocketry/RocketFlightSim),
and the 2025 lookup-table work for Hyperion II continued in
[werocketry/airbrakes-lookuptable-generator](https://github.com/werocketry/airbrakes-lookuptable-generator).
Anything still worth doing belongs in one of those repositories. The
`TODO` comments are left in the code unchanged as part of the record.

| Location (at `99d8a5c`) | TODO | Disposition |
| --- | --- | --- |
| `controller_flight_simulator.py:35` | Ways to improve efficiency | Superseded |
| `controller_flight_simulator.py:88` | Model closing the airbrakes at the end of the controller's simulation | Superseded |
| `controller_flight_simulator.py:123` | Choose the timestep properly, possibly dynamically | Superseded |
| `sensitivity_analysis.py:7` | Move the Monte Carlo mechanics to RocketFlightSim | Superseded: belongs in RocketFlightSim |
| `sensitivity_analysis.py:21`, `:33` | Richer output from the linear and Gaussian analyses | Superseded |
| `stopping_power_analysis.py:4`, `:12` | Other drag coefficients; uncontrolled conditions or worst case | Superseded |
| `configs.py:272-274` | Confirm Prometheus reference area, tube OD and mass | Superseded (Prometheus inputs, 2022 flight) |
| `configs.py:282` | Read the motor from RocketFlightSim instead of defining it here | Superseded: belongs in RocketFlightSim |
| `configs.py:313`, `:323` | SAC 2024 launch time and weather; wind heading has no effect in the sim | Superseded |
| `configs.py:330-332` | Confirm flap Cd and the deployment and retraction rates after loaded testing | Superseded; the loaded-test stall is tracked in [#16](https://github.com/burnoutlabs/airbrakes-SR/issues/16) |
| `visualizations_cleaned.ipynb`, cell 6 | Non-simulation dataset path needs updating | Superseded |

The barometric lag explanation in the notes above has been checked against
the flight logs in
[`Prometheus_flight_data/baro_lag_check.md`](Prometheus_flight_data/baro_lag_check.md).
The barometer does read about 360 m (1180 ft) low at burnout on the 2022
flight, but the logs do not fit a 0.8 s delay; the mechanism is unresolved.
