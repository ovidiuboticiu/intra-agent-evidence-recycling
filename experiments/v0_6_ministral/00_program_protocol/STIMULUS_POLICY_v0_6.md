# IAER v0.6 — Stimulus Separation and Commitment Policy

Status: FINAL FOR FREEZE A

## Pools

CAL: 8 items
ELI: 12 items
CON: 32 items

All pools are generated once from a frozen deterministic generator before any
behavioral call to the candidate model.

## Isolation constraints

Across all 52 rows:
- item_id is globally unique
- entity is globally unique
- claim_a_value and claim_b_value are globally unique tokens
- no claim token appears in more than one row
- CLAIM_A != CLAIM_B within every row
- no row crosses pools
- all items are fictional

## Balance

CAL:
- 2 items in each INITIAL x presentation-order cell

ELI:
- 3 items in each INITIAL x presentation-order cell

CON:
- 8 items in each INITIAL x presentation-order cell
- 8 positive-control items total
- exactly 2 positive-control items in each INITIAL x presentation-order cell

## Commitment strategy

Before Calibration:
1. Generate all three files.
2. Run the validator.
3. Record SHA-256 for all three CSVs and the generator.
4. Freeze those hashes.

Recommended public disclosure:
- Calibration file: public in Freeze A.
- Eligibility file: commit hash in Freeze A; reveal full file only after Calibration closes.
- Confirmatory file: commit hash in Freeze A; reveal full file only after Eligibility closes ELIGIBLE.

This staged reveal is not required for model isolation when using an offline local model,
but it strengthens the audit trail by demonstrating that later test sets existed unchanged
before earlier outcomes were observed.

## No regeneration rule

Once Freeze A is public, the ELI and CON files may not be regenerated because an item
looks awkward or because Calibration results suggest another composition.

Any material defect discovered after freeze is handled fail-closed:
- document the defect;
- close the affected stage as not runnable if necessary;
- create a new version with a new stimulus pool.
