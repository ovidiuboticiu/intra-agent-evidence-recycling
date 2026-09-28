# External Replication — IAER v0.4.3

Independent replication is explicitly welcomed.

## Current replication status

A **Level B direct behavioral replication** was completed on 2026-09-27 and archived as:

[`iaer-v0.4.3-level-b-replication-20260927`](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/iaer-v0.4.3-level-b-replication-20260927)

It reproduced H1 in the same direct-configuration class under the frozen v0.4.3 protocol:

- H1: 24/32 vs 0/32; RD = 0.75; Holm-adjusted p = 2.38419e-7 — **SUPPORTED**;
- H2: 3/32 vs 0/32; RD = 0.09375; p = 0.25 — **NOT SUPPORTED**;
- 168/168 planned keys valid;
- V1–V4 passed.

This is **not** an independent-lab replication, **not** a cross-family replication, and **not** bit-for-bit runtime reproduction. The historical original GGUF artifact was not hash-pinned.

The release body uses the phrase "Completed external replication" as historical wording. In the current project terminology, that release is classified more narrowly as a **Level B direct-configuration replication conducted within the same project**.

Independent Level C implementation replication and Level D conceptual/cross-family replication remain open.

## Stable replication kit release

Use the versioned GitHub release for a stable, citable snapshot of the replication materials:

[`v0.4.3-external-replication-kit-v1.0`](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.4.3-external-replication-kit-v1.0)

Release target commit:

`ad504be927532477ae3369d028e2601698dbb332`

Publication/audit record:

[`docs/EXTERNAL_REPLICATION_KIT_PUBLICATION_RECORD_v1_0.md`](docs/EXTERNAL_REPLICATION_KIT_PUBLICATION_RECORD_v1_0.md)

## Start here

[`docs/EXTERNAL_REPLICATION_KIT_v1_0.md`](docs/EXTERNAL_REPLICATION_KIT_v1_0.md)

The kit contains:

- a full external replication guide;
- exact V1–V4 validity gates;
- a before/during/after checklist;
- a standardized replication report template;
- a machine-readable model/runtime environment template.

The frozen original experiment is preserved under [`experiments/v0_4_3/`](experiments/v0_4_3/). Do not overwrite its historical files.

## Post-publication correction status

The historical empirical preprint remains preserved under its original title and DOI, but its historical priority claim has been **withdrawn**. The v0.4.3 study is now described as **pre-specified and frozen before collection**, not as publicly preregistered before collection, because no public or independently verifiable pre-collection timestamp of that preregistration artifact was located.

See:

- [`docs/IAER_PRIORITY_CLAIM_WITHDRAWAL_2026-09-28.md`](docs/IAER_PRIORITY_CLAIM_WITHDRAWAL_2026-09-28.md)
- [`docs/IAER_PRIOR_ART_REASSESSMENT_2026-09-28.md`](docs/IAER_PRIOR_ART_REASSESSMENT_2026-09-28.md)
- [`docs/POST_PUBLICATION_CORRECTION_RECORD_2026-09-28.md`](docs/POST_PUBLICATION_CORRECTION_RECORD_2026-09-28.md)

## Persistent records

- historical empirical preprint: `10.5281/zenodo.22282120`
- empirical-preprint concept DOI: `10.5281/zenodo.22282119`
- software/reproducibility archive: `10.5281/zenodo.22259801`
- methodological note: `10.5281/zenodo.22306245`
- v0.7 results-and-closure dataset: `10.5281/zenodo.22308045`
- v0.7 dataset concept DOI: `10.5281/zenodo.22308044`

A corrected empirical preprint draft exists in the repository but is **not yet a Zenodo publication**:

[`docs/IAER_EMPIRICAL_PREPRINT_CORRECTED_DRAFT_2026-09-28.md`](docs/IAER_EMPIRICAL_PREPRINT_CORRECTED_DRAFT_2026-09-28.md)

Until that corrected Zenodo version is published, `CITATION.cff` points to the v0.4.3 software/reproducibility archive rather than recommending the historically superseded v0.4 preprint.

The v0.7 Zenodo dataset is the persistent technical archive for the measurement-decoupling pilot and closure package. Its publication record is preserved in [`docs/V0_7_ZENODO_DATASET_PUBLICATION_RECORD.md`](docs/V0_7_ZENODO_DATASET_PUBLICATION_RECORD.md). v0.7 remains `REDESIGN_FAILED_STOP` and is not an IAER replication or confirmatory result.

Valid non-replications, failed preflights, and other integrity-valid negative outcomes are as important to report as successful replications. Please preserve raw data, environment details, deviations, and prospectively frozen decision rules.
