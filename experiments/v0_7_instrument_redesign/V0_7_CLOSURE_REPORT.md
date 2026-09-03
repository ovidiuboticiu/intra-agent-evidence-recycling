# IAER v0.7 — Measurement-Decoupling Pilot Closure Report

## Final status

**REDESIGN_FAILED_STOP**

v0.7 was preregistered as an instrument-redesign pilot, not as an IAER replication,
eligibility study, or confirmatory experiment.

The frozen decision rule required P1-P5 all to pass for
`INSTRUMENT_CANDIDATE_VIABLE`. P1 passed, but P2-P5 did not. Under the frozen rule,
v0.7 therefore stops without prompt tuning, rescue interfaces, or a second behavioral
run.

## Public preregistration

The complete preregistration release was published before behavioral collection:

- tag: `v0.7-instrument-preregistration`
- frozen commit: `db3fce24466ab7c21d2e9aee369082236db536d8`
- frozen archive: `iaer_v0_7_preregistration_frozen.zip`
- frozen archive SHA-256: `398999d2cca55f2fca240d8740b8f279a57f0b3a39a9f5e64fcaaa02bf7f23a3`

The release asset digest was verified before behavioral authorization.

## Frozen model/configuration

- model: Ministral-3-8B-Instruct-2512
- GGUF: Q4_K_M
- model SHA-256: `e7480c2c16298ca644c9980e1301b6fea087f210900e69ada57ffd83d6016c02`
- LM Studio: 0.4.23
- context length: 8192
- temperature: 0
- seed: 42
- sequential calls
- one fixed response interface
- fixed N = 48

## Integrity

- 48/48 planned rows valid
- 0 failure rows
- 0 missing keys
- 0 extra keys
- 0 duplicate keys
- 0 metadata-error rows
- all finish reasons: `stop`
- all transport attempts: 1
- model ID consistent across all rows
- model SHA-256 consistent across all rows
- temperature=0 throughout
- seed=42 throughout
- frozen manifest SHA consistent throughout
- frozen prompt-spec SHA consistent throughout

**P1 integrity: PASS**

## Prespecified behavioral results

| Condition | Correct | Result |
| --- | ---: | --- |
| `two_initial_one_counter` | 12/12 | PASS |
| `one_initial_two_counter` | 11/12 | PASS |
| `derived_lure_initial_two_counter` | 7/12 | FAIL |
| `three_initial_two_counter` | 12/12 | PASS |

Frozen gates:

- P1 integrity: PASS
- P2 condition accuracy: FAIL
- P3 INITIAL-label symmetry: FAIL
- P4 presentation-order symmetry: FAIL
- P5 derived-record lure: FAIL

Frozen decision:

> **REDESIGN_FAILED_STOP**

## Descriptive pattern

The model performed almost perfectly when only independent root sources were present:
35/36 correct across R1, R2, and R4 combined.

Performance dropped specifically in R3, where five surface records were explicitly
marked as DERIVED from one INITIAL root and as adding zero new epistemic votes:
7/12 correct.

The five R3 errors all selected the INITIAL claim rather than the normatively required
COUNTER claim.

This is compatible with the possibility that repeated derivative surface records can
interfere with application of an explicit root-counting rule, but v0.7 was not
preregistered to estimate an IAER effect and cannot establish that interpretation.

### R3 descriptive cross-cell breakdown

- CLAIM_A × A_FIRST: 3/3 correct
- CLAIM_A × B_FIRST: 2/3 correct; failed items: R7I002
- CLAIM_B × A_FIRST: 2/3 correct; failed items: R7I009
- CLAIM_B × B_FIRST: 0/3 correct; failed items: R7I003, R7I007, R7I001

The observed R3 asymmetry means the failure is not cleanly invariant to label/order.
Because each cell contains only three items and no cross-cell hypothesis was
preregistered, these cell patterns are descriptive only.

## Interpretation boundary

v0.7 tests instrument usability only.

It does **not**:
- confirm IAER in Ministral;
- refute IAER in Ministral;
- estimate an IAER effect size;
- establish a mechanism for the R3 failures;
- alter the completed v0.4.3 Qwen confirmatory result.

## Scientific disposition

The v0.7 instrument-redesign path is exhausted under its frozen rule.

No v0.7 rescue run is permitted.

The IAER project is therefore marked:

> **PAUSED — instrument redesign path exhausted under v0.7**

A future return to IAER should begin only with a materially new measurement idea and
a new version identifier, not by tuning v0.7 or searching additional models until one
passes.

## Recommended next scientific action

Before any v0.8 proposal, conduct a program-level audit of v0.2-v0.7 to separate:

1. confirmed findings;
2. qualification/calibration observations;
3. instrument failures;
4. descriptive patterns worth following up;
5. claims that remain unsupported.

That audit should determine whether a new IAER study is scientifically justified or
whether the project should remain paused.
