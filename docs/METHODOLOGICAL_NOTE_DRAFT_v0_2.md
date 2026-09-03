# Before Calling It a Non-Replication: Instrument Qualification Across LLM Families

**Draft v0.2 — methodological note / negative-results case study**  
**Status:** working manuscript; no new behavioral data

## Abstract

If a behavioral effect disappears on another large language model, when is that evidence of non-replication—and when has the new model simply failed the instrument? We examine this distinction using a transparent sequence of cross-family qualification attempts following a completed confirmatory evidence-weighting study. The original Qwen study found that five explicitly derivative reviews of one source increased retention of an initial claim relative to an equal-sized unrelated-memory control (22/32 versus 0/32; paired risk difference 0.6875; Holm-adjusted exact McNemar p = 9.5367e-7). Subsequent Phi and Ministral programs used frozen preflight, eligibility, calibration, and redesign gates before permitting confirmatory collection. None reached a valid cross-family confirmatory estimate: Phi-4-mini-instruct failed mandatory preflight; Phi-4-mini-reasoning completed a technically valid eligibility pilot but was behaviorally ineligible; Ministral passed simple controls but failed multiple-independent-evidence aggregation under two prespecified interfaces; and a later preregistered redesign removed probabilistic aggregation but still failed its accuracy and symmetry gates. These outcomes are not negative replications of the original effect because the confirmatory construct was never validly measured in the new configurations. We present this history as a case study in measurement transport: surface reuse of an LLM task does not guarantee that the instrument retains the same interpretive meaning across model families. We propose a practical reporting distinction among valid replication/non-replication, model/instrument ineligibility, and invalid/inconclusive execution, and argue that qualification gates should be frozen before cross-family confirmatory inference.

## 1. Introduction

A common pattern in LLM research is straightforward: observe an effect in one model, rerun the same task on another family, and interpret a smaller or absent effect as weak generalization or non-replication.

That interpretation assumes the task functions as the same measurement instrument on both models.

The assumption is often untested.

LLM behavioral instruments can simultaneously require instruction following, response-format compliance, order robustness, belief revision, quantitative evidence integration, and the target behavior of scientific interest. A second model may fail one of these auxiliary demands even if the target construct itself remains unresolved. In such a case, an absent target effect is not interpretable as a negative replication.

This note documents that problem through the post-confirmatory history of the Intra-Agent Evidence Recycling (IAER) project. IAER originally tested whether several memory records explicitly derived from one external source could acquire excess behavioral weight relative to unrelated memory. A completed confirmatory Qwen study produced a strong preregistered effect. We then attempted to transport the paradigm across Phi and Ministral configurations.

The cross-family program never reached a valid post-Qwen confirmatory comparison. Instead, successive versions stopped at mandatory preflight, eligibility, calibration, and instrument-redesign gates.

The central argument is therefore methodological:

> **An absent cross-family effect should not be called a non-replication unless the candidate model first demonstrates that the instrument can validly support the intended comparison.**

We do not claim priority for repeated-evidence or dependent-evidence effects. By 2026, prior work already shows that repetition, paraphrase, redundancy, order, belief revision, and source dependence can strongly affect LLM evidence aggregation. The contribution here is the preserved empirical lineage of an attempted cross-family replication that repeatedly stopped before the target hypothesis could legitimately be tested.

## 2. Related work

### 2.1 Repetition, dependence, and evidence aggregation

Prior work already establishes substantial overlap with the broad IAER phenomenon. Naphade (2026) reports that paraphrasing an argument can be more persuasive than distinct independent support and documents presentation-order effects in RAG evidence aggregation. Ross et al. (2026) compare duplicate, paraphrased, and diverse retrieved documents under controlled conditions. Rahadi (2026) explicitly frames copied documents as dependent evidence that should not be counted as independent corroboration. Cho and Lee (2026) develop redundancy-aware retrieval evaluation for high-similarity corpora.

Accordingly, our contribution is not the general claim that repeated or dependent evidence can influence an LLM.

### 2.2 Belief revision and auxiliary evidence-integration demands

Wilie et al. (2024) show that LMs often struggle to revise prior conclusions when new information changes the appropriate inference. Kim, Kim, and Thorne (2025) find that LMs do not consistently follow Bayesian epistemic assumptions under evidence with different reliability and informativeness.

These results matter because an instrument designed to measure one behavioral construct may unintentionally require reliable belief revision or probabilistic evidence aggregation as an auxiliary capability.

### 2.3 Construct validity in LLM evaluation

Recent evaluation work argues that benchmark scores should not be equated with an intended capability without evidence that the instrument measures that construct rather than task-specific or method-specific variance. Alaa et al. (2025) make this argument explicitly for medical LLM benchmarks, and later work has continued to emphasize construct-valid task design and sensitivity to unintended demands.

We therefore use **instrument qualification** as a pragmatic operational concept, not as a claim of formal psychometric measurement invariance. A candidate configuration is “qualified” only when it passes frozen controls required to interpret the later target comparison.

## 3. The confirmatory target

