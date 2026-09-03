# IAER Program-Level Scientific Audit — v0.2 to v0.7

**Audit status:** post-program methodological synthesis; no new behavioral data  
**Scope:** IAER v0.2 through v0.7  
**Current disposition:** **PAUSED**

## Executive conclusion

The IAER program has produced **one completed confirmatory finding** and a sequence of exploratory, qualification, calibration, and instrument-redesign results that constrain how that finding may be generalized.

The strongest supported statement remains the v0.4.3 H1 result:

> Under the frozen v0.4.3 task family and `qwen3.5-4b` configuration, five explicitly derivative reviews of one initial source substantially increased retention of the initial claim relative to five unrelated filler records.

The corresponding paired result was 22/32 versus 0/32, RD = 0.6875, with Holm-adjusted exact McNemar p = 9.5367432e-7.

The v0.4.3 H2 lineage-mitigation hypothesis was **not supported**. Cross-family generalization of H1 remains **unresolved rather than falsified**, because the Phi and Ministral programs did not reach a valid confirmatory IAER comparison.

v0.7 was a preregistered measurement-decoupling pilot. It removed probability/reliability arithmetic and asked the model to count independent root sources while assigning zero new votes to derived records. The model was correct on 35/36 calls across the three conditions containing only independent roots, but only 7/12 in the derived-record lure condition. All five lure errors selected the INITIAL claim. This is scientifically interesting as a descriptive pattern, but v0.7 explicitly cannot confirm, refute, or estimate IAER.

The program should therefore remain **PAUSED**. No v0.8 run is recommended under the current measurement family, and additional model-shopping is not justified.

## 1. Evidence classification

### Tier A — confirmatory evidence

#### v0.4.3

- fixed-N behavioral-confirmatory study;
- 168/168 planned trajectories valid;
- all preregistered validity gates passed;
- H1 `passive_repeat > neutral_filler`: supported;
- H2 `active_plain > active_lineage`: not supported;
- provenance exactness 168/168: descriptive/exploratory only.

This is the **only version included in confirmatory IAER inference**.

### Tier B — exploratory, qualification, calibration, or redesign evidence

#### v0.3.1

Calibration/discovery only. It motivated the later confirmatory design but cannot itself confirm an IAER effect.

#### v0.5.1

Exploratory response-interface diagnostic on Phi-4-mini-instruct. It showed substantial representation sensitivity and weak performance on multiple-evidence integration.

#### v0.5.2

Preregistered eligibility pilot on Phi-4-mini-reasoning. Integrity passed, but behavioral eligibility gates failed. The model/configuration was `INELIGIBLE`; no confirmatory IAER run followed.

#### v0.6

Preregistered staged Ministral program. Both calibration interfaces had complete technical integrity but failed the same `independent_five_initial` control. Final decision: `CALIBRATION_FAILURE — STOP BEFORE ELIGIBILITY`.

#### v0.7

Preregistered measurement-decoupling redesign on Ministral. Integrity passed, but the derived-record lure gate failed and the frozen decision was `REDESIGN_FAILED_STOP`.

### Tier C — instrument/process failures

#### v0.2

Measurement-limited early instrument. Its null/weak result is not treated as decisive evidence against the research question.

#### v0.4.1

Aborted confirmatory attempt after a manipulation-validity failure. Partial observations are not used for confirmatory inference.

#### v0.4.2

Aborted before confirmatory data collection after a mandatory provenance preflight failure. It established that provenance measurement was not yet stable enough to remain a validity gate.

#### v0.6 publication process

The original Freeze-A public tag omitted several calibration-specific implementation files that the publication checklist had intended to include. This was documented after closure without rewriting the original tag. The deviation reduces the evidentiary value of the claim that the *complete* v0.6 implementation was publicly frozen before outcomes, but it does not alter the descriptive calibration rows or the stopping decision.

## 2. What is supported

### Supported claim A

In v0.4.3, under the exact frozen Qwen task/configuration, passive repetition of five explicitly derivative reviews substantially increased resistance to later counterevidence relative to an equal-sized neutral-filler control.

### Supported claim B

The v0.4.3 effect is behaviorally measurable without requiring a mechanistic claim that the model literally represents repeated records as independent sources.

### Supported methodological claim

Cross-model IAER replication cannot be interpreted safely unless the candidate model first demonstrates adequate task/interface competence. The v0.5-v0.7 sequence shows why eligibility and instrument validation must be separated from confirmatory inference.

