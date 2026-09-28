# MDP-Candidate 0.6 — Pre-Data Closure Record

**Date:** 2026-09-28  
**Status:** **NO-GO — prospective lineage-metadata branch closed before behavioral collection**

## Purpose

This record documents the closure of the prospective Multiplicity Decomposition Pilot design discussed after IAER v0.7.

The working designs were referred to as **MDP-Candidate 0.5** and **MDP-Candidate 0.6**. They were prospective design drafts only. They were never frozen as an official IAER version and are not part of the completed v0.2–v0.7 empirical record.

## What was not done

For MDP-Candidate 0.5/0.6:

- no behavioral target calls were made;
- no confirmatory or exploratory target dataset was collected;
- no runner for this candidate was written or executed;
- no MDP preregistration/freeze was published;
- no result about Ministral, provenance use, or IAER was produced.

The decision below is therefore a **design-level stopping decision**, not an empirical negative result.

## Intended question

The candidate attempted to isolate a narrow follow-up question motivated by the ambiguous v0.7 derived-record lure result:

> When auxiliary records are already explicitly marked as non-independent and as contributing zero epistemic votes, does explicit lineage/root-link metadata change their behavioral influence?

The design was deliberately narrower than the original IAER hypothesis and was not intended to establish internal provenance graphs, source-counting mechanisms, or architecture-independent behavior.

## Design evolution

### Candidate 0.5

The initial U/L contrast compared auxiliary records with no real root link against otherwise matched records explicitly linked to a real evidence root.

The audit identified a confound: a sentinel such as `NONE`, `NO_ROOT`, or `R0` differs lexically and structurally from a real root identifier such as `R1`.

### Candidate 0.6

The revision kept the same candidate root identifier in both conditions and proposed changing only a linkage-validity field, for example:

```text
candidate_root_id = R1
root_link_valid = false | true
```

This removed the identifier-presence confound but introduced a more fundamental semantic ambiguity: `false` can be interpreted as an invalid, rejected, malformed, low-quality, or untrusted association rather than merely "no lineage link."

## Audit process

Before any code or behavioral collection, the design was subjected to adversarial review.

### Internal adversarial audit

The initial audit returned **REVISE**. It identified, among other issues:

- incomplete isolation of the root-link construct;
- ambiguity in the no-root encoding;
- insufficient prospective justification for N=64;
- lack of inherited justification for `|Delta_LINK| >= 0.25`;
- weaknesses in the proposed symmetry gates and positive control;
- strong prior-art overlap around repetition, redundancy, provenance, and evidential ancestry.

### External AI-model audit A — Codex

Codex returned **REVISE**.

Its central findings were:

- the boolean contrast identifies a text/metadata intervention, not a provenance mechanism;
- `Delta_LINK` is an interaction estimating differential linkage effects by AUX direction, not an omnibus "does linkage matter?" effect;
- item-level inference requires a defined stimulus-generating population;
- ordinary bootstrap intervals can behave poorly for sparse/degenerate discrete item-level interaction values;
- N=64 is not justified without a planning target and distributional assumptions;
- the broad conceptual space is already substantially occupied by prior art.

The audit is preserved at:

- [`docs/audits/MDP_CANDIDATE_0_6_CODEX_AUDIT_2026-09-28.md`](audits/MDP_CANDIDATE_0_6_CODEX_AUDIT_2026-09-28.md)

### External AI-model audit B — Claude

Claude returned **NO-GO**.

Its central findings were:

- `root_link_valid=false` versus `true` is naturally confounded with credibility/validity and record-quality semantics;
- the U condition can be internally ambiguous because `independent=false` is asserted while the named dependency is marked invalid;
- the primary interaction has floor/asymmetry problems and does not cleanly diagnose the v0.7 observation;
- a null result cannot distinguish "metadata has no effect" from "metadata was not behaviorally used/read";
- the statistical defects are repairable, but the construct ambiguity and prior-art overlap substantially reduce the expected scientific value;
- the closest surrounding prior art already studies provenance identifiers, distinct-origin instructions, ancestry, and redundant evidence.

The audit is preserved at:

- [`docs/audits/MDP_CANDIDATE_0_6_CLAUDE_AUDIT_2026-09-28.md`](audits/MDP_CANDIDATE_0_6_CLAUDE_AUDIT_2026-09-28.md)

These are **external AI-model audits**, not human peer review.

## Reconciled scientific judgment

The audits converged on the following points:

1. The candidate cannot cleanly isolate "provenance linkage" from the semantics of the representation used to express linkage.
2. Replacing one encoding with another changes the scientific question rather than eliminating semantics.
3. The proposed interaction estimand is narrower than the verbal question and can equal zero despite nonzero linkage effects in both directional arms.
4. N=64 and the historical 0.25 threshold do not transfer automatically to the new interaction estimand.
5. A sufficiently rigorous study would require a newly defined stimulus population, stronger qualification/symmetry procedures, a revised inferential plan, and substantially more design work and potentially more items.
6. Current prior art already occupies most of the broad space around repetition, redundant evidence, provenance identifiers, evidential ancestry, and origin-aware aggregation.
7. The remaining contribution would therefore be highly interface-specific.

The project judged that the expected information gain no longer justified another redesign cycle.

## Final decision

**NO-GO — MDP-Candidate 0.6**

The prospective post-v0.7 lineage-metadata redesign branch is closed before behavioral collection.

This decision:

- does **not** invalidate IAER v0.4.3;
- does **not** alter the direct-configuration replication record;
- does **not** constitute evidence for or against IAER on Ministral;
- does **not** establish that provenance metadata is behaviorally inert;
- does **not** establish a provenance mechanism.

It establishes only that this prospective instrument was judged insufficiently interpretable and insufficiently valuable to justify further collection.

## Restart boundary

No MDP 0.7/0.8 rescue sequence is authorized from this design.

Any future return must begin from a **materially new scientific question and measurement idea**, not from another encoding tweak to the same normatively-zero lineage-metadata contrast.

The existing IAER repository status therefore remains:

> **PAUSED — instrument redesign path exhausted under v0.7.**

The completed historical evidence and all prior stopping decisions remain unchanged.
