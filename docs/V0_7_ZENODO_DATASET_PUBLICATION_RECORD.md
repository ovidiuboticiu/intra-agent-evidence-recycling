# IAER v0.7 — Zenodo Dataset Publication Record

## Persistent identifiers

- Version DOI: `10.5281/zenodo.22308045`
- Concept DOI: `10.5281/zenodo.22308044`
- Zenodo record: `https://zenodo.org/records/22308045`
- Version: `v0.7`
- Resource type: Dataset
- Publication date: 2026-09-04
- Creator: Boticiu, Ovidiu — Independent Researcher
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)

## Published title

`IAER v0.7 — Measurement-Decoupling Instrument Redesign: Results and Closure Dataset`

## Main archive

- `iaer_v0_7_closure_final.zip`
- SHA-256: `120c7d37d4327797ccdcb141f27bf01726298cc86cb1e86d70f182ddd7c4c943`

A separate checksum text file was also published on Zenodo.

## Scientific status

v0.7 was a publicly preregistered measurement-decoupling instrument-redesign pilot using a frozen Ministral-3-8B-Instruct-2512 configuration. It was not an IAER replication, eligibility study, or confirmatory experiment.

All 48 planned rows were valid. P1 integrity passed. Prespecified condition accuracy was:

- `two_initial_one_counter`: 12/12
- `one_initial_two_counter`: 11/12
- `derived_lure_initial_two_counter`: 7/12
- `three_initial_two_counter`: 12/12

Under the frozen decision rule, P2 condition accuracy, P3 INITIAL-label symmetry, P4 presentation-order symmetry, and P5 derived-record lure failed. Final decision: `REDESIGN_FAILED_STOP`.

Across the three conditions containing only independent root sources, the model was correct on 35/36 calls. In the derived-record lure condition, all five errors selected the INITIAL claim. This pattern is descriptive only and does not confirm, refute, or estimate IAER in Ministral.

## Related persistent records

- Methodological note: `10.5281/zenodo.22306245` — dataset is registered as a supplement to this publication.
- Original empirical preprint: `10.5281/zenodo.22282120` — referenced by the dataset.
- Software/reproducibility archive: `10.5281/zenodo.22259801` — referenced by the dataset.

## GitHub records

- Preregistration tag: `v0.7-instrument-preregistration`
- Results tag: `v0.7-instrument-results`
- Results release: `https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.7-instrument-results`

## Final disposition

The IAER experimental program remains `PAUSED`. No v0.8 behavioral run is authorized. This Zenodo dataset is the persistent technical archive for the v0.7 result and closure package.
