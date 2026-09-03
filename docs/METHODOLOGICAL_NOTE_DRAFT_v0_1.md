# When Replication Stops at the Instrument: Cross-Family Qualification Failure in an LLM Evidence-Weighting Study

**Draft v0.1 — methodological note / negative-results case study**  
**Status:** working draft; not a preregistration and not a new experiment  
**Project:** Intra-Agent Evidence Recycling (IAER)

## Abstract

Cross-model replication of large-language-model behavioral effects is often treated as a straightforward portability test: apply the same instrument to another model family and compare the resulting effect. This assumption can fail when the instrument itself requires auxiliary capabilities that are not stable across models. We report a transparent sequence of cross-family qualification attempts following a completed confirmatory IAER study on a Qwen configuration. The original confirmatory study found that five explicitly derivative reviews of one source increased retention of an initial claim relative to an equal-sized unrelated-memory control (22/32 versus 0/32; paired risk difference 0.6875; Holm-adjusted exact McNemar p = 9.5367e-7). We then attempted to transport the measurement paradigm to Phi and Ministral configurations using fail-closed preflight, eligibility, calibration, and redesign stages. No later version reached a valid confirmatory cross-family IAER comparison. Phi-4-mini-instruct failed a mandatory behavioral preflight. A preregistered Phi-4-mini-reasoning eligibility pilot was technically valid but behaviorally ineligible. Ministral passed simple single-source controls but failed repeated independent-evidence aggregation under two prespecified response interfaces. A subsequent preregistered measurement-decoupling redesign removed probability/reliability arithmetic and replaced it with an explicit independent-root counting rule. The model was correct on 35/36 independent-root-only control calls but only 7/12 in a derived-record lure condition; the redesign nevertheless failed its frozen accuracy and symmetry gates and was stopped. These outcomes do not constitute negative replications of IAER. Instead, they illustrate a measurement problem: before interpreting cross-family absence of an effect, the candidate model must first demonstrate that the instrument measures the intended construct rather than auxiliary evidence-integration demands. We propose a practical distinction among confirmatory non-replication, model/instrument ineligibility, and invalid/inconclusive execution, and argue for preregistered qualification gates when behavioral instruments are transported across LLM families.

## 1. Introduction

Behavioral experiments on large language models increasingly make claims that extend beyond a single model configuration. Once an effect is observed in one system, a natural next question is whether it replicates across model families. In practice, however, a behavioral instrument is not a neutral window onto a latent model property. It is a task that itself places demands on instruction following, evidence integration, response representation, order robustness, and sometimes probabilistic reasoning.

This creates a basic interpretation problem. Suppose an effect observed in Model A disappears in Model B. There are at least two qualitatively different explanations:

1. Model B validly performs the measurement task but does not show the target effect.
2. Model B does not satisfy prerequisites required for the instrument to measure the target construct in the first place.

Only the first case is a negative replication.

This distinction is familiar from construct-validity arguments in evaluation research, but it is easy to lose in LLM experimentation, where the same prompt or benchmark is often transferred across models as if identical surface form guaranteed identical measurement meaning. Recent work has explicitly called for stronger construct validity in LLM benchmarks and for separating target capabilities from construct-irrelevant task demands. At the same time, evidence-aggregation research has shown that LLM behavior is sensitive to repetition, paraphrase, order, reliability, and belief-revision structure.

The Intra-Agent Evidence Recycling (IAER) project provides a compact empirical case study of this problem. A completed confirmatory study on a Qwen configuration produced a strong behavioral effect under a frozen task family. Subsequent attempts to qualify Phi and Ministral configurations for cross-family replication repeatedly stopped before a valid confirmatory IAER comparison could be made. Rather than silently adjusting the task until the new models passed, the project preserved failed qualification stages and ultimately stopped the redesign path under a preregistered rule.

The contribution of this note is therefore methodological rather than a claim of conceptual priority for dependent-evidence effects. Prior work already demonstrates that repeated/paraphrased evidence can influence LLM aggregation, that belief revision is unreliable, and that dependent or redundant evidence is a problem for RAG systems. Our narrower contribution is to show, in one fully documented experimental lineage, how an intended cross-family replication can become uninterpretable unless model/task eligibility is established before confirmatory inference.

