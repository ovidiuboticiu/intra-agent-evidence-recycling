# IAER v0.4.3 — Post-Publication Forensic Validation Addendum v1.0

**Date:** 4 September 2026  
**Scope:** IAER v0.4.3 only  
**New behavioral data:** none  
**New LLM calls:** none  
**Purpose:** document post-publication checks that test data integrity, statistical reproducibility, pair-level implementation fidelity, claim boundaries, and publication wording.

## 1. Why this addendum exists

After publication of the v0.4.3 empirical result, the project conducted an adversarial forensic validation intended to find errors rather than defend the original conclusion. The audit was explicitly allowed to weaken or invalidate the result if a material defect was found.

The frozen v0.4.3 experiment files and raw data were not modified.

## 2. Data and statistical integrity

The forensic reanalysis used the archived raw `results_v0_4_3.jsonl` dataset with SHA-256:

`5af33c11104bdd18dce9e945d5f2fce885f93c6cb1322f9b2f2469c38082cc54`

Expected item-condition keys were reconstructed independently from the frozen stimulus table and study design rather than inferred from observed rows.

Results:

- 168 JSONL rows;
- 168 valid rows;
- 168 expected unique keys;
- 0 missing keys;
- 0 extra keys;
- 0 duplicate valid keys;
- 0 stored-versus-recomputed outcome mismatches.

The behavioral outcome was recomputed directly from `belief.chosen_claim` and `initial_supported_claim`, without trusting the stored `retain_initial` field. All 168 stored outcomes matched the independent reconstruction.

The independent reanalysis reproduced the published co-primary results exactly:

| Hypothesis | Retention | Paired RD | Exact two-sided p | Holm p | Status |
| --- | ---: | ---: | ---: | ---: | --- |
| H1 `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 0.6875 | 4.76837158203125e-7 | 9.5367431640625e-7 | Supported |
| H2 `active_plain > active_lineage` | 2/32 vs 0/32 | 0.0625 | 0.50 | 0.50 | Not supported |

All four frozen validity gates were also independently reproduced.

**Forensic conclusion:** no material computational, pairing, scoring, completeness, or statistical error was found.

## 3. Pair-level red-team of H1

All 22 discordant pairs responsible for the binary H1 effect were inspected individually.

For every pair:

- the same frozen item was used in both conditions;
- E1 was identical across the pair;
- both conditions contained six memory records;
- all five neutral records had the prescribed unrelated-memory structure;
- all five passive records had the prescribed derivative-review structure;
- every passive derivative explicitly stated that it was not a new external source;
- neutral selected COUNTER and passive selected INITIAL;
- provenance classification was exact in both members;
- the belief calls used one transport attempt.

**22/22 pair-integrity checks passed.**

## 4. Secondary behavior and representation sensitivity

The confidence-derived implied support for INITIAL moved in the passive direction on 32/32 H1 pairs, with a mean paired increase of approximately 48.13 percentage points relative to neutral filler. This is secondary/descriptive evidence only; confidence is not treated as calibrated probability.

The binary H1 effect was exactly symmetric by INITIAL label:

- INITIAL=`CLAIM_A`: 11/16 passive retains;
- INITIAL=`CLAIM_B`: 11/16 passive retains.

A post-hoc presentation-order signal was observed:

- `A_FIRST`: 14/16 passive retains;
- `B_FIRST`: 8/16 passive retains;
- Fisher exact two-sided p approximately 0.0538.

This analysis was not preregistered as a moderator test. It is hypothesis-generating only and should not be reported as confirmed moderation.

## 5. Central construct-isolation limitation

The H1 manipulation is behaviorally clear but is not a pure manipulation of epistemic dependence.

Both `neutral_filler` and `passive_repeat` contain six memory entries, but the passive condition additionally repeats target-consistent INITIAL information five times and contains more explicit E1 references. Recorded final belief prompts are also longer on average in the passive condition.

Therefore v0.4.3 jointly changes:

- derivative-memory multiplicity;
- lexical repetition of INITIAL;
- target-consistent salience;
- explicit references to the root source;
- prompt/token length.

These factors cannot be separated retrospectively.

### Strongest supported claim

> Under the frozen v0.4.3 task family and Qwen configuration, five explicitly derivative, target-consistent reviews of one initial source substantially increased retention of the initial claim relative to five unrelated memory records.

### Not established

> The model internally counted the five derivative reviews as five independent evidence sources.

The provenance probe was exact, which further requires behavioral weighting and explicit provenance judgment to remain distinct constructs.

## 6. Preregistration / chronology clarification

The v0.4.3 package contains a frozen pre-specification of hypotheses, gates, stimuli, runner, and analysis, and stable package hashes are embedded consistently across all 168 result rows. A timestamped pre-collection screenshot also shows the mandatory behavioral preflight completed immediately before confirmatory collection with `completed_valid=0`.

However, the forensic chronology audit did not locate a separate public or independently timestamped copy of the v0.4.3 preregistration artifact before the first behavioral call. The earliest public GitHub repository commit occurred after collection had already begun.

Accordingly, new project summaries should prefer:

> **pre-specified and frozen before collection**

rather than the stronger phrase:

> **publicly preregistered before collection**

for v0.4.3.

This is a documentation/prospectivity-verification limitation. It does not alter the numerical H1/H2 results.

Later versions with independently verifiable public preregistration before collection, including v0.5.2 and v0.7, retain that terminology.

## 7. Control-matching wording clarification

The v0.4 empirical manuscript used wording such as `length-matched neutral memory`; some repository summaries used `equal-sized unrelated-memory control`.

The forensic audit verified equal **record count**, not exact textual/token length matching.

Preferred wording for future summaries:

> **an equal-count control containing five unrelated memory records**

or simply:

> **five unrelated memory records**

## 8. Audit-independence wording clarification

The existing public record uses `independently audited` in places. Unless an external human/institutional auditor is explicitly identified, that phrase can be read as third-party review.

Preferred wording:

> **post-run integrity audit and separate statistical recomputation**

This describes what was actually performed without implying external peer review.

## 9. What is unchanged

The forensic validation does **not** change:

- the 168/168 completeness result;
- the H1 numerical result;
- the H2 numerical result;
- the original raw dataset;
- the frozen v0.4.3 files;
- the cross-family status, which remains unresolved rather than falsified.

No historical artifact should be silently rewritten.

## 10. Recommended public-record action

1. Preserve the original Zenodo v0.4 preprint and v0.4.3 software archive as historical versions.
2. Link this addendum or a corrected preprint version from future project summaries.
3. Use corrected terminology in the methodological note before assigning it a DOI.
4. Update the living GitHub README transparently, with a commit message that explicitly states that wording is being clarified after forensic validation.
5. Do not claim literal source-counting mechanism from v0.4.3.
6. Do not run a rescue experiment to remove these limitations retrospectively; a future mechanistic study should use a new, prospectively frozen design.

## 11. Overall forensic verdict

**No material data or statistical error found.**  
**H1 numerical status preserved.**  
**Mechanistic interpretation remains unresolved.**  
**Publication wording requires narrowing in several places.**  
**Independent external replication remains desirable.**
