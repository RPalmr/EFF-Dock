# Optional benchmark tooling

EFF-Dock evaluation and aggregation are available through:

```bash
uv run eff-dock evaluate --help
uv run eff-dock benchmark --help
```

[External-model adapters](external_models/README.md) include separately pinned
third-party environments, input preparation, runners and evaluators. They are
not needed to run the released EFF-Dock model. Their upstream code, weights and
datasets must be obtained separately under the relevant licenses.

`inputs/` retains metadata used by the supported workflows, including the
[released training memberships](inputs/training_membership/README.md).
Manuscript figures and saved benchmark result tables are not distributed here.
Cluster wrappers have site-specific defaults that must be adapted to the
execution environment.