## 2. Background and positioning

### 2.1 Evidence repetition, dependence, and belief revision

The broad phenomenon that repeated or paraphrased evidence can alter LLM outputs is not unique to IAER. Naphade (2026), using GroupQA, reports that paraphrasing an argument can be more persuasive than providing distinct independent support and also documents presentation-order effects. Ross et al. (2026) study duplicate, paraphrased, and diverse retrieval sets in a controlled RAG setting. Rahadi (2026) explicitly frames dependent document copies as a source-independence problem in RAG and proposes dependence-aware diagnostics. Cho and Lee (2026) address redundancy-aware retrieval evaluation in high-similarity corpora.

Related work also shows that LLMs do not reliably revise or aggregate evidence in normatively expected ways. Wilie et al. (2024) find broad difficulties in belief revision when new premises require suppression or revision of prior conclusions. Kim, Kim, and Thorne (2025) show that language models do not consistently follow Bayesian epistemic assumptions under evidence with varying informativeness and reliability.

Accordingly, this note does not claim that repetition effects, dependent-evidence problems, or non-Bayesian evidence integration are new.

### 2.2 Construct validity and transportability of LLM instruments

Alaa et al. (2025) argue that benchmark performance should not be equated with an intended underlying capability without empirical construct validation. More recent work has further emphasized sensitivity and specificity of evaluation tasks to intended versus unintended demands. This perspective is directly relevant to cross-family replication: a task that operationalizes a construct adequately for one model may introduce construct-irrelevant failure modes for another.

We use the term **instrument qualification** pragmatically rather than as a claim of full psychometric measurement invariance. In this project, qualification means that the candidate model must pass frozen controls demonstrating that the response interface and task semantics are behaviorally usable before a confirmatory effect estimate is collected.

## 3. Original confirmatory target

The cross-family program was motivated by IAER v0.4.3, a completed behavioral-confirmatory study using 32 balanced fictional items under a frozen `qwen3.5-4b` configuration.

The primary behavioral contrast of interest was:

`passive_repeat > neutral_filler`

In both conditions, one initial external source supported an INITIAL claim. In `neutral_filler`, five unrelated memory records were added. In `passive_repeat`, five target-consistent reviews explicitly derived from the same initial source were added. A later independent counter-source then favored the opposing claim.

The v0.4.3 dataset contained 168/168 valid planned trajectories and passed all preregistered validity gates. The primary result was:

- `passive_repeat`: 22/32 retained INITIAL;
- `neutral_filler`: 0/32 retained INITIAL;
- paired risk difference: 0.6875;
- Holm-adjusted exact paired McNemar p = 9.5367432e-7.

A second preregistered lineage-mitigation hypothesis was not supported.

The strongest defensible v0.4.3 claim is therefore narrow: under that frozen Qwen task/configuration, explicitly derivative reviews substantially increased retention of an initial claim relative to equal-sized unrelated memory. The study did not establish a general mechanism across model families.

## 4. Cross-family qualification sequence

### 4.1 v0.5.0 — Phi-4-mini-instruct: preflight failure

The first cross-family attempt froze a confirmatory H1 replication package with 32 new items and a mandatory behavioral preflight. Three of four preflight cases passed. The mirrored `independent_evidence` case with INITIAL=`CLAIM_B` failed.

Under the frozen fail-closed rule, confirmatory collection was not authorized.

**Classification:** `INVALID/INCONCLUSIVE` for qualification; no IAER outcome collected.

The important point is interpretive: the absence of a confirmatory run cannot be described as a Phi non-replication of IAER because the candidate failed the prerequisite gate.

### 4.2 v0.5.1 — exploratory response-interface diagnostic

An exploratory diagnostic tested three response/instruction representations to determine whether the v0.5.0 failure was largely an interface artifact.

All 48 planned calls completed, but overall normative accuracy was 29/48 and varied substantially across response representations. Performance on multiple-evidence integration remained substantially weaker than on simpler source-only cases.

This result suggested that the cross-family problem was not reducible to one trivial output-format choice, but because v0.5.1 was exploratory it was not used as confirmatory evidence.

