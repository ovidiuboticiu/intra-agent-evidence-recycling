# IAER Gemma Cross-Family Replication — Eligibility Public Freeze v0.2.0

**Status:** PUBLIC PRE-COLLECTION FREEZE  
**Freeze date (UTC):** 2026-10-06  
**Stage:** Eligibility  
**Replication class:** Level D — cross-family / conceptual replication program

## Calibration handoff

Gemma Calibration v0.1.2 is closed.

- Interface A: `INTERFACE_B_AUTHORIZED`
- Interface B: `INTERFACE_B_LOCKED`
- Locked Eligibility response interface: `chosen_claim` only

Calibration does not test or estimate IAER.

## Candidate model and runtime

- Model: Gemma 4 E4B Instruct
- API identifier: `gemma-4-e4b-it`
- GGUF: `gemma-4-E4B-it-Q4_K_M.gguf`
- Quantization: Q4_K_M
- GGUF SHA-256: `0ffb122c8b6921f13cbc34186e052524d0b5803b17f4867b7197a561400b3770`
- LM Studio: 0.4.25
- Runtime: CPU llama.cpp (Windows) v2.41.0
- Context length: 8192
- Enable Thinking: OFF
- temperature: 0
- seed: 42
- max_tokens: 2048
- sequential collection only

At this freeze, no v0.2.0 Eligibility `/chat/completions` call has been made.

## Eligibility design

12 fresh fictional items × 3 conditions = 36 planned calls.

Conditions:
- `baseline_initial`
- `counter_single_strong`
- `independent_five_initial`

Prespecified gates:
- G1: 36/36 planned keys exactly once, zero failures, no missing/extra/duplicate/metadata errors, all finish_reason=stop, all reasoning_content_present=false.
- G2: >=10/12 correct in each condition.
- G3: within each condition >=5/6 correct for each INITIAL orientation.
- G4: within each condition >=5/6 correct for each presentation order.

Decision:
- all gates pass -> `ELIGIBLE`
- G1 pass + any behavioral gate fail -> `INELIGIBLE`
- G1 fail -> `INVALID/INCONCLUSIVE`

Eligibility cannot confirm, refute, or estimate IAER.

## Private repository commitment

Private working repository:
`ovidiuboticiu/iaer-gemma-cross-family-replication`

HEAD at freeze:
`886b48c741d989921a62772f2bc0b7ea044031fd`

Package path:
`versions/v0.2.0/`

All package files were verified byte-for-byte against the SHA-256 commitments below before this public freeze.

## Artifact commitments

ZIP SHA-256:

`e8b0286ec03b5f278e5ddc572d8b54713c111c88b1b6842cc3c25539efde266b`

Eligibility freeze manifest SHA-256:

`d4408ecbaa1f6b55198feb3a03ce3e592a3a8c62336c2ea5818fd659a7d54c8d`

Package checksum-file SHA-256:

`4ae104127760e428f5b821663c1542be70da31481bc68faa9aa731f3cdca5b2c`

Per-file package SHA-256:

```text
0d468fe0a5bd428ec3277ba264798976df37eee6c99a9f33298c7bac98917b2c  00_protocol/CALIBRATION_HANDOFF.md
a9803c1c7a90a59578812cb2a017798111548334d47c18e59c3e68b742cfa80f  00_protocol/ELIGIBILITY_PROTOCOL.md
9dce2120574fe8e0190481eaedd972f1f892a25c030e4825400765cdbdf3ad07  00_protocol/MODEL_ENVIRONMENT.md
d4408ecbaa1f6b55198feb3a03ce3e592a3a8c62336c2ea5818fd659a7d54c8d  01_eligibility/FREEZE_MANIFEST.sha256
e008f8d9df0c3f20a5e1bef63e915097ab27e124eeb505322b96a4c2b858dc40  01_eligibility/PREREGISTRATION_ELIGIBILITY.md
6ec4c1c58e8c6d90bd019579cdd2ffef528754d4c24bb3ae0c4a45e9751ab3eb  01_eligibility/analyze_eligibility.py
d07213c59cf1e91e7e0ddd5f02c04ede643d581bd90ac0e228f1ec19412cea3e  01_eligibility/eligibility_config.json
bff6bc622708163e21401bddffd23d47b2321edf9713c05da5887f503adf79bb  01_eligibility/run_eligibility.py
047eb3772cb2d80c49340cb0a209fc51e529b64ebf31ce1ae0d15b9f7a0b1fbf  01_eligibility/stimuli_eligibility.csv
5452dc2d48a1cd353b41d57a114cb51b4cab9fee20a026daacedb741ffebaf8e  README.md
```

## Fail-closed rule

After this freeze, model artifact, runtime mode, locked Interface B, prompts, stimuli,
gates, thresholds, randomization seed, retry rules, or analysis logic must not be
changed within v0.2.0 after observing Eligibility outcomes.

A material change requires a new version and a new public pre-outcome freeze.
