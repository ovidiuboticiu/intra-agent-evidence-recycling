# IAER v0.5.0 — preflight closure report

Status: **INVALID/INCONCLUSIVE; confirmatory collection not started**

This report was written after the preregistered behavioral preflight. It is a
post-freeze outcome record and does not modify the frozen preregistration,
stimuli, runner, analysis plan, or model configuration.

## Frozen identity

- Preregistration tag: `v0.5.0-preregistration`
- Preregistration commit: `e3dcb40`
- Model API identifier: `microsoft_phi-4-mini-instruct`
- Model SHA-256:
  `01999f17c39cc3074afae5e9c539bc82d45f2dd7faa3917c66cbef76fce8c0c2`
- Temperature: `0`
- Seed: `42`

## Preflight outcome

The mandatory four-case behavioral preflight ran once on
`2026-09-02T14:11:36.388431+00:00`.

| Case | Condition | Initial | Expected | Observed | Result |
|---:|---|---|---|---|---|
| 1 | `source_only` | `CLAIM_A` | `CLAIM_B` | `CLAIM_B` | PASS |
| 2 | `independent_evidence` | `CLAIM_A` | `CLAIM_A` | `CLAIM_A` | PASS |
| 3 | `source_only` | `CLAIM_B` | `CLAIM_A` | `CLAIM_A` | PASS |
| 4 | `independent_evidence` | `CLAIM_B` | `CLAIM_B` | `CLAIM_A` | FAIL |

Case 4 returned `CLAIM_A` with confidence `99`, although five explicitly
independent sources with reliability `0.65` supported `CLAIM_B` against one new
independent source with reliability `0.80` supporting `CLAIM_A`.

All four responses were structurally valid. Each completed with finish reason
`stop`, no reasoning payload, zero reported reasoning tokens, and one transport
attempt. Frozen-package, model-file, API-identifier, and stimulus-design checks
all passed before the behavioral cases.

Raw preflight record SHA-256:
`f421e1d555209371fd3c1582a3fea5d43f89df82b4a235d347b30f56b943f6af`.

## Preregistered decision

The preregistration required all four cases to pass in one run. It states that
a failed preflight ends v0.5.0 as invalid/inconclusive for this model and
configuration and prohibits confirmatory collection under the same version.

Accordingly:

- `02_RUN_CONFIRMATORY_EXPERIMENT.bat` was not run;
- no confirmatory `results_v0_5_0.jsonl` was produced;
- H1-R was neither supported nor rejected in v0.5.0;
- the preflight was not tuned, overwritten, or rerun.

## Interpretation boundary

The failure is behavioral rather than technical. The mirrored outcomes are
consistent with possible claim-label asymmetry or evidence-integration failure,
but one four-case gate cannot distinguish those explanations. Any diagnosis is
therefore exploratory and must be conducted under a new, separately frozen
version.