### 4.3 v0.5.2 — Phi-4-mini-reasoning: preregistered eligibility failure

The next Phi study separated eligibility from confirmation using 12 balanced items across three normative conditions:

- `baseline_initial`;
- `counter_single_strong`;
- `independent_five_initial`.

All 36/36 planned trajectories were technically valid. Behavioral results were:

| Condition | Correct |
| --- | ---: |
| `baseline_initial` | 4/12 |
| `counter_single_strong` | 12/12 |
| `independent_five_initial` | 2/12 |

The frozen eligibility gates failed, yielding `INELIGIBLE`.

Again, this was not an IAER effect estimate. It established only that the exact Phi-4-mini-reasoning configuration was unsuitable for the frozen instrument.

### 4.4 v0.6 — Ministral: calibration failure under two interfaces

The Ministral program formalized three strictly separated stages:

**Calibration → Eligibility → Confirmatory IAER**

Calibration contained only normative evidence-integration controls and no IAER treatment condition.

Interface A required `chosen_claim` plus a confidence field. It produced 24/24 valid calls with the following condition accuracy:

- `baseline_initial`: 8/8;
- `counter_single_strong`: 8/8;
- `independent_five_initial`: 0/8.

Because integrity passed but behavioral gates failed, the frozen A→B rule authorized Interface B, which removed the confidence field and retained only `chosen_claim`.

Interface B again produced 24/24 valid calls and exactly the same condition pattern:

- `baseline_initial`: 8/8;
- `counter_single_strong`: 8/8;
- `independent_five_initial`: 0/8.

The frozen decision was `CALIBRATION_FAILURE — STOP BEFORE ELIGIBILITY`.

The identical 0/8 multiple-independent-evidence failure under both interfaces suggested that the problem was not primarily caused by the confidence output field. More importantly, it exposed an auxiliary-capability confound: the intended IAER instrument required the candidate model to aggregate several independent reliability-weighted sources in a normatively expected way before derivative-versus-independent source structure could be interpreted.

### 4.5 v0.7 — measurement decoupling

v0.7 was designed specifically to remove the probabilistic aggregation demand. Reliability values were eliminated. The model instead received an explicit rule:

1. each distinct independent ROOT SOURCE contributes one epistemic vote;
2. a DERIVED RECORD contributes zero new votes;
3. multiple records from one root do not add votes;
4. choose the claim with more independent root votes.

Twelve fresh balanced items were run in four conditions, producing 48 planned calls.

Three conditions contained only independent roots:

- R1: 2 INITIAL roots vs 1 COUNTER root;
- R2: 1 INITIAL root vs 2 COUNTER roots;
- R4: 3 INITIAL roots vs 2 COUNTER roots.

The critical R3 condition contained:

- 1 independent INITIAL root;
- five records explicitly marked as derived from that same INITIAL root and as adding zero new epistemic votes;
- 2 independent COUNTER roots.

The model therefore needed only to count root IDs, not integrate probabilities.

All 48/48 calls were technically valid. Results were:

| Condition | Correct |
| --- | ---: |
| R1 `two_initial_one_counter` | 12/12 |
| R2 `one_initial_two_counter` | 11/12 |
| R3 `derived_lure_initial_two_counter` | 7/12 |
| R4 `three_initial_two_counter` | 12/12 |

Across independent-root-only controls R1, R2, and R4, performance was 35/36. In R3, performance fell to 7/12, and all five R3 errors selected the INITIAL claim. However, R3 was not cleanly symmetric across label/order strata: INITIAL=`CLAIM_A` scored 5/6 while INITIAL=`CLAIM_B` scored 2/6; A_FIRST scored 5/6 while B_FIRST scored 2/6.

The preregistered P2–P5 gates therefore failed, yielding `REDESIGN_FAILED_STOP`.

This pattern is descriptively compatible with interference from derivative surface multiplicity, but v0.7 was explicitly an instrument-usability pilot and cannot confirm, refute, or estimate IAER.

## 5. Why these are not negative replications

A negative replication requires a valid opportunity for the target effect to occur and be measured.

In the post-v0.4.3 sequence, that condition was never satisfied:

