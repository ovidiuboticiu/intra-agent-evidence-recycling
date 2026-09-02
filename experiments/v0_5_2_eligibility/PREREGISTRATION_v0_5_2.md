# PREREGISTRATION — IAER v0.5.2 eligibility pilot

Frozen before any v0.5.2 behavioral outcome is collected.

## Study status

Fixed-N behavioral **eligibility pilot**, not a confirmatory IAER hypothesis test.

The pilot asks whether the candidate model and one prespecified response interface are sufficiently reliable to justify a future, separately preregistered cross-family replication. Eligibility cannot confirm, refute, or estimate the v0.4.3 memory-source multiplication effect.

## Candidate model and execution configuration

- Model: Microsoft Phi-4-mini-reasoning, GGUF Q4_K_M
- LM Studio API identifier: `microsoft_phi-4-mini-reasoning`
- Model SHA-256: `ce8becd58f350d8ae0ec3bbb201ab36f750ffab17ab6238f39292d12ab68ea06`
- LM Studio local OpenAI-compatible API
- Context length: 8192
- temperature: 0
- seed: 42
- maximum output tokens: 2048
- timeout: 600 seconds per transport attempt
- at most one automatic retry, and only after a timeout/network/connection failure
- sequential calls; no concurrent predictions
- JSON Schema structured output with boolean `strict=true`

The neutral technical smoke test passed before this freeze. Its raw machine-readable result is included and is not a behavioral outcome.

## Stimuli and balancing

Twelve new fictional binary-choice items are fixed in `stimuli_v0_5_2.csv`.

- INITIAL orientation: 6 `CLAIM_A`, 6 `CLAIM_B`
- presentation order: 6 `A_FIRST`, 6 `B_FIRST`
- full crossing: 3 items in each INITIAL × presentation-order cell
- the two claims are mutually exclusive and exhaustive
- prior probability before evidence is 50/50
- source reliability has its explicit probabilistic meaning
- no real-world knowledge is relevant

## Prespecified response interface

Every trajectory uses exactly one response representation:

- `chosen_claim`: `CLAIM_A` or `CLAIM_B`
- `confidence_chosen`: number from 0 through 100

The response representation will not be changed or selected after observing outcomes. `chosen_claim` is the behavioral outcome; confidence is descriptive only.

## Conditions

Each of the 12 items is run once in each condition.

### 1. `baseline_initial`

One independent external source with reliability 0.65 supports INITIAL. No counterevidence is supplied.

Normative expected choice: INITIAL.

### 2. `counter_single_strong`

One independent external source with reliability 0.65 supports INITIAL. One new independent source with reliability 0.80 supports COUNTER.

Normative expected choice: COUNTER.

### 3. `independent_five_initial`

Five mutually independent external sources, each with reliability 0.65, support INITIAL. One new independent source with reliability 0.80 supports COUNTER.

Normative expected choice: INITIAL.

Total planned trajectories: 12 × 3 = 36.

## Prespecified eligibility gates

All gates must pass.

### G1 — completeness and integrity

- all 36 planned item-condition keys have exactly one valid row;
- no recorded failure row exists;
- every row matches the frozen model identifier, model SHA-256, temperature, seed, and manifest SHA-256.

### G2 — overall condition accuracy

At least 10 of 12 normative choices are correct in **each** condition.

### G3 — INITIAL-orientation symmetry

Within each condition:

- at least 5 of 6 items with INITIAL=`CLAIM_A` are correct; and
- at least 5 of 6 items with INITIAL=`CLAIM_B` are correct.

### G4 — presentation-order symmetry

Within each condition:

- at least 5 of 6 `A_FIRST` items are correct; and
- at least 5 of 6 `B_FIRST` items are correct.

## Decision rule

- If G1-G4 all pass: `ELIGIBLE` for designing a fresh v0.6.0 confirmatory preregistration.
- If G1 passes but any of G2-G4 fails: `INELIGIBLE` under this model/interface/configuration.
- If G1 fails: `INVALID/INCONCLUSIVE`; do not interpret behavioral accuracy.

No statistical-significance claim is made. Thresholds are engineering eligibility criteria fixed before outcomes.

## Randomization and stopping

- Item-condition execution order is deterministically shuffled with frozen seed `20260902`.
- No outcome is printed during collection.
- No scientific peeking, early stopping, adaptive prompt editing, or valid-response reruns.
- Collection ends only after all 36 valid keys or after a fail-closed error.

## Failure and resumption policy

The runner may retry once only for transport-level timeout/network/connection failure. It does not retry a returned model response.

A parse error, empty final answer, non-`stop` finish reason, schema violation, metadata mismatch, or exhausted transport retry writes a failure row and stops the pilot. Once a failure row exists, frozen collection must not be resumed or repaired in place.

After an external interruption that leaves no failure row, rerunning the frozen runner is permitted. It skips already valid keys and never reruns them.

## Interpretation boundary

Passing establishes only task-interface eligibility for this quantized model under the frozen configuration. It is not evidence that the v0.4.3 IAER effect generalizes. A future v0.6.0 study must use new stimuli, a new public preregistration, and confirmatory validity gates.
