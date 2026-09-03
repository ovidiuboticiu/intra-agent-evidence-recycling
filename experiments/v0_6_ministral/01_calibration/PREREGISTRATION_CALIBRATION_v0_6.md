# PREREGISTRATION — IAER v0.6 Calibration

Status: FINAL CONTENT FOR PUBLIC FREEZE A

This document must be publicly frozen before the first behavioral Calibration call.

## Study status

Fixed-N behavioral calibration study, not a confirmatory IAER test. The sole purpose is to select one prespecified response interface for `ministral-3-8b-instruct-2512`. Calibration cannot confirm, refute, estimate, or tune toward the IAER memory-source multiplication effect.

## Model/configuration

- Model: Ministral-3-8B-Instruct-2512 GGUF Q4_K_M
- LM Studio API identifier: `ministral-3-8b-instruct-2512`
- GGUF filename: `Ministral-3-8B-Instruct-2512-Q4_k_m.gguf`
- GGUF SHA-256: `e7480c2c16298ca644c9980e1301b6fea087f210900e69ada57ffd83d6016c02`
- GGUF size: `5198386976` bytes
- LM Studio: 0.4.23
- context length: 8192
- temperature: 0
- request seed: 42
- max output tokens: 512
- sequential calls
- timeout: 600 s
- maximum one retry, transport-level failure only
- JSON Schema structured output with boolean `strict=true`

## Stimuli

Eight fresh CAL items are frozen in `stimuli_calibration_v0_6.csv`.

Balance:
- 4 INITIAL=CLAIM_A, 4 INITIAL=CLAIM_B
- 4 A_FIRST, 4 B_FIRST
- exactly 2 items in each INITIAL x presentation-order cell

No CAL item is reused in ELI or CON. The ELI and CON pools were generated before Calibration and are committed by SHA-256 before any Calibration behavioral outcome.

## Conditions

Each of 8 items is run once in each condition.

1. `baseline_initial`: one independent r=0.65 source supports INITIAL; normative expected choice INITIAL.
2. `counter_single_strong`: one independent r=0.65 source supports INITIAL plus one new independent r=0.80 source supports COUNTER; normative expected choice COUNTER.
3. `independent_five_initial`: five mutually independent r=0.65 sources support INITIAL plus one new independent r=0.80 source supports COUNTER; normative expected choice INITIAL.

Total: 24 planned calls per tested interface.

## Interface A

Required fields: `chosen_claim` and `confidence_chosen` (0..100). Only `chosen_claim` is behavioral; confidence is descriptive only.

## Interface B

Required field: `chosen_claim`.

## Prespecified selection rule

Interface A is always tested first.
- A integrity FAIL -> `INVALID/INCONCLUSIVE`; STOP; B forbidden.
- A integrity PASS and C1-C4 PASS -> `INTERFACE_A_LOCKED`; B forbidden.
- A integrity PASS but any behavioral gate C2-C4 FAIL -> `INTERFACE_A_FAILED_BEHAVIORALLY`; B authorized.

If B is authorized:
- B integrity FAIL -> `INVALID/INCONCLUSIVE`; STOP.
- B integrity PASS and all gates PASS -> `INTERFACE_B_LOCKED`.
- B integrity PASS but any behavioral gate FAIL -> `CALIBRATION_FAILURE`; STOP.

There is no Interface C in v0.6.

## Gates

C1: exactly 24 valid planned keys; zero failure, missing, duplicate, extra, or frozen-metadata-mismatch rows.
C2: at least 7/8 normative choices correct in EACH condition.
C3: within EACH condition, at least 3/4 correct for each INITIAL orientation.
C4: within EACH condition, at least 3/4 correct for each presentation order.

## Execution and stopping

Deterministic order, fixed N, blinded progress output, no scientific peeking, no outcome-based early stopping, no prompt editing after outcomes, no returned model-response rerun, one retry only for transport failure, fail-closed schema/parse handling.

## Interpretation boundary

Passing Calibration establishes only that one prespecified response interface is usable on normative control tasks for this exact frozen model/configuration. Eligibility and Confirmatory IAER remain separate later studies.
