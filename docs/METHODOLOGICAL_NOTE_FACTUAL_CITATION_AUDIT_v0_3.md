# Factual and Citation Audit — Methodological Note v0.3

**Date:** 2026-09-03  
**Status:** PASS WITH NARROWED CLAIMS  
**Scope:** manuscript `Before Calling It a Non-Replication: Instrument Qualification Across LLM Families`

## 1. Audit purpose

This audit checks two distinct evidence layers before a preprint-ready draft is prepared:

1. **internal empirical claims** against the public IAER repository and frozen reports;
2. **external literature claims** against primary or high-authority publication records where available.

The audit does not introduce new behavioral data and does not upgrade exploratory or qualification results into confirmatory evidence.

## 2. Internal empirical claims — verified

### v0.4.3 confirmatory target

Verified against `experiments/v0_4_3/AUDIT_REPORT_v0_4_3.md` and the frozen preregistration:

- 168/168 planned trajectories valid;
- all preregistered validity gates passed;
- H1 `passive_repeat > neutral_filler`: 22/32 versus 0/32;
- paired risk difference = 0.6875;
- Holm-adjusted exact paired McNemar p = 9.5367432e-7;
- H1 supported;
- H2 `active_plain > active_lineage`: 2/32 versus 0/32, RD = 0.0625, Holm p = 0.50; not supported.

**Allowed manuscript claim:** v0.4.3 supplies one completed confirmatory target on the frozen Qwen configuration.

**Forbidden extrapolation:** general IAER mechanism or cross-family generalization.

### v0.5.0 Phi-4-mini-instruct

Verified against `experiments/v0_5_0/preflight_v0_5_0.json`:

- mandatory four-case behavioral preflight;
- three cases passed;
- mirrored `independent_evidence` case with INITIAL=`CLAIM_B` failed;
- confirmatory collection was not authorized.

**Allowed manuscript classification:** qualification stopped before confirmatory collection; no Phi confirmatory IAER estimate exists.

### v0.5.1 exploratory diagnostic

Verified against `experiments/v0_5_1_diagnostic/diagnostic_report_v0_5_1.txt`:

- 48/48 planned rows valid;
- 0 retained technical-failure rows;
- overall normative accuracy 29/48;
- `independent_five` accuracy: 4/8 (`claim_label`), 0/8 (`value_token`), 3/8 (`explicit_odds`);
- `source_only` accuracy: 8/8, 7/8, 7/8 respectively;
- representation changes affected accuracy;
- report is explicitly descriptive/exploratory only.

**Allowed manuscript claim:** the diagnostic showed representation sensitivity and weaker multiple-evidence integration than source-only performance.

### v0.5.2 Phi-4-mini-reasoning

Verified against `experiments/v0_5_2_eligibility/eligibility_report_v0_5_2.txt`:

- 36/36 planned trajectories valid;
- 0 failure rows;
- `baseline_initial`: 4/12;
- `counter_single_strong`: 12/12;
- `independent_five_initial`: 2/12;
- integrity PASS; behavioral accuracy/symmetry gates FAIL;
- final decision `INELIGIBLE`.

**Allowed manuscript claim:** technically valid eligibility pilot, behaviorally ineligible under the frozen instrument.

### v0.6 Ministral calibration

Verified against the public calibration reports and closure record:

Interface A:
- 24/24 valid;
- `baseline_initial` 8/8;
- `counter_single_strong` 8/8;
- `independent_five_initial` 0/8;
- integrity PASS; behavioral gates FAIL;
- `INTERFACE_A_FAILED_BEHAVIORALLY`.

Interface B:
- 24/24 valid;
- same 8/8, 8/8, 0/8 condition pattern;
- integrity PASS; behavioral gates FAIL;
- `CALIBRATION_FAILURE`.

Eligibility and Confirmatory IAER were not run.

**Allowed manuscript classification:** calibration failure before eligibility, not IAER non-replication.

### v0.6 publication-process deviation

Verified against `FREEZE_A_PUBLICATION_DEVIATION_v0_6.md`:

- program-level materials were publicly frozen before collection;
- several calibration-specific implementation files intended by the Freeze-A checklist were absent from the tagged commit;
- later archival publication cannot be described as retroactive preregistration;
- original tag was not rewritten.

**Required manuscript treatment:** retain this limitation in the main text.

### v0.7 measurement-decoupling redesign

Verified against `V0_7_CLOSURE_REPORT.md` and `results/report_v0_7.json`:

- complete preregistration archive published and verified before behavioral authorization;
- 48/48 planned rows valid;
- P1 integrity PASS;
- R1 12/12;
- R2 11/12;
- R3 derived-record lure 7/12;
- R4 12/12;
- P2-P5 FAIL;
- final decision `REDESIGN_FAILED_STOP`;
- 35/36 correct across independent-root-only conditions R1+R2+R4;
- all five R3 errors selected INITIAL;
- R3 showed label/order asymmetry and cross-cell n=3.

**Allowed manuscript interpretation:** v0.7 shows that removing probabilistic aggregation did not produce a stable instrument; its R3 pattern is descriptive only.

**Forbidden claim:** v0.7 confirms IAER on Ministral.

## 3. External literature — verified

### Naphade 2026 — direct phenomenon overlap

Atharv Naphade, *Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering*, Findings of ACL 2026, pages 40293–40311. DOI: `10.18653/v1/2026.findings-acl.2003`.

Verified high-level claim: the paper reports that paraphrasing an argument can be more persuasive than distinct independent support and reports presentation-order effects.

**Use:** strongest reason not to claim novelty for repeated/paraphrased-evidence persuasion.

### Cho & Lee 2026 — redundancy-aware evaluation

Hanjun Cho and Jay-Yoon Lee, *RARE: Redundancy-Aware Retrieval Evaluation Framework for High-Similarity Corpora*, ACL 2026, pages 20160–20185. DOI: `10.18653/v1/2026.acl-long.923`.

Verified high-level claim: redundant/high-similarity corpora can undermine standard retrieval evaluation assumptions, motivating redundancy-aware evaluation.

**Use:** evidence that redundancy-aware evaluation is already an active peer-reviewed research area.

### Ross et al. 2026 — preprint, not peer-reviewed in this audit

Jonathan J. Ross, Bevan Koopman, Anton van der Vegt, Guido Zuccon, *How retriever redundancy and diversity impact RAG effectiveness*, arXiv:2608.13956, submitted 14 August 2026.

Verified design: controlled comparison of duplicate, paraphrased, and diverse retrieved document sets on fictional QA.

**Use:** adjacent current preprint; label explicitly as preprint.

### Rahadi 2026 — position paper/preprint

Irwan Rahadi, *Counting Copies as Evidence: Confidence Inflation from Dependent Evidence in Retrieval-Augmented Generation (RAG)*, August 2026 position paper/preprint. DOI: `10.5281/zenodo.21923648`.

Verified high-level framing: copied/dependent documents should not be treated as independent corroboration; proposes dependence-aware concepts and diagnostics.

**Use:** direct conceptual overlap; label explicitly as position paper/preprint.

### Wilie et al. 2024 — belief revision

Bryan Wilie, Samuel Cahyawijaya, Etsuko Ishii, Junxian He, Pascale Fung, *Belief Revision: The Adaptability of Large Language Models Reasoning*, EMNLP 2024, pages 10480–10496. DOI: `10.18653/v1/2024.emnlp-main.586`.

Verified high-level claim: evaluated about 30 LMs and found that LMs generally struggle to revise beliefs appropriately when new information changes the warranted inference.

### Kim, Kim & Thorne 2025 — Bayesian evidence updating

Minsu Kim, Sangryul Kim, James Thorne, *From Evidence to Belief: A Bayesian Epistemology Approach to Language Models*, NAACL 2025, pages 10578–10611. DOI: `10.18653/v1/2025.naacl-long.531`.

Verified high-level claim: LMs do not consistently follow Bayesian epistemic assumptions when evidence varies in informativeness and reliability.

### Alaa et al. 2025 — construct validity

Ahmed Alaa et al., *Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity*, ICML 2025, PMLR 267:80991–81004.

Verified claim: benchmark performance should support the interpretation of the intended construct; the paper explicitly imports construct-validity reasoning from psychological measurement.

### Bean et al. 2025 — systematic construct-validity review

Andrew M. Bean et al., *Measuring what Matters: Construct Validity in Large Language Model Benchmarks*, NeurIPS 2025 Datasets & Benchmarks Track. DOI: `10.52202/085713-0590`.

Verified claim: systematic review of 445 LLM benchmarks with 29 expert reviewers; identifies recurring construct-validity problems and provides recommendations.

**Use:** stronger general construct-validity anchor than relying only on a domain-specific medical position paper.

### Zhou et al. 2026 — general scales for AI evaluation

Lexin Zhou et al., *General scales unlock AI evaluation with explanatory and predictive power*, Nature 652, 58–67 (2026). DOI: `10.1038/s41586-026-10303-2`.

Verified claim: introduces demand/ability profiles across tasks and LLMs and explicitly discusses construct validity via benchmark sensitivity/specificity and task demand profiles.

**Use:** supports the broader point that benchmark scores combine task demands and system abilities rather than functioning as model-invariant measures.

## 4. Claim revisions required for v0.3

1. Replace broad wording such as “the instrument was not valid for the model” with the narrower operational statement “the candidate did not pass the frozen prerequisites required to interpret the target comparison.”
2. Use **measurement transport / instrument qualification** as pragmatic language; do not claim formal psychometric measurement invariance.
3. Use “replication program” or “attempt to reach a confirmatory replication test,” not “failed replication,” for v0.5–v0.7.
4. State that direct repeated/dependent-evidence novelty is already substantially occupied by 2026 literature.
5. State that construct-validity arguments are established prior art; the contribution is the longitudinal, auditable case study.
6. Keep v0.7 descriptive and explicitly mention the label/order asymmetry.
7. Keep the v0.6 Freeze-A publication deviation in the main limitations.
8. Do not imply that the proposed reporting taxonomy has been externally validated.

## 5. Audit decision

**PASS FOR PREPRINT-READY v0.3**, provided the manuscript adopts the narrowed claims above.

No additional IAER behavioral experiment is required to prepare the methodological note for preprint. A new behavioral study would constitute a separate scientific project/version, not a missing step in this manuscript.
