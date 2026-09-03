# Prior-Art / Novelty Gate — IAER Methodological Note v0.1

**Date:** 2026-09-03  
**Scope:** proposed paper centered on the post-v0.4.3 cross-family program (v0.5.0–v0.7)  
**Decision:** **GO — methodological / negative-results case study; do not claim conceptual priority for dependent-evidence effects**

## 1. Proposed paper question

The proposed note does **not** ask whether repeated or dependent evidence can influence LLM outputs in general. That space now has substantial prior art.

The defensible paper question is:

> What should count as a valid cross-family non-replication when the new model does not first demonstrate that the measurement instrument itself is behaviorally valid for that model?

IAER v0.5.0–v0.7 provides a concrete empirical case study in which attempts to transport a previously successful behavioral instrument across model families repeatedly stopped at preflight, eligibility, calibration, or instrument-redesign gates before any valid confirmatory cross-family IAER comparison was reached.

## 2. High-overlap prior art: dependent/repeated evidence

### Naphade (Findings of ACL 2026), *Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering*

This is the strongest direct overlap with the broad IAER phenomenon. GroupQA studies how LLMs combine conflicting groups of retrieved evidence and reports that paraphrasing an argument can be more persuasive than distinct independent support, alongside order effects and other aggregation heuristics.

**Implication for novelty:** IAER must not claim that it is the first demonstration that repeated/paraphrased support can outweigh or distort independent support in LLM evidence aggregation.

### Rahadi (August 2026 preprint), *Counting Copies as Evidence: Confidence Inflation from Dependent Evidence in Retrieval-Augmented Generation (RAG)*

This position/preprint paper explicitly frames copied or dependent documents as a source-independence problem and argues that repeated copies can inflate evidential confidence. It proposes dependence-aware diagnostics and aggregation concepts.

**Implication for novelty:** IAER must not claim conceptual priority for the proposition that multiple dependent records should not be treated as multiple independent sources.

### Cho & Lee (ACL 2026), *RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora*

RARE focuses on redundancy in retrieved corpora and benchmark validity under highly similar documents.

**Implication for novelty:** redundancy-aware evaluation is already an active research area; IAER's contribution must be narrower than “RAG evaluation should account for redundancy.”

### Ross et al. (2026 preprint), *How retriever redundancy and diversity impact RAG effectiveness*

This work directly compares duplicate, paraphrased, and diverse retrieved documents under controlled conditions.

**Implication for novelty:** controlled manipulation of duplicate/paraphrased/diverse context is not itself novel.

## 3. Adjacent prior art: evidence revision and aggregation

### Wilie et al. (EMNLP 2024), *Belief Revision: The Adaptability of Large Language Models Reasoning*

Belief-R evaluates whether LMs revise prior conclusions when new information is introduced and finds broad difficulty with appropriate belief revision.

### Kim, Kim & Thorne (NAACL 2025), *From Evidence to Belief: A Bayesian Epistemology Approach to Language Models*

This work tests response/confidence updating under evidence of varying informativeness and reliability and finds that LMs do not consistently follow Bayesian epistemic assumptions.

**Implication for novelty:** failures in belief revision and probabilistic evidence integration are established phenomena. The Phi/Ministral qualification failures should therefore be framed as a measurement-transport problem, not as a new discovery that LLMs are non-Bayesian.

## 4. Adjacent prior art: construct validity of LLM evaluation

### Alaa et al. (ICML 2025), *Medical Large Language Model Benchmarks Should Prioritize Construct Validity*

This paper argues explicitly that LLM benchmark performance should not be equated with the underlying construct unless the instrument has empirical construct validity.

### *General scales unlock AI evaluation with explanatory and predictive power* (Nature, 2026)

This work emphasizes sensitivity/specificity and construct-valid benchmark design, including the need to separate target abilities from unintended demands.

### Kearns et al. / related 2025–2026 construct-validity work

Recent work increasingly treats benchmark scores as measurements that can conflate intended capabilities with prompt/method variance or other auxiliary demands.

**Implication for novelty:** “construct validity matters in LLM evaluation” is not a novel thesis.

## 5. What appears defensibly distinctive in the IAER post-v0.4.3 program

The publishable contribution is the **empirical structure of the replication attempt**, not conceptual priority for the underlying phenomena.

### A. Explicit separation of hypothesis failure from instrument/model eligibility failure

The program records multiple cases where a cross-family confirmatory test was *not* run because the candidate model first failed a frozen measurement prerequisite.

This supports a concrete methodological distinction:

- **valid non-replication:** the model passes the measurement/eligibility gates and the confirmatory effect is absent;
- **ineligibility/calibration failure:** the model fails capabilities required for the instrument to measure the target construct, so the target hypothesis remains untested.

### B. Sequential fail-closed qualification history

The post-v0.4.3 program contains a rare transparent sequence:

- v0.5.0: cross-family preflight failure before confirmatory data;
- v0.5.1: exploratory response-interface diagnostic;
- v0.5.2: preregistered eligibility pilot -> INELIGIBLE;
- v0.6: staged Calibration -> Eligibility -> Confirmatory architecture, stopped at Calibration;
- v0.7: preregistered measurement-decoupling redesign, stopped under its own frozen rule.

