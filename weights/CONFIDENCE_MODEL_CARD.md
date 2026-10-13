# EFF-Dock S50 raw+refined pose-confidence checkpoint

**Feature provenance:** this unchanged checkpoint was trained on docking features from `legacy_rt_w`. Scoring corrected `rw` features is a cross-operator frozen-weight evaluation, reported separately; it is not a retrained confidence model. See [orientation compatibility](../docs/ORIENTATION_INJECTION.md).

- File: `effdock_confidence_s50_raw_refined_u70k.pt`
- SHA-256: `ce59be42f0ca613871ca079127c3296f5ca9a4ec72e44a9e5cf61878351c2638`
- Model type: `docking_graph_pose_confidence`
- Training update: 70,000 of the registered 100,000-update run
- Selection metric: validation Top-1 symmetry-aware RMSD `<2A`
- Paired docking checkpoint: `effdock_docking_early_time_t0p10_50k.pt`
- Default sampler: N100/S10/sigma-2/late-power-3/pocket-10A
- Default selector: stable minimum predicted pose RMSD

## Intended use

Rank multiple poses generated for the same receptor, ligand, and explicit
pocket. The promoted contract uses 100 poses, 10 ODE steps, translation sigma
2.0, and a 10A protein crop. The checkpoint predicts pose RMSD and success plus
per-atom displacement and success heads. These are within-complex ranking
signals; they are not calibrated across targets and do not predict binding
affinity.

The confidence model consumes t=1 ligand hidden representations from the
paired docking model. The default files, sampling preset, and pure-confidence
selector form one versioned stack. Using a different generator, sigma, pose
count, ODE budget, or protein crop is a distribution shift and must be reported
explicitly.

## Training and internal selection

The run used 43,092 training samples and initialized from the terminal U50k
symmetry-confidence state, with
one balanced per-complex mixture of 32 raw sigma-2 poses, 32 deterministically
refined poses, and one mapped crystal anchor. Pose-level training and selection
labels use RDKit `CalcRMS` symmetry-aware no-alignment heavy-atom RMSD.

The checkpoint was selected only on the fixed 1,035-complex PLINDER validation
bank. U70k reached 622/1,035 (60.10%) Top-1 `<2A`, the best registered value in
the 100k run. U100k reached 617/1,035 (59.61%) and remains the terminal training
state, not the deployment checkpoint.

## Inference conventions

For the evaluated coordinate conventions, explicitly request `rw` orientation
injection and `contextual_v1` confidence frames with the paired docking model.
The public `dock()` API generates and confidence-ranks raw poses. Energy
refinement and input-chirality-filtered reselection are separate workflows.
Historical checkpoint-compatible defaults remain available.

## Limitations

- Requires an explicit pocket and compatible EFF-Dock hidden features.
- Performance can shift with receptor preparation, ligand protonation or
  stereochemistry, pose count, sigma, ODE budget, crop, or generator weights.
- Reference structures are used only for evaluation labels, not ranking.
- The external studies are pocket-redocking evaluations, not blind pocket
  discovery or prospective screening.
- The model does not predict affinity or binder/non-binder status.

Exact [training membership](../benchmarks/inputs/training_membership/README.md),
[method equations](../docs/methods/05_confidence_model_and_loss.md),
[training settings](../docs/methods/06_training_and_checkpoint_selection.md), and
the model configuration and training-membership metadata are public. The
43,092 confidence training IDs and 47,277 docking IDs are independently filtered
sets sharing 43,067 IDs, not a nested pair.

This checkpoint is released together with the paired docking checkpoint under
Apache-2.0. See `DOCKING_MODEL_CARD.md` and `MANIFEST.md` for the complete
deployment identity.
