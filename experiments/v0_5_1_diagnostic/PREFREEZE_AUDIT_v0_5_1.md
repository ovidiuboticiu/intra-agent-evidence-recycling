# IAER v0.5.1 diagnostic — prefreeze audit

Audit completed before any v0.5.1 diagnostic model call.

## Scope and separation

- v0.5.1 is explicitly exploratory/diagnostic.
- It does not rerun the v0.5.0 preflight sentinels.
- It cannot change or rescue the v0.5.0 INVALID/INCONCLUSIVE status.
- No confirmatory claim, alpha threshold, or stopping based on behavioral
  outcomes is defined.

## Stimulus audit

- 8 unique item IDs and 8 unique fictional entities.
- 16 unique four-letter claim-value tokens.
- INITIAL: 4 `CLAIM_A`, 4 `CLAIM_B`.
- Presentation order: 4 `A_FIRST`, 4 `B_FIRST`.
- Each INITIAL × presentation-order cell contains exactly 2 items.
- The 24 entity/token values are internally unique.
- No entity or claim-value token overlaps the v0.4.3 stimuli, the v0.5.0
  confirmatory stimuli, or the two v0.5.0 preflight sentinels.

## Planned-call audit

- 2 evidence conditions.
- 3 response/instruction modes.
- `8 × 2 × 3 = 48` unique planned keys.
- Task order is fixed by deterministic shuffle seed 510.
- The runner prints validity/progress but not observed choices.

## Code-path audit

- Python syntax compilation passed for runner and analyzer.
- Dry-run produced 8 items and 48 planned calls.
- Strict JSON schema uses boolean `True`, not a string.
- A mocked end-to-end collection produced exactly 48 valid unique rows.
- The frozen analyzer accepted the complete mocked dataset and wrote its
  descriptive report.
- The analyzer rejects missing, extra, duplicate, unresolved-failure, or
  model-identity-mismatched planned records.
- Batch launchers choose `py -3` when available and otherwise use `python`;
  they do not retry a behavioral run after a nonzero process exit.

## Integrity audit

- The runner verifies every file named in `FREEZE_MANIFEST_v0_5_1.sha256`.
- It verifies the full local GGUF hash before collection.
- It requires the exact API model identifier before collection.
- Runtime outputs are not part of the frozen-input manifest.

