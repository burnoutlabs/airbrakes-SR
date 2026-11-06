# KiCad backups and autosaves: inventory before removal

The KiCad projects `dmats_hw_v1_0` and `dmats_hw_v2_0` were committed with
the editor's timestamped backup zips, autosave files, a symbol-library
`.bak`, footprint caches and per-user `.kicad_prl` files. They are removed
in the commit after this one
([#5](https://github.com/burnoutlabs/airbrakes-SR/issues/5)). This file
records what they held, so nothing is lost without a record.

Every removed file stays in git history. To recover one, check it out from
`main` as it was before the removal (commit `99d8a5c`):

```sh
git show 99d8a5c:"electrical/dmats_hw_v2_0/dmats_hw_v2_0-backups/dmats_hw_v2_0-2024-04-08_173040.zip" > backup.zip
```

## How this was produced

For each zip, every member was hashed as a git blob (after converting the
zip's CRLF line endings to LF, which is how the same files are stored in
git) and compared with:

1. the file of the same name in the project folder at `main` (`99d8a5c`);
2. every blob anywhere in the repository's history (`git rev-list --all --objects`),
   which includes the capstone history before the split.

A member matching neither exists only in the zips. Zip timestamps come from
the file names (KiCad writes local time). There are 13 zips for v1_0 and 25
for v2_0. Git history holds the project folders only from the split commit
`2a644e5` (2024-04-09) onward, plus the capstone commits under the old
`electrical-design/` path.

## Summary

- **Nothing in the zips is newer than the files at `main`.** The newest zip
  of each project (`dmats_hw_v1_0-2024-04-09_005957.zip`,
  `dmats_hw_v2_0-2024-04-09_010004.zip`) matches git history in every file.
- The states that exist only in the zips are **intermediate work on
  2024-03-12 and 2024-04-01 to 2024-04-08**: earlier schematic states with
  fewer symbols and wires, and PCB routing in progress (29 to 37 footprints,
  64 to 189 track segments, 3 to 24 vias, against 37 / 205 / 27 at `main`).
  They are listed in full below.
- One zip-only state has content that `main` lacks: `dmats_hw_v2_0/portenta_h7.kicad_sch`
  as of 2024-04-02 22:52:57 holds 2 symbols; at `main` that sheet is empty
  and no other sheet references it.

## Per zip

| Project | Zip | Timestamp (from name) | Files | Same as file at main | Matches a blob in git history | Only in zips |
| --- | --- | --- | --- | --- | --- | --- |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-03-12_091108.zip` | 2024-03-12 09:11:08 | 9 | 7 | 2 | 0: none |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-03-12_103231.zip` | 2024-03-12 10:32:31 | 9 | 7 | 1 | 1: `dmats_hw_v1_0.kicad_sch` |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-03-12_111046.zip` | 2024-03-12 11:10:46 | 9 | 7 | 1 | 1: `dmats_hw_v1_0.kicad_sch` |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-03-12_121403.zip` | 2024-03-12 12:14:03 | 9 | 7 | 2 | 0: none |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-03-12_131805.zip` | 2024-03-12 13:18:05 | 9 | 7 | 2 | 0: none |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-04-01_214730.zip` | 2024-04-01 21:47:30 | 11 | 8 | 1 | 2: `dmats_hw_v1_0.kicad_pro`, `dmats_hw_v1_0.kicad_sch` |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-04-01_232709.zip` | 2024-04-01 23:27:09 | 12 | 11 | 1 | 0: none |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-04-07_224631.zip` | 2024-04-07 22:46:31 | 12 | 11 | 0 | 1: `dmats_hw_v1_0.kicad_sch` |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-04-07_225550.zip` | 2024-04-07 22:55:50 | 12 | 11 | 0 | 1: `dmats_hw_v1_0.kicad_sch` |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-04-08_002345.zip` | 2024-04-08 00:23:45 | 12 | 11 | 0 | 1: `dmats_hw_v1_0.kicad_sch` |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-04-08_103952.zip` | 2024-04-08 10:39:52 | 12 | 11 | 0 | 1: `dmats_hw_v1_0.kicad_sch` |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-04-08_160031.zip` | 2024-04-08 16:00:31 | 12 | 12 | 0 | 0: none |
| dmats_hw_v1_0 | `dmats_hw_v1_0-2024-04-09_005957.zip` | 2024-04-09 00:59:57 | 12 | 12 | 0 | 0: none |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-02_164801.zip` | 2024-04-02 16:48:01 | 11 | 2 | 9 | 0: none |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-02_223507.zip` | 2024-04-02 22:35:07 | 11 | 2 | 9 | 0: none |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-02_225257.zip` | 2024-04-02 22:52:57 | 12 | 2 | 6 | 4: `A4957_driver.kicad_sch`, `dmats_hw_v2_0.kicad_pro`, `dmats_hw_v2_0.kicad_sch`, `portenta_h7.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-02_233208.zip` | 2024-04-02 23:32:08 | 10 | 3 | 2 | 5: `A4957_driver.kicad_sch`, `DMATS_capstone.kicad_sym`, `dmats_hw_v2_0.kicad_pro`, `dmats_hw_v2_0.kicad_sch`, `fp-lib-table` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-03_005055.zip` | 2024-04-03 00:50:55 | 13 | 8 | 3 | 2: `dmats_hw_v2_0.kicad_pro`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-03_201706.zip` | 2024-04-03 20:17:06 | 13 | 7 | 5 | 1: `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-03_203126.zip` | 2024-04-03 20:31:26 | 15 | 8 | 4 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `_autosave-dmats_hw_v2_0.kicad_sch`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-03_203626.zip` | 2024-04-03 20:36:26 | 14 | 8 | 4 | 2: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-03_204707.zip` | 2024-04-03 20:47:07 | 14 | 8 | 4 | 2: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-04_231801.zip` | 2024-04-04 23:18:01 | 15 | 10 | 2 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `_autosave-dmats_hw_v2_0.kicad_sch`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-04_232559.zip` | 2024-04-04 23:25:59 | 15 | 10 | 1 | 4: `_autosave-dmats_hw_v2_0.kicad_pcb`, `_autosave-dmats_hw_v2_0.kicad_sch`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-04_233315.zip` | 2024-04-04 23:33:15 | 14 | 10 | 1 | 3: `_autosave-dmats_hw_v2_0.kicad_sch`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-04_234515.zip` | 2024-04-04 23:45:15 | 15 | 10 | 1 | 4: `_autosave-dmats_hw_v2_0.kicad_pcb`, `_autosave-dmats_hw_v2_0.kicad_sch`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-04_235549.zip` | 2024-04-04 23:55:49 | 14 | 10 | 2 | 2: `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-05_001552.zip` | 2024-04-05 00:15:52 | 15 | 10 | 2 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-05_002412.zip` | 2024-04-05 00:24:12 | 15 | 10 | 2 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-05_003438.zip` | 2024-04-05 00:34:38 | 15 | 10 | 2 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-05_004229.zip` | 2024-04-05 00:42:29 | 14 | 10 | 3 | 1: `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-05_004813.zip` | 2024-04-05 00:48:13 | 13 | 9 | 4 | 0: none |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-08_165813.zip` | 2024-04-08 16:58:13 | 18 | 13 | 2 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-08_171131.zip` | 2024-04-08 17:11:31 | 18 | 13 | 2 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-08_172016.zip` | 2024-04-08 17:20:16 | 18 | 13 | 2 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-08_173040.zip` | 2024-04-08 17:30:40 | 18 | 13 | 2 | 3: `_autosave-dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_pcb`, `dmats_hw_v2_0.kicad_sch` |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-08_173857.zip` | 2024-04-08 17:38:57 | 17 | 17 | 0 | 0: none |
| dmats_hw_v2_0 | `dmats_hw_v2_0-2024-04-09_010004.zip` | 2024-04-09 01:00:04 | 17 | 17 | 0 | 0: none |

## Distinct file states that exist only in the zips

Each row is one distinct content (by git blob hash) not found anywhere in git history. 'First seen' is the earliest zip holding it. 'vs main' compares with the file of the same name at `main` (line diff, then structural counts).

| Project | File | First seen | Blob | vs main (lines -/+) | Zip state | main state |
| --- | --- | --- | --- | --- | --- | --- |
| dmats_hw_v1_0 | `dmats_hw_v1_0.kicad_sch` | 2024-03-12 10:32:31 | `9304be1beb` | -2006/+1487 | 36 symbols, 88 wires, 0 hier. labels, 0 sheets | 51 symbols, 145 wires, 0 hier. labels, 0 sheets |
| dmats_hw_v1_0 | `dmats_hw_v1_0.kicad_pro` | 2024-04-01 21:47:30 | `a6a94dd634` | -0/+4 | 11121 bytes | - |
| dmats_hw_v1_0 | `dmats_hw_v1_0.kicad_sch` | 2024-04-01 21:47:30 | `ec2c512e41` | -3941/+960 | 38 symbols, 88 wires, 0 hier. labels, 1 sheets | 51 symbols, 145 wires, 0 hier. labels, 0 sheets |
| dmats_hw_v1_0 | `dmats_hw_v1_0.kicad_sch` | 2024-04-07 22:46:31 | `6c4fc3b16a` | -796/+582 | 46 symbols, 135 wires, 0 hier. labels, 0 sheets | 51 symbols, 145 wires, 0 hier. labels, 0 sheets |
| dmats_hw_v1_0 | `dmats_hw_v1_0.kicad_sch` | 2024-04-07 22:55:50 | `beee5e47f5` | -195/+96 | 48 symbols, 139 wires, 0 hier. labels, 0 sheets | 51 symbols, 145 wires, 0 hier. labels, 0 sheets |
| dmats_hw_v2_0 | `A4957_driver.kicad_sch` | 2024-04-02 22:52:57 | `445ce88de4` | -986/+826 | 21 symbols, 84 wires, 23 hier. labels, 0 sheets | 21 symbols, 75 wires, 25 hier. labels, 0 sheets |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_pro` | 2024-04-02 22:52:57 | `460a0fdb16` | -22/+9 | 11198 bytes | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-02 22:52:57 | `9e442a5a1c` | -2123/+2091 | 23 symbols, 55 wires, 0 hier. labels, 2 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `portenta_h7.kicad_sch` | 2024-04-02 22:52:57 | `11b66f9968` | -1/+1317 | 2 symbols, 0 wires, 0 hier. labels, 0 sheets | 0 symbols, 0 wires, 0 hier. labels, 0 sheets |
| dmats_hw_v2_0 | `A4957_driver.kicad_sch` | 2024-04-02 23:32:08 | `543d2a6d05` | -986/+826 | 21 symbols, 84 wires, 23 hier. labels, 0 sheets | 21 symbols, 75 wires, 25 hier. labels, 0 sheets |
| dmats_hw_v2_0 | `DMATS_capstone.kicad_sym` | 2024-04-02 23:32:08 | `6015f77c9f` | -349/+87 | 6 symbols (21 symbol and unit blocks) | 7 symbols (24 symbol and unit blocks) |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-02 23:32:08 | `d9f9ce017f` | -2045/+1218 | 25 symbols, 55 wires, 0 hier. labels, 2 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `fp-lib-table` | 2024-04-02 23:32:08 | `94325bc778` | -1/+2 | 255 bytes | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_pro` | 2024-04-03 00:50:55 | `55509ceba9` | -16/+7 | 11254 bytes | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-03 00:50:55 | `e5fed52bdd` | -1903/+1142 | 25 symbols, 54 wires, 0 hier. labels, 2 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-03 20:17:06 | `880b3a0fe8` | -1919/+662 | 23 symbols, 54 wires, 0 hier. labels, 2 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-03 20:31:26 | `16b807b952` | no file at main | 30 footprints, 0 segments, 0 vias | - |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_sch` | 2024-04-03 20:31:26 | `33b3ce17fc` | no file at main | 25 symbols, 54 wires, 0 hier. labels, 1 sheets | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-03 20:31:26 | `c401d0b494` | -1899/+1144 | 25 symbols, 54 wires, 0 hier. labels, 2 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-03 20:36:26 | `e447fb1d37` | -1314/+536 | 25 symbols, 54 wires, 0 hier. labels, 1 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-03 20:47:07 | `11749dc822` | no file at main | 29 footprints, 0 segments, 0 vias | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-03 20:47:07 | `53ae9f846c` | -1314/+536 | 25 symbols, 54 wires, 0 hier. labels, 1 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-04 23:18:01 | `0981ecc637` | no file at main | 29 footprints, 64 segments, 3 vias | - |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_sch` | 2024-04-04 23:18:01 | `02b20bea65` | no file at main | 26 symbols, 56 wires, 0 hier. labels, 1 sheets | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-04 23:18:01 | `b9aa37d5f0` | -1277/+532 | 26 symbols, 56 wires, 0 hier. labels, 1 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_pcb` | 2024-04-04 23:25:59 | `9ee061d78e` | -17641/+798 | 29 footprints, 84 segments, 3 vias | 37 footprints, 205 segments, 27 vias |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_pcb` | 2024-04-04 23:33:15 | `ede11f0e3b` | -17625/+790 | 29 footprints, 92 segments, 3 vias | 37 footprints, 205 segments, 27 vias |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-04 23:45:15 | `bd044c2260` | no file at main | 29 footprints, 105 segments, 5 vias | - |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_sch` | 2024-04-04 23:45:15 | `283e04086f` | no file at main | 26 symbols, 56 wires, 0 hier. labels, 1 sheets | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_pcb` | 2024-04-04 23:55:49 | `e7d005ee3a` | -17607/+799 | 29 footprints, 113 segments, 9 vias | 37 footprints, 205 segments, 27 vias |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-05 00:15:52 | `94f5919255` | no file at main | 29 footprints, 113 segments, 9 vias | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_pcb` | 2024-04-05 00:24:12 | `4e81a47b5e` | -17369/+879 | 29 footprints, 117 segments, 15 vias | 37 footprints, 205 segments, 27 vias |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-05 00:34:38 | `4eea25232e` | no file at main | 29 footprints, 116 segments, 14 vias | - |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-08 16:58:13 | `d2ab0a25aa` | no file at main | 37 footprints, 116 segments, 12 vias | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_pcb` | 2024-04-08 16:58:13 | `073cfc23a3` | -12214/+9486 | 37 footprints, 116 segments, 12 vias | 37 footprints, 205 segments, 27 vias |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_sch` | 2024-04-08 16:58:13 | `d4a9591120` | -38/+38 | 38 symbols, 84 wires, 0 hier. labels, 1 sheets | 38 symbols, 84 wires, 0 hier. labels, 1 sheets |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-08 17:11:31 | `9cda9c3905` | no file at main | 37 footprints, 131 segments, 13 vias | - |
| dmats_hw_v2_0 | `dmats_hw_v2_0.kicad_pcb` | 2024-04-08 17:20:16 | `38526b37c7` | -9529/+9420 | 37 footprints, 158 segments, 18 vias | 37 footprints, 205 segments, 27 vias |
| dmats_hw_v2_0 | `_autosave-dmats_hw_v2_0.kicad_pcb` | 2024-04-08 17:30:40 | `4c3e02de85` | no file at main | 37 footprints, 189 segments, 24 vias | - |

`.kicad_prl` files and the remaining members not listed above match a blob
in git history.

## Autosaves in the project folders

| File | Saved sheet | Difference | Disposition |
| --- | --- | --- | --- |
| `dmats_hw_v2_0/_autosave-hall_effect_sensor.kicad_sch` | None. No `hall_effect_sensor.kicad_sch` exists in git history (current or capstone paths) or in any zip; all 25 v2_0 zips hold this same autosave (identical after line-ending normalisation). | This is the only copy of the sheet. `dmats_hw_v2_0.kicad_sch` does not reference it (its only sheet file is `A4957_driver.kicad_sch`). | Kept: renamed unchanged to `dmats_hw_v2_0/hall_effect_sensor.kicad_sch`. It is an unreferenced, unfinished sheet. |
| `dmats_hw_v1_0/_autosave-portenta_h7.kicad_sch` | `dmats_hw_v1_0/portenta_h7.kicad_sch` | The autosave adds four unconnected hierarchical labels, shown below. The saved sheet is not referenced by `dmats_hw_v1_0.kicad_sch`, so the labels connect to nothing. | Removed; the labels are recorded here and the file stays in history. |

The four labels in `_autosave-portenta_h7.kicad_sch` that
`portenta_h7.kicad_sch` lacks (`diff portenta_h7.kicad_sch _autosave-portenta_h7.kicad_sch`):

```
2338a2339,2355
>   (hierarchical_label "+3V3" (shape input) (at 138.43 46.99 0) (fields_autoplaced)
>     (effects (font (size 1.27 1.27)) (justify left))
>     (uuid 3cb760a7-a36e-41cc-b389-bca71025d867)
>   )
>   (hierarchical_label "+5V" (shape input) (at 138.43 44.45 0) (fields_autoplaced)
>     (effects (font (size 1.27 1.27)) (justify left))
>     (uuid 42d0be7b-2a5e-471f-b927-d51e47757230)
>   )
>   (hierarchical_label "D0" (shape input) (at 138.43 57.15 0) (fields_autoplaced)
>     (effects (font (size 1.27 1.27)) (justify left))
>     (uuid b5eb8412-5cb0-4622-956e-3fa2cb5a7f97)
>   )
>   (hierarchical_label "D1" (shape input) (at 138.43 59.69 0) (fields_autoplaced)
>     (effects (font (size 1.27 1.27)) (justify left))
>     (uuid f65a8311-92a8-47e0-aa8e-48e0dac792c1)
>   )
> 
```

## Other removed files

| File | What it is | Notes |
| --- | --- | --- |
| `dmats_hw_v2_0/DMATS_capstone.bak` | An older copy of the `DMATS_capstone.kicad_sym` symbol library (18,639 bytes, 5 symbols in 17 symbol and unit blocks). | All 5 symbols are present in the current `DMATS_capstone.kicad_sym`, which has 7 (24 blocks); it adds `A4957` and `ABX00042`. |
| `dmats_hw_v1_0/fp-info-cache`, `dmats_hw_v2_0/fp-info-cache` | KiCad's footprint library cache (2 bytes and 3.3 MB). | Regenerated by KiCad on demand. |
| `dmats_hw_v1_0/dmats_hw_v1_0.kicad_prl`, `dmats_hw_v2_0/dmats_hw_v2_0.kicad_prl` | Per-user project state (open layers, view settings). | Not design data; KiCad recreates it. |

`dmats_hw_v1_0/external-components/ABX00042.zip` is a vendor download of
the Portenta H7 (ABX00042) part, not a KiCad backup, and is kept.
