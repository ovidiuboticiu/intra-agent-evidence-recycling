# Experiment History

This document records the methodological evolution of the **Intra-Agent Evidence Recycling** project.

The purpose of this history is not to present every version as successful. It preserves the sequence of hypotheses, instrument failures, calibration decisions, technical amendments, and confirmatory attempts in a transparent audit trail.

## Research question

The project asks whether information originating from a single external source can acquire excess behavioral weight after it is repeated or reused within persistent LLM memory, despite the absence of additional genuinely independent evidence.

A related mitigation question asks whether explicit lineage metadata can reduce that behavioral effect.

The project does **not** equate behavioral resistance to counterevidence with proof that the model internally counts repeated records as independent sources.

# v0.2 — Early instrument

**Status:** CLOSED — measurement-limited

v0.2 compared several memory conditions, including independent evidence, active reuse, self-labeled reuse, lineage-labeled reuse, and passive repetition.

The run eventually produced a complete valid dataset after technical timeout events were separately rerun.

## Main limitations

1. `old_value` / `new_value` wording was semantically ambiguous.
2. `confidence_old` was not interpreted consistently as a 0–100 belief measure.
3. Counterevidence wording was too strong in places, producing a ceiling effect.
4. Source-count / provenance questions were not sufficiently concrete.

## Scientific status

The preregistered effect was not supported.

Because of the measurement problems, the result was treated as **measurement-limited rather than decisive evidence against the broader research question**.

# v0.3 / v0.3.1 — Calibration and discovery pilot

**Status:** COMPLETED — exploratory / calibration only

v0.3 introduced major repairs:

- `CLAIM_A` / `CLAIM_B` replaced ambiguous old/new wording;
- provenance was measured using concrete memory-record IDs;
- a `source_only` baseline was added;
- counterevidence was calibrated at multiple strengths;
- a semantic provenance preflight was required;
- the run was explicitly designated a **calibration pilot**, not a confirmatory study.

An initial v0.3 execution failed before any valid trajectory because a free-text `reason` field was truncated inside structured JSON.

Because `completed_valid=0`, the schema was technically amended before scientific data collection. The amended version is referred to as **v0.3.1**.

## v0.3.1 completion

The study completed:

- **48 / 48 valid trajectories**
- 8 fictional items
- 6 conditions per item

All preregistered calibration gates passed.

## Exploratory behavioral pattern at q = 0.80

| Condition | Retained initial claim |
|---|---:|
| `source_only` | 0 / 8 |
| `passive_repeat` | 8 / 8 |
| `active_plain` | 8 / 8 |
| `active_self_labeled` | 7 / 8 |
| `active_lineage` | 0 / 8 |
| `independent_evidence` | 8 / 8 |

These findings were treated as **exploratory**.

The key candidate phenomenon became broader than self-reuse alone:

> Multiple target-consistent memory records derived from a single epistemic root may produce substantially greater behavioral resistance to counterevidence than a single source alone.

The pilot also suggested that explicit lineage metadata might reduce this effect.

# v0.4.1 — First confirmatory attempt

**Status:** ABORTED — manipulation validity failure

v0.4.1 introduced:

- 32 new items;
- balanced initial claim labels;
- balanced claim presentation order;
- a neutral-filler control;
- paired exact tests;
- Holm family-wise correction;
- a minimum effect-size requirement.

## Abort event

The run produced 7 valid trajectories and then stopped at:

- item: `C16`
- condition: `active_lineage`
- operation: `O2`
- expected: `CLAIM_B`
- returned: `CLAIM_A`

The active manipulation asked the model to choose the claim again at each reuse step.

The preregistration defined any spontaneous switch during these steps as a `MANIPULATION_FAILURE`.

Therefore the study was stopped fail-closed and was not resumed.

## Interpretation

This was **not** treated as evidence against H1 or H2.

The experiment failed to implement the intended manipulation reliably.

# v0.4.2 — Second confirmatory attempt

**Status:** ABORTED BEFORE DATA COLLECTION — provenance preflight failure

