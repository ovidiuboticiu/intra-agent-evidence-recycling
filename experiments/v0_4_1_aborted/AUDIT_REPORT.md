# Independent Archival Audit — v0.4.1

## 1. Package classification

The supplied archive is a partial confirmatory-attempt package, not a completed confirmatory dataset.

Archival classification:

> **v0.4.1 — ABORTED / manipulation validity failure**

## 2. Supplied files

The original archive contains 12 files:

- `stimuli_v0_4.csv`
- `FREEZE_MANIFEST_v0_4.sha256`
- `POWER_NOTE_v0_4.md`
- `run_experiment_v0_4.py`
- `README_v0_4_1.md`
- `README_v0_4.md`
- `results_v0_4.jsonl`
- `RATIONALE_v0_4.md`
- `FREEZE_MANIFEST_v0_4_1.sha256`
- `analyze_v0_4.py`
- `AMENDMENT_v0_4_1.md`
- `PREREGISTRATION_v0_4.md`

No original supplied file has been rewritten in the GitHub-ready archival package.

## 3. Stimulus-plan check

The supplied stimulus file contains:

- 32 items;
- 16 INITIAL=CLAIM_A;
- 16 INITIAL=CLAIM_B;
- 16 A_FIRST presentation order;
- 16 B_FIRST presentation order;
- 8 prespecified positive-control items.

This matches the v0.4 preregistration.

## 4. Manifest verification

### `FREEZE_MANIFEST_v0_4_1.sha256`

All listed files verify successfully.

Result:

> **PASS — current v0.4.1 frozen package is internally hash-consistent.**

### Historical `FREEZE_MANIFEST_v0_4.sha256`

The older v0.4 manifest no longer matches:

- `PREREGISTRATION_v0_4.md`
- `run_experiment_v0_4.py`

All other files listed by that historical manifest match.

This is consistent with the documented v0.4.1 preflight amendment, which changed the preflight implementation and amended the preregistration before confirmatory data collection.

The older manifest should remain archived as historical evidence, but `FREEZE_MANIFEST_v0_4_1.sha256` is the relevant frozen manifest for the actual v0.4.1 attempt.

## 5. Raw partial-result audit

`results_v0_4.jsonl` contains:

- total rows: 8
- valid rows: 7
- manipulation-failure rows: 1
- technical-failure rows: 0

The valid rows are:

1. C02 / source_only
2. C02 / neutral_filler
3. C02 / active_plain
4. C02 / independent_evidence
5. C02 / passive_repeat
6. C02 / active_lineage
7. C16 / source_only

The eighth row is:

```text
status = manipulation_failure
item = C16
condition = active_lineage
operation = O2
expected = CLAIM_B
got = CLAIM_A
```

## 6. Hash consistency in raw valid rows

Every valid row embeds the same hashes for:

- preregistration;
- stimuli;
- rationale.

All three embedded hashes match the files supplied in the v0.4.1 archive.

## 7. Runtime diagnostics

Across the seven valid trajectories there are 24 stored model-call diagnostic records.

All 24 show:

```text
reasoning_present = false
transport_attempts = 1
```

There is therefore no evidence in the saved valid trajectories of reasoning mode being enabled or of a transport retry affecting those observations.

## 8. Provenance in the saved valid rows

All seven valid rows have exact provenance bookkeeping.

This fact is descriptive only; the dataset is too incomplete for the preregistered provenance-use interpretation gate.

## 9. Confirmatory inference

The planned fixed-N dataset required 168 valid trajectories and no unresolved manipulation failure.

The saved dataset has only 7 valid trajectories and contains an unresolved manipulation failure.

Therefore:

- V4 manipulation integrity: **FAIL**
- V5 dataset completeness: **FAIL**
- H1 confirmatory inference: **NOT PERMITTED**
- H2 confirmatory inference: **NOT PERMITTED**

Any numerical contrast computed from C02 alone would be exploratory inspection of an invalid partial dataset and must not be reported as a confirmatory result.

## 10. Known structured-output bug

The archived `run_experiment_v0_4.py` contains three instances of:

```python
"strict": "true"
```

rather than boolean `True`.

Classification:

- standards/type compliance bug: **confirmed**
- historically present in the executed code: **yes**
- repaired retrospectively in this archive: **no**
- plausible explanation for the C16 semantic claim switch: **not supported by the saved evidence**

The C16 event was a valid claim label inside the allowed response domain, not an unparsable or out-of-schema value.

## 11. Important logging limitation

The `manipulation_failure` row stores the failure summary but does not preserve the full partial active memory / O1 output / O2 raw structured response.

From the stopping location we can infer that O1 completed successfully, because otherwise the runner would have stopped at O1.

However, the precise internal sequence leading to the O2 switch cannot be reconstructed from `results_v0_4.jsonl` alone.

This is an archival limitation worth preserving explicitly.

## 12. Archival verdict

**Suitable for GitHub inclusion only under an explicit `v0_4_1_aborted` label.**

Required interpretation:

> v0.4.1 is evidence about the validity of the experimental manipulation, not a completed test of H1 or H2.

The partial raw file should remain unchanged and should never be merged into v0.4.2, v0.4.3, or any later confirmatory dataset.