## 3. What is not supported

The program does **not** establish any of the following:

- universal or architecture-independent IAER;
- successful cross-family replication of v0.4.3 H1;
- that LLMs internally count duplicate/derived records as independent evidence;
- a general mechanism explaining the v0.4.3 behavioral effect;
- a reliable medium-to-large mitigation effect from explicit lineage metadata;
- that v0.7 is a confirmation or non-replication of IAER;
- that Phi or Ministral refuted IAER.

## 4. Cross-version pattern that deserves attention

A recurring difficulty appears in how non-Qwen candidate configurations handle multiple pieces of evidence.

- Phi-4-mini-instruct failed the mandatory v0.5.0 mirrored independent-evidence preflight case.
- v0.5.1 showed strong representation sensitivity and poor `independent_five` accuracy.
- Phi-4-mini-reasoning v0.5.2 was 2/12 on `independent_five_initial` and was declared `INELIGIBLE`.
- Ministral v0.6 was 0/8 on `independent_five_initial` under both prespecified response interfaces, while scoring 8/8 on the baseline and 8/8 on the stronger-counter condition.
- v0.7 removed reliability scores and probabilistic aggregation. Ministral then scored 35/36 across root-only counting conditions, but 7/12 when five explicitly derivative INITIAL records were added to a 1-root-vs-2-root decision.

This sequence motivates, but does not prove, a hypothesis that **surface multiplicity and/or initial-claim anchoring can interfere with epistemically correct source-lineage use even when an explicit root-counting rule is provided**.

The v0.7 asymmetry across label/order cells means that hypothesis is not yet isolated from representation/order effects.

## 5. Why no immediate v0.8 is recommended

Continuing by changing prompts, labels, thresholds, or candidate models until one passes would create a serious risk of post-hoc instrument tuning and model-shopping.

The v0.7 preregistration explicitly specified `REDESIGN_FAILED_STOP` when integrity passed but any behavioral gate failed. That outcome occurred. Respecting that stop is part of the scientific result.

A future return is justified only by a **materially new measurement idea**, not a rescue modification of v0.7.

## 6. Minimum restart criteria for any future IAER study

A future version should not begin until all of the following are satisfied:

1. **Confound separation:** derivative multiplicity must be separable from label orientation, presentation order, record position, record length, and simple repetition count.
2. **Independent instrument validation:** the new measurement logic should be checked against a deterministic oracle and, where feasible, an independent implementation before model outcomes are collected.
3. **Direct paired contrast:** a future IAER test should compare carefully matched derivative versus non-derivative structures rather than infer the effect through a control that also requires unrelated probabilistic competence.
4. **Fresh stimuli:** any materially redesigned confirmatory/eligibility study must use new held-out stimuli.
5. **Complete pre-outcome freeze:** code, prompts, stimuli, config, manifest, analysis, and the complete archive asset must be publicly frozen and verified before the first behavioral call.
6. **No adaptive model-shopping:** if multiple model families are to be tested, the family set and qualification procedure should be prespecified before outcomes rather than expanded until a positive result appears.
7. **Explicit interpretation boundary:** behavioral weighting, provenance judgment, and mechanistic explanation must remain separate claims.

## 7. Publication value of the program as it stands

The project already has publication value as a transparent small-scale research program because it preserves:

- a valid confirmatory positive H1 on one configuration;
- a failed co-primary H2;
- two aborted attempts with explicit reasons;
- cross-family qualification failures rather than hidden model selection;
- a documented preregistration publication deviation;
- a preregistered instrument redesign that failed its own gate and was stopped rather than rescued.

A defensible future scholarly output would be a **methods/research note about replication qualification and measurement failure in IAER**, not a claim that v0.5-v0.7 replicated v0.4.3.

No new Zenodo revision is required merely to continue experimenting. If a methods note is prepared, it should be citation-locked only after this audit and the public repository record are stable.

## 8. Final program decision

**PAUSE, PRESERVE, AND AUDIT — DO NOT RUN v0.8 NOW.**

The v0.4.3 H1 finding remains valid within its frozen scope. Cross-family generalization remains unresolved. v0.5-v0.7 reveal substantial measurement/eligibility constraints and provide hypotheses for future work, but they do not justify an immediate additional behavioral run.

Any future restart should begin from the restart criteria above and receive a new version identifier with a new public preregistration.