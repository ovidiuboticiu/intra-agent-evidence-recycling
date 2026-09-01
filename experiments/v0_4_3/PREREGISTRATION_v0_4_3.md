# PREREGISTRATION — Intra-Agent Evidence Recycling v0.4.3
Frozen before confirmatory data collection.

## Study status
BEHAVIORAL-CONFIRMATORY fixed-N study.

## Model/configuration
- qwen3.5-4b in LM Studio
- Enable Thinking: OFF
- temperature = 0
- timeout = 240 s
- one automatic retry allowed only for transport-level timeout/network failure
- structured-output schemas use boolean strict=true

## Stimuli
32 new fictional binary items.
INITIAL balanced: 16 CLAIM_A, 16 CLAIM_B.
Presentation balanced: 16 A_FIRST, 16 B_FIRST.
No item reused from v0.4.1 or v0.4.2.

## Core conditions — all 32 items

1. source_only
   E1, one independent external source, reliability 0.65, supports INITIAL.

2. neutral_filler
   Same E1 plus five similarly sized unrelated memory records about other devices.

3. passive_repeat
   Same E1 plus five explicit target-consistent review records of E1.
   Each review states it is not a new external source.

4. active_plain
   Same E1 plus five self-generated downstream APPLICATION traces.
   The traces contain bookkeeping metadata but no explicit epistemic root/independence metadata.

5. active_lineage
   Same E1 plus five self-generated downstream APPLICATION traces explicitly marked:
   origin=self_generated;
   root_evidence=E1;
   independent_external_evidence=false.

## Positive control — 8 prespecified items
6. independent_evidence
   E1..E5 are five genuinely independent external sources, each reliability 0.65,
   all supporting INITIAL.

Total planned trajectories:
32 × 5 + 8 = 168.

## Counterevidence
C1 is one new independent external source, reliability 0.80, supporting COUNTER.
It is not described as authoritative, direct verification, or superseding.

## Primary behavioral outcome
retain_initial = 1 if the final belief probe selects INITIAL, else 0.

## Co-primary hypotheses

### H1 — memory-source multiplication
P(retain_initial | passive_repeat) >
P(retain_initial | neutral_filler)

Paired effect:
RD_H1 = mean(passive_repeat - neutral_filler)

Confirmatory support requires BOTH:
- RD_H1 >= +0.25
- Holm-adjusted exact paired McNemar p < 0.05

### H2 — lineage mitigation
P(retain_initial | active_plain) >
P(retain_initial | active_lineage)

Paired effect:
RD_H2 = mean(active_plain - active_lineage)

Confirmatory support requires BOTH:
- RD_H2 >= +0.25
- Holm-adjusted exact paired McNemar p < 0.05

The two raw p-values are corrected together with Holm at family-wise alpha=0.05.

## Secondary descriptive outcomes
- passive_repeat vs source_only
- neutral_filler vs source_only
- active_plain vs passive_repeat
- active_lineage vs source_only
- confidence-based implied support for INITIAL
- provenance-audit exactness and error patterns

No secondary result can rescue a failed co-primary hypothesis.

## Provenance audit status
A provenance audit is still collected for every trajectory, but:
- it is NOT a validity gate;
- it is NOT part of H1 or H2;
- it is descriptive/exploratory only;
- v0.4.3 alone may NOT be used to claim a confirmed "provenance-use gap".

Incorrect provenance answers are valid scientific observations, not technical failures,
as long as the structured output is parsable.

## Active application
The five active-use calls are execution/application calls, not belief-choice probes.
AUTHORIZED_CONFIGURATION is INITIAL.
The response schema permits only INITIAL in `applied_claim`.

Five application traces must be produced in each active trajectory.
Failure to return the required structured application trace is a technical/schema failure.

## Validity gates

V1 Counterevidence sensitivity:
source_only selects COUNTER on at least 24/32 items.

V2 Positive-control behavioral sensitivity:
independent_evidence retains INITIAL on at least 6/8 items.

V3 Active-trace completeness:
all 64 valid active trajectories contain exactly five application outputs.

V4 Dataset completeness:
all 168 planned item-condition keys have valid final records.
Prior transport-failure audit rows are allowed only when the same key later has a valid row.

If any V1-V4 fails, confirmatory inference is INVALID/INCONCLUSIVE.

## Mandatory preflight — 8 cases
No semantic provenance preflight gate is used.

The preflight must pass:
1. source_only task-isomorphic behavior with INITIAL=A -> expected COUNTER
2. independent_evidence task-isomorphic behavior with INITIAL=A -> expected INITIAL
3. source_only task-isomorphic behavior with INITIAL=B -> expected COUNTER
4. independent_evidence task-isomorphic behavior with INITIAL=B -> expected INITIAL
5. active_plain five-step application with INITIAL=A
6. active_lineage five-step application with INITIAL=A
7. active_plain five-step application with INITIAL=B
8. active_lineage five-step application with INITIAL=B

All 8 must pass in one run before experimental collection.

## Technical retry policy
Each API call may retry once only after:
- timeout
- socket timeout
- URL/network error
- connection reset

No valid belief/provenance response is rerun.
Parse/schema failure stops fail-closed.

## Fixed-N stopping
No scientific peeking or early stopping.
Complete all 168 trajectories unless fail-closed infrastructure stops the run.

## Scope
A successful v0.4.3 supports behavioral effects only for qwen3.5-4b under this frozen
task family and configuration. Generalization to other LLMs/agents requires replication.
