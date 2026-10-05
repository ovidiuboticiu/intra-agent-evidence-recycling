# IAER Gemma Cross-Family Public Freeze v0.1.1

**Status:** PUBLIC PRE-COLLECTION FREEZE  
**Freeze date (UTC):** 2026-10-05  
**Program:** IAER Gemma Qualification v0.1.1  
**Replication class:** Level D — cross-family / conceptual replication program

## Reason for v0.1.1

The first v0.1 calibration attempt stopped fail-closed on its first call with:

`NON_STOP_FINISH_REASON: 'length'`

No valid behavioral response was available from that attempt. v0.1 is therefore archived as:

`INVALID/INCONCLUSIVE — TECHNICAL FAILURE`

v0.1.1 makes exactly one technical execution change:

- `max_tokens`: **512 -> 2048**

No other design element is changed.

Unchanged:
- candidate model and exact GGUF artifact;
- stimuli;
- Interface A / Interface B ordering rule;
- temperature;
- seed;
- normative control conditions;
- C1–C4 thresholds;
- retry policy;
- fail-closed rule;
- analyzer logic.

## Candidate model

- Family: Gemma
- API identifier: `gemma-4-e4b-it`
- GGUF filename: `gemma-4-E4B-it-Q4_K_M.gguf`
- Quantization: Q4_K_M
- GGUF SHA-256: `0ffb122c8b6921f13cbc34186e052524d0b5803b17f4867b7197a561400b3770`
- LM Studio: 0.4.25
- Runtime: CPU llama.cpp (Windows) v2.41.0
- API base: `http://127.0.0.1:1234/v1`
- Context length: 8192
- Request temperature: 0
- Request seed: 42
- Max output tokens: 2048
- Sequential calls only

## Calibration design

Interface A is tested first:
- `chosen_claim`
- `confidence_chosen`

Interface B is permitted only if Interface A passes integrity but fails one or more behavioral gates.

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

Private repository:
`ovidiuboticiu/iaer-gemma-cross-family-replication`

Committed HEAD at this freeze:
`563d368f62ea37c659b5d1acc9bed6a9c9df6a15`

Frozen v0.1.1 package path in the private repository:

`versions/v0.1.1/`

The v0.1 failed attempt is preserved separately under:

`archive/v0.1/`

## v0.1.1 package commitments

ZIP SHA-256:

`c16dc6637e20b7709054a4e57de0036fb1dcfd8256cd6d43acf2cb34fb4ea716`

`PACKAGE_SHA256SUMS.txt` SHA-256:

`fa52666f6b7b88f4764bc35991ec47ee6bc0b08e5128e1171946286413684369`

Calibration freeze-manifest SHA-256:

`efb52f053ff61157aa89120825eef6c558f59de82f3799cde1fe2919bb91c34c`

Critical frozen calibration files:

```text
522f6706b641bff46ba3be6684d2a46abafb5aefb802df05d1894982194bb64c  01_calibration/CALIBRATION_PROMPT_SPEC.json
efb52f053ff61157aa89120825eef6c558f59de82f3799cde1fe2919bb91c34c  01_calibration/FREEZE_MANIFEST.sha256
af26f023d73259eefd376a11f2cc7d8b43b55d51897757b9e98a9511eb208acd  01_calibration/PREREGISTRATION_CALIBRATION.md
cd6aff29f3dd699759032562daf1d7980e679aea40f530b4a26ddf5d222864af  01_calibration/analyze_calibration.py
37bbe24087685f5a71104ad4bdd5599f008b22303f261ddd275ab1d6dacd61fa  01_calibration/calibration_config.json
a698b22cb7ef1cf4a38b3b5dc0874272bdd8ce331b6bb1b5820caf4daf75a79e  01_calibration/run_calibration.py
11db75723713593db45cfc7d65432506c89c084ceff92a98b0b1e50e29ee75d3  01_calibration/stimuli_calibration.csv
```

## Fail-closed rule

After this public freeze, no prompt, threshold, stimulus, model, runtime, interface-selection rule, or analysis rule may be modified within v0.1.1 after observing calibration outcomes.

A further material change requires a new version and a new public pre-collection freeze.
