# Reproducibility

The [orientation and confidence-input contract](ORIENTATION_INJECTION.md) distinguishes `rw` evaluation from the historical `legacy_rt_w` training convention. The manuscript uses explicit `--orientation-injection rw`, `--confidence-frame-policy contextual_v1` and generation-consistent ligand references, with the released weights frozen. Compatibility defaults retain the historical operator and frame recovery; do not rely on those defaults to reproduce the manuscript. Checkpoint resume cannot silently switch operators.

The environment is locked by `pyproject.toml` and `uv.lock`, including PyTorch
2.10.0 CUDA 13.0 wheels and matching PyG extension wheels.

```bash
git lfs install
uv sync --frozen --python 3.12 --group dev
uv run python scripts/verify_release.py
uv run pytest -q
uv run ruff check src tests scripts benchmarks
```

The primary inference surface is Python:

```python
from effdock.inference import DockingOptions, dock
```

The commands below are thin wrappers retained for exact training and
benchmark reproduction:

```bash
uv run eff-dock train --config configs/train.yaml
uv run eff-dock train --config configs/train.yaml --resume outputs/RUN/checkpoints/latest.pt
uv run eff-dock confidence prepare \
  --checkpoint weights/effdock_docking_early_time_t0p10_50k.pt --split train
uv run eff-dock confidence train \
  --config configs/train_confidence_s50_raw_refined_100k.yaml
```

For fresh corrected-Rw training, use `configs/train_rw.yaml`. The historical
`configs/train.yaml` and its pinned hash are unchanged. This changes the operator,
not the training architecture or hyperparameters.

The public inference pair is
`effdock_docking_early_time_t0p10_50k.pt` (SHA-256
`65be44d7dc8f0867eb9fc5d22214b80f93971ea4702679a527c665046e91e6b6`)
and `effdock_confidence_s50_raw_refined_u70k.pt` (SHA-256
`ce59be42f0ca613871ca079127c3296f5ca9a4ec72e44a9e5cf61878351c2638`).
The matching deployment preset is N100/S10, translation sigma 2.0, a 10A
pocket crop, late-power-3 scheduling, and pure predicted-RMSD ranking.

The training entry point seeds Python, NumPy, and PyTorch. Resume checkpoints
contain model, EMA, every optimizer and scheduler, config, global step/epoch,
best metric, RNG states, metrics, and run ID. `--resume` requires the same
optimizer/scheduler layout; `--init-from` performs an explicit weights-only
migration with new optimizer state.

Record the Git commit, `uv.lock`, config, split/data manifest, checkpoint hash,
hardware, world size, effective batch size, seed, and command for every run.
CUDA scatter/atomic kernels and multi-GPU reduction order can remain
nondeterministic; do not claim bitwise reproducibility unless separately
verified.

The [released membership manifest](../benchmarks/inputs/training_membership/README.md)
publishes original sample IDs, separate docking/confidence eligibility and
hashes. It preserves the released split; the newer strict split builder is not
a reproduction of those checkpoint inventories.

GPU work runs through the project Slurm scripts. `confidence_prepare.sbatch`
generates immutable-by-default labeled pose shards and
`confidence_train.sbatch` consumes them. The Slurm files record the original
paper workflow but contain site-specific resource defaults. Benchmark job IDs,
hashes, logs, and the complete machine ledger remain under ignored local
storage; manuscript materials and saved result tables remain local.
