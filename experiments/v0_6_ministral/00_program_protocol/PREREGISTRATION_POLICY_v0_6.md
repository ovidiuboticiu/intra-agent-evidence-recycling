# IAER v0.6 — Preregistration and Freeze Policy

Status: FINAL FOR FREEZE A

## Freeze A — Program + Calibration

Must occur before the first behavioral Calibration call.

Freeze:
- program protocol
- calibration protocol/gates
- candidate interfaces A and B
- A -> B -> STOP selection rule
- deterministic stimulus generator
- CAL stimulus file
- SHA-256 commitments for ELI and CON stimulus files
- provisional execution settings
- exact model identity and local GGUF SHA-256
- Calibration runner and analyzer when later implemented
- freeze manifest

No Calibration behavioral outcome may exist before this freeze.

## Freeze B — Eligibility

May occur only after Calibration is formally closed.

Freeze:
- Calibration closure report and raw results
- selected interface
- exact prompts and JSON Schema
- exact frozen execution configuration
- ELI stimulus file matching its Freeze-A commitment
- Eligibility runner/analyzer
- G1-G4 unchanged from the program protocol
- freeze manifest

No Eligibility behavioral outcome may exist before Freeze B.

## Freeze C — Confirmatory IAER

May occur only if Eligibility is formally ELIGIBLE.

Freeze:
- Eligibility closure report and raw results
- CON stimulus file matching its Freeze-A commitment
- confirmatory runner/analyzer
- one primary hypothesis: passive_repeat > neutral_filler
- N=32 core items
- 8 prespecified positive-control items
- 104 planned trajectories
- RD >= +0.25 criterion
- two-sided exact paired McNemar p < 0.05
- V1-V3
- fixed-N stopping
- retry/failure policy
- freeze manifest

No confirmatory behavioral outcome may exist before Freeze C.

## Public record rule

Failed stages remain visible.
No failed freeze is deleted or silently replaced.
No raw data from incompatible versions are pooled.

## Outcome labels

Calibration:
- INTERFACE_A_LOCKED
- INTERFACE_B_LOCKED
- CALIBRATION_FAILURE
- INVALID/INCONCLUSIVE

Eligibility:
- ELIGIBLE
- INELIGIBLE
- INVALID/INCONCLUSIVE

Confirmatory:
- REPLICATED
- VALID NON-REPLICATION
- INVALID/INCONCLUSIVE
