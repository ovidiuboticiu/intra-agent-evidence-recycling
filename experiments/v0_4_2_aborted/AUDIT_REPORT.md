# Independent Archival Audit — v0.4.2

## 1. Classification

The supplied package is a **frozen pre-data confirmatory-attempt package**.

It is not a completed experiment and contains no confirmatory result file.

Correct archival label:

> **v0.4.2 — ABORTED BEFORE DATA COLLECTION / semantic-provenance preflight failure**

## 2. Supplied files

The archive contains 9 original files:

- `ABORT_NOTE_v0_4_1.md`
- `analyze_v0_4_2.py`
- `FREEZE_MANIFEST_v0_4_2.sha256`
- `POWER_NOTE_v0_4_2.md`
- `PREREGISTRATION_v0_4_2.md`
- `RATIONALE_v0_4_2.md`
- `README_v0_4_2.md`
- `run_experiment_v0_4_2.py`
- `stimuli_v0_4_2.csv`

No `results_v0_4_2.jsonl` is present.

That absence is consistent with the documented rule that confirmatory collection must not begin after a failed mandatory preflight.

## 3. Manifest verification

`FREEZE_MANIFEST_v0_4_2.sha256` contains 8 entries.

Verification result:

```text
failed entries: 0
```

All frozen files match their recorded SHA-256 hashes.

## 4. Stimulus-plan verification

The frozen stimulus file contains:

- items: 32
- INITIAL=CLAIM_A: 16
- INITIAL=CLAIM_B: 16
- A_FIRST: 16
- B_FIRST: 16
- positive controls: 8

These values match the preregistered design.

## 5. Active-manipulation repair

Static inspection confirms that v0.4.2 changes the active operation from a fresh belief-choice task to a constrained downstream application task.

The relevant structured response requires:

- `applied_claim` = the already authorized INITIAL claim;
- `operation_status` = `APPLIED`.

Five such application calls are required per active trajectory.

This repair addresses the structural problem that caused the v0.4.1 C16/O2 manipulation failure.

## 6. Structured-output bug repair

Static inspection of the supplied runner finds:

```text
"strict": True       occurrences = 4
"strict": "true"     occurrences = 0
```

Therefore the previously identified string/boolean bug is repaired in v0.4.2.

## 7. Preflight architecture

The supplied code implements 11 mandatory cases:

### Provenance cases 1–3

1. one independent source + review + application record -> expected `["E1"]`
2. three independent sources -> expected `["E1","E2","E3"]`
3. one independent source + lineage-marked derived traces -> expected `["E1"]`

### Behavioral cases 4–7

Task-isomorphic `source_only` and `independent_evidence` checks for:

- INITIAL=A
- INITIAL=B

### Active-application cases 8–11

Five-operation checks for:

- active_plain / INITIAL=A
- active_lineage / INITIAL=A
- active_plain / INITIAL=B
- active_lineage / INITIAL=B

The code raises `SEMANTIC_PREFLIGHT_FAILED` if any case fails.

## 8. Observed preflight outcome

The contemporaneous execution capture showed that case 3 returned:

```text
expected = ["E1"]
got = []
pass = false
```

and the run ended with `SEMANTIC_PREFLIGHT_FAILED`.

The displayed cases 1–2 and 4–11 passed.

### Evidence limitation

The archive itself does not contain the terminal output as a machine-readable file.

Consequently, this exact observed outcome cannot be regenerated from the frozen package without running the model again, and rerunning the model would not constitute verification of the historical execution.

This audit therefore distinguishes:

- **frozen-code fact:** case 3 is mandatory and expects `["E1"]`;
- **historical execution fact:** the contemporaneous console capture showed `got=[]`;
- **archive fact:** no confirmatory result file exists.

## 9. Confirmatory-inference status

Since the mandatory preflight did not pass:

- fixed-N collection never began;
- dataset completeness cannot be satisfied;
- H1: **NOT TESTED**
- H2: **NOT TESTED**
- no effect estimate from v0.4.2 exists.

This is an abort due to instrument/preflight validity, not a negative confirmatory result.

## 10. Reproducibility limitation identified

The runner does not persist the preflight outcome before exiting.

For stronger archival reproducibility, later runners should save a timestamped preflight JSON artifact before either passing or failing.

This is a logging/reproducibility improvement; changing it retrospectively here would be inappropriate.

## 11. Archival verdict

**Suitable for inclusion in GitHub under `experiments/v0_4_2_aborted/`.**

The folder should be presented as evidence of methodological iteration and transparent stopping, not as a scientific result.

The exact original files should remain unchanged.