The value is that failed gates, aborted paths, and redesign attempts remain visible rather than being silently tuned away.

### C. Empirical demonstration of an auxiliary-capability confound

The original cross-family instrument required candidate models to integrate multiple independent reliability-weighted sources. Phi/Ministral qualification failures showed that this auxiliary demand could prevent interpretation of the IAER construct itself.

v0.7 then removed probability/reliability arithmetic and used an explicit root-counting rule. Ministral performed 35/36 on independent-root-only controls but only 7/12 on the derived-record lure condition; however, label/order asymmetries caused the redesign to fail its frozen gates.

This progression is useful as a case study in **construct-irrelevant variance / measurement transportability**.

### D. Stopping discipline as data, not housekeeping

The methodological note can document why repeated reruns until a gate passes would convert qualification into model-shopping or post-hoc instrument tuning.

The empirical record shows the practical consequences of enforcing STOP rules.

## 6. Claims that are NOT allowed in the note

Do not claim:

- IAER is the first dependent-evidence / repeated-evidence effect in LLMs;
- v0.7 confirms IAER on Ministral;
- Phi or Ministral falsified IAER;
- the models internally counted derived records as independent sources;
- lineage metadata is a proven mitigation;
- the proposed qualification architecture is the first use of construct validity in LLM evaluation;
- cross-family measurement invariance has been formally established psychometrically.

## 7. Claims that ARE defensible

The note may claim:

1. The completed v0.4.3 Qwen study supplied the target effect that motivated cross-family replication attempts.
2. None of v0.5.0, v0.5.2, v0.6, or v0.7 produced a valid confirmatory cross-family IAER estimate.
3. Therefore the later results are not valid negative replications of v0.4.3.
4. Multiple candidate configurations failed prerequisites required to interpret the original instrument.
5. The sequence illustrates why cross-family LLM replication may require model-specific instrument qualification before hypothesis testing.
6. v0.7 shows descriptively that removing probabilistic aggregation did not fully produce a stable instrument: independent-root controls were nearly perfect while the derived-record lure condition failed and showed label/order asymmetry.
7. Transparent fail-closed reporting prevented these qualification/redesign failures from being misrepresented as either confirmations or refutations.

## 8. Novelty judgment

### Conceptual novelty of dependent-evidence phenomenon

**LOW to MODERATE.** Strong direct prior art exists by 2026.

### Novelty of general construct-validity argument

**LOW.** The topic is already established in LLM evaluation research.

### Novelty of this concrete empirical replication/qualification case study

**MODERATE.** The combination of a prior confirmatory target, two model families, explicit preflight/eligibility/calibration gates, a measurement-decoupling redesign, preserved failed attempts, and a fail-closed stopping interpretation appears sufficiently distinctive for a methodological research note or negative-results paper.

## 9. Publication gate

**GO**, under the following positioning:

> A transparent empirical case study of why cross-family replication of an LLM behavioral effect can fail *before the hypothesis is tested*, and why model ineligibility / instrument failure must not be mislabeled as a negative replication.

Recommended article type:

- methodological note;
- negative-results / replication-methodology paper;
- workshop or Findings-style short paper if the venue accepts this scope;
- preprint first.

A full main-conference paper would likely require either a broader systematic sample of models/instruments or a new valid cross-family confirmatory experiment. That is **not** recommended before writing and evaluating the current note.

## 10. Prior-art references checked for this gate

- Wilie, B., Cahyawijaya, S., Ishii, E., He, J., & Fung, P. (2024). *Belief Revision: The Adaptability of Large Language Models Reasoning*. EMNLP 2024. DOI: 10.18653/v1/2024.emnlp-main.586.
- Kim, M., Kim, S., & Thorne, J. (2025). *From Evidence to Belief: A Bayesian Epistemology Approach to Language Models*. NAACL 2025. DOI: 10.18653/v1/2025.naacl-long.531.
- Alaa, A. et al. (2025). *Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity*. ICML 2025, PMLR 267.
- Naphade, A. (2026). *Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering*. Findings of ACL 2026. DOI: 10.18653/v1/2026.findings-acl.2003.
- Cho, H., & Lee, J.-Y. (2026). *RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora*. ACL 2026. DOI: 10.18653/v1/2026.acl-long.923.
- Ross, J. J., Koopman, B., van der Vegt, A., & Zuccon, G. (2026). *How retriever redundancy and diversity impact RAG effectiveness*. arXiv:2608.13956.
- Rahadi, I. (2026). *Counting Copies as Evidence: Confidence Inflation from Dependent Evidence in Retrieval-Augmented Generation (RAG)*. Preprint/position paper, DOI: 10.5281/zenodo.21923648.
- *General scales unlock AI evaluation with explanatory and predictive power*. Nature (2026), DOI: 10.1038/s41586-026-10303-2.

This gate is a literature-positioning audit, not a claim of exhaustive bibliographic coverage.