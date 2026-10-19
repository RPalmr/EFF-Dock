# Method illustrations

These images are web exports of the manuscript workflow and architecture
figures, included with the authors' permission under the repository's
[Apache License 2.0](../../LICENSE). They illustrate the method; they are not
additional benchmark results. The PNGs preserve the source figure content
and were exported at 2,400 pixels wide without redrawing molecular structures.

| Image | Description | Source PDF SHA-256 |
| --- | --- | --- |
| [workflow.png](workflow.png) | Supplied-pocket docking workflow | `64491ede678dd72f9750c9fd88b5f0b009e3b5398d82891ea91c13f516385820` |
| [architecture.png](architecture.png) | Docking and confidence model architecture | `345f3f8d20cbcad2e1d52cbc6cafb0062d77fbd1321b17902ec5cea0d8089a6c` |

The workflow includes study-stage post-refinement and chirality-aware
reselection. The basic `eff-dock dock` command generates and confidence-ranks
poses; it does not automatically perform those additional stages. Crystal
RMSDs shown in the example are retrospective labels, not selection inputs.

The architecture depicts the released primary Newton–Euler readout. Its
model source was checked against the released docking, confidence and
equivariant-layer implementations. See [the model contract](../MODEL.md)
for checkpoint and coordinate-convention details.

## Animations

Three lightweight GIFs are rendered directly from saved molecular coordinates
with [3Dmol.js](https://3dmol.org/) 2.5.5 and CPU software WebGL. They use the same
Astex Diverse Set 1T46–STI example as the workflow figure. This is an illustration,
not an additional benchmark or a molecular-dynamics simulation.

| Animation | What moves |
| --- | --- |
| [pocket-context.gif](pocket-context.gif) | The camera zooms from the actual receptor to the supplied 10 Å pocket; the full-receptor cartoon fades for display. Atomic coordinates stay fixed. |
| [fragment-flow.gif](fragment-flow.gif) | All 11 stored ODE states of the independent N1/S10, seed 42, unguided Rw illustration. Six rigid fragments retain their identity and element-colored heteroatoms. |
| [confidence-ranking.gif](confidence-ranking.gif) | Four already-refined candidates from a separate N100 repeat 0 bank, ordered for display by ranks 100, 50, 25 and 1 under contextual_v1 confidence scoring. Small turns change only the camera. |

ODE time is dimensionless; playback timing is chosen for readability. No
intermediate molecular coordinates are synthesized. Cut interfragment bonds
are omitted in the flow view for clarity, without implying a chemical reaction.
The N1 trajectory uses its supplied starting conformer; the N100 bank uses the
SMILES-prepared generation conformer. These are separate runs, not a single
continuous pipeline movie.

In the confidence view, teal carbons identify the candidate and amber identifies
the crystal reference. The selected candidate has predicted RMSD 1.55 Å and
retrospective symmetry-aware RMSD 1.36 Å. Crystal coordinates and observed RMSD
are used for illustration/evaluation only, never ranking. Rank changes in the
carousel show examples, not the execution order of the confidence network.

[animations.json](animations.json) records source hashes, saved flow times,
actual candidate indices and scores, rendering identities, encoded frame counts,
playback durations and GIF checksums. The displayed structures and predictions
are unchanged from the source records used for the workflow figure. Only GIFs
and provenance are distributed here; raw benchmark coordinates, browser captures
and local render environments are not added to the repository.
