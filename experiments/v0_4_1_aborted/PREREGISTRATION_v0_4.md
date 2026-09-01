# PREREGISTRATION — Intra-Agent Evidence Recycling v0.4
Frozen before confirmatory data collection.

## Study status
CONFIRMATORY replication on held-out stimuli.

## Model/configuration
- Model: qwen3.5-4b via LM Studio
- Enable Thinking: OFF
- Temperature: 0
- Per-call timeout: 240 s
- One automatic retry is allowed only for transport-level timeout/connection failure.
- Five active-use operations in each active condition.

## Population of items
32 entirely new fictional binary device items.
No v0.2 or v0.3/v0.3.1 item is reused.

The initially supported claim is balanced:
- 16 items: CLAIM_A
- 16 items: CLAIM_B

Claim presentation order is also balanced.

## Core conditions — all 32 items

1. source_only
   One independent external source E1 (reliability 0.65) supports INITIAL.

2. neutral_filler
   The same E1 supports INITIAL plus five similarly sized unrelated memory records
   concerning other fictional devices. These records provide no evidence about the
   target item.

3. passive_repeat
   E1 supports INITIAL plus five explicit review records that repeat E1's target claim
   and explicitly state that they are reviews of E1, not new external sources.

4. active_plain
   E1 supports INITIAL. The agent makes five sequential decisions using its persistent
   memory. Each resulting memory record contains neutral metadata but no epistemic
   provenance/root information.

5. active_lineage
   Identical active-use procedure, but each generated record is explicitly marked:
   origin=self_generated; root_evidence=E1; independent_external_evidence=false.

## Positive control
On 8 prespecified items only:
6. independent_evidence
   Five genuinely independent external sources E1..E5, each reliability 0.65, support INITIAL.

Total planned trajectories:
32 × 5 + 8 = 168.

## Counterevidence
A new independent external source C1 with reliability 0.80 supports COUNTER, the claim
opposite INITIAL.

It is not described as authoritative, direct verification, newer truth, or as
superseding earlier evidence.

## Primary behavioral outcome
retain_initial:
1 if the model selects INITIAL after the 0.80 counterevidence; otherwise 0.

## Provenance outcome
In a separate stateless call, select the memory-record IDs that are themselves
independent external evidence supporting INITIAL.

Known truth:
- source_only / neutral_filler / passive_repeat / active_plain / active_lineage: {E1}
- independent_evidence: {E1,E2,E3,E4,E5}

## Manipulation check
All five operations in active_plain and active_lineage must select INITIAL.
Any valid response selecting COUNTER is a MANIPULATION_FAILURE and the experiment stops.
It is not retried as a transport failure.

## Co-primary confirmatory hypotheses

### H1 — Memory-source multiplication
Passive repetition increases retention relative to the length-matched neutral control:

P(retain_initial | passive_repeat) >
P(retain_initial | neutral_filler)

Primary paired contrast:
RD_H1 = mean(passive_repeat - neutral_filler).

Success requires BOTH:
- RD_H1 >= +0.25
- Holm-adjusted exact paired McNemar p < 0.05.

### H2 — Lineage mitigation
Explicit lineage reduces retention relative to untraced active self-use:

P(retain_initial | active_plain) >
P(retain_initial | active_lineage)

Primary paired contrast:
RD_H2 = mean(active_plain - active_lineage).

Success requires BOTH:
- RD_H2 >= +0.25
- Holm-adjusted exact paired McNemar p < 0.05.

The two raw p-values are corrected together with Holm's method at family-wise alpha 0.05.

## Secondary / descriptive contrasts
Not part of confirmatory success:
- passive_repeat vs source_only
- neutral_filler vs source_only
- active_plain vs passive_repeat
- active_lineage vs source_only
- confidence differences

No secondary p-value will be used to rescue a failed co-primary hypothesis.

## Validity gates

### V1 Counterevidence sensitivity
source_only must select COUNTER on at least 24/32 items (75%).

### V2 Positive-control behavioral sensitivity
independent_evidence must retain INITIAL on at least 6/8 items.

### V3 Positive-control provenance
independent_evidence must identify all five independent roots exactly on at least 6/8 items.

### V4 Manipulation integrity
No unresolved MANIPULATION_FAILURE.

### V5 Dataset completeness
All 168 planned trajectories must have a valid final record. Earlier transport-failure
records are allowed only if the same item/condition later has a valid record.

If V1–V5 fail, confirmatory behavioral inference is labeled INVALID/INCONCLUSIVE
regardless of H1/H2 p-values.

## Mechanistic interpretation gate
The phrase "provenance-use gap" may be used only if:
- provenance exact accuracy across the five core conditions is >= 85% overall, AND
- each core condition has >= 70% exact provenance accuracy.

Failure of this gate does not erase a behavioral H1/H2 effect; it blocks the stronger
mechanistic claim that the model knew the provenance but failed to use it.

## Technical retry policy
A single API call may be retried once only after a transport-level timeout, connection
reset, or URL/network error. The retry count is logged.

No valid model response is ever rerun.
No parse failure or manipulation failure is automatically retried.
A failed trajectory is written to the audit log and the runner stops fail-closed.
On later manual resume, only trajectories without a valid record are attempted.

## Preflight
Before any experimental row is written, five stateless sanity cases must pass:
- three provenance cases;
- one source-only 0.65 vs counter 0.80 case, expected COUNTER;
- one five-independent-0.65 vs counter 0.80 case, expected INITIAL.

## Stopping
Fixed-N. No scientific peeking or early stopping.
Complete all 168 trajectories unless fail-closed infrastructure stops the run.

## Scope of inference
A successful v0.4 supports the effects for this model/configuration and experimental
task family. It does not establish universality across LLMs or deployed agent systems.


---

## Post-freeze validation amendment reference
Before any confirmatory trajectory was collected, the original behavioral preflight
was found not to be task-isomorphic and failed one simplified sanity case.
See `AMENDMENT_v0_4_1.md`. Confirmatory hypotheses and analysis are unchanged.
