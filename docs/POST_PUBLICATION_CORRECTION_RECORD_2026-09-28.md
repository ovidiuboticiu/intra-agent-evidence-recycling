# IAER Post-Publication Correction Record — 2026-09-28

## Purpose

This document records the GitHub-side correction actions completed after post-publication forensic and prior-art review of the historical IAER empirical preprint.

It does not replace the historical publication. It documents what changed, what did not change, and what remains pending outside GitHub.

## Historical record

Historical empirical preprint:

- title: *When One Source Returns: A Preregistered Behavioral Study of Intra-Agent Evidence Recycling*
- Version 0.4
- DOI: `10.5281/zenodo.22282120`
- publication date: 2026-09-03

The historical PDF, title, DOI, and frozen v0.4.3 experiment are preserved.

## Corrections now recorded on GitHub

### 1. Priority claim withdrawn

The historical bounded statement that IAER was, "to our knowledge," the first preregistered controlled test of the complete operational combination is **withdrawn**.

Reason: the later literature reassessment showed that the evidential basis was not sufficient for a responsible priority claim. Some highly relevant work had not been identified before publication, while some close work already cited in Version 0.4 had not been weighted conservatively enough when the "first" wording was formulated.

Canonical notice:

`docs/IAER_PRIORITY_CLAIM_WITHDRAWAL_2026-09-28.md`

### 2. v0.4.3 preregistration wording narrowed

Current wording:

> **pre-specified and frozen before collection**

The project does not currently use "publicly preregistered before collection" for v0.4.3 because the forensic chronology audit did not locate a public or independently verifiable pre-collection timestamp of the preregistration artifact itself.

This does not alter the internal freeze evidence or the numerical result.

### 3. Neutral control wording corrected

Historical shorthand such as "length-matched" or "equal-sized" is replaced in current summaries by:

> **equal-count unrelated-memory control**

The verified design matched record count, not exact text/token length.

### 4. Level B replication integrated

A fresh 2026-09-27 Level B direct-configuration replication of the frozen v0.4.3 protocol was completed and archived.

- H1: 24/32 vs 0/32; RD = 0.75; Holm-adjusted p = 2.38419e-7 — **SUPPORTED**;
- H2: 3/32 vs 0/32; RD = 0.09375; p = 0.25 — **NOT SUPPORTED**;
- 168/168 planned keys valid;
- V1–V4 passed.

Scope:

- same project;
- same direct-configuration class under the frozen protocol;
- not independent-lab;
- not cross-family;
- not bit-for-bit runtime reproduction because the historical original GGUF artifact was not hash-pinned.

### 5. Citation metadata made fail-safe

Because no corrected Zenodo preprint version is currently planned, `CITATION.cff` does not recommend the historically superseded v0.4 preprint as the preferred citation. It points to the v0.4.3 software/reproducibility archive:

`10.5281/zenodo.22259801`

If a corrected Zenodo version is ever published later, `CITATION.cff` can be updated then.

## What remains unchanged

The following are not altered by this correction:

- frozen v0.4.3 raw data;
- frozen stimuli, runner, and analysis artifacts;
- 168/168 valid original trajectories;
- original H1: 22/32 vs 0/32; RD = 0.6875; Holm-adjusted p = 9.5367432e-7;
- original H2: 2/32 vs 0/32; RD = 0.0625; Holm-adjusted p = 0.50;
- provenance exactness 168/168 as a descriptive/exploratory outcome;
- aborted and failed historical attempts;
- later v0.5–v0.7 stop decisions;
- historical GitHub tags/releases and their immutable audit role.

## Current contribution boundary

The current defensible empirical statement is:

> Under the frozen v0.4.3 task family and Qwen direct-configuration class, five explicitly derivative, target-consistent reviews of one initial source substantially increased retention of the source-supported claim relative to five unrelated memory records, and this behavioral contrast was reproduced in a fresh same-project Level B collection.

The project does **not** claim:

- conceptual priority for repetition or dependent-evidence effects;
- a literal internal source-counting mechanism;
- independent-lab replication;
- cross-family generality.

## GitHub correction commit chain

The scientific-integrity principle and the priority-claim correction were integrated into `main` through explicit pull requests rather than by silently rewriting historical release artifacts.

The GitHub-side finalization changes were merged through **PR #7** (`Finalize GitHub record after IAER correction`) at merge commit `b3fc62669cb928f36a9b354efe2ef2f73b560880`.

## External Zenodo correction — completed 2026-09-28

A corrected empirical preprint draft remains preserved at:

`docs/IAER_EMPIRICAL_PREPRINT_CORRECTED_DRAFT_2026-09-28.md`

No new Zenodo preprint version was created. Instead, the existing historical Version 0.4 record (`10.5281/zenodo.22282120`) received a **metadata/description-only post-publication correction**.

The public record now states that:

- the historical priority claim is withdrawn;
- v0.4.3 is described as **pre-specified and frozen before collection** rather than publicly preregistered before collection;
- the neutral control is described as an **equal-count control containing five unrelated memory records** rather than length-matched;
- the original v0.4.3 numerical results are unchanged;
- the 2026-09-27 Level B same-project direct-configuration replication reproduced H1 while H2 remained unsupported;
- the Level B replication is not independent-lab, not cross-family, and not bit-for-bit runtime reproduction.

The historical PDF, title, Version 0.4 identifier, and DOI were not replaced or deleted.

GitHub issue #8 tracked this action and is closed after verification of the public Zenodo page.

See:

`docs/ZENODO_CORRECTED_VERSION_CHECKLIST_2026-09-28.md`
