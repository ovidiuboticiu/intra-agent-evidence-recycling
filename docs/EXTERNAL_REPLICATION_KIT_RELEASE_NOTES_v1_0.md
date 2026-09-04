# IAER v0.4.3 — External Replication Kit v1.0 — Release Notes

## Recommended GitHub release

- **Tag:** `v0.4.3-external-replication-kit-v1.0`
- **Release title:** `IAER v0.4.3 — External Replication Kit v1.0`
- **Target commit:** `ad504be927532477ae3369d028e2601698dbb332`
- **Release type:** normal release (not prerelease)

## Purpose

This release freezes the public materials intended to support independent reproduction and replication of the preserved IAER v0.4.3 behavioral study.

The release does **not** modify the frozen v0.4.3 experiment, raw results, or historical manifests. It packages the replication guidance and reporting structure around the preserved source study.

## Included replication materials

- `EXTERNAL_REPLICATION.md`
- `docs/EXTERNAL_REPLICATION_KIT_v1_0.md`
- `docs/EXTERNAL_REPLICATION_GUIDE_v1_0.md`
- `docs/EXTERNAL_REPLICATION_VALIDITY_GATES_v1_0.md`
- `docs/EXTERNAL_REPLICATION_CHECKLIST_v1_0.md`
- `docs/EXTERNAL_REPLICATION_REPORT_TEMPLATE_v1_0.md`
- `docs/EXTERNAL_REPLICATION_ENVIRONMENT_TEMPLATE_v1_0.json`

The preserved source experiment remains under:

- `experiments/v0_4_3/`

## Replication scope

The kit distinguishes:

- **Level A — analysis reproduction**
- **Level B — direct behavioral replication**
- **Level C — independent implementation replication**
- **Level D — conceptual / cross-family replication**

A different model family is not treated as a direct v0.4.3 replication by default.

## Validity discipline

A direct replication must pass the frozen v0.4.3 validity gates before H1/H2 are interpreted:

- V1: `source_only` chooses COUNTER on at least 24/32 items;
- V2: `independent_evidence` retains INITIAL on at least 6/8 items;
- V3: all 64 active trajectories contain all five valid application outputs;
- V4: all 168 planned item-condition keys are present as valid trajectories.

If a mandatory gate fails, the attempt is not interpreted as a valid negative replication.

## Original result being replicated

The original configuration-specific behavioral result was:

- H1 `passive_repeat > neutral_filler`: 22/32 vs 0/32; paired RD = 0.6875; Holm-adjusted exact McNemar p = 9.5367432e-7; supported under the frozen rule.
- H2 `active_plain > active_lineage`: 2/32 vs 0/32; paired RD = 0.0625; Holm-adjusted p = 0.50; not supported.

The target is behavioral. The original study does not establish literal independent-source counting as the internal mechanism.

## Known limitations inherited by a faithful direct replication

- derivative multiplicity is not isolated from lexical repetition;
- passive repetition increases target-consistent salience;
- prompt length differs between `passive_repeat` and `neutral_filler`;
- presentation order may affect magnitude;
- the exact historical model artifact/runtime was not fully pinned.

## Persistent records

- Empirical preprint: `10.5281/zenodo.22282120`
- Software/reproducibility archive: `10.5281/zenodo.22259801`
- Methodological note: `10.5281/zenodo.22306245`

## Recommended publication policy for external attempts

Publish successful replications, valid non-replications, failed preflights, and invalid/inconclusive attempts with equal transparency. Preserve raw data, environment details, protocol timestamps, deviations, hashes, and analysis outputs.

## Integrity note

The target commit includes the forensic chronology clarification in `CITATION.cff` while preserving the historical preprint title unchanged. No frozen v0.4.3 experimental artifact is rewritten by this release.
