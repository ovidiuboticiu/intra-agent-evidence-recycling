# Experiment History

This document records the methodological evolution of the **Intra-Agent Evidence Recycling (IAER)** project. It preserves hypotheses, instrument failures, calibration decisions, amendments, aborted attempts, qualification studies, confirmatory results, publication deviations, and stopping decisions as a transparent audit trail.

## Research question

The project asks whether information originating from a single external source can acquire excess behavioral weight after it is repeated or reused within persistent LLM memory, despite the absence of additional genuinely independent evidence.

A related mitigation question asks whether explicit lineage metadata can reduce that behavioral effect. Behavioral resistance to counterevidence is not treated as proof that the model internally counts repeated records as independent sources.

# v0.2 — Early instrument

**Status:** CLOSED — measurement-limited

v0.2 compared independent evidence, active reuse, self-labeled reuse, lineage-labeled reuse, and passive repetition.

Main limitations included ambiguous old/new wording, inconsistent confidence interpretation, excessively strong counterevidence in places, and insufficiently concrete provenance/source-count questions.

The preregistered effect was not supported. Because the instrument itself had substantial measurement limitations, this was not treated as decisive evidence against the broader research question.

# v0.3 / v0.3.1 — Calibration and discovery pilot

**Status:** COMPLETED — exploratory/calibration only

v0.3 repaired the early instrument by introducing explicit `CLAIM_A` / `CLAIM_B` labels, concrete record-ID provenance auditing, a `source_only` baseline, graded counterevidence, and a semantic provenance preflight.

The first v0.3 execution failed before any valid trajectory because a free-text structured-output field was truncated. Since no scientific trajectory had completed, a technical amendment removed the unused free-text field. The amended version was v0.3.1.

## v0.3.1 result

- 48/48 valid trajectories;
- 8 fictional items;
- all preregistered calibration gates passed.

At q=0.80:

| Condition | Retained INITIAL |
| --- | ---: |
| `source_only` | 0/8 |
| `passive_repeat` | 8/8 |
| `active_plain` | 8/8 |
| `active_self_labeled` | 7/8 |
| `active_lineage` | 0/8 |
| `independent_evidence` | 8/8 |

These were explicitly exploratory findings. They motivated later confirmatory hypotheses but did not confirm them.

A historical Structured Output compliance bug (`"strict": "true"` instead of boolean `True`) remained in the archived runner; outputs used in analysis were nevertheless parseable and bounded. The bug was repaired in later versions rather than rewritten retrospectively.

# v0.4.1 — First confirmatory attempt

**Status:** ABORTED — manipulation validity failure

v0.4.1 froze two co-primary hypotheses:

- H1: `passive_repeat > neutral_filler`;
- H2: `active_plain > active_lineage`.

Each required RD ≥ +0.25 and Holm-adjusted exact paired McNemar p < 0.05.

The run produced 7 valid trajectories, then stopped at item `C16`, condition `active_lineage`, operation `O2`, where the model returned the counter claim during a manipulation that required application of the initial claim.

The preregistered rule classified this as `MANIPULATION_FAILURE`. The partial observations were retained for audit but not used to test H1/H2.

# v0.4.2 — Second confirmatory attempt

**Status:** ABORTED BEFORE DATA COLLECTION — mandatory provenance preflight failure

v0.4.2 repaired the active manipulation by separating downstream application from repeated epistemic re-decision. It also corrected the `strict` boolean compliance bug.

The mandatory preflight required provenance, behavioral-control, and active-application cases to pass. One provenance sanity case failed: expected independent root `["E1"]`, returned `[]`.

No confirmatory trajectories were collected. Re-running until the gate happened to pass would have undermined the purpose of the gate.

This motivated v0.4.3, where provenance remained measured but was no longer a behavioral validity gate.

# v0.4.3 — Behavioral-confirmatory study

**Status:** COMPLETED — VALID DATASET; H1 SUPPORTED; H2 NOT SUPPORTED

v0.4.3 used 32 new balanced fictional items, fixed-N stopping, paired risk differences, exact paired McNemar tests, Holm correction across H1/H2, and four preregistered validity gates.

## Integrity

- 168/168 valid unique trajectories;
- 0 technical-failure rows;
- 0 duplicate, missing, extra, or unresolved keys;
- all 64 active trajectories contained exactly five valid application outputs;
- all four validity gates passed.

## Confirmatory results

