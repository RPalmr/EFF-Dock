# External docking models

Each comparison model owns an isolated uv project:

```text
benchmarks/external_models/environments/<model>/
├── pyproject.toml   # tracked dependency contract
├── uv.lock          # tracked resolved Python lock
├── .python-version  # tracked interpreter series
├── .venv/           # ignored, model-local environment
├── .cache/uv/       # ignored, model-local download/build cache
├── upstream         # ignored pinned upstream checkout
├── weights          # ignored model-local checkpoint view
└── bin/             # ignored non-Python native tools, when required
```

The active environment is never shared between models and micromamba is not
part of this runtime path. Existing sources and weights under the sibling
`runtime/` tree are linked into each model workspace. The source revision is
still checked against `benchmarks/external_models/models.json` before
synchronization.

Synchronize and verify one model with:

```bash
bash benchmarks/external_models/tools/sync_model.sh sigmadock
bash benchmarks/external_models/tools/sync_model.sh surfdock
bash benchmarks/external_models/tools/sync_model.sh diffbindfr
bash benchmarks/external_models/tools/sync_model.sh interformer
```

Run a command in a synchronized model without touching another environment:

```bash
bash benchmarks/external_models/tools/run_model.sh interformer python -c \
  'import torch, pyvina_core; print(torch.__version__)'
```

Long installations run through `benchmarks/external_models/slurm/others_uv_sync.sbatch` on the
`cpu_only` partition.  GPU inference scripts consume these same model-local
environments. Interformer's Boost 1.84, Reduce 4.14, and `obrms` runtime are
also model-local. If no archived copy exists, synchronization downloads the
exact checksum-pinned native packages and materializes only the required files
below `benchmarks/external_models/environments/interformer/bin`.

SigmaDock uses the official `v0.1.0-beta` checkpoint and GNINA 1.3.2 from the
ignored legacy artifact cache.  Both artifacts are checksum-verified before
the model-local environment is accepted.  Its native comparison arm uses 40
independent seeds, 25 diffusion steps, and Vinardo ranking.

## Pillow security compatibility

CVE-2026-112897 (GHSA-q45j-58j2-45rg) affects Pillow through 12.3.0.
Pillow 13.0.0 fixes the TIFF decoding issue and requires Python 3.11 or newer.
The main project, Interformer, and SigmaDock require Pillow >=13.0.0.

SurfDock (Python 3.10) and DiffBindFR (Python 3.9) still resolve affected Pillow
versions. Their pinned upstream runtimes cannot install Pillow 13.0.0, and no
compatible patched Pillow release was available on 2026-10-25. These two
environments remain affected; updating the other locks does not remediate them.
Do not process untrusted TIFF images in these legacy environments. A complete
fix requires a compatible upstream backport or a separately validated migration
of each model's Python and native dependency stack. Do not bypass Pillow's
Python requirement to force the upgrade. Historical benchmark manifests and
recorded execution environments remain unchanged by this dependency update.

References:

- https://github.com/python-pillow/Pillow/security/advisories/GHSA-q45j-58j2-45rg
- https://github.com/python-pillow/Pillow/releases/tag/13.0.0
