# Stage 4 — Pre-Merge Audit

**Date:** 4 September 2026  
**Branch:** `forensic-validation-stage4`  
**PR:** #1  
**Status:** **PASS — READY FOR REVIEW/MERGE**

## 1. Purpose

This audit checks whether the Stage 4 transparency package is internally consistent before any change reaches `main`.

## 2. Checks passed

- PR #1 is mergeable and was maintained as a draft during correction work.
- Frozen v0.4.3 experimental files are untouched.
- No numerical H1/H2 result is changed.
- The forensic addendum distinguishes private corroborating chronology evidence from a public preregistration record.
- The correction log uses the same chronology standard.
- Zenodo metadata points to the final visually verified v0.4 PDF.
- Final v0.4 DOCX/PDF pair renders cleanly at 12 pages.
- Final v0.4 PDF SHA-256:

`f1bdb42562c6e3f5bbce4d32c8eb08368a4f6669ee213e343d24106a0df07882`

- `docs/METHODOLOGICAL_NOTE_PREPRINT_v0_4.md` is now present on the Stage 4 branch.
- The README patch is fail-safe and no longer risks pointing to a nonexistent v0.4 source file.
- The living `README.md` is intentionally not modified in this PR. The proposed README wording is preserved in `docs/STAGE4_README_PATCH.md` and should be applied after the methodological-note Zenodo DOI is known, allowing the README to link directly to the final published record.

## 3. Residual limitations that are intentionally preserved

These are scientific/documentation limitations, not merge blockers:

- no public or independently verifiable pre-collection timestamp of the v0.4.3 preregistration artifact has been located;
- the privately archived preflight screenshot is corroborating project evidence, not a public registration record;
- H1 does not isolate derivative multiplicity from lexical repetition, target-consistent salience, explicit E1 references, and prompt length;
- exact bit-for-bit replication of the original v0.4.3 runtime is not guaranteed because every external runtime/model artifact detail was not pinned;
- external replication remains absent.

## 4. Post-merge sequence

1. Preserve the merged Stage 4 documentation as the public transparency record.
2. Publish the final methodological note v0.4 as a **new Zenodo preprint record**, not as a version of the empirical preprint DOI.
3. Record the new DOI.
4. Apply the README clarification patch and link directly to the new DOI plus the forensic addendum.
5. Decide separately whether the historical empirical preprint should receive a corrected version or a linked post-publication addendum; do not silently overwrite its historical record.

## 5. Pre-merge verdict

**Scientific content:** PASS.  
**Numerical integrity:** PASS.  
**Transparency wording:** PASS after chronology refinement.  
**Artifact hash consistency:** PASS for final local PDF and branch metadata.  
**Repository completeness:** PASS; v0.4 Markdown source is present.  
**Historical preservation:** PASS; frozen v0.4.3 files are untouched.  
**Merge authorization:** READY.
