# Proposed README clarification patch — Stage 4

This patch is intended for the living repository README. It must not alter frozen historical experiment files.

## 1. v0.4.3 status row

Replace:

`Completed and independently audited; H1 supported, H2 not supported`

with:

`Completed; post-run integrity audit and separate recomputation performed; H1 supported, H2 not supported`

## 2. Methodological note pointer

Replace the current preprint-ready pointer from `METHODOLOGICAL_NOTE_PREPRINT_v0_3.md` only after the v0.4 manuscript source is present in the repository. The intended target is:

`docs/METHODOLOGICAL_NOTE_PREPRINT_v0_4.md`

Add links to:

- `docs/METHODOLOGICAL_NOTE_CORRECTION_LOG_v0_4.md`
- `docs/V0_4_3_FORENSIC_VALIDATION_ADDENDUM_v1_0.md`

Do not create a broken README link if the v0.4 manuscript source has not yet been committed.

## 3. v0.4.3 gate wording

Replace:

`all four preregistered validity gates passed`

with:

`all four frozen pre-specified validity gates passed`

Then add:

> The v0.4.3 package has strong internal freeze consistency, including stable preregistration/stimuli/rationale hashes embedded in all result rows. A privately archived preflight screenshot corroborates that the mandatory preflight was completed immediately before confirmatory collection, but it is not a public registration record. A public or independently verifiable pre-collection timestamp of the v0.4.3 preregistration artifact has not been established. For this reason, new project summaries describe v0.4.3 as pre-specified/frozen rather than publicly preregistered. Later publicly preregistered stages retain their original terminology.

## 4. Strongest supported H1 claim

Replace:

`relative to an equal-sized unrelated-memory control`

with:

`relative to an equal-count control containing five unrelated memory records`

Then add:

> Post-publication forensic validation independently reproduced the H1/H2 calculations and found no material data or statistical error. It also confirmed that H1 does not isolate derivative dependence from lexical repetition, target-consistent salience, explicit root references, and prompt length. The behavioral contrast is supported; literal independent-source counting is not established.

## 5. Preprint section

Keep the historical Zenodo title exactly as published, but append:

> **Post-publication clarification:** the historical title is preserved as part of the published record. A later forensic chronology audit found strong evidence of pre-specification/freeze consistency and a privately archived preflight screenshot that corroborates the operational sequence, but did not locate a public or independently verifiable pre-collection timestamp of the v0.4.3 preregistration artifact. See `docs/V0_4_3_FORENSIC_VALIDATION_ADDENDUM_v1_0.md`.

## 6. Experimental discipline

Retain:

`preregistration before confirmatory or qualification collection where applicable`

because later stages such as v0.5.2 and v0.7 do have public preregistration evidence. Do not imply that every historical version met the same registration standard.

## 7. Repository structure/current work product

Add the Stage 4 files. Change the current methodological-note path to v0.4 only after `docs/METHODOLOGICAL_NOTE_PREPRINT_v0_4.md` is actually present, or after the Zenodo DOI is available and the README can point directly to the published record.