The cross-family program followed IAER v0.4.3, a fixed-N behavioral-confirmatory study on a `qwen3.5-4b` configuration.

The primary comparison was:

`passive_repeat > neutral_filler`

Both conditions began with one external source supporting an INITIAL claim. `neutral_filler` added five unrelated memory records. `passive_repeat` added five target-consistent reviews explicitly derived from the same initial source. A later independent counter-source favored the opposing claim.

The dataset contained 168/168 valid planned trajectories and passed all preregistered validity gates. The primary result was:

- `passive_repeat`: 22/32 retained INITIAL;
- `neutral_filler`: 0/32 retained INITIAL;
- paired RD = 0.6875;
- Holm-adjusted exact McNemar p = 9.5367432e-7.

A second lineage-mitigation hypothesis was not supported.

The cross-family question was therefore legitimate but narrow: could the primary behavioral contrast be validly estimated in another model family?

## 4. Where the replication program stopped

| Version | Candidate / role | Gate reached | Key result | Confirmatory IAER estimate? |
| --- | --- | --- | --- | --- |
| v0.5.0 | Phi-4-mini-instruct | mandatory preflight | 1/4 required cases failed | No |
| v0.5.1 | Phi exploratory diagnostic | interface diagnosis | 29/48 normative accuracy; representation sensitivity | No |
| v0.5.2 | Phi-4-mini-reasoning | preregistered eligibility | 4/12 baseline, 12/12 strong counter, 2/12 independent-five | No |
| v0.6 A | Ministral calibration | Interface A | 8/8, 8/8, 0/8 across three controls | No |
| v0.6 B | Ministral calibration | Interface B | same 8/8, 8/8, 0/8 pattern | No |
| v0.7 | Ministral redesign pilot | explicit root-counting instrument | 35/36 independent-root controls; 7/12 derived lure; symmetry gates failed | No |

### 4.1 Phi: technical validity without measurement eligibility

v0.5.0 required a four-case behavioral preflight before confirmatory collection. One mirrored independent-evidence case failed, so the program stopped before collecting target outcomes.

An exploratory interface diagnostic then showed substantial response-representation sensitivity and weak multiple-evidence integration.

v0.5.2 formalized eligibility with 36 planned calls. All 36 were technically valid, but the candidate failed the frozen behavioral gates. The final classification was `INELIGIBLE`.

No Phi version generated a confirmatory IAER effect estimate.

### 4.2 Ministral: calibration isolates an auxiliary capability problem

v0.6 separated the program into:

**Calibration → Eligibility → Confirmatory IAER**

Calibration intentionally excluded IAER treatment conditions.

Under Interface A, Ministral scored:

- 8/8 on a one-source INITIAL baseline;
- 8/8 when a stronger single counter-source should overturn INITIAL;
- 0/8 when five independent moderate INITIAL sources should collectively defeat one stronger counter-source.

Interface B removed the confidence field and produced the same 8/8, 8/8, 0/8 pattern.

The frozen decision was `CALIBRATION_FAILURE — STOP BEFORE ELIGIBILITY`.

This did not show that IAER failed on Ministral. It showed that the planned instrument depended on an evidence-aggregation operation that the candidate did not perform normatively under the frozen task.

### 4.3 v0.7: remove the probabilistic confound, then stop again

v0.7 removed reliability scores and Bayesian-style aggregation entirely. The candidate received an explicit rule:

- each independent root source contributes one vote;
- derived records contribute zero new votes;
- repeated records from one root do not add votes;
- choose the claim with more independent roots.

Across three conditions containing only independent roots, Ministral was correct on 35/36 calls.

The critical condition added five records explicitly marked as derived from one INITIAL root and as contributing zero new epistemic votes, while two independent COUNTER roots were present. Accuracy fell to 7/12.

However, the critical condition also showed label/order asymmetry. The preregistered accuracy and symmetry gates failed, yielding `REDESIGN_FAILED_STOP`.

The project therefore stopped rather than retuning the prompt or adding a rescue interface.

## 5. Why this is not a sequence of negative replications

The post-Qwen history contains repeated **attempts to reach a valid replication test**, not repeated valid tests with null results.

A negative replication requires at minimum:

1. technical integrity;
2. an instrument that is behaviorally usable for the candidate configuration;
3. a frozen confirmatory comparison whose target effect can be interpreted.

The later IAER versions failed before condition 3.

Calling these runs “Phi failed to replicate” or “Ministral failed to replicate” would collapse two different statements:

- the target effect was absent under a valid instrument;
- the instrument did not establish the prerequisites needed to measure the target effect.

The data support only the second statement.

## 6. A practical reporting taxonomy

We propose an operational distinction for cross-family behavioral studies.

### A. Valid replication / valid non-replication

The candidate passes integrity and prespecified qualification gates, and the frozen target comparison is collected.

Only this class supports inference about cross-family generalization.

### B. Model/instrument ineligibility

Technical collection is valid, but frozen prerequisite behavioral gates fail before target collection.

Interpretation:

> the exact model/interface/configuration is not eligible for an interpretable test under this instrument.

