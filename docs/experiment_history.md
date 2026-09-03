# Experiment History

This document records the methodological evolution of the **Intra-Agent Evidence Recycling (IAER)** project. It preserves hypotheses, instrument failures, calibration decisions, amendments, aborted attempts, qualification studies, confirmatory results, and publication deviations as a transparent audit trail.

## Research question

The project asks whether information originating from a single external source can acquire excess behavioral weight after it is repeated or reused within persistent LLM memory, despite the absence of additional genuinely independent evidence.

A related mitigation question asks whether explicit lineage metadata can reduce that behavioral effect. Behavioral resistance to counterevidence is not treated as proof that the model internally counts repeated records as independent sources.

# v0.2 — Early instrument

**Status:** CLOSED — measurement-limited

v0.2 compared independent evidence, active reuse, self-labeled reuse, lineage-labeled reuse, and passive repetition.

## Main limitations

1. `old_value` / `new_value` wording was semantically ambiguous.
2. `confidence_old` was not interpreted consistently as a 0–100 belief measure.
3. Counterevidence wording was too strong in places, producing a ceiling effect.
4. Source-count and provenance questions were insufficiently concrete.

## Scientific status

The preregistered effect was not supported. Because of the measurement problems, the result was treated as measurement-limited rather than decisive evidence against the broader research question.

# v0.3 / v0.3.1 — Calibration and discovery pilot

**Status:** COMPLETED — exploratory/calibration only

v0.3 introduced major repairs:

- `CLAIM_A` / `CLAIM_B` replaced ambiguous old/new wording;
- provenance was measured using concrete memory-record IDs;
- a `source_only` baseline was added;
- counterevidence was calibrated at multiple strengths;
- a semantic provenance preflight was required;
- the run was explicitly designated a calibration pilot.

An initial v0.3 execution failed before any valid trajectory because a free-text `reason` field was truncated inside structured JSON. Because `completed_valid=0`, the schema was technically amended before scientific data collection. The amended version is v0.3.1.

## v0.3.1 completion

- 48/48 valid trajectories;
- 8 fictional items;
- 6 conditions per item;
- all preregistered calibration gates passed.

## Exploratory behavioral pattern at q = 0.80

| Condition | Retained initial claim |
| --- | ---: |
| `source_only` | 0/8 |
| `passive_repeat` | 8/8 |
| `active_plain` | 8/8 |
| `active_self_labeled` | 7/8 |
| `active_lineage` | 0/8 |
| `independent_evidence` | 8/8 |

These findings were exploratory. The pilot suggested that multiple target-consistent records derived from one epistemic root might create behavioral resistance to counterevidence and that explicit lineage metadata might reduce it.

# v0.4.1 — First confirmatory attempt

**Status:** ABORTED — manipulation validity failure

v0.4.1 introduced 32 new balanced items, a neutral-filler control, paired exact tests, Holm correction, and a minimum effect-size requirement.

## Abort event

The run produced 7 valid trajectories and then stopped at item `C16`, condition `active_lineage`, operation `O2`: expected `CLAIM_B`, returned `CLAIM_A`.

The active manipulation asked the model to choose the claim again at every reuse step. The preregistration defined any spontaneous switch as a manipulation failure, so the study stopped fail-closed and was not resumed.

## Interpretation

This was not treated as evidence against H1 or H2. The experiment failed to implement the intended manipulation reliably.

# v0.4.2 — Second confirmatory attempt

**Status:** ABORTED BEFORE DATA COLLECTION — provenance preflight failure

v0.4.2 repaired the active manipulation: the model performed a downstream application task with an already authorized configuration instead of reassessing the claim at every step. The inherited Structured Output bug was also repaired by using Python boolean `True` for `strict`.

## Preflight outcome

Behavioral controls and all active application checks passed. One provenance sanity test failed: expected independent root `["E1"]`, returned `[]`.

Because provenance was still a mandatory gate, no confirmatory collection began. Repeatedly rerunning the provenance gate until it passed would have undermined its purpose.

# v0.4.3 — Behavioral-confirmatory study

**Status:** COMPLETED — VALID DATASET; H1 SUPPORTED; H2 NOT SUPPORTED

v0.4.3 retained the repaired application manipulation and the original behavioral co-primary hypotheses, used 32 fresh fictional items, and classified provenance as secondary/descriptive rather than as a validity gate.

## Frozen design

- 32 core items;
- five core conditions on every item;
- eight prespecified positive-control trajectories;
- 168 planned valid trajectories;
- paired RD threshold of at least +0.25 for each hypothesis;
- two-sided exact paired McNemar tests;
- Holm correction across H1 and H2;
- fixed-N stopping and fail-closed technical behavior.

