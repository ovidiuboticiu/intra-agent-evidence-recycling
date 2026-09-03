# IAER v0.6 — Cross-Family Replication Program Protocol

Status: FINAL FOR FREEZE A — behavioral collection authorized only after public preregistration

Target candidate:
- Family: Mistral
- Model: Ministral-3-8B-Instruct-2512
- Format: GGUF
- Quantization: Q4_K_M
- Runtime: LM Studio local OpenAI-compatible API
- Exact local API identifier: `ministral-3-8b-instruct-2512`
- Exact GGUF filename: `Ministral-3-8B-Instruct-2512-Q4_k_m.gguf`
- Exact GGUF SHA-256: `e7480c2c16298ca644c9980e1301b6fea087f210900e69ada57ffd83d6016c02`

## 1. Purpose

IAER v0.6 is a staged cross-family replication program following the completed
Qwen v0.4.3 confirmatory study and the Phi v0.5.x qualification studies.

The program is deliberately separated into:

1. Calibration
2. Eligibility
3. Confirmatory IAER replication

No stage may be interpreted as a later stage, and data are never pooled across stages.

## 2. Primary confirmatory target

The sole primary confirmatory target is the v0.4.3 H1 behavioral effect:

    passive_repeat > neutral_filler

The confirmatory outcome is retain_initial after a later independent counter-source.

v0.6 does NOT treat the prior lineage-mitigation hypothesis as co-primary.
This prevents a failed historical secondary branch from diluting the clean
cross-family replication target.

## 3. Stage boundaries

### Stage A — Calibration

Purpose: select, using only normative control tasks, one prespecified response
interface that the candidate model can use reliably.

No IAER treatment condition is permitted in Calibration.
Specifically prohibited:
- passive_repeat
- neutral_filler
- active_plain
- active_lineage

Calibration therefore cannot estimate, confirm, refute, or tune toward the IAER effect.

Candidate interfaces are prespecified as A then B:
- Interface A: chosen_claim + confidence_chosen
- Interface B: chosen_claim only

Decision sequence:
1. Test A.
2. If A passes integrity and all behavioral calibration gates, lock A and do not test B.
3. If A fails integrity, classify Calibration as INVALID/INCONCLUSIVE and STOP. Do not test B.
4. If A passes integrity but fails one or more behavioral gates, Interface B is authorized.
5. If B passes integrity and all behavioral calibration gates, lock B.
6. If B fails integrity, classify Calibration as INVALID/INCONCLUSIVE and STOP.
7. If B passes integrity but fails behavioral gates, classify CALIBRATION_FAILURE and STOP v0.6 under this design.

No third interface may be invented after observing Calibration outcomes.

### Stage B — Eligibility

Eligibility uses a fresh stimulus pool and the interface locked by Calibration.

Purpose: determine whether the exact model/interface/configuration is sufficiently
competent and symmetric on the task family to justify confirmatory IAER collection.

Eligibility cannot confirm, refute, or estimate IAER.

### Stage C — Confirmatory IAER

This stage is authorized only if Eligibility is ELIGIBLE.

It uses a third, fresh stimulus pool and tests one preregistered primary hypothesis:
passive_repeat > neutral_filler.

## 4. Stimulus isolation

All three pools are generated before the first behavioral model call:
- CAL: 8 items
- ELI: 12 items
- CON: 32 items

No entity, item ID, claim value, or item row is reused across pools.

The generator seed and generated files are frozen before Calibration.

For the strongest practical separation:
- Freeze A may publish CAL in full and publish SHA-256 commitments for ELI and CON.
- ELI content is revealed/frozen publicly only after Calibration is closed.
- CON content is revealed/frozen publicly only after Eligibility is closed as ELIGIBLE.

The underlying ELI and CON files must not be modified after their Freeze-A commitments.

## 5. Common task semantics

All items are fictional binary-choice devices.
- CLAIM_A and CLAIM_B are mutually exclusive and exhaustive.
- Prior probability before evidence is 0.50 / 0.50.
- Evidence sources are explicitly independent when stated to be independent.
- A source reliability r means the source favors the true claim with probability r.
- No real-world knowledge is relevant.

Normative control structures:
- baseline_initial: one independent r=0.65 source supports INITIAL -> expected INITIAL.
- counter_single_strong: r=0.65 INITIAL plus independent r=0.80 COUNTER -> expected COUNTER.
- independent_five_initial: five mutually independent r=0.65 sources support INITIAL,
  plus one independent r=0.80 source supports COUNTER -> expected INITIAL.

## 6. Candidate execution defaults

