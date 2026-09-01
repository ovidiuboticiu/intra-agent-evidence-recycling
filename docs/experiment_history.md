# Experiment History

This document records the methodological evolution of the **Intra-Agent Evidence Recycling** project. It preserves hypotheses, instrument failures, calibration decisions, amendments, aborted attempts, and confirmatory results as a transparent audit trail.

## Research question

The project asks whether information originating from a single external source can acquire excess behavioral weight after it is repeated or reused within persistent LLM memory, despite the absence of additional genuinely independent evidence.

A related mitigation question asks whether explicit lineage metadata can reduce that behavioral effect. Behavioral resistance to counterevidence is not treated as proof that the model internally counts repeated records as independent sources.

# v0.2 — Early instrument

**Status:** CLOSED — measurement-limited

v0.2 compared independent evidence, active reuse, self-labeled reuse, lineage-labeled reuse, and passive repetition. It eventually produced a complete valid dataset after technical timeout events were separately rerun.

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
- every row embedded hashes matching the frozen preregistration, stimuli, and rationale;
- all four validity gates passed;
- the final release was independently audited and fixed through a post-collection SHA-256 manifest.

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

# Version classification summary

| Version | Classification | Included in confirmatory inference? |
| --- | --- | --- |
| v0.2 | Early/measurement-limited | No |
| v0.3.1 | Calibration/exploratory | No |
| v0.4.1 | Aborted confirmatory attempt | No |
| v0.4.2 | Aborted pre-data confirmatory attempt | No |
| v0.4.3 | Behavioral-confirmatory; completed and audited | **Yes, v0.4.3 only** |

# General methodological lessons

1. Instrument failure is not hypothesis failure.
2. A pilot result is not confirmation.
3. Aborted attempts should remain visible in the scientific record.
4. Technical failures and scientific outcomes must be logged separately.
5. Confirmatory thresholds must be frozen before collection.
6. Fresh stimuli should be used after materially redesigned failed attempts.
7. Behavioral effects should not be overinterpreted as proof of an internal mechanism.
8. A provenance audit is itself a measurement instrument.
9. Structured-output compliance is part of reproducibility.
10. Partial confirmation is scientifically informative when reported without rescuing failed hypotheses.

# Next research steps

- replicate H1 on additional models and runtimes;
- test whether the effect survives less explicit or more naturalistic memory records;
- design a dedicated, independently validated provenance-use study;
- refine lineage interventions rather than treating the v0.4.3 H2 failure as proof that lineage can never help;
- prepare a manuscript or preprint without generalizing beyond the frozen scope.
