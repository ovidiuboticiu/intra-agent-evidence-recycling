# Stage 4 — Pre-Merge Audit

**Date:** 4 September 2026  
**Branch:** `forensic-validation-stage4`  
**PR:** #1  
**Status:** **DO NOT MERGE YET**

## 1. Purpose

This audit checks whether the Stage 4 transparency package is internally consistent before any change reaches `main`.

## 2. Checks passed

- PR #1 is mergeable and remains a draft.
- Frozen v0.4.3 experimental files are untouched.
- No numerical H1/H2 result is changed.
- The forensic addendum now distinguishes private corroborating chronology evidence from a public preregistration record.
- The correction log uses the same chronology standard.
- Zenodo metadata now points to the final visually verified v0.4 PDF.
- Final v0.4 DOCX/PDF pair renders cleanly at 12 pages.
- Final v0.4 PDF SHA-256:

`f1bdb42562c6e3f5bbce4d32c8eb08368a4f6669ee213e343d24106a0df07882`

- The README patch is fail-safe: it explicitly forbids changing the README pointer to a nonexistent v0.4 source file.

## 3. Remaining blocker

`docs/METHODOLOGICAL_NOTE_PREPRINT_v0_4.md` is not yet present on the Stage 4 branch.

Therefore:

- do not apply a README link to that path yet;
- do not describe the GitHub source package as complete for v0.4 yet;
- the Zenodo PDF can be prepared independently, but the repository should either receive the v0.4 source manuscript or the README should point directly to the final Zenodo DOI after publication.

This blocker does not affect the forensic addendum or the H1/H2 audit conclusions.

## 4. Recommended sequence

1. Keep PR #1 in draft state.
2. Publish or otherwise freeze the final v0.4 methodological-note artifact only after the final metadata check.
3. Add the v0.4 source manuscript to GitHub if practical; otherwise wait for the Zenodo DOI and link the README to the DOI rather than to a missing file.
4. Apply the living README clarification after the destination link is known.
5. Re-run a final PR diff review.
6. Only then mark PR #1 ready and merge.

## 5. Pre-merge verdict

**Scientific content:** PASS.  
**Numerical integrity:** PASS.  
**Transparency wording:** PASS after chronology refinement.  
**Artifact hash consistency:** PASS for final local PDF and branch metadata.  
**Repository completeness:** BLOCKED pending a valid v0.4 manuscript destination.  
**Merge authorization:** NOT YET.
