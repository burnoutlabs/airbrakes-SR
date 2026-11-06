# Mechanical

CAD, analysis and strength-test data for the airbrakes mechanism: three
flaps driven by push rods from a nut on a central lead screw. A 3D-printed
prototype was built and load-tested; it never flew
([docs/status.md](../docs/status.md)).

## Contents

| Path | What it is | How to open |
| --- | --- | --- |
| [`CAD/airbrakes_CAD_V5_0_0/`](CAD/airbrakes_CAD_V5_0_0/) | The final three-flap design. Top assembly `Airbrake 3-Flap.SLDASM` with its parts (flaps, platforms, lead screw, push rods, hinges) and McMaster-Carr purchased parts (files named by part number). | SolidWorks. There is no STEP or other neutral export of this assembly in the repository. |
| [`CAD/battery_pack_scad/`](CAD/battery_pack_scad/) | Parametric 3S 18650 battery pack holder, with rendered images and STL exports. `README` holds a link to the nickel strip used. | OpenSCAD: open `battery_assem_x3.scad` or `battery_assem-x1.scad`; they `use` `18650_Holder.scad` and `battery_lib.scad`. |
| [`CAD/components-electrical-ardupro/`](CAD/components-electrical-ardupro/) | Third-party models of the electronics for fit checks: Nicla Sense ME and Portenta H7 (from GrabCAD, see each `attrib.txt`), Hall-effect switch assembly and L298N driver. | STEP/IGES/STL/OBJ in any CAD tool; the Hall-effect and L298N models are SolidWorks only. |
| [`mech_design/CF_forged_flaps/mould_V1/`](mech_design/CF_forged_flaps/mould_V1/) | `Mould Base.STEP` and `Mould Top.STEP`: compression mould for forged carbon-fibre flaps. That process was abandoned after the flaps failed (Design Day slide 19); the flaps were cut from woven carbon-fibre tube instead. | STEP, stored in Git LFS. If a checkout shows LFS pointer text (`version https://git-lfs.github.com/spec/v1`) instead of the model, the `.gitattributes` patterns do not yet match upper-case extensions ([#3](https://github.com/burnoutlabs/airbrakes-SR/issues/3)); run `git lfs pull` once they do. |
| [`mech_design/Lead Screw Cost Comparison.xlsx`](<mech_design/Lead Screw Cost Comparison.xlsx>) | Cost comparison of lead screw options (the design uses a 1/4-12 lead screw; see [docs/detailed_design.md](../docs/detailed_design.md), Off-the-Shelf Components). | Spreadsheet. |
| [`load_analysis.ipynb`](load_analysis.ipynb) | Static load analysis of the linkage, lead screw efficiency, and driving and holding torque. A note in the notebook says its hard-coded values are no longer current and that the live calculations moved into the flight simulator ([`flight_sims/`](../flight_sims/)). | Jupyter. |
| [`internal_loading_pics/`](internal_loading_pics/) | Linkage diagrams at 0°, 22° and 45° used by the notebook, and `load_analysis_statics.pdf`, a statics write-up of the linkage. | Images and PDF. |
| [`strength_testing/jan_23_2024_flaps_test/`](strength_testing/jan_23_2024_flaps_test/) | Flap load tests of a Blue Tube flap and a forged carbon-fibre flap: one spreadsheet each, plus photos (`.heic`) and videos (`.MOV`). | Spreadsheet; photos and videos. |
| [`strength_testing/mar_8_2024_compression_test/`](strength_testing/mar_8_2024_compression_test/) | Compression tests in Western's testing lab: the body tube with flap cutouts (`.1348`) and a small flap (`.1331`), plus photos and videos. The tube result is written up in [docs/prod_test.md](../docs/prod_test.md), Tube Crushing. | See below. |

## Reading the compression test exports

The `.1331` and `.1348` files are text exports from an Adelaide Testing
Machines controller: ISO-8859-1 encoded, CRLF line endings. The first 42
lines are numbered, comma-separated machine settings. After them comes a
fixed-width table with the columns `Point No.`, `Time (s)`, `Axial Pos.
(mm)`, `DC1 (N)` (load) and three unused channels. Compression shows as
negative load.

Peak load magnitude, from the `DC1` column:

| File | Points | Peak load |
| --- | --- | --- |
| `MAR0824 tube with cutouts.1348` | 43 | 2373.9 N |
| `MAR0824 small flap.1331` | 51 | 235.8 N |

To reproduce, keep the 7-field rows whose first field is an integer and
take the maximum absolute value of the fourth field.