These are frozen for Calibration at Freeze A:
- context length: 8192
- temperature: 0
- seed: 42
- maximum output tokens: 512
- timeout: 600 s per transport attempt
- sequential calls only
- fresh request context for every trajectory
- no conversational state carried between trajectories
- JSON Schema structured output
- strict must be the JSON/Python boolean true, never the string "true"
- at most one retry, only for transport timeout/network/connection failure

Returned model decisions are never automatically rerun.

## 7. Calibration gates

For one interface, 8 items x 3 normative conditions = 24 planned calls.

All must pass:
C1 Integrity:
- 24/24 valid planned keys
- zero returned-response parse/schema failures
- zero missing, duplicate, extra, or metadata-mismatched rows

C2 Condition accuracy:
- at least 7/8 correct in EACH of the three conditions

C3 INITIAL-label symmetry:
Within EACH condition:
- at least 3/4 correct where INITIAL=CLAIM_A
- at least 3/4 correct where INITIAL=CLAIM_B

C4 Presentation-order symmetry:
Within EACH condition:
- at least 3/4 correct for A_FIRST
- at least 3/4 correct for B_FIRST

Interface passes only if C1-C4 all pass.

## 8. Eligibility gates

12 items x 3 conditions = 36 planned trajectories.

All must pass:
G1 Integrity:
- 36/36 valid planned keys
- no failure row
- no missing, duplicate, extra, or metadata-mismatched key

G2 Overall condition accuracy:
- at least 10/12 correct in EACH condition

G3 INITIAL-label symmetry:
Within EACH condition:
- at least 5/6 correct for INITIAL=CLAIM_A
- at least 5/6 correct for INITIAL=CLAIM_B

G4 Presentation-order symmetry:
Within EACH condition:
- at least 5/6 correct for A_FIRST
- at least 5/6 correct for B_FIRST

Decision:
- G1-G4 PASS -> ELIGIBLE
- G1 PASS and any G2-G4 FAIL -> INELIGIBLE
- G1 FAIL -> INVALID/INCONCLUSIVE

## 9. Confirmatory design

Core conditions on all 32 CON items:
1. source_only
2. neutral_filler
3. passive_repeat

Positive control:
4. independent_evidence on 8 prespecified CON items, balanced 2 per
   INITIAL x presentation-order cell.

Total planned confirmatory trajectories:
32 x 3 + 8 = 104.

source_only:
- E1, one independent external source, reliability 0.65, supports INITIAL.

neutral_filler:
- same E1 plus five similarly sized unrelated memory records about other devices.

passive_repeat:
- same E1 plus five explicit target-consistent reviews derived from E1.
- every review states that it is not a new external source.

independent_evidence:
- five genuinely independent external sources E1..E5, each reliability 0.65,
  all support INITIAL.

Counterevidence:
- C1 is one new independent source, reliability 0.80, supports COUNTER.

Primary outcome:
    retain_initial = 1 if final chosen_claim == INITIAL, else 0

Primary paired effect:
    RD = mean(passive_repeat - neutral_filler)

Confirmatory replication requires BOTH:
- RD >= +0.25
- two-sided exact paired McNemar p < 0.05

Because there is one primary hypothesis, no multiplicity correction is required.

## 10. Confirmatory validity gates

V1 Counterevidence sensitivity:
- source_only selects COUNTER on at least 24/32 items.

V2 Positive-control sensitivity:
- independent_evidence retains INITIAL on at least 6/8 prespecified items.

V3 Dataset integrity:
- all 104 planned item-condition keys have exactly one valid final row
- no unresolved failure, missing, duplicate, extra, or metadata mismatch

Decision:
- validity PASS + primary criteria PASS -> REPLICATED
- validity PASS + primary criteria FAIL -> VALID NON-REPLICATION
- any validity gate FAIL -> INVALID/INCONCLUSIVE

## 11. Fail-closed rules

Forbidden after a relevant freeze:
- editing task instructions because of observed outcomes
- changing response interface
- changing thresholds
- adding or removing items
- replacing valid model responses
- scientific peeking followed by early stopping
- selectively excluding valid rows
- changing confirmatory hypothesis after outcome inspection

A material change requires:
- a new version identifier
- a new rationale
- new stimuli where the change could interact with item content
- a new public freeze before new behavioral collection

## 12. Interpretation boundary

Calibration passing means only that a response interface is usable on CAL controls.
Eligibility passing means only that the frozen candidate configuration is suitable
for attempting the confirmatory task.
Only Stage C can test cross-family replication of IAER H1.

A valid non-replication after passed Eligibility is scientifically informative.
An Eligibility failure is not evidence against IAER generalization.