| Version | Stage reached | Final classification | Confirmatory IAER estimate? |
| --- | --- | --- | --- |
| v0.5.0 | mandatory preflight | invalid/inconclusive qualification | No |
| v0.5.1 | exploratory diagnostic | exploratory only | No |
| v0.5.2 | eligibility | INELIGIBLE | No |
| v0.6 | calibration | CALIBRATION_FAILURE | No |
| v0.7 | instrument redesign pilot | REDESIGN_FAILED_STOP | No |

It would therefore be incorrect to summarize the project as “Qwen replicated, Phi and Ministral failed to replicate.” Phi and Ministral did not produce valid confirmatory cross-family estimates.

This distinction matters because otherwise an instrument's inability to function on a candidate model is silently converted into evidence about the target hypothesis.

## 6. A practical taxonomy for cross-family LLM replication

We propose three outcome classes for behavioral cross-family replication programs.

### 6.1 Valid replication / valid non-replication

Requirements:

- technical integrity passes;
- the candidate model passes prespecified instrument-qualification controls;
- the confirmatory target is run under frozen analysis rules.

Only here may the result be interpreted as evidence for or against cross-family generalization.

### 6.2 Model/instrument ineligibility

Requirements:

- technical integrity passes;
- one or more frozen prerequisite behavioral gates fail;
- the confirmatory target is not run.

Interpretation:

> the frozen model/interface/configuration cannot support an interpretable test of the target construct under this instrument.

This is neither confirmation nor non-replication.

### 6.3 Invalid/inconclusive execution

Examples include:

- missing/duplicate planned keys;
- response-schema failure;
- manipulation validity failure;
- failed mandatory preflight integrity;
- unresolved technical errors.

Interpretation:

> no scientific target inference is permitted.

## 7. Methodological implications

### 7.1 Same prompt does not imply same measurement

Transporting a prompt verbatim across model families may change the effective demands of the task. One model may treat an auxiliary evidence-integration operation as trivial; another may fail it systematically. Surface invariance of the instrument is therefore not evidence of construct invariance.

### 7.2 Qualification controls should target construct-irrelevant demands

Before collecting a confirmatory effect, controls should test whether the candidate can perform the auxiliary operations required by the instrument. In IAER these included:

- following the forced-choice response contract;
- responding symmetrically to label/order reversals;
- responding to strong counterevidence;
- aggregating genuinely independent evidence when the instrument requires it.

If those operations fail, the target manipulation becomes difficult or impossible to interpret.

### 7.3 Qualification should be frozen before outcomes

A major temptation is to adjust prompts or response interfaces until the candidate model “passes.” That approach risks converting eligibility into model-shopping. The IAER sequence instead treated each material redesign as a new version, retained failures, and stopped when frozen rules required stopping.

### 7.4 Instrument redesign can generate information without rescuing the hypothesis

v0.7 is a useful example. Removing probabilistic aggregation greatly improved performance on independent-root controls, suggesting that the earlier instrument had indeed imposed a substantial auxiliary demand. Yet the redesigned instrument still failed its own preregistered gates. The correct conclusion is not that IAER was confirmed after redesign; it is that the redesign clarified part of the measurement problem but did not produce a sufficiently stable instrument.

### 7.5 Failed qualification is scientifically reportable

Qualification failures often disappear from final papers because they are treated as development noise. This creates a distorted literature: successful transport attempts are visible while failed measurement transport is hidden. Reporting these stages can help distinguish model-family differences in target phenomena from differences in task usability.

## 8. Limitations

This note is a single-project case study, not a systematic benchmark of measurement transportability.

First, only one configuration produced a completed confirmatory IAER result. Cross-family generalization therefore remains unresolved.

Second, the post-v0.4.3 program involved only Phi and Ministral configurations. The proposed taxonomy is broader than the empirical sample and should be treated as a practical framework rather than a validated universal standard.

Third, v0.7 used only 12 items and showed label/order asymmetry in the critical derived-record condition. It cannot identify the mechanism of those errors.

Fourth, v0.6 had a documented publication-process deviation: the preregistration tag omitted some calibration-specific files that the intended freeze checklist had called for. The omission was documented rather than retrospectively rewritten. This weakens the evidentiary value of the v0.6 public freeze relative to v0.7, whose complete preregistration archive was verified before collection.