All eight behavioral preflight cases passed before collection was authorized.

## Completion and integrity

- 168/168 valid unique trajectories;
- zero technical-failure rows;
- zero duplicate, missing, extra, or unresolved keys;
- all 64 active trajectories contained exactly five valid application outputs;
- every row embedded hashes matching the frozen materials;
- all four validity gates passed.

## Validity gates

| Gate | Observed | Verdict |
| --- | ---: | --- |
| V1: `source_only` selects COUNTER | 32/32 | Pass |
| V2: positive control retains INITIAL | 7/8 | Pass |
| V3: complete active traces | 64/64 | Pass |
| V4: complete valid planned dataset | 168/168 | Pass |

## Confirmatory results

| Hypothesis | Retention | Discordant pairs | RD | Holm p | Verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| H1: `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 22/0 | 0.6875 | 9.5367e-7 | **Supported** |
| H2: `active_plain > active_lineage` | 2/32 vs 0/32 | 2/0 | 0.0625 | 0.50 | **Not supported** |

Full two-effect confirmation was not achieved because H2 failed both the preregistered effect-size threshold and significance criterion.

## Provenance result

The provenance audit was exact in 168/168 trajectories, with zero false independent IDs and zero missed roots. Per the preregistration, this is descriptive/exploratory only. It does not rescue H2 or establish a confirmed provenance-use mechanism.

## Supported claim

Under this frozen task family and `qwen3.5-4b` configuration, five explicitly derivative reviews of one initial source substantially increased retention of the initial claim relative to an equal-sized unrelated-memory control.

## Claims not established

- A medium-to-large lineage-mitigation effect was not confirmed.
- No general mechanism across models or agent architectures was established.
- Exact provenance judgments do not by themselves prove how provenance was used internally.

# v0.5.0 — Phi-4-mini-instruct cross-family qualification attempt

**Status:** CLOSED — INVALID/INCONCLUSIVE; no confirmatory outcomes collected

The frozen package and technical checks passed, but one of four mandatory behavioral preflight cases failed. Under the fail-closed rule, the configuration was not allowed to proceed to confirmatory IAER collection.

This was treated as a model/interface qualification failure, not as evidence against the IAER research question.

# v0.5.1 — Exploratory response-interface diagnostic

**Status:** COMPLETED — exploratory only

v0.5.1 examined whether response representation contributed to the Phi-4-mini-instruct qualification problem.

- 48/48 planned calls completed;
- overall normative accuracy: 29/48;
- accuracy varied substantially across `claim_label`, `value_token`, and `explicit_odds` response interfaces.

The result suggested substantial representation sensitivity and unreliable evidence aggregation under that model/configuration. Because the study was exploratory, it did not alter the status of v0.5.0 and did not test IAER confirmatorily.

# v0.5.2 — Phi-4-mini-reasoning eligibility pilot

**Status:** COMPLETED — VALID DATASET; INELIGIBLE

v0.5.2 was a preregistered fixed-N behavioral eligibility pilot using Microsoft Phi-4-mini-reasoning GGUF Q4_K_M.

## Integrity

- 36/36 valid planned trajectories;
- 0 failure rows;
- 0 missing, extra, duplicate, or metadata-mismatched keys;
- frozen model, SHA-256, temperature, seed, and manifest matched.

## Prespecified behavioral results

| Condition | Correct | Requirement | Result |
| --- | ---: | ---: | --- |
| `baseline_initial` | 4/12 | at least 10/12 | FAIL |
| `counter_single_strong` | 12/12 | at least 10/12 | PASS |
| `independent_five_initial` | 2/12 | at least 10/12 | FAIL |

G1 integrity passed, while the condition-accuracy and symmetry gates failed. The preregistered decision was therefore `INELIGIBLE`.

## Interpretation

This exact quantized model/interface/prompt/configuration could not proceed to confirmatory IAER collection. The result did not confirm, refute, or estimate IAER and did not alter v0.4.3.

# v0.6 — Ministral staged cross-family program

**Status:** CLOSED — CALIBRATION_FAILURE; STOP BEFORE ELIGIBILITY

v0.6 introduced a stricter three-stage architecture:

**Calibration → Eligibility → Confirmatory IAER**

The candidate model was Ministral-3-8B-Instruct-2512 GGUF Q4_K_M under LM Studio 0.4.23, context 8192, temperature 0, seed 42.

The confirmatory target, had the model reached Stage C, would have been the v0.4.3 H1 effect `passive_repeat > neutral_filler`. No confirmatory IAER collection occurred in v0.6.

## Calibration design

Calibration used only normative evidence-integration controls and explicitly excluded IAER treatment conditions. Two response interfaces were prespecified:

- Interface A: `chosen_claim` + descriptive `confidence_chosen`;
- Interface B: `chosen_claim` only.

The intended rule was fail-closed:

- technical/integrity failure → `INVALID/INCONCLUSIVE` and stop;
- Interface A integrity PASS plus behavioral gate failure → Interface B authorized;
- Interface B behavioral failure → `CALIBRATION_FAILURE` and stop;
- no Interface C.

## Interface A result

- 24/24 valid planned rows;
- 0 failure rows;
- C1 integrity: PASS;
- `baseline_initial`: 8/8 correct;
- `counter_single_strong`: 8/8 correct;
- `independent_five_initial`: 0/8 correct.

The failure was symmetric over INITIAL orientation and presentation order. Decision: `INTERFACE_A_FAILED_BEHAVIORALLY`. Interface B was therefore authorized.

## Interface B result

- 24/24 valid planned rows;
- 0 failure rows;
- C1 integrity: PASS;
- `baseline_initial`: 8/8 correct;
- `counter_single_strong`: 8/8 correct;
- `independent_five_initial`: 0/8 correct.

The same symmetric pattern recurred. Decision: `CALIBRATION_FAILURE`.

## Final v0.6 decision

**STOP BEFORE ELIGIBILITY.**

Eligibility was not authorized. Confirmatory IAER was not authorized. v0.6 is therefore a calibration failure, not an IAER non-replication.

The repeated 0/8 result on `independent_five_initial` across both prespecified response interfaces is a descriptive calibration observation. It does not identify an internal mechanism and does not establish evidence for or against IAER.

## Freeze-A publication deviation

A closure audit discovered that the public preregistration tag contained the program-level protocol but omitted several calibration-specific implementation files that the publication checklist had intended to include. The complete local pre-run package was preserved and later archived with the outcomes, but this post-outcome archival publication must not be described as retroactive preregistration.

The original preregistration tag was not rewritten. The deviation is explicitly documented in `experiments/v0_6_ministral/01_calibration/FREEZE_A_PUBLICATION_DEVIATION_v0_6.md` and in the v0.6 results release.

The same closure audit also documented a stale simplified A→B summary line in `INTERFACES_v0_6.json`. It had no realized decision impact because Interface A integrity passed before Interface B was authorized.

# Version classification summary

| Version | Classification | Included in confirmatory inference? |
| --- | --- | --- |
| v0.2 | Early/measurement-limited | No |
| v0.3.1 | Calibration/exploratory | No |
| v0.4.1 | Aborted confirmatory attempt | No |
| v0.4.2 | Aborted pre-data confirmatory attempt | No |
| v0.4.3 | Behavioral-confirmatory; completed and audited | **Yes, v0.4.3 only** |
| v0.5.0 | Cross-family qualification; invalid/inconclusive | No |
| v0.5.1 | Exploratory interface diagnostic | No |
| v0.5.2 | Preregistered eligibility pilot; INELIGIBLE | No |
| v0.6 | Staged Ministral program; CALIBRATION_FAILURE before eligibility | No |

# General methodological lessons

1. Instrument failure is not hypothesis failure.
2. A pilot or eligibility result is not confirmation.
3. Aborted and failed qualification attempts should remain visible in the scientific record.
4. Technical failures and scientific outcomes must be logged separately.
5. Confirmatory thresholds must be frozen before collection.
6. Fresh stimuli should be used after materially redesigned failed attempts.
7. Behavioral effects should not be overinterpreted as proof of an internal mechanism.
8. A provenance audit is itself a measurement instrument.
9. Structured-output compliance is part of reproducibility.
10. Partial confirmation is scientifically informative when reported without rescuing failed hypotheses.
11. Cross-model replication requires model/task eligibility before confirmatory comparison.
12. Public freeze completeness must itself be audited; a post-outcome archive cannot retroactively substitute for a missing pre-outcome public artifact.
13. Repeated qualification failure on evidence aggregation is a reason to redesign the instrument, not to keep searching models until one passes.

# Current research disposition

The only completed confirmatory IAER result remains v0.4.3 on the frozen Qwen configuration.

The Phi and Ministral follow-ups show that cross-family replication is presently limited by task/interface eligibility and evidence-aggregation behavior. The strongest defensible next step, if the project continues, is a new instrument-redesign version with a complete pre-outcome public freeze, rather than immediately testing additional model families under the unchanged aggregation control.
