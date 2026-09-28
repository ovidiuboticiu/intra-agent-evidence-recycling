# IAER v0.4.3 — External Replication Kit v1.0 — Publication Record

## GitHub release

- Tag: `v0.4.3-external-replication-kit-v1.0`
- Release title: `IAER v0.4.3 — External Replication Kit v1.0`
- Target commit: `ad504be927532477ae3369d028e2601698dbb332`
- Release ID: `382854511`
- Published: `2026-09-04T15:59:48Z`
- Release type: normal release (`prerelease=false`)
- Release URL: `https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.4.3-external-replication-kit-v1.0`

The tag resolves directly to the target commit above. GitHub provides immutable source snapshots for the tag as Source code (zip) and Source code (tar.gz).

## Scope

This release freezes the external-replication guidance around the preserved IAER v0.4.3 source study. It does not rewrite the frozen historical experiment, raw results, or historical manifests.

The kit provides:

- Level A — analysis reproduction;
- Level B — direct behavioral replication;
- Level C — independent implementation replication;
- Level D — conceptual / cross-family replication;
- exact V1–V4 validity gates;
- preflight and STOP rules;
- environment-capture template;
- standardized replication report template;
- interpretation boundaries separating behavioral effects from mechanistic claims.

## Related persistent records

- Empirical preprint: `10.5281/zenodo.22282120`
- Concept DOI for empirical preprint versions: `10.5281/zenodo.22282119`
- Software/reproducibility archive: `10.5281/zenodo.22259801`
- Methodological note: `10.5281/zenodo.22306245`

## Historical Zenodo metadata clarification

On 2026-09-04, the existing Zenodo metadata for the historical empirical preprint record `10.5281/zenodo.22282120` was updated in place, without creating a new version and without replacing the original PDF or changing the historical title.

The added post-publication clarification states that:

- a no-new-data forensic validation reproduced the v0.4.3 H1/H2 calculations exactly;
- no material data or statistical error was found;
- the materials were pre-specified and internally frozen before collection;
- a public or independently verifiable pre-collection timestamp of the preregistration artifact itself was not located;
- the H1 behavioral finding remains unchanged;
- literal independent-source counting is not established as the mechanism.

The full forensic clarification is preserved in:

`docs/V0_4_3_FORENSIC_VALIDATION_ADDENDUM_v1_0.md`

## Final disposition

The IAER experimental program remains `PAUSED` after v0.7. No v0.8 behavioral run is authorized. The project is now preserved for external reproduction/replication, methodological inspection, and future restart only under a materially new measurement design.


## Post-publication status update — 2026-09-28

A Level B direct behavioral replication was completed on 2026-09-27 and archived under:

`iaer-v0.4.3-level-b-replication-20260927`

Results:

- 168/168 planned keys valid;
- V1–V4 passed;
- H1: 24/32 vs 0/32; RD = 0.75; Holm-adjusted p = 2.38419e-7 — **SUPPORTED**;
- H2: 3/32 vs 0/32; RD = 0.09375; p = 0.25 — **NOT SUPPORTED**.

The release body uses the phrase "Completed external replication" as historical wording. The current classification is narrower: **Level B direct-configuration replication conducted within the same project**. It is not an independent-lab replication, not cross-family, and not bit-for-bit runtime reproduction because the historical original GGUF artifact was not hash-pinned.

Independent Level C implementation replication and Level D conceptual/cross-family replication remain open.

The historical empirical preprint's priority claim was subsequently withdrawn. See `IAER_PRIORITY_CLAIM_WITHDRAWAL_2026-09-28.md` and `IAER_PRIOR_ART_REASSESSMENT_2026-09-28.md`.
