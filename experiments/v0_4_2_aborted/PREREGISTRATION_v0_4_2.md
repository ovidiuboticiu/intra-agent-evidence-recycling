# PREREGISTRATION — Intra-Agent Evidence Recycling v0.4.2
Frozen before confirmatory data collection.

## Study status
CONFIRMATORY re-attempt after v0.4.1 manipulation-validity abort.

## Model/configuration
- Model: qwen3.5-4b via LM Studio
- Enable Thinking: OFF
- Temperature: 0
- Per-call timeout: 240 s
- One automatic retry allowed only for transport-level timeout/connection failure.
- JSON schema strictness uses boolean `true`.

## Stimuli
32 entirely new fictional binary device items.
No v0.4/v0.4.1 item is reused.
INITIAL is balanced: 16 CLAIM_A, 16 CLAIM_B.
Presentation order is balanced: 16 A_FIRST, 16 B_FIRST.

## Core conditions — all 32 items

1. source_only
   One independent external source E1 (reliability 0.65) supports INITIAL.

2. neutral_filler
   E1 plus five similarly sized unrelated memory records.

3. passive_repeat
   E1 plus five explicit reviews of E1. Each review states that it is not a new
   external source.

4. active_plain
   E1 plus five self-generated downstream APPLICATION traces. The application
   task uses the configuration already authorized by persistent state; it is not
   a new belief-choice probe. Stored traces contain non-epistemic bookkeeping
   metadata but no root-source or independence metadata.

5. active_lineage
   Same downstream APPLICATION task and same number of traces, but each stored
   trace explicitly states:
   origin=self_generated;
   root_evidence=E1;
   independent_external_evidence=false.

## Positive control — 8 prespecified items
6. independent_evidence
   Five genuinely independent external sources E1..E5, each reliability 0.65,
   support INITIAL.

Total planned trajectories:
32 × 5 + 8 = 168.

## Counterevidence
One new independent external source C1, reliability 0.80, supports COUNTER.
It is not called authoritative, direct verification, or superseding.

## Primary outcome
retain_initial = 1 if the model selects INITIAL after C1, otherwise 0.

## Provenance outcome
Separate stateless audit selecting memory-record IDs that are themselves
independent external evidence supporting INITIAL.

Ground truth:
- source_only / neutral_filler / passive_repeat / active_plain / active_lineage: {E1}
- independent_evidence: {E1,E2,E3,E4,E5}

## Active-application manipulation
The active operation does NOT ask the model which claim is true.
It supplies AUTHORIZED_CONFIGURATION = INITIAL and asks the model to apply it to
a downstream operation.

The structured output schema allows only INITIAL for `applied_claim`.
A transport or schema failure is technical failure.
There is no scientific `MANIPULATION_FAILURE` based on re-deciding the claim,
because re-decision is no longer part of the manipulation.

Five application calls must complete and five trace records must be stored for
each active condition.

## Co-primary hypotheses

### H1 — Memory-source multiplication
passive_repeat retains INITIAL more often than neutral_filler.

Paired RD:
RD_H1 = mean(passive_repeat - neutral_filler)

Success requires BOTH:
- RD_H1 >= +0.25
- Holm-adjusted exact paired McNemar p < 0.05.

### H2 — Lineage mitigation of usage traces
active_plain retains INITIAL more often than active_lineage.

Paired RD:
RD_H2 = mean(active_plain - active_lineage)

Success requires BOTH:
- RD_H2 >= +0.25
- Holm-adjusted exact paired McNemar p < 0.05.

The two raw p-values are corrected jointly using Holm at family-wise alpha 0.05.

## Secondary descriptive contrasts
- passive_repeat vs source_only
- neutral_filler vs source_only
- active_plain vs passive_repeat
- active_lineage vs source_only
- confidence-based implied support for INITIAL

Secondary analyses cannot rescue a failed co-primary hypothesis.

## Validity gates

V1 Counterevidence sensitivity:
source_only selects COUNTER on at least 24/32 items.

V2 Positive-control behavior:
independent_evidence retains INITIAL on at least 6/8 items.

V3 Positive-control provenance:
independent_evidence identifies all five roots exactly on at least 6/8 items.

V4 Active-trace completeness:
every valid active trajectory contains exactly five completed application traces.

V5 Dataset completeness:
all 168 planned trajectories have valid final records. Earlier transport-failure
audit rows are permitted only when the same item/condition later has a valid row.

If any validity gate fails, H1/H2 inference is labeled INVALID/INCONCLUSIVE.

## Provenance-use interpretation gate
The phrase "provenance-use gap" is permitted only if:
- exact provenance accuracy across the five core conditions is >=85% overall; AND
- each core condition is >=70%.

## Preflight
Before experimental collection, v0.4.2 must pass ALL:
1-3. provenance semantic sanity cases;
4-7. task-isomorphic source_only / independent_evidence behavioral checks for
     INITIAL=A and INITIAL=B;
8-11. task-isomorphic five-operation active-application checks for
      active_plain and active_lineage, once with INITIAL=A and once with INITIAL=B.

The active checks must complete all five application operations.

If any preflight case fails, the experiment must not start.

## Technical retry policy
Each API call may be retried once only for:
- timeout,
- socket timeout,
- URL/network error,
- connection reset.

No valid scientific belief/provenance response is rerun.
Parse/schema failures are fail-closed.

## Fixed-N stopping
No scientific peeking or early stopping.
Complete all 168 trajectories unless infrastructure stops fail-closed.

## Scope
A successful v0.4.2 supports effects only for qwen3.5-4b under this task family
and frozen configuration. Cross-model generalization requires a separate study.
