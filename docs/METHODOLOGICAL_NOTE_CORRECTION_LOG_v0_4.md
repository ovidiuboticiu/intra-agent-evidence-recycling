# Methodological Note v0.4 — Correction and Transparency Log

**Manuscript:** *Before Calling It a Non-Replication: Instrument Qualification Across LLM Families*  
**Previous public draft:** v0.3  
**Revised preprint-ready version:** v0.4  
**Date:** 4 September 2026

## Revision principle

Version v0.4 is a transparency revision following post-publication forensic validation of the underlying v0.4.3 empirical target. It does not change raw data or the numerical H1/H2 results.

## Material wording changes

| v0.3 wording | v0.4 wording | Reason |
| --- | --- | --- |
| `equal-sized unrelated-memory control` | `equal-count control containing five unrelated memory records` | Equal record count is verified; exact length matching is not. |
| `strong preregistered effect` for v0.4.3 | `strong configuration-specific behavioral effect` in a pre-specified fixed-N study | A public/independent timestamp for the v0.4.3 preregistration artifact before the first behavioral call was not located. |
| `preregistered contrast` for v0.4.3 | `frozen pre-specified contrast` | Same chronology limitation. |
| `preregistered validity gates` for v0.4.3 | `frozen pre-specified validity gates` | Same chronology limitation. |
| `independently audited` | `post-run integrity audit and separate statistical recomputation` | Avoid implying third-party external audit. |

## New limitations added in v0.4

1. v0.4.3 has strong internal freeze consistency but lacks a located independent/public pre-collection timestamp of the preregistration document itself.
2. H1 does not isolate epistemic source dependence from lexical repetition, target-consistent salience, explicit E1 references, and prompt length.
3. The strongest claim is behavioral and configuration-specific; literal independent-source counting is not established.

## Forensic validation integrated in v0.4

The revised manuscript records that:

- the 168 planned keys were independently reconstructed;
- `retain_initial` was independently recomputed from `belief.chosen_claim`;
- H1 and H2 were exactly reproduced;
- all 22 H1 discordant pairs passed pair-level structural audit;
- no new behavioral data or LLM calls were introduced by the forensic audit.

## Unchanged scientific results

- H1: 22/32 vs 0/32, RD 0.6875, Holm p 9.5367432e-7 — supported under the frozen decision rule.
- H2: 2/32 vs 0/32, RD 0.0625, Holm p 0.50 — not supported.
- Cross-family generalization remains unresolved because Phi and Ministral did not reach a valid confirmatory target comparison.

## Versioning policy

The historical v0.3 draft is retained in Git history. v0.4 should be used for Zenodo publication of the methodological note. Historical v0.4.3 empirical files and the existing Zenodo empirical preprint should not be silently overwritten.