Fifth, the original v0.4.3 archive did not pin every external runtime detail/model artifact hash to the standard later adopted in v0.6–v0.7.

Finally, the underlying dependent-evidence phenomenon has substantial prior art by 2026. The contribution of this note is therefore methodological and archival, not priority for the phenomenon itself.

## 9. Recommendations for future replication studies

For behavioral effects that depend on nontrivial task semantics, we recommend the following sequence:

1. **Define the target construct separately from auxiliary capabilities.**
2. **Design controls for those auxiliary capabilities before cross-family confirmation.**
3. **Freeze qualification thresholds and stopping rules before behavioral outcomes.**
4. **Classify qualification failure separately from hypothesis failure.**
5. **Do not rerun or retune until the model passes within the same frozen version.**
6. **Use fresh stimuli after material redesigns.**
7. **Preserve failed/aborted stages in the public audit trail.**
8. **Require a new version for material prompt/interface changes.**
9. **Only label an absent effect a non-replication after instrument qualification passes.**
10. **Report the scope of inference at the exact model/interface/configuration level.**

## 10. Conclusion

The post-v0.4.3 IAER program did not establish cross-family replication, but it also did not produce a valid cross-family refutation. Instead, it exposed a practical measurement problem. Phi and Ministral configurations repeatedly failed prerequisites needed to interpret the original instrument, and a later redesign removed one major auxiliary demand without producing a sufficiently stable replacement.

The central methodological lesson is simple:

> **Before interpreting a cross-family absence of an LLM behavioral effect, establish that the new model is eligible for the measurement instrument.**

A model that fails the instrument has not necessarily failed the hypothesis.

This distinction is particularly important for LLM experiments because prompts simultaneously define the intervention, the measurement interface, and multiple auxiliary cognitive demands. Transparent qualification gates and fail-closed stopping rules can prevent instrument failure from being misreported as scientific non-replication.

## References — working list

- Alaa, A., Hartvigsen, T., Golchini, N., Dutta, S., Dean, F., Raji, I. D., & Zack, T. (2025). *Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity*. Proceedings of ICML 2025, PMLR 267.
- Cho, H., & Lee, J.-Y. (2026). *RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora*. ACL 2026. https://doi.org/10.18653/v1/2026.acl-long.923
- Kim, M., Kim, S., & Thorne, J. (2025). *From Evidence to Belief: A Bayesian Epistemology Approach to Language Models*. NAACL 2025. https://doi.org/10.18653/v1/2025.naacl-long.531
- Naphade, A. (2026). *Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering*. Findings of ACL 2026. https://doi.org/10.18653/v1/2026.findings-acl.2003
- Rahadi, I. (2026). *Counting Copies as Evidence: Confidence Inflation from Dependent Evidence in Retrieval-Augmented Generation (RAG)*. Preprint/position paper. https://doi.org/10.5281/zenodo.21923648
- Ross, J. J., Koopman, B., van der Vegt, A., & Zuccon, G. (2026). *How retriever redundancy and diversity impact RAG effectiveness*. arXiv:2608.13956.
- Wilie, B., Cahyawijaya, S., Ishii, E., He, J., & Fung, P. (2024). *Belief Revision: The Adaptability of Large Language Models Reasoning*. EMNLP 2024. https://doi.org/10.18653/v1/2024.emnlp-main.586
- *General scales unlock AI evaluation with explanatory and predictive power*. (2026). Nature. https://doi.org/10.1038/s41586-026-10303-2

## Internal project sources

The empirical claims in this draft are grounded in the public IAER repository, especially:

- `docs/experiment_history.md`
- `docs/program_audit_v0_2_to_v0_7.md`
- `experiments/v0_4_3/AUDIT_REPORT_v0_4_3.md`
- `experiments/v0_5_2_eligibility/eligibility_report_v0_5_2.txt`
- `experiments/v0_6_ministral/01_calibration/`
- `experiments/v0_7_instrument_redesign/V0_7_CLOSURE_REPORT.md`
- public preregistration/results releases for v0.6 and v0.7

No new behavioral data are introduced in this note.