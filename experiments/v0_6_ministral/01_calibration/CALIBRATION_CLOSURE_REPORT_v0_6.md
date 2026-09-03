# IAER v0.6 — Calibration Closure Report

## Final status

**CALIBRATION_FAILURE — STOP BEFORE ELIGIBILITY**

IAER v0.6 used a staged design: Calibration → Eligibility → Confirmatory IAER.

The candidate model was Ministral-3-8B-Instruct-2512 GGUF Q4_K_M.

No Eligibility or Confirmatory IAER run is authorized under v0.6.

## Interface A

Response representation: `chosen_claim` + `confidence_chosen`.

Integrity: 24/24 valid rows, 0 failures, no missing/extra/duplicate/metadata-error rows; C1 PASS.

Behavior:
- `baseline_initial`: 8/8 correct
- `counter_single_strong`: 8/8 correct
- `independent_five_initial`: 0/8 correct

The 0/8 failure was symmetric across INITIAL label and presentation order.

Decision: `INTERFACE_A_FAILED_BEHAVIORALLY`. Under the prespecified A→B rule, Interface B was authorized.

## Interface B

Response representation: `chosen_claim` only.

Integrity: 24/24 valid rows, 0 failures, no missing/extra/duplicate/metadata-error rows; C1 PASS.

Behavior:
- `baseline_initial`: 8/8 correct
- `counter_single_strong`: 8/8 correct
- `independent_five_initial`: 0/8 correct

The 0/8 failure was again symmetric across INITIAL label and presentation order.

Decision: `CALIBRATION_FAILURE`.

## Interpretation

Both prespecified response interfaces produced the same qualitative pattern: perfect performance on the single-source baseline and single stronger counter-source condition, but zero normative accuracy when five independent moderate sources supported INITIAL against one stronger counter-source.

Because the failure persisted after removing the confidence field and was fully symmetric across INITIAL label and presentation order, the tested response-interface difference, label orientation, and order do not explain the failure.

This does not identify an internal mechanism. It is a calibration observation only.

This result does NOT confirm IAER, refute IAER, estimate the IAER effect in Ministral, or alter the completed v0.4.3 Qwen result.

## Stopping rule

The v0.6 design contains no Interface C. No prompt tuning or rescue rerun is permitted within v0.6. Eligibility and Confirmatory IAER are not run. Any redesign requires a new version and a new pre-outcome public freeze.

## Publication deviation

During closure audit, the public Freeze-A tag was found to contain the program-level protocol but not all calibration-specific implementation files that the publication checklist intended to include. This is documented separately in `FREEZE_A_PUBLICATION_DEVIATION_v0_6.md`.

The local pre-run package preserved the exact files used, and those materials are archived with the outcomes. This retrospective archival action must not be described as a retroactive preregistration. The deviation note also records a stale summary line in `INTERFACES_v0_6.json`; it had no realized decision impact because Interface A integrity passed before Interface B was authorized.

## Scientific disposition

v0.6 closes as a **calibration failure**, not as an IAER non-replication.

The strongest defensible next step, if the project continues, is instrument redesign under a new version rather than testing additional models with the same aggregation control unchanged.
