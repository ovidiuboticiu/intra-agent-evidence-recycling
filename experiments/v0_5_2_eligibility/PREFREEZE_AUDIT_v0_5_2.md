# Prefreeze audit — IAER v0.5.2

Audit performed before behavioral collection.

## Technical-smoke evidence

- raw file SHA-256: `a96c33443ab538bf25fbd56ce170d4b9e89a5fa62719e18a240f4fe591ff9266`
- status: PASS
- model hash match: true
- API model match: true
- strict JSON match: true
- finish reason: stop
- reasoning tokens: 0
- duration: 8.026 seconds

## Static design audit

- 12 unique item IDs
- 6 INITIAL=`CLAIM_A`; 6 INITIAL=`CLAIM_B`
- 6 `A_FIRST`; 6 `B_FIRST`
- 3 items in every INITIAL × presentation-order cell
- 3 conditions for every item
- 36 unique planned keys
- one fixed structured response representation
- boolean JSON Schema `strict=true`
- fixed model identifier, model file hash, seed, temperature, timeout, and deterministic schedule seed
- analyzer decision gates correspond to the preregistration
- no behavioral result file included in the freeze

## Boundary

This audit verifies package consistency and design implementation. It does not certify future runtime behavior and contains no v0.5.2 eligibility outcome.
