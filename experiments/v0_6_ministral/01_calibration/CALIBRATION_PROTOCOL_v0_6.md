# IAER v0.6 — Calibration Protocol

Status: FINAL FOR FREEZE A — do not collect before public preregistration

## Purpose

Calibration selects one response interface using only normative evidence-integration controls. It does not contain any IAER manipulation and cannot estimate IAER.

## Candidate interfaces

Interface A — canonical:
- chosen_claim: CLAIM_A | CLAIM_B
- confidence_chosen: 0..100
- chosen_claim is the only behavioral field
- confidence is descriptive only

Interface B — minimal:
- chosen_claim: CLAIM_A | CLAIM_B

The semantic evidence prompt, source records, reliabilities, item contents, system instruction, temperature, seed, and task conditions are identical across interfaces. Only the required response representation and the final response-format instruction differ.

## Selection rule

A is always tested first.

A outcomes:
- Integrity FAIL -> INVALID/INCONCLUSIVE; STOP; B forbidden.
- Integrity PASS + all behavioral gates PASS -> INTERFACE_A_LOCKED; B forbidden.
- Integrity PASS + any behavioral gate FAIL -> INTERFACE_A_FAILED_BEHAVIORALLY; B authorized.

B outcomes, if authorized:
- Integrity FAIL -> INVALID/INCONCLUSIVE; STOP.
- Integrity PASS + all behavioral gates PASS -> INTERFACE_B_LOCKED.
- Integrity PASS + any behavioral gate FAIL -> CALIBRATION_FAILURE; STOP v0.6 under this design.

No third interface exists in v0.6.

## Stimuli

8 fresh CAL items, exactly:
- 4 INITIAL=CLAIM_A, 4 INITIAL=CLAIM_B
- 4 A_FIRST, 4 B_FIRST
- 2 in every INITIAL x presentation-order cell

## Conditions

Each CAL item is run once in each condition.

baseline_initial:
- one independent external source reliability 0.65 supports INITIAL
- expected choice INITIAL

counter_single_strong:
- one independent source reliability 0.65 supports INITIAL
- one new independent source reliability 0.80 supports COUNTER
- expected choice COUNTER

independent_five_initial:
- five mutually independent sources reliability 0.65 support INITIAL
- one new independent source reliability 0.80 supports COUNTER
- expected choice INITIAL

24 planned calls per tested interface.

## Gates

C1 — Integrity:
- exactly 24 valid planned keys
- zero failure rows
- zero missing, duplicate, extra, or metadata-mismatched rows

C2 — Overall condition accuracy:
- at least 7/8 normative choices correct in EACH condition

C3 — INITIAL symmetry:
Within EACH condition:
- at least 3/4 correct for INITIAL=CLAIM_A
- at least 3/4 correct for INITIAL=CLAIM_B

C4 — Presentation-order symmetry:
Within EACH condition:
- at least 3/4 correct for A_FIRST
- at least 3/4 correct for B_FIRST

## Blinding and stopping

Collection order is deterministically shuffled with a frozen interface-specific seed. The runner prints progress counts but not chosen claims, correctness, or confidence. No scientific peeking or early stopping is allowed.

A returned model response is never rerun. One retry is allowed only for transport timeout/network/connection failure.

A parse error, schema violation, empty content, non-stop finish reason, metadata mismatch, or exhausted transport retry writes a failure row and stops fail-closed.

After a pure external interruption that created no failure row, unchanged frozen collection may resume. Existing valid keys are skipped and never rerun.
