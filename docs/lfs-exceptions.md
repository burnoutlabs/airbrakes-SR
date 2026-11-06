# Git LFS exceptions

`.gitattributes` sends CAD files (STEP, STP, STL, SolidWorks, IGES, OBJ),
test photos and videos (MOV, HEIC) and archives (ZIP) to Git LFS, matching
their extensions case-insensitively. The patterns apply to files added or
changed **from now on**.

Files committed before the patterns covered them were **not** converted.
They stay ordinary Git blobs, so `git lfs fsck --pointers` reports them and
`git status` may list them as modified even though their contents equal the
committed version. Converting them forward (`git add --renormalize`) and
rewriting history (`git lfs migrate import`) were both deferred by the owner
on 2026-11-05. If either is done later, this list is the scope.

Listed at commit `99d8a5c`. Sizes are the committed blob sizes.

## Matching files stored as plain blobs (102 files, 377.3 MB)

### KiCad backup zips (38 files, 7.4 MB)

All `*.zip` under `electrical/dmats_hw_v1_0/dmats_hw_v1_0-backups/` and
`electrical/dmats_hw_v2_0/dmats_hw_v2_0-backups/`. They are removed by the
KiCad cleanup ([#5](https://github.com/burnoutlabs/airbrakes-SR/issues/5)),
after which they drop off this list.

### Other files (64 files, 369.9 MB)

| Size | Path |
| --- | --- |
| 41.4 MB | `electrical/dmats_hw_v1_0/external-components/ABX00042.zip` |
| 40.6 MB | `electrical/dmats_hw_v1_0/external-components/ABX00042/ABX00042.step` |
| 0.1 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/6338K563_Oil-Embedded Flanged Sleeve Bearing.SLDPRT` |
| 0.6 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/94622A215_Cadmium-Plated Steel Hex Head Screw.SLDPRT` |
| 0.6 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/94887A363_Low-Profile Binding Barrels and Screws.SLDPRT` |
| 1.0 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/95075A340_Plastic Externally Threaded Precision Acme Nut.SLDPRT` |
| 0.4 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/95082A641_Precision Acme Flange.SLDPRT` |
| 0.5 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/97763A431_18-8 Stainless Steel Button Head Hex Drive Screws.SLDPRT` |
| 16.5 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Airbrake 3-Flap.SLDASM` |
| 0.3 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Bottom Platform.SLDPRT` |
| 0.5 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Coupler tube.SLDPRT` |
| 0.2 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Flap Support.SLDPRT` |
| 0.1 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Flap.SLDPRT` |
| 4.1 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Lead Screw.SLDPRT` |
| 0.4 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Motor Platform.SLDPRT` |
| 0.1 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Platform Spacers.SLDPRT` |
| 0.1 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Push Rod - 3.SLDPRT` |
| 0.3 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Rivet Pressed.SLDPRT` |
| 0.5 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Rocket Shell - 3.SLDPRT` |
| 0.4 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Rod Nut.SLDPRT` |
| 0.3 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Shell Epoxy Platform - No Standoffs.SLDPRT` |
| 0.5 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Shell Epoxy Platform.SLDPRT` |
| 0.2 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Top Hinge.SLDPRT` |
| 0.5 MB | `mechanical/CAD/airbrakes_CAD_V5_0_0/Top-Bottom Platform.SLDPRT` |
| 0.1 MB | `mechanical/CAD/battery_pack_scad/stl/battery_assem-x1.stl` |
| 0.2 MB | `mechanical/CAD/battery_pack_scad/stl/battery_assem_x3.stl` |
| 0.7 MB | `mechanical/CAD/components-electrical-ardupro/arduino-nicla-sense-me/Nicla Sense v4.stl` |
| 3.0 MB | `mechanical/CAD/components-electrical-ardupro/arduino-nicla-sense-me/Nicla Sense.iges` |
| 1.7 MB | `mechanical/CAD/components-electrical-ardupro/arduino-nicla-sense-me/Nicla Sense.obj` |
| 1.9 MB | `mechanical/CAD/components-electrical-ardupro/arduino-nicla-sense-me/Nicla Sense.step` |
| 5.0 MB | `mechanical/CAD/components-electrical-ardupro/arduino-pro-portenta-h7/Arduino-Portenta-H7-STEP-A210428.step` |
| 3.1 MB | `mechanical/CAD/components-electrical-ardupro/hall-effect-sensor/Linear Magnetic Hall Effect Switches.SLDASM` |
| 0.4 MB | `mechanical/CAD/components-electrical-ardupro/motor-driver-l298n/MOTOR_DRIVER_L298N.SLDPRT` |
| 1.7 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_004755100_iOS.heic` |
| 1.4 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_004757586_iOS.heic` |
| 1.5 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_004758979_iOS.heic` |
| 1.5 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_005258451_iOS.heic` |
| 30.0 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_005317000_iOS.MOV` |
| 37.9 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_010508000_iOS.MOV` |
| 12.1 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_010617000_iOS.MOV` |
| 2.2 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_011337380_iOS.heic` |
| 1.7 MB | `mechanical/strength_testing/jan_23_2024_flaps_test/Pictures and Videos/20240124_012046358_iOS.heic` |
| 1.1 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_182419336_iOS.heic` |
| 1.4 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_182421612_iOS.heic` |
| 1.3 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_182437524_iOS.heic` |
| 2.2 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_183343435_iOS.heic` |
| 1.3 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_183432276_iOS.heic` |
| 1.5 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_183505240_iOS.heic` |
| 1.4 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_183507296_iOS.heic` |
| 1.8 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_183509655_iOS.heic` |
| 1.4 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_183651367_iOS.heic` |
| 1.7 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_183653045_iOS.heic` |
| 1.6 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_183731237_iOS.heic` |
| 1.4 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_184558046_iOS.heic` |
| 1.5 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_184559770_iOS.heic` |
| 1.5 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_184603837_iOS.heic` |
| 2.3 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_184625814_iOS.heic` |
| 1.5 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_184630018_iOS.heic` |
| 1.6 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_184632669_iOS.heic` |
| 1.5 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/20240308_184711346_iOS.heic` |
| 4.3 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/video-20240308-182810-9b01a17c.mov` |
| 27.7 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/video-20240308-183913-caa326f0.mov` |
| 42.3 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/video-20240308-184040-b9e3b5a9.mov` |
| 51.2 MB | `mechanical/strength_testing/mar_8_2024_compression_test/Pictures and Videos/video-20240308-184550-c6b7a480.mov` |

## Existing LFS pointers (2 files)

These were committed as LFS pointers but matched no pattern on a
case-sensitive checkout, so the working tree held the pointer text. With
the case-insensitive patterns they check out as the real files. Their LFS
objects are in this repository's LFS store.

| Path | Object (sha256) | Size |
| --- | --- | --- |
| `mechanical/mech_design/CF_forged_flaps/mould_V1/Mould Base.STEP` | `b836a819ac65f7e6f225619522cd366f1d7e343abf7ec5626b64d9dfa86e0bd2` | 56,659 bytes |
| `mechanical/mech_design/CF_forged_flaps/mould_V1/Mould Top.STEP` | `b543530855c4f8b9e8e210043598a1c9b94e83a8271f3d05eed863d4a431a8b2` | 73,987 bytes |
