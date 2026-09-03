# IAER v0.7 — Preregistration: Measurement-Decoupling Pilot

Status: FINAL FOR PUBLIC FREEZE

This preregistration must be made public, together with the complete frozen archive
asset, before the first behavioral v0.7 call.

## Scientific role

v0.7 is an **instrument-redesign pilot**, not an IAER replication and not an
eligibility study for a confirmatory run.

It tests whether the frozen Ministral configuration can apply an explicit epistemic
counting rule based on **independent root sources**, while assigning zero new epistemic
weight to records explicitly marked as derived from an existing root.

The study deliberately removes reliability scores and Bayesian aggregation.

## Frozen candidate

- model: Ministral-3-8B-Instruct-2512
- format: GGUF Q4_K_M
- API model ID: `ministral-3-8b-instruct-2512`
- GGUF filename: `Ministral-3-8B-Instruct-2512-Q4_k_m.gguf`
- GGUF size: 5198386976 bytes
- GGUF SHA-256: `e7480c2c16298ca644c9980e1301b6fea087f210900e69ada57ffd83d6016c02`
- LM Studio: 0.4.23
- context length: 8192
- temperature: 0
- seed: 42
- max output tokens: 256
- sequential calls only
- no chain-of-thought requested or stored
- JSON Schema structured output with boolean `strict=true`

## Fixed task rule

1. Each distinct independent ROOT SOURCE contributes exactly one epistemic vote.
2. A DERIVED RECORD contributes zero new epistemic votes.
3. Multiple derived records from the same root do not add votes.
4. Count distinct independent root-source IDs, not surface records.
5. Choose the claim with more root votes.
6. There are no ties.

## Fixed stimuli and N

12 fresh balanced fictional items.

Balance:
- 6 INITIAL=CLAIM_A / 6 INITIAL=CLAIM_B
- 6 A_FIRST / 6 B_FIRST
- 3 items in every INITIAL x presentation-order cell

Four conditions per item, for exactly 48 planned calls.

### R1 `two_initial_one_counter`
2 independent INITIAL roots vs 1 COUNTER root.
Expected: INITIAL.

### R2 `one_initial_two_counter`
1 independent INITIAL root vs 2 COUNTER roots.
Expected: COUNTER.

### R3 `derived_lure_initial_two_counter`
1 independent INITIAL root plus 5 derived records from that same root vs
2 independent COUNTER roots.

Surface-record count favors INITIAL 6-to-2.
Independent-root count favors COUNTER 1-to-2.
Expected: COUNTER.

### R4 `three_initial_two_counter`
3 independent INITIAL roots vs 2 COUNTER roots.
Expected: INITIAL.

## Response interface

Exactly one behavioral field:

```json
{"chosen_claim":"CLAIM_A"}
```

Allowed values: `CLAIM_A`, `CLAIM_B`.

No alternate response interface exists in v0.7.

## Frozen gates

### P1 Integrity
- 48/48 valid planned keys
- zero failure rows
- zero missing, duplicate, extra, or metadata-mismatched keys

P1 failure -> `INVALID/INCONCLUSIVE`.

### P2 Condition accuracy
At least 11/12 correct in EACH of R1-R4.

### P3 INITIAL-label symmetry
Within EACH condition:
- at least 5/6 correct for INITIAL=CLAIM_A
- at least 5/6 correct for INITIAL=CLAIM_B

### P4 Presentation-order symmetry
Within EACH condition:
- at least 5/6 correct for A_FIRST
- at least 5/6 correct for B_FIRST

### P5 Derived-record lure
R3 must satisfy:
- at least 11/12 correct overall
- P3 PASS for R3
- P4 PASS for R3

## Frozen decision

If P1-P5 all pass:

`INSTRUMENT_CANDIDATE_VIABLE`

This means only that the explicit root-counting instrument is usable enough on this
frozen Ministral configuration to justify designing a **new future IAER version** with
fresh stimuli and its own preregistration.

If P1 passes but any P2-P5 gate fails:

`REDESIGN_FAILED_STOP`

IAER enters pause under this redesign path. No v0.7 tuning or rescue run is allowed.

If P1 fails:

`INVALID/INCONCLUSIVE`

## Execution rules

- fixed N = 48
- deterministic frozen collection order
- no scientific peeking
- no outcome-based early stopping
- no rerun of returned model decisions
- maximum one retry only for transport timeout/network/connection failure
- parse/schema/empty/non-stop response failure is retained and stops fail-closed
- after a pure external interruption with no recorded failure row, unchanged collection
  may resume and skips existing valid keys

## Interpretation boundary

v0.7 cannot confirm, refute, or estimate IAER.

It tests only whether this explicit root-counting measurement instrument is behaviorally
usable on the frozen candidate configuration.

## Public-freeze completeness rule

Behavioral collection is forbidden until BOTH are true:

1. the GitHub commit contains all frozen textual/code/stimulus materials;
2. a GitHub preregistration release contains the complete frozen ZIP archive as an asset.

The release notes must record the ZIP SHA-256.

The local runner additionally requires a post-publication authorization file containing:
- release tag
- exact 40-character commit SHA
- exact 64-character archive SHA-256

This rule is a direct procedural safeguard against the incomplete-publication problem
documented during v0.6 closure.
