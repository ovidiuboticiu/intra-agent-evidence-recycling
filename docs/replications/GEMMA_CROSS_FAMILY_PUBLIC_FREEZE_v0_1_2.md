# IAER Gemma Cross-Family Replication — Public Freeze v0.1.2

**Status:** PUBLIC PRE-COLLECTION FREEZE
**Freeze date (UTC):** 2026-10-06
**Replication class:** Level D — cross-family / conceptual replication program

## Reason for v0.1.2

v0.1.1 was interrupted and classified `INVALID/INCONCLUSIVE — CONFIGURATION DEVIATION` after the LM Studio inference panel was observed with `Enable Thinking = ON`. No partial v0.1.1 behavioral outcome is used for scientific inference or tuning.

v0.1.2 keeps the v0.1.1 design and requires:

- LM Studio `Enable Thinking = OFF`
- `max_tokens = 2048`

No stimulus, prompt semantics, calibration gate, threshold, model artifact, seed, temperature, interface-selection rule, or analysis rule is changed.

## Candidate model

- Family: Gemma
- API identifier: `gemma-4-e4b-it`
- GGUF: `gemma-4-E4B-it-Q4_K_M.gguf`
- Quantization: Q4_K_M
- GGUF SHA-256: `0ffb122c8b6921f13cbc34186e052524d0b5803b17f4867b7197a561400b3770`
- LM Studio: 0.4.25
- Runtime: CPU llama.cpp (Windows) v2.41.0
- Context length: 8192
- Request temperature: 0
- Request seed: 42
- Max output tokens: 2048
- Sequential calls only
- `Enable Thinking = OFF`

At the time of this freeze, no v0.1.2 calibration `/chat/completions` call had been made.

## Calibration design

Interface A is tested first:
- `chosen_claim`
- `confidence_chosen`

Interface B is permitted only if Interface A passes integrity but fails one or more behavioral gates.

Planned calls per tested interface: 24 = 8 items × 3 normative-control conditions.

Calibration gates remain:
- C1: 24/24 valid planned keys; zero failure rows; no missing/duplicate/extra/metadata mismatch.
- C2: >=7/8 correct in each condition.
- C3: within each condition >=3/4 correct for each INITIAL orientation.
- C4: within each condition >=3/4 correct for each presentation order.

Passing Calibration does not test or estimate IAER.

## Private working repository commitment

Private repository: `ovidiuboticiu/iaer-gemma-cross-family-replication`

HEAD at this freeze:
`291b88ba3a31159154464ff56ce9eeec1dedf013`

The freeze-critical v0.1.2 files in the private repository were verified against the hashes below before this public freeze.

## Artifact commitments

ZIP SHA-256:
`a8f51680649b3429f301667d0691c0637003cc3afb12c16149d2f2d48f3f565b`

Calibration freeze manifest SHA-256:
`12aac353518953b88df814b62ea0fb0e0ed5c8c671e01054b0faf3ebe0bdb752`

Package checksum-file SHA-256:
`c49061ec9dbd295d28a776e7e28589bcc33aba31dd24425bdd63bcfac539f0d7`

Freeze-critical per-file SHA-256:

```text
c9b646b6b73636a2f81c22ddda5cd2fae2cfa6ca4c649bd71134a12a245f5b8e  PREREGISTRATION_CALIBRATION.md
a89bcae1da078db0ecd0d7aec752d213ef00cc924cc51b74b39ac124f383ba10  CALIBRATION_PROMPT_SPEC.json
7d07d46e11e974dab05d4c7ee599ad3d2f3f040f3eea3caf6d2cb95e001c509e  calibration_config.json
11db75723713593db45cfc7d65432506c89c084ceff92a98b0b1e50e29ee75d3  stimuli_calibration.csv
a698b22cb7ef1cf4a38b3b5dc0874272bdd8ce331b6bb1b5820caf4daf75a79e  run_calibration.py
cd6aff29f3dd699759032562daf1d7980e679aea40f530b4a26ddf5d222864af  analyze_calibration.py
```

## Fail-closed rule

After this freeze, model artifact, runtime mode, prompts, stimuli, gates, thresholds, interface-selection logic, retry rules, or analysis logic must not be changed within v0.1.2 after observing calibration outcomes. A material change requires a new version and a new public pre-collection freeze.
