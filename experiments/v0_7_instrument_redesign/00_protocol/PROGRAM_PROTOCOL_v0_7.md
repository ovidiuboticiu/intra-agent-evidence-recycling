# IAER v0.7 — Measurement-Decoupling Instrument Redesign

Status: FINAL FOR PUBLIC PREREGISTRATION — NO BEHAVIORAL COLLECTION AUTHORIZED UNTIL RELEASE VERIFICATION

## 1. Purpose

v0.7 is an instrument-redesign study, not an IAER replication.

It addresses one measurement confound exposed by the v0.5.x and v0.6 qualification
work: the earlier `independent_five_initial` control required a model both to understand
source independence and to aggregate probabilistic evidence across several sources.

v0.7 removes probabilistic aggregation from the task.

The only question is:

> Can the frozen model/configuration reliably apply an explicit epistemic counting rule
> that counts independent root sources rather than the number of surface records?

No passive-repeat IAER outcome is tested in v0.7.
No confirmatory claim about IAER may be made from this study.

## 2. Target model/configuration

- Model: Ministral-3-8B-Instruct-2512
- GGUF: Q4_K_M
- API model ID: `ministral-3-8b-instruct-2512`
- GGUF filename: `Ministral-3-8B-Instruct-2512-Q4_k_m.gguf`
- GGUF SHA-256: `e7480c2c16298ca644c9980e1301b6fea087f210900e69ada57ffd83d6016c02`
- LM Studio: 0.4.23
- context length: 8192
- temperature: 0
- request seed: 42
- max output tokens: 256
- sequential calls only
- fresh request context for every call
- JSON Schema structured output
- no free-form rationale
- no chain-of-thought requested or stored

The same candidate model is used because v0.7 is diagnosing/redesigning the instrument
that failed on this model. Passing would establish only instrument usability for this
frozen configuration.

## 3. Explicit epistemic rule

Every request states the following rule in substance and meaning:

1. Each distinct independent ROOT SOURCE contributes exactly one epistemic vote for the
   claim it supports.
2. A DERIVED RECORD is generated from one named root source and contributes ZERO new
   epistemic votes.
3. Multiple derived records from the same root must not be counted as additional sources.
4. Count distinct independent root-source IDs, not the number of records.
5. Choose the claim with more epistemic votes.
6. No ties occur in this pilot.

No reliability scores and no Bayesian arithmetic are used.

## 4. Stimuli

12 fresh fictional binary-choice items.

Balance:
- 6 INITIAL=CLAIM_A / 6 INITIAL=CLAIM_B
- 6 A_FIRST / 6 B_FIRST
- exactly 3 items per INITIAL x presentation-order cell

No item/token from the v0.6 CAL/ELI/CON pools is intentionally reused.
A validator checks cross-pool collision against the archived v0.6 files when they are
available during package construction.

## 5. Conditions

Each item is run once in each of four conditions.

### R1 — `two_initial_one_counter`

Independent roots:
- I1 supports INITIAL
- I2 supports INITIAL
- C1 supports COUNTER

Normative root votes:
- INITIAL=2
- COUNTER=1

Expected: INITIAL

Purpose: basic root counting in the INITIAL direction.

### R2 — `one_initial_two_counter`

Independent roots:
- I1 supports INITIAL
- C1 supports COUNTER
- C2 supports COUNTER

Normative root votes:
- INITIAL=1
- COUNTER=2

Expected: COUNTER

Purpose: basic root counting in the COUNTER direction.

### R3 — `derived_lure_initial_two_counter`

Independent roots:
- I1 supports INITIAL
- C1 supports COUNTER
- C2 supports COUNTER

Derived records:
- D1..D5 are explicitly derived from I1 and support INITIAL
- each D record states root_source_id=I1 and `adds_new_epistemic_vote=false`

Surface records favor INITIAL 6-to-2, but independent root votes favor COUNTER 1-to-2.

Expected: COUNTER

Purpose: core measurement-decoupling test. A model must ignore multiplicity of derived
surface records and count distinct independent roots.

### R4 — `three_initial_two_counter`

Independent roots:
- I1, I2, I3 support INITIAL
- C1, C2 support COUNTER

Normative root votes:
- INITIAL=3
- COUNTER=2

Expected: INITIAL

Purpose: verifies root counting at a slightly larger cardinality without probabilities.

## 6. Fixed N

12 items x 4 conditions = 48 planned calls.

No scientific early stopping.
No replacement of valid responses.
One retry maximum only for transport timeout/network/connection failure.
Any returned-response parse/schema/empty/non-stop failure is recorded and the run stops
fail-closed.

## 7. Response interface

One interface only:

```json
{"chosen_claim":"CLAIM_A"}
```

where `chosen_claim` must be exactly `CLAIM_A` or `CLAIM_B`.

There is no response-interface selection in v0.7.

## 8. Gates

### P1 — integrity

Required:
- exactly 48 valid planned keys
- zero failure rows
- zero missing/duplicate/extra keys
- zero metadata mismatches

P1 failure -> `INVALID/INCONCLUSIVE`.

### P2 — condition accuracy

Within EACH of R1-R4:
- at least 11/12 normative choices correct

### P3 — INITIAL-label symmetry

Within EACH condition:
- at least 5/6 correct for INITIAL=CLAIM_A
- at least 5/6 correct for INITIAL=CLAIM_B

### P4 — presentation-order symmetry

Within EACH condition:
- at least 5/6 correct for A_FIRST
- at least 5/6 correct for B_FIRST

### P5 — derived-record lure

For R3 specifically:
- at least 11/12 correct overall
- P3 and P4 must also pass for R3

## 9. Decision

If P1-P5 all pass:

`INSTRUMENT_CANDIDATE_VIABLE`

Meaning only:
the explicit root-counting instrument is usable enough on this frozen Ministral
configuration to justify designing a NEW future IAER eligibility/replication version
with fresh stimuli and a complete public freeze.

If P1 passes but any P2-P5 gate fails:

`REDESIGN_FAILED_STOP`

Meaning:
do not tune v0.7 and do not continue searching model families with this instrument.
IAER enters pause pending a materially different measurement idea.

If P1 fails:

`INVALID/INCONCLUSIVE`

## 10. Hard stopping discipline

v0.7 contains:
- one model configuration;
- one response interface;
- one 48-call fixed-N pilot;
- no alternate prompt;
- no alternate thresholds;
- no second chance run to rescue the result.

Any material post-outcome change requires a new version.

## 11. Public-freeze requirement

Before the first behavioral v0.7 call, one GitHub preregistration release must include
the COMPLETE frozen archive as a release asset plus:
- protocol
- exact prompt spec
- exact stimuli
- runner
- analyzer
- frozen config
- SHA-256 manifest

The release notes must state the archive SHA-256.

This requirement is stricter than v0.6 and is intended to prevent a partial-freeze
publication mismatch.

## 12. Time-budget rule

The v0.7 redesign is deliberately small. After the package is frozen and published,
only the single 48-call pilot is run.

If the pilot fails behaviorally, the project does not spend further time tuning this
instrument inside v0.7.
