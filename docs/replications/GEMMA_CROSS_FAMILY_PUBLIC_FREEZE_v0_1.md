# IAER Gemma Cross-Family Replication — Public Freeze Record v0.1

**Status:** PUBLIC PRE-COLLECTION FREEZE  
**Freeze date (UTC):** 2026-10-05  
**Program:** IAER Gemma Qualification v0.1  
**Replication class:** Level D — cross-family / conceptual replication program

## Candidate model

- Family: Gemma
- LM Studio API identifier: `gemma-4-e4b-it`
- GGUF filename: `gemma-4-E4B-it-Q4_K_M.gguf`
- Quantization: Q4_K_M
- GGUF SHA-256: `0ffb122c8b6921f13cbc34186e052524d0b5803b17f4867b7197a561400b3770`
- LM Studio: 0.4.25
- Runtime: CPU llama.cpp (Windows) v2.41.0
- API base: `http://127.0.0.1:1234/v1`
- Context length: 8192
- Request temperature: 0
- Request seed: 42
- Max output tokens: 512
- Sequential calls only

At the time of this freeze, only non-behavioral verification had been run. No calibration `/chat/completions` collection had started.

## Calibration design

Interface A is tested first:
- `chosen_claim`
- `confidence_chosen`

Interface B is permitted only if Interface A passes integrity but fails one or more behavioral gates:
- `chosen_claim` only

Planned calls per tested interface: 24 = 8 items × 3 normative-control conditions.

Conditions:
- `baseline_initial`
- `counter_single_strong`
- `independent_five_initial`

Calibration gates:
- C1: 24/24 valid planned keys; zero failure rows; no missing/duplicate/extra/metadata mismatch.
- C2: >=7/8 correct in each condition.
- C3: within each condition >=3/4 correct for each INITIAL orientation.
- C4: within each condition >=3/4 correct for each presentation order.

Passing Calibration does not test or estimate IAER.

## Private working repository commitment

Private working repository:
`ovidiuboticiu/iaer-gemma-cross-family-replication`

Committed HEAD at freeze:
`fde14d30099c6981e8643e8bafd62787e1643f68`

The repository was private at freeze time. This public record therefore serves as the pre-collection public timestamp and hash commitment.

## Package commitment

ZIP SHA-256:

`323746826531084968614847ab493d806eba50fc0ae9e37610d9c0df38c613d3`

Per-file SHA-256 commitments:

```text
5896fe41d5561547b210b979043bb03d59d4e03e92284000e35d21c30e639e83  00_protocol/GATES.json
8ccd74edb50fdbadd1d3bf942ca2bd39870167b7ce7226386370b1fbcbe362f9  00_protocol/MODEL_ENVIRONMENT.md
372e2750764d17b890ac392a8f66c042e27d288645eafa9c2db0d3a57982d8d0  00_protocol/PROGRAM_PROTOCOL.md
5eafcdf9b2f38235065f733cb0bfb1bbc024734f77b97399179b32d2dd279d0f  01_calibration/CALIBRATION_PROMPT_SPEC.json
bf32cc5fc0f5c1fb1caa53dce9d15e4f8edfa2334c3860712341146b5151ce16  01_calibration/FREEZE_MANIFEST.sha256
672f88605fd5afcdbc99249b4af2163459fda554efe9967656c137461a651a9f  01_calibration/PREREGISTRATION_CALIBRATION.md
cd6aff29f3dd699759032562daf1d7980e679aea40f530b4a26ddf5d222864af  01_calibration/analyze_calibration.py
7603282a4dee580fc6f1156f3805a3ae0f75c7623664c6f05f280362d1df1a00  01_calibration/calibration_config.json
c13ee94942fc9f55a811ca5f9a2a99d801b786d7701f60666f9b995b578178ae  01_calibration/run_calibration.py
11db75723713593db45cfc7d65432506c89c084ceff92a98b0b1e50e29ee75d3  01_calibration/stimuli_calibration.csv
c6f1e8c8c5427a73161a6a3b18cdf7c4b58ca5df693d251cbca6566190a4a1b5  README.md
```

`PACKAGE_SHA256SUMS.txt` SHA-256:
`b938b5c92716ac31f557183400099ec800d6968b24fe2c5c409a6517111d06fe`

## Fail-closed rule

After this freeze, prompt wording, model, model artifact, runtime, thresholds, stimuli, interface-selection logic, or analysis logic must not be altered within v0.1 after observing calibration outcomes.

A material change requires a new version and a new public pre-collection freeze.
