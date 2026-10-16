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
