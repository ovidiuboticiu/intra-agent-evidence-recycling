# IAER v0.5.2 Closure Report

## Final status

**CLOSED — INELIGIBLE**

IAER v0.5.2 was a fixed-N behavioral eligibility pilot for Microsoft Phi-4-mini-reasoning under one frozen response interface and execution configuration. It was not a confirmatory replication of the IAER v0.4.3 findings.

The collection is technically valid and complete. The candidate model/configuration failed the prespecified behavioral eligibility gates and must not proceed to an IAER v0.6.0 confirmatory study in this form.

## Public freeze and provenance

- Public preregistration tag: `v0.5.2-preregistration`
- Public preregistration release: <https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.5.2-preregistration>
- Frozen archive: `iaer_v0_5_2_eligibility_frozen.zip`
- Frozen archive SHA-256: `6aa7f92394f030bbc1fcd9989c16ea600d6d4c821250816aec74ca066e3f8a85`
- Candidate model: Microsoft Phi-4-mini-reasoning, GGUF Q4_K_M
- LM Studio API identifier: `microsoft_phi-4-mini-reasoning`
- Model SHA-256: `ce8becd58f350d8ae0ec3bbb201ab36f750ffab17ab6238f39292d12ab68ea06`
- Temperature: `0`
- Seed: `42`
- Planned trajectories: `36`

The preregistration and frozen archive were public before any v0.5.2 behavioral outcome was collected.

## Integrity result

The frozen analyzer recorded:

- 36/36 valid planned rows;
- 0 failure rows;
- 0 missing keys;
- 0 extra keys;
- 0 duplicate keys;
- 0 metadata errors.

All rows match the frozen model identifier, model SHA-256, temperature, seed, and manifest SHA-256. Therefore, G1 passed and the behavioral eligibility result is interpretable under the preregistered decision rule.

The uploaded text and JSON reports were also independently regenerated from the raw JSONL file with the frozen analyzer. Their substantive contents matched exactly; only platform line endings differed during byte-level comparison.

## Prespecified gate results

| Gate | Result |
|---|---|
| G1 — completeness and integrity | **PASS** |
| G2 — overall condition accuracy | **FAIL** |
| G3 — INITIAL-orientation symmetry | **FAIL** |
| G4 — presentation-order symmetry | **FAIL** |

Because G1 passed but one or more behavioral gates failed, the preregistered decision is **INELIGIBLE**.

## Results by condition

| Condition | Correct | Required | Result |
|---|---:|---:|---|
| `baseline_initial` | 4/12 (0.333) | at least 10/12 | FAIL |
| `counter_single_strong` | 12/12 (1.000) | at least 10/12 | PASS |
| `independent_five_initial` | 2/12 (0.167) | at least 10/12 | FAIL |

### INITIAL orientation

| Condition | INITIAL=`CLAIM_A` | INITIAL=`CLAIM_B` | Required per cell |
|---|---:|---:|---:|
| `baseline_initial` | 3/6 | 1/6 | at least 5/6 |
| `counter_single_strong` | 6/6 | 6/6 | at least 5/6 |
| `independent_five_initial` | 1/6 | 1/6 | at least 5/6 |

### Presentation order

| Condition | `A_FIRST` | `B_FIRST` | Required per cell |
|---|---:|---:|---:|
| `baseline_initial` | 2/6 | 2/6 | at least 5/6 |
| `counter_single_strong` | 6/6 | 6/6 | at least 5/6 |
| `independent_five_initial` | 0/6 | 2/6 | at least 5/6 |

## Descriptive interpretation

The model selected the normatively expected counter-claim in all 12 `counter_single_strong` trajectories. However, it selected the expected INITIAL claim in only 4/12 `baseline_initial` trajectories and only 2/12 `independent_five_initial` trajectories.

This pattern is inconsistent with reliable normative evidence aggregation under the frozen task interface. In particular, five mutually independent sources of reliability 0.65 did not reliably overcome one counter-source of reliability 0.80. The poor baseline result also means that the failure cannot be attributed solely to multi-source aggregation; the model/interface combination was not behaviorally stable enough even in the simplest INITIAL-support condition.

The observed pattern is compatible with strong counter-evidence or prompt-position dominance, but this pilot was not designed to identify an internal mechanism. Any such explanation remains descriptive and exploratory.

## Interpretation boundary

This eligibility decision:

- does not confirm the IAER effect;
- does not refute the IAER effect;
- does not estimate the size of the IAER effect;
- does not alter the preregistered v0.4.3 result;
- applies only to this quantized model, response interface, prompt design, and execution configuration.

## Consequence for the research program

No IAER v0.6.0 confirmatory run may use this exact candidate configuration. The v0.5.2 outcomes must not be repaired, selectively rerun, or reclassified.

Any future confirmatory attempt requires a new candidate-selection decision, new stimuli, a separately frozen analysis plan, and a new public preregistration created before confirmatory outcomes are collected. Any prompt or interface modification must be treated as a new version rather than as a continuation of v0.5.2.

## Archived outcome files

- `results_v0_5_2.jsonl` — raw behavioral outcomes
- `eligibility_report_v0_5_2.txt` — human-readable frozen-analyzer report
- `eligibility_report_v0_5_2.json` — machine-readable frozen-analyzer report
- `POSTRUN_MANIFEST_v0_5_2.sha256` — integrity hashes for the archived outcome files

