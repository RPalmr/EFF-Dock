# Supplied-pocket external-model comparison

Three-repeat means and sample SD. GOLD and AutoDock Vina are deposited PoseBusters values.
`RMSD` is Top-1 symmetry-aware heavy-atom RMSD < 2 Å; `Joint` additionally requires the
same pose to pass all 27 official PoseBusters 0.6.5 redock checks. Missing or
evaluator-error targets remain failures. Values match the manuscript source data
(`papers/data/source_data.json`); per-repeat values and provenance are in
[`pocket_only_pb_valid_comparison.json`](pocket_only_pb_valid_comparison.json).

## Astex Diverse (N=85)

| Method | Repeats | RMSD (%) | Joint (%) |
|---|---:|---:|---:|
| EFF-Dock | 3 | 83.14 ± 0.68 | 80.00 ± 0.00 |
| SigmaDock | 3 | 90.59 ± 1.18 | 89.02 ± 1.36 |
| DiffDock-Pocket | 3 | 53.73 ± 0.68 | 31.37 ± 3.40 |
| RLDiff RL++ | 3 | 84.31 ± 2.45 | 82.35 ± 4.08 |
| DiffBindFR + MDN/EC | 3 | 80.78 ± 2.96 | 68.63 ± 3.59 |
| SurfDock, no force optimization | 3 | 90.20 ± 3.59 | 64.31 ± 2.96 |
| SurfDock | 3 | 90.59 ± 2.04 | 85.88 ± 3.11 |
| GOLD | 1 | 67.06 | 63.53 |
| AutoDock Vina | 1 | 57.65 | 56.47 |

## PoseBusters v2 (N=308)

| Method | Repeats | RMSD (%) | Joint (%) |
|---|---:|---:|---:|
| EFF-Dock | 3 | 82.14 ± 0.56 | 79.76 ± 0.19 |
| SigmaDock | 3 | 78.90 ± 0.32 | 76.41 ± 0.19 |
| DiffDock-Pocket | 3 | 31.82 ± 0.65 | 14.83 ± 0.68 |
| RLDiff RL++ | 3 | 74.46 ± 1.35 | 72.94 ± 0.68 |
| DiffBindFR + MDN/EC | 3 | 54.22 ± 2.27 | 36.04 ± 2.45 |
| SurfDock, no force optimization | 3 | 81.49 ± 0.65 | 43.72 ± 0.68 |
| SurfDock | 3 | 84.31 ± 0.82 | 77.81 ± 0.99 |
| GOLD | 1 | 58.12 | 54.55 |
| AutoDock Vina | 1 | 59.74 | 58.12 |

## Four-state failure partition

Official PoseBusters 0.6.5 (redock) labels on every candidate assign each complex and repeat
to one state: no candidate with RMSD < 2 Å; near-native candidates exist but none passes
all checks; a valid near-native candidate exists but was not selected; or success.
Percentages of the full cohort, three-repeat means. Source:
`papers/data/stage_partition.json`.

### Astex Diverse (N=85)

| Method | No near-native | No valid near-native | Not selected | Success |
|---|---:|---:|---:|---:|
| EFF-Dock (40 poses) | 5.1 | 2.7 | 14.1 | 78.0 |
| EFF-Dock (100 poses) | 3.5 | 2.4 | 14.1 | 80.0 |
| SigmaDock | 1.6 | 2.7 | 6.7 | 89.0 |
| DiffDock-Pocket | 34.1 | 18.4 | 16.1 | 31.4 |
| RLDiff RL++ | 7.5 | 0.0 | 10.2 | 82.4 |
| DiffBindFR + MDN/EC | 5.1 | 6.3 | 20.0 | 68.6 |
| SurfDock | 1.6 | 0.4 | 12.2 | 85.9 |
| SurfDock, no force opt. | 3.1 | 7.1 | 25.5 | 64.3 |

### PoseBusters v2 (N=308)

| Method | No near-native | No valid near-native | Not selected | Success |
|---|---:|---:|---:|---:|
| EFF-Dock (40 poses) | 6.3 | 1.8 | 14.5 | 77.4 |
| EFF-Dock (100 poses) | 5.1 | 1.2 | 14.0 | 79.8 |
| SigmaDock | 7.5 | 5.8 | 10.3 | 76.4 |
| DiffDock-Pocket | 47.8 | 22.3 | 15.0 | 14.8 |
| RLDiff RL++ | 16.6 | 1.5 | 9.0 | 72.9 |
| DiffBindFR + MDN/EC | 14.7 | 15.2 | 34.1 | 36.0 |
| SurfDock | 6.2 | 2.3 | 13.7 | 77.8 |
| SurfDock, no force opt. | 6.6 | 20.5 | 29.2 | 43.7 |
