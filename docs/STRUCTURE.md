# Repository structure

| Path | Purpose |
|---|---|
| `src/effdock/` | Preparation, docking/confidence models, sampling, training and evaluation |
| `configs/` | Model and workflow configurations |
| `weights/` | Released checkpoint pair, checksums and model cards |
| `scripts/` | Workflow helpers and verification commands |
| `tests/` | Unit, scientific-contract and regression tests |
| `docs/` | Usage, model and implementation documentation |
| `benchmarks/external_models/` | Optional third-party model adapters and environment locks |
| `benchmarks/inputs/` | Input and training-membership metadata for retained workflows |

The Python inference interface is `effdock.inference.DockingOptions` and
`effdock.inference.dock`. The `eff-dock` command wraps the same workflows.
Run examples from the repository root so config and checkpoint paths resolve.

```text
receptor + ligand + explicit pocket center
  -> graph preparation
  -> flow sampling
  -> confidence scoring and selection
  -> SDF + results.pt + provenance
```

Energy refinement and chirality-filtered reselection are explicit additional
workflows. Third-party installations, raw data, generated poses, manuscript
materials, result tables and execution logs remain outside the public tree.