v0.4.2 repaired the active manipulation.

Instead of asking the model to reassess the claim during every reuse step, the model performed a downstream **application task** using an already authorized configuration.

The inherited Structured Output bug was also repaired:

```python
"strict": True
```

replaced the non-standard string form:

```python
"strict": "true"
```

## Preflight outcome

Behavioral controls passed.

The repaired active manipulation also passed all active application checks.

However, one provenance sanity test failed:

- expected independent root: `["E1"]`
- returned: `[]`

Because provenance was still a mandatory preflight gate in v0.4.2, no confirmatory data collection began.

## Interpretation

The behavioral infrastructure and active-use manipulation were now stable, while explicit provenance auditing remained less robust.

Repeatedly rerunning the provenance preflight until it passed would have undermined the purpose of the gate.

The study was therefore aborted before data collection.

# v0.4.3 — Behavioral-confirmatory study

**Status:** IN PROGRESS

v0.4.3 retains the repaired active-application manipulation and the original behavioral co-primary hypotheses.

It uses another entirely fresh set of 32 fictional items.

## Key methodological decision

Provenance is still recorded but is no longer a validity gate.

It is now:

- secondary;
- descriptive / exploratory;
- excluded from the co-primary hypotheses;
- insufficient on its own to support a strong mechanistic "provenance-use gap" claim.

## Frozen co-primary hypotheses

### H1 — Memory-source multiplication

`passive_repeat` retains the initial claim more often than `neutral_filler`.

Confirmatory support requires:

- paired risk difference ≥ +0.25;
- Holm-adjusted exact paired McNemar p < 0.05.

### H2 — Lineage mitigation

`active_plain` retains the initial claim more often than `active_lineage`.

The same thresholds apply.

## Planned sample

- 32 core items
- 5 core conditions on every item
- 8 prespecified positive-control trajectories
- **168 total planned valid trajectories**

## Preflight

The behavioral preflight contains 8 mandatory cases covering:

- source-only and independent-evidence controls for INITIAL=A;
- source-only and independent-evidence controls for INITIAL=B;
- five-step `active_plain` application for INITIAL=A;
- five-step `active_lineage` application for INITIAL=A;
- five-step `active_plain` application for INITIAL=B;
- five-step `active_lineage` application for INITIAL=B.

All eight preflight cases passed before confirmatory collection was authorized.

## Current interpretation policy

No v0.4.3 result will be treated as confirmatory until:

1. all 168 planned trajectories are completed or the study is invalidated by a frozen validity rule;
2. the preregistered analysis is run;
3. the raw JSONL is audited independently;
4. the final status of H1 and H2 is reported without changing thresholds.

# Version classification summary

| Version | Classification | Included in confirmatory inference? |
|---|---|---|
| v0.2 | Early / measurement-limited | No |
| v0.3.1 | Calibration / exploratory | No |
| v0.4.1 | Aborted confirmatory attempt | No |
| v0.4.2 | Aborted pre-data confirmatory attempt | No |
| v0.4.3 | Behavioral-confirmatory | Pending completion |

# General methodological lessons

1. **Instrument failure is not hypothesis failure.**
2. **A pilot result is not confirmation.**
3. **Aborted attempts should remain visible in the scientific record.**
4. **Technical failures and scientific outcomes must be logged separately.**
5. **Confirmatory thresholds must be frozen before data collection.**
6. **Fresh stimuli should be used after a failed confirmatory attempt when redesign changes are material.**
7. **Behavioral effects should not be overinterpreted as proof of a specific internal mechanism.**
8. **A provenance audit is itself a measurement instrument and must be validated independently.**
9. **Structured-output compliance is part of reproducibility and portability.**
10. **Negative or failed confirmation is publishable if the protocol and audit trail are rigorous.**

# Next steps

After v0.4.3:

- freeze and audit the raw result file;
- run the preregistered confirmatory analysis;
- report H1 and H2 independently;
- prepare a reproducibility release;
- decide whether a dedicated provenance study is warranted;
- consider replication on additional models before making broad claims about LLM agents.