| Hypothesis | Retention | RD | Holm p | Verdict |
| --- | ---: | ---: | ---: | --- |
| H1 `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 0.6875 | 9.5367432e-7 | **Supported** |
| H2 `active_plain > active_lineage` | 2/32 vs 0/32 | 0.0625 | 0.50 | **Not supported** |

The provenance audit was exact for 168/168 trajectories but was preregistered as descriptive/exploratory. It cannot rescue H2 or establish an internal provenance-use mechanism.

## Supported claim

Under the frozen v0.4.3 task family and `qwen3.5-4b` configuration, five explicitly derivative reviews of one initial source substantially increased retention of the initial claim relative to an equal-sized unrelated-memory control.

## Limitations

The archive does not pin every external runtime detail/model artifact hash, so exact computational replication requires additional environment metadata. Generalization to other model families was not established by v0.4.3.

# v0.5.0 — Phi-4-mini-instruct cross-family qualification attempt

**Status:** CLOSED — INVALID/INCONCLUSIVE; no confirmatory outcomes collected

v0.5.0 froze a cross-family replication package for H1 with 32 new items, 104 planned confirmatory trajectories, and a mandatory four-case behavioral preflight.

Three cases passed. The mirrored `independent_evidence` case with INITIAL=`CLAIM_B` failed: expected `CLAIM_B`, returned `CLAIM_A`.

Under the fail-closed rule, confirmatory collection was not authorized. This was a model/interface qualification failure, not evidence against IAER.

# v0.5.1 — Exploratory response-interface diagnostic

**Status:** COMPLETED — exploratory only

v0.5.1 examined possible causes of the v0.5.0 preflight failure using three response/instruction modes.

- 48/48 planned calls completed;
- overall normative accuracy: 29/48;
- substantial variation across `claim_label`, `value_token`, and `explicit_odds`;
- `independent_five` performance was consistently weaker than `source_only`.

The diagnostic was descriptive only and did not alter v0.5.0.

# v0.5.2 — Phi-4-mini-reasoning eligibility pilot

**Status:** COMPLETED — VALID DATASET; INELIGIBLE

v0.5.2 was a preregistered fixed-N eligibility pilot with 12 balanced items × 3 conditions = 36 planned calls.

## Integrity

- 36/36 valid planned trajectories;
- 0 failure rows;
- 0 missing, extra, duplicate, or metadata-mismatched keys.

## Results

| Condition | Correct | Requirement | Result |
| --- | ---: | ---: | --- |
| `baseline_initial` | 4/12 | ≥10/12 | FAIL |
| `counter_single_strong` | 12/12 | ≥10/12 | PASS |
| `independent_five_initial` | 2/12 | ≥10/12 | FAIL |

G1 integrity passed; behavioral accuracy/symmetry gates failed. Final decision: `INELIGIBLE`.

No confirmatory IAER run followed. Eligibility was explicitly not confirmation, refutation, or estimation of IAER.

# v0.6 — Ministral staged cross-family program

**Status:** CLOSED — CALIBRATION_FAILURE; STOP BEFORE ELIGIBILITY

v0.6 introduced a three-stage architecture:

**Calibration → Eligibility → Confirmatory IAER**

Target model: Ministral-3-8B-Instruct-2512 GGUF Q4_K_M under LM Studio 0.4.23, context 8192, temperature 0, seed 42.

Calibration used only normative evidence-integration controls and excluded IAER treatment conditions.

## Interface A

- 24/24 valid;
- 0 failure rows;
- `baseline_initial`: 8/8;
- `counter_single_strong`: 8/8;
- `independent_five_initial`: 0/8;
- C1 integrity PASS, behavioral gates FAIL;
- decision: `INTERFACE_A_FAILED_BEHAVIORALLY`.

Because integrity passed and the failure was behavioral, Interface B was authorized under the frozen rule.

## Interface B

- 24/24 valid;
- 0 failure rows;
- `baseline_initial`: 8/8;
- `counter_single_strong`: 8/8;
- `independent_five_initial`: 0/8;
- C1 integrity PASS, behavioral gates FAIL;
- decision: `CALIBRATION_FAILURE`.

## Final v0.6 decision

**STOP BEFORE ELIGIBILITY.**

Eligibility and Confirmatory IAER were not run. v0.6 is a calibration failure, not an IAER non-replication.

## Freeze-A publication deviation

A closure audit found that the public Freeze-A tag contained the program-level protocol but omitted several calibration-specific implementation files intended by the publication checklist. The exact local materials were later archived, but this post-outcome publication cannot retroactively substitute for a complete pre-outcome public freeze.

The original tag was not rewritten. A stale simplified A→B sentence in `INTERFACES_v0_6.json` was also documented; it had no realized decision impact because Interface A integrity passed before B was authorized.

# v0.7 — Measurement-decoupling instrument redesign

**Status:** CLOSED — REDESIGN_FAILED_STOP; PROJECT PAUSED

v0.7 addressed the main v0.6 measurement confound by removing reliability scores and Bayesian evidence aggregation.

The frozen rule was explicit:

1. each independent ROOT SOURCE contributes one vote;
2. a DERIVED RECORD contributes zero new votes;
3. multiple records from the same root do not add votes;
4. choose the claim with more distinct independent root votes.

The complete preregistration commit and full frozen ZIP asset were publicly published and verified before the first behavioral call.

## Design

12 fresh balanced items × 4 conditions = 48 planned calls.

- R1 `two_initial_one_counter`: 2 independent INITIAL roots vs 1 COUNTER root;
- R2 `one_initial_two_counter`: 1 INITIAL root vs 2 COUNTER roots;
- R3 `derived_lure_initial_two_counter`: 1 INITIAL root + 5 explicitly derivative INITIAL records vs 2 COUNTER roots;
- R4 `three_initial_two_counter`: 3 INITIAL roots vs 2 COUNTER roots.

## Integrity

- 48/48 planned rows valid;
- 0 failure rows;
- 0 missing, extra, duplicate, or metadata-error rows;
- exact model identity/SHA, temperature, seed, manifest, and prompt-spec metadata were consistent.

P1 integrity: PASS.

## Results

| Condition | Correct | Prespecified condition threshold |
| --- | ---: | --- |
| R1 `two_initial_one_counter` | 12/12 | PASS |
| R2 `one_initial_two_counter` | 11/12 | PASS |
| R3 `derived_lure_initial_two_counter` | 7/12 | FAIL |
| R4 `three_initial_two_counter` | 12/12 | PASS |

Frozen gates:

- P1 integrity: PASS;
- P2 condition accuracy: FAIL;
- P3 INITIAL-label symmetry: FAIL;
- P4 presentation-order symmetry: FAIL;
- P5 derived-record lure: FAIL.

Final frozen decision:

> **REDESIGN_FAILED_STOP**

No rescue interface, alternate prompt, or second v0.7 run is permitted.

## Descriptive v0.7 pattern

Across R1, R2, and R4, where only independent root sources were present, the model was correct on 35/36 calls.

In R3, where five records were explicitly marked as derived from one INITIAL root and as adding zero new epistemic votes, accuracy was 7/12. All five R3 errors selected the INITIAL claim.

R3 was not cleanly symmetric: INITIAL=`CLAIM_A` scored 5/6, INITIAL=`CLAIM_B` 2/6; A_FIRST scored 5/6, B_FIRST 2/6. Cross-cell n was only three items.

Therefore the pattern is compatible with—but does not establish—the possibility that derivative surface multiplicity interferes with correct source-lineage use. Label/order/representation effects remain possible confounds.

## Interpretation boundary

v0.7 was preregistered as an instrument-usability redesign, not an IAER replication. It cannot confirm, refute, or estimate IAER and does not alter v0.4.3.

## Raw-data archive location

The raw `results_v0_7.jsonl` is contained in the public results-release ZIP and is identified by SHA-256 in the repository. It is not duplicated as a standalone ordinary repository file. See `experiments/v0_7_instrument_redesign/RAW_DATA_LOCATION_v0_7.md`.

# Version classification summary

| Version | Classification | Included in confirmatory IAER inference? |
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
| v0.7 | Preregistered instrument redesign; REDESIGN_FAILED_STOP | No |

# General methodological lessons

1. Instrument failure is not hypothesis failure.
2. A pilot or eligibility result is not confirmation.
3. Aborted and failed qualification attempts should remain visible.
4. Technical failures and scientific outcomes must be logged separately.
5. Confirmatory thresholds must be frozen before collection.
6. Fresh stimuli should follow materially redesigned failed attempts.
7. Behavioral effects should not be overinterpreted as internal mechanisms.
8. A provenance audit is itself a measurement instrument.
9. Structured-output compliance is part of reproducibility.
10. Partial confirmation must be reported without rescuing failed co-primary hypotheses.
11. Cross-model replication requires model/task eligibility before confirmatory comparison.
12. Public freeze completeness must itself be audited; a post-outcome archive cannot retroactively substitute for a missing pre-outcome artifact.
13. Repeated evidence-aggregation qualification failure is a reason to redesign the instrument, not to search models until one passes.
14. Explicit lineage labels do not guarantee that a model will apply a root-counting rule correctly when derivative surface multiplicity is present.
15. A failed preregistered redesign can still be scientifically informative, but it must not be reinterpreted as confirmatory evidence.
16. Once a preregistered redesign reaches its STOP rule, further prompt/interface tuning belongs to a new scientific idea and version, not a rescue run.

# Current research disposition

**PAUSED — instrument redesign path exhausted under v0.7.**

The only completed confirmatory IAER result remains v0.4.3 on the frozen Qwen configuration. Cross-family generalization remains unresolved: later Phi and Ministral programs did not reach a valid confirmatory IAER comparison.

The next step is not v0.8. The project has completed a program-level scientific audit in [`program_audit_v0_2_to_v0_7.md`](program_audit_v0_2_to_v0_7.md). A future restart should occur only if a materially new measurement idea satisfies the restart criteria recorded there.