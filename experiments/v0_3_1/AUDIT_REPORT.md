# Independent Archival Audit — v0.3.1

Audit purpose: determine whether the supplied v0.3.1 folder can be archived as a reproducible pilot package without silently rewriting its historical files.

## 1. Package contents

The supplied archive contained:

- `FREEZE_MANIFEST_v0_3.sha256`
- `FREEZE_MANIFEST_v0_3_1.sha256`
- `PREREGISTRATION_v0_3.md`
- `RATIONALE_FROM_v0_2.md`
- `README_v0_3.md`
- `README_v0_3_1.md`
- `TECHNICAL_AMENDMENT_v0_3_1.md`
- `analyze_v0_3.py`
- `results_v0_3_1.jsonl`
- `run_experiment_v0_3.py`
- `stimuli_v0_3.csv`

No original file was edited for this GitHub-ready package.

## 2. Freeze-manifest verification

`FREEZE_MANIFEST_v0_3_1.sha256` verifies successfully for every file it lists.

The older `FREEZE_MANIFEST_v0_3.sha256` does **not** verify the current runner and analyzer, because those filenames were replaced by the v0.3.1 technical amendment. This is expected from the amendment history, but it means that the original pre-amendment v0.3 runner/analyzer cannot be reconstructed from this folder alone.

This is an archival limitation, not evidence of a problem in the v0.3.1 result file.

## 3. Raw-result integrity

`results_v0_3_1.jsonl`:

- rows: 48
- valid rows: 48
- non-valid rows: 0
- unique item-condition keys: 48
- expected item-condition keys: 48
- missing keys: 0
- duplicate valid keys: 0
- model: `qwen3.5-4b` for all rows
- temperature: `0.0` for all rows

SHA-256:

```text
c5fe7f0b645d8997488dc6bedaec305409ccc0b970a3187d98ada940f1d296de
```

The result metadata embeds identical frozen hashes across all 48 rows for:

- preregistration
- stimuli
- v0.2 rationale

Those embedded hashes match the corresponding files in the supplied package.

## 4. Active-manipulation integrity

There are 24 active-condition trajectories:

- 8 `active_plain`
- 8 `active_self_labeled`
- 8 `active_lineage`

Every valid active trajectory contains exactly five recorded active-operation diagnostics.

Because the runner stops fail-closed if an active operation selects `CLAIM_B`, valid status implies all five active operations selected `CLAIM_A` for every active trajectory.

## 5. Belief-output integrity

Every valid trajectory contains all three preregistered correction strengths:

- `0.55`
- `0.68`
- `0.80`

Every `chosen_claim` is one of the two allowed labels, and every recorded confidence lies within 0–100.

## 6. Provenance-score consistency

The audit recomputed the provenance bookkeeping fields from:

- selected evidence IDs
- true root IDs

No inconsistency was found between the raw selected IDs and:

- `exact_correct`
- `false_independent_ids`
- `missed_root_ids`

## 7. Reasoning mode

Across all recorded diagnostics, there are **312 model-call diagnostic records**:

- 120 active-operation calls
- 48 provenance calls
- 144 belief calls

All 312 record:

```text
reasoning_present = false
```

This is consistent with the documented Thinking=OFF configuration.

## 8. Calibration analysis reproduction

Running the supplied `analyze_v0_3.py` on the supplied raw result file reproduces:

### Belief retention

- `source_only`: 7/8 at q=.55, 2/8 at q=.68, 0/8 at q=.80
- `passive_repeat`: 8/8, 8/8, 8/8
- `active_plain`: 8/8, 8/8, 8/8
- `active_self_labeled`: 8/8, 8/8, 7/8
- `active_lineage`: 8/8, 8/8, 0/8
- `independent_evidence`: 8/8, 8/8, 8/8

### Provenance

- source_only: exact 8/8
- passive_repeat: exact 8/8
- active_plain: exact 8/8
- active_self_labeled: exact 8/8
- active_lineage: exact 6/8, with 2 missed roots and 0 false-positive IDs
- independent_evidence: exact 8/8

### Preregistered gates

- G1 dynamic range: PASS
- G2 positive-control sensitivity: PASS
- G3 provenance positive control: PASS
- G4 transport/integrity: PASS
- overall calibration status: PASS

## 9. Known code bug

The original `run_experiment_v0_3.py` contains three occurrences of:

```python
"strict": "true"
```

where a boolean `True` is the standards-correct representation.

Classification:

- code/type compliance bug: **yes**
- reason to rewrite archived historical code: **no**
- evidence that the 48 recorded outputs violated the bounded fields used in analysis: **no**

The historical runner should remain untouched. A corrected implementation belongs only in later versions.

## 10. Analysis-script limitation

The supplied analyzer counts 48 valid rows but does not independently check duplicate item-condition keys. The archival audit did perform that check and found:

- 48 unique keys
- no duplicates
- no missing keys

Therefore this limitation does not affect the reported v0.3.1 dataset, but should be improved in later confirmatory analyzers.

## 11. Archival verdict

**Suitable for inclusion in the private research repository as an exploratory/calibration pilot package.**

Required interpretive label:

> v0.3.1 is a completed calibration/discovery pilot and must not be presented as confirmatory evidence.

The package should preserve both the successful v0.3.1 manifest and the historical v0.3 manifest, with the amendment history explaining why the latter no longer matches the amended runner/analyzer filenames.
