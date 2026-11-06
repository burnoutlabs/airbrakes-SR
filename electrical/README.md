# Electrical

Schematics, PCB layout and supporting analysis for the DMATS electronics.
None of this hardware flew; see [docs/status.md](../docs/status.md).

## Contents

| Path | What it is | State |
| --- | --- | --- |
| [`dmats_hw_v1_0/`](dmats_hw_v1_0/) | KiCad project for the **functional prototype**: Portenta H7, Nicla Sense ME, L298N driver module, L7805 regulator, gearmotor with encoder, buzzers, switches, 3S 18650 pack. | Schematic only. The prototype was hand-wired from modules ([docs/plan_prod.md](../docs/plan_prod.md)). The PCB file holds 2 footprints and no tracks. `A4957_driver.kicad_sch` and `portenta_h7.kicad_sch` sit in the folder but the top sheet does not reference them. |
| [`dmats_hw_v2_0/`](dmats_hw_v2_0/) | KiCad project for the **production prototype**: the Allegro A4957 discrete MOSFET motor driver (sheet `A4957_driver.kicad_sch`) replaces the L298N, with Hall-effect end stops, on a circular PCB. Project symbol and footprint library in `DMATS_capstone.kicad_sym` and `DMATS_capstone/`. | PCB laid out: 37 footprints, 205 track segments, 27 vias. No fabrication outputs; never manufactured or tested ([#15](https://github.com/burnoutlabs/airbrakes-SR/issues/15)). |
| [`power_analysis/`](power_analysis/README.md) | Power budget and battery cell selection. | Complete as written for the report. |
| [`motor_analysis/servo_analysis.ipynb`](motor_analysis/servo_analysis.ipynb) | An early study of a servo motor (MG996R) as the actuator. | Superseded: the design moved to a brushed DC gearmotor. The final load and torque analysis is in [`mechanical/load_analysis.ipynb`](../mechanical/load_analysis.ipynb). |
| `datasheets/` (in each project) | A4957 and A1324/5/6 datasheets, one marked up. | Reference. |

KiCad backup zips (`*-backups/`), autosaves (`_autosave-*`), caches
(`fp-info-cache`) and per-user `.kicad_prl` files are editor leftovers, not
design files. Any such files in the project folders are slated for removal
([#5](https://github.com/burnoutlabs/airbrakes-SR/issues/5)); once that
cleanup lands, `electrical/BACKUPS.md` records what they held.

## Opening the projects

Use **KiCad 7 or later**. The `.kicad_pcb` files are format `20221018` and
the `.kicad_sch` files `20230121`, both KiCad 7. One sheet,
`dmats_hw_v1_0/A4957_driver.kicad_sch`, is in the older `20211123` (KiCad 6)
format; KiCad 7 opens it and converts it on save.

Open `dmats_hw_v1_0/dmats_hw_v1_0.kicad_pro` or
`dmats_hw_v2_0/dmats_hw_v2_0.kicad_pro`. Each project's `sym-lib-table`
and `fp-lib-table` point at a library inside its own folder (`ABX00042` in
v1_0, `DMATS_capstone` in v2_0). KiCad also embeds the symbols used in each
schematic, so the sheets open without the libraries; the v1_0 schematic's
`custom:` symbols have no library table entry at all.

## Future Work

### Electrical Hardware Revision

Future work will also focus on the revision of the electrical hardware,
namely the manufacture and testing of the printed circuit board for the
presented Production Prototype version of the electrical system.

### Flight Computer Development

As the development of a complete flight computer is a large undertaking,
future development is required to satisfy this component. The team will
work closely with the sponsor to ensure that our development efforts run
parallel to their future development of SRAD flight computers.

### Software Integration

The core software components of the system presented complete herein
still require careful development and planning for their integration
into a single standalone program capable of running this entire complex
system.

### Model-Based Control for Drag Modulation

The current mechanism controller uses a look up table calculated offline
to determine the motor action required to produce the desired drag.
Future work will focus on the use of a Model Prediction Control
algorithm which uses an internal model of the rocket to predict the path
and actively mitigate deviations from the desired path in the presence
of external disturbances.