This is not evidence for or against the target effect.

### C. Invalid/inconclusive execution

Manipulation validity, schema integrity, missingness, duplication, or other mandatory execution rules fail.

No target inference is permitted.

This taxonomy is proposed as a practical reporting distinction derived from one research program; it is not presented as a validated universal framework.

## 7. Methodological lessons

### 7.1 Same task text does not guarantee same measurement

An identical prompt can impose different effective demands on different model families. Surface replication of the instrument is not evidence that the instrument transports.

### 7.2 Qualification gates should test auxiliary demands before the hypothesis

If a target manipulation assumes that the model can integrate independent evidence, revise prior beliefs, or use a response representation symmetrically, those assumptions should be tested before the confirmatory effect is interpreted.

### 7.3 Failed qualification should remain visible

Silently modifying a task until each model passes biases the visible record toward successful transport. Preserving failed preflights and ineligibility decisions makes the scope of generalization clearer.

### 7.4 STOP rules reduce model-shopping

A gate has little methodological value if it is rerun after failure until a favorable draw or prompt variant passes. Material changes should create a new version with fresh frozen rules.

### 7.5 Redesign can clarify a confound without validating the target construct

v0.7 showed that removing probabilistic aggregation greatly improved independent-root controls. That is evidence that the earlier instrument contained an auxiliary demand. But because the redesigned instrument itself failed frozen gates, it could not be promoted into confirmatory evidence.

## 8. Limitations

This is a single-program case study rather than a systematic study of instrument transport across many LLM tasks.

Only Qwen v0.4.3 produced a completed confirmatory IAER estimate. Phi and Ministral did not.

v0.7 used only 12 items, and the critical condition showed label/order asymmetry, preventing mechanism-level interpretation.

v0.6 also had a documented publication-process deviation: several calibration-specific files intended for the public Freeze-A package were not actually present in the original preregistration tag. The historical record was preserved and the omission was documented rather than retroactively rewritten. v0.7 subsequently required a complete frozen ZIP release asset before behavioral authorization.

The original v0.4.3 archive also did not pin every external runtime/model-artifact detail to the stronger standard later adopted.

Finally, dependent-evidence and repetition effects have substantial prior art. The contribution here is not priority for that phenomenon but the measurement/replication case study.

## 9. Recommendations

For cross-family behavioral replication of LLM effects:

1. separate the target construct from auxiliary task demands;
2. define qualification controls for those demands;
3. freeze qualification gates before candidate outcomes;
4. distinguish instrument ineligibility from target-effect absence;
5. forbid same-version rescue tuning after failed gates;
6. use new versions and fresh stimuli after material redesign;
7. retain failed and aborted stages in the public record;
8. reserve the term “non-replication” for candidates that first pass the measurement prerequisites.

## 10. Conclusion

The IAER cross-family program did not establish replication beyond Qwen, but neither did it establish a valid cross-family null result. It stopped because the candidate configurations repeatedly failed prerequisites required to interpret the instrument, and the later measurement redesign failed its own preregistered gates.

The broader lesson is not specific to IAER:

> **Before calling an absent LLM effect a non-replication, establish that the new model can validly participate in the measurement instrument.**

For LLM behavioral science, the instrument itself must be treated as part of the hypothesis-testing pipeline rather than as a transparent, model-invariant interface.

## Working references

- Alaa, A. et al. (2025). *Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity*. ICML 2025, PMLR 267.
- Cho, H., & Lee, J.-Y. (2026). *RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora*. ACL 2026. DOI: 10.18653/v1/2026.acl-long.923.
- Kim, M., Kim, S., & Thorne, J. (2025). *From Evidence to Belief: A Bayesian Epistemology Approach to Language Models*. NAACL 2025. DOI: 10.18653/v1/2025.naacl-long.531.
- Naphade, A. (2026). *Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering*. Findings of ACL 2026. DOI: 10.18653/v1/2026.findings-acl.2003.
- Rahadi, I. (2026). *Counting Copies as Evidence: Confidence Inflation from Dependent Evidence in Retrieval-Augmented Generation (RAG)*. Preprint/position paper. DOI: 10.5281/zenodo.21923648.
- Ross, J. J., Koopman, B., van der Vegt, A., & Zuccon, G. (2026). *How retriever redundancy and diversity impact RAG effectiveness*. arXiv:2608.13956.
- Wilie, B., Cahyawijaya, S., Ishii, E., He, J., & Fung, P. (2024). *Belief Revision: The Adaptability of Large Language Models Reasoning*. EMNLP 2024. DOI: 10.18653/v1/2024.emnlp-main.586.
- *General scales unlock AI evaluation with explanatory and predictive power*. (2026). Nature. DOI: 10.1038/s41586-026-10303-2.

## Project evidence base

Empirical values in this manuscript are drawn from the public IAER audit trail, including `docs/experiment_history.md`, `docs/program_audit_v0_2_to_v0_7.md`, the v0.4.3 audit, v0.5.2 eligibility report, v0.6 calibration reports, and v0.7 closure report/releases. No new behavioral data are introduced here.
