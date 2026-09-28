# Zenodo Corrected-Version Checklist — IAER

**Date prepared:** 2026-09-28  
**Status:** PENDING MANUAL ZENODO PUBLICATION

This checklist begins only after the GitHub correction record is merged and stable.

## Before opening Zenodo

- [ ] Confirm `main` contains:
  - [ ] `docs/IAER_PRIORITY_CLAIM_WITHDRAWAL_2026-09-28.md`
  - [ ] `docs/IAER_PRIOR_ART_REASSESSMENT_2026-09-28.md`
  - [ ] `docs/IAER_EMPIRICAL_PREPRINT_CORRECTED_DRAFT_2026-09-28.md`
  - [ ] `docs/POST_PUBLICATION_CORRECTION_RECORD_2026-09-28.md`
- [ ] Generate final DOCX/PDF from the corrected draft.
- [ ] Perform one final citation, number, title, DOI, and formatting audit on the actual PDF.
- [ ] Confirm the historical v0.4 PDF remains unchanged.

## Zenodo publication

- [ ] Open the historical empirical-preprint record/concept.
- [ ] Create **New version** rather than silently replacing the historical PDF.
- [ ] Upload the audited corrected PDF.
- [ ] Use the corrected title:
  - *When One Source Returns: A Pre-Specified Behavioral Study of Intra-Agent Evidence Recycling*
- [ ] Describe the version explicitly as a post-publication corrected version.
- [ ] State that the historical priority claim is withdrawn.
- [ ] State that v0.4.3 is described as pre-specified/frozen rather than publicly preregistered before collection.
- [ ] State that numerical v0.4.3 results are unchanged.
- [ ] State that the 2026-09-27 Level B same-project direct-configuration replication is included.
- [ ] Publish the new version.

## After Zenodo publication

- [ ] Record the new version DOI and concept/version metadata.
- [ ] Update `CITATION.cff` to make the corrected preprint the preferred manuscript citation.
- [ ] Update README historical/publication section with the new DOI.
- [ ] Update `EXTERNAL_REPLICATION.md` persistent records section.
- [ ] Add a GitHub publication record containing:
  - [ ] new DOI;
  - [ ] publication timestamp;
  - [ ] final PDF SHA-256;
  - [ ] title/version;
  - [ ] relationship to historical v0.4.
- [ ] Commit the post-Zenodo metadata update separately from the scientific correction itself.

## Do not do

- Do not delete or overwrite the historical Version 0.4 record.
- Do not remove the historical "preregistered" title from archival citations to Version 0.4.
- Do not change frozen v0.4.3 experiment files.
- Do not describe the Level B replication as independent-lab or cross-family.
- Do not restore a "first" or equivalent priority claim.
