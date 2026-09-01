# TECHNICAL AMENDMENT v0.3.1
Date: 2026-08-31

## Trigger
The first attempted v0.3 experimental trajectory failed before any valid trajectory
was written (`completed_valid=0`) because a structured JSON response was truncated
inside the free-text `reason` field, producing `UNPARSABLE_JSON`.

## Interpretation
This is a transport/serialization failure, not a scientific outcome and not a
semantic-preflight failure.

## Changes
No hypothesis, item, condition, counterevidence reliability, randomization seed,
calibration gate, stopping rule, or measured construct is changed.

The following purely technical changes are made before collection of any valid v0.3 data:
1. Remove free-text `reason` from provenance output.
2. Remove free-text `reason` from belief output.
3. Keep only fields actually used by the preregistered calibration analysis:
   - independent_external_evidence_ids
   - chosen_claim
   - confidence_chosen
4. Reduce output token budgets because outputs are now bounded and short.
5. Preserve fail-closed parsing.

The original v0.3 failed row must not be merged into scientific data. Start v0.3.1
with a new results file.
