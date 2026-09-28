# When One Source Returns

## A Pre-Specified Behavioral Study of Intra-Agent Evidence Recycling

**Ovidiu Boticiu**  
Independent researcher  
**Corrected post-publication draft — 28 September 2026**  
Historical Version 0.4 DOI: `10.5281/zenodo.22282120`  
**Status:** draft for a new Zenodo version; not yet published; not peer reviewed

---

## Correction note

This draft supersedes the *positioning* of the historical Version 0.4 preprint while preserving its historical record.

Three post-publication changes are explicit:

1. The historical statement that IAER was, "to our knowledge, the first preregistered controlled test of that complete operational combination," is **withdrawn**. A broader later prior-art audit found both materially close work that had not been identified before publication and close work already cited in Version 0.4 that had not been weighted conservatively enough when the priority wording was formulated. No priority claim is made in this draft.
2. For v0.4.3, `pre-specified and frozen before collection` replaces `publicly preregistered before collection`. A forensic chronology audit found strong internal freeze consistency but did not locate a public or independently verifiable pre-collection timestamp of the preregistration artifact itself.
3. The neutral control is described as an **equal-count unrelated-memory control**, not as length-matched.

No v0.4.3 raw data, numerical result, H1/H2 verdict, or frozen historical artifact is changed.

A later 2026-09-27 **direct-configuration replication** is also reported. It is a fresh behavioral collection using the frozen v0.4.3 materials in the same tested model/configuration class; it is **not** an independent-lab or cross-family replication.

See:
- `docs/IAER_PRIORITY_CLAIM_WITHDRAWAL_2026-09-28.md`
- `docs/IAER_PRIOR_ART_REASSESSMENT_2026-09-28.md`
- `docs/V0_4_3_FORENSIC_VALIDATION_ADDENDUM_v1_0.md`

---

## Rezumat în limba română

Acest studiu investighează dacă o singură sursă poate dobândi o influență comportamentală excesivă atunci când reapare ulterior în context sub forma unor înregistrări de memorie derivate, fără adăugarea unei surse externe independente. În studiul confirmatoriu v0.4.3, pre-specificat și înghețat înainte de colectare, configurația `qwen3.5-4b` a parcurs 168/168 traiectorii valide pe 32 de itemi ficționali echilibrați. Condiția `passive_repeat` a păstrat afirmația inițială în 22/32 de cazuri, comparativ cu 0/32 pentru controlul cu cinci înregistrări de memorie fără legătură cu ținta (RD = 0,6875; p Holm ≈ 9,54 × 10⁻⁷). Contrastul de lineage `active_plain > active_lineage` nu a fost susținut.

Auditul forensic post-publicare nu a identificat erori materiale de date, împerechere sau analiză statistică, dar a restrâns interpretarea: manipularea H1 modifică simultan repetarea semantică și lexicală, saliența, referințele explicite la sursa-rădăcină și structura promptului, astfel încât nu demonstrează un mecanism literal de „numărare a copiilor ca surse independente”.

O replicare directă în aceeași configurație, colectată la 27 septembrie 2026, a produs din nou un efect H1 mare: 24/32 versus 0/32 (RD = 0,75; Holm p ≈ 2,38 × 10⁻⁷). H2 a rămas nesusținut (3/32 versus 0/32; RD = 0,09375; p = 0,25). Rezultatul principal este astfel reprodus în configurația testată, dar generalizarea cross-family rămâne nerezolvată.

O reevaluare ulterioară a literaturii a identificat lucrări anterioare importante privind repetiția, dovezile dependente, memoria corelată și proveniența. În consecință, versiunea corectată nu revendică prioritate conceptuală sau experimentală. Contribuția este prezentată ca un studiu controlat, specific configurației, și ca o extensie experimentală în interiorul unui domeniu de cercetare deja existent.

---

## Abstract

Large language model agents increasingly retain summaries, reviews, and execution traces derived from earlier observations. Such records may later re-enter context alongside the evidence from which they were produced, creating a risk that one epistemic source acquires additional behavioral influence. We use *intra-agent evidence recycling* (IAER) as a behavioral label for this possibility.

We report a pre-specified, fixed-N behavioral study using 32 balanced fictional binary-choice items and `qwen3.5-4b` under a frozen local inference configuration. Each core H1/H2 trajectory began with one initial external source supporting an initial claim and later received a stronger independent counter-source; the separate positive-control trajectories used genuinely independent corroborating sources. H1 tested whether five derivative, target-consistent review records increased retention relative to an equal-count control containing five unrelated memory records. H2 tested whether explicit lineage metadata reduced retention relative to unlabeled self-generated application traces.

All 168 planned trajectories were valid and all four frozen pre-specified validity gates passed. H1 was supported: `passive_repeat` retained the initial claim in 22/32 items versus 0/32 under `neutral_filler` (paired risk difference = 0.6875; bootstrap 95% CI [0.531, 0.844]; Holm-adjusted exact McNemar p = 9.54 × 10⁻⁷). H2 was not supported (2/32 versus 0/32; risk difference = 0.0625; Holm-adjusted p = 0.50).

A post-publication forensic audit reproduced the outcomes from raw final choices and found no material data, pairing, or statistical error. It also established an important construct limitation: H1 jointly changes derivative multiplicity, lexical/semantic repetition, target-consistent salience, explicit root references, and prompt structure, so the result does not identify literal independent-source counting as the mechanism.

A fresh 2026-09-27 direct-configuration replication reproduced H1 in the same direct-configuration class under the frozen v0.4.3 protocol: 24/32 versus 0/32 (risk difference = 0.75; 95% CI [0.59375, 0.90625]; Holm-adjusted p = 2.38419 × 10⁻⁷). H2 again was not supported (3/32 versus 0/32; risk difference = 0.09375; p = 0.25). This is not an independent-lab or cross-family replication.

A post-publication prior-art reassessment identified substantial pre-existing work on repetition, dependent evidence, correlated memory, and provenance. This revision therefore makes no priority claim. IAER is positioned as a configuration-specific controlled study and experimental extension within that broader literature.

---

# 1. Introduction

Agent-style systems do not reason only over freshly retrieved evidence. They also consume records created by earlier stages of their own operation: summaries, reflections, reviews, decisions, plans, and execution traces. These records can compress long histories and support continuity, but they can also blur the difference between repeated representation and independent corroboration.

The distinction matters because one report repeated many times is not equivalent to many independent witnesses. LLM behavior, however, is sensitive to repetition, presentation order, credibility cues, retrieval composition, and self-generated context. Prior work published before the IAER empirical preprint had already established important parts of this landscape. Schuster et al. (2026) showed that repetition can reverse source preferences under knowledge conflict. Naphade (2026) reported that paraphrasing an argument can be more persuasive than providing distinct independent support. CUE-R manipulated duplicate evidence directly, while Ross et al. (2026) compared duplicate, paraphrased, and diverse retrieval contexts. Work on agent memory and provenance, including GovMem, Memory Echo, MemLineage, and CAMA, further addressed correlated memories, repeated upstream sources, provenance tags, and lineage-aware handling.

IAER therefore does not claim discovery of repetition bias, dependent-evidence failure, provenance, or memory correlation. It asks a narrower experimental question: under one controlled agent-style trajectory, what happens when information downstream of one external source returns through later memory records and is then confronted by stronger independent counterevidence?

We define *intra-agent evidence recycling* behaviorally as the reintroduction of records semantically downstream of an earlier source into a later decision context without the addition of independent external evidence. The definition does not assume a Bayesian mechanism, conscious source counting, or any specific internal representation.

The v0.4.3 study tested two contrasts. H1 compared passive derivative reviews with unrelated intervening memory. H2 compared self-generated application traces without lineage metadata against otherwise analogous traces marked self-generated, rooted in E1, and non-independent. A positive control tested whether the instrument responded to genuinely independent corroboration.

---

# 2. Contributions and claim boundary

This revision claims the following contributions:

- a pre-specified, fixed-N behavioral assay separating observed choice, explicit provenance judgment, and mechanistic interpretation;
- a controlled configuration-specific comparison between derivative target-consistent memory and an equal-count unrelated-memory control;
- a positive control using genuinely independent corroboration;
- a large H1 effect in the original v0.4.3 collection;
- a fresh direct-configuration replication that reproduced H1 with similar magnitude;
- a null/negative result for the pre-specified medium-to-large lineage-mitigation contrast;
- a preserved fail-closed record of cross-family qualification attempts that did not yield a valid cross-family confirmatory estimate;
- a post-publication forensic audit and public correction trail.

This revision explicitly **does not claim**:

- the first repetition effect in LLMs;
- the first dependent-evidence effect;
- the first correlated-memory effect;
- the first provenance or lineage approach;
- that the model counted derivative records as independent sources;
- cross-family generality;
- an independently replicated effect by a separate laboratory.

The historical Version 0.4 priority statement is withdrawn.

---

# 3. Related work and literature positioning

## 3.1 Repetition, knowledge conflict, and source preference

Controlled work on knowledge conflict shows that models can alter decisions when contextual evidence conflicts with prior or competing information. Schuster, Gautam, and Markert (2026) evaluated 13 open-weight models and found that repeating information from less credible sources could reverse source preferences.

Naphade (2026), in Findings of ACL, introduced GroupQA and studied how models aggregate groups of conflicting evidence. A particularly relevant result is that paraphrasing an argument can be more persuasive than providing distinct independent support. This is direct prior art for the broad repetition-versus-independence problem.

These studies preclude any claim that IAER first demonstrated that repeated support can distort evidence aggregation.

## 3.2 Duplicate and redundant retrieval

CUE-R (Jain & Vedam, 2026) applies REMOVE, REPLACE, and DUPLICATE interventions to retrieved evidence and reports that duplication can be answer-redundant while remaining behaviorally non-neutral.

Ross et al. (2026) compare duplicate, paraphrased, and diverse retrieval sets under a controlled fictional QA design. Their work directly separates redundancy from diversity and shows that diverse support can outperform duplicate or paraphrased redundancy.

## 3.3 Memory-carried and correlated evidence

GovMem (Qi, Xu, & Li, 2026) treats repeated observations from agents as potentially correlated by copied sources, shared prompts, shared tools, stale environments, or scope. It evaluates dependency-aware promotion into long-term memory.

Toeda's *Memory Echo and How to Stop It* (2026) describes a failure in which model-generated interpretation is stored, retrieved later, and treated as if independently grounded; it uses provenance-tagged memory as part of the proposed remedy.

CAMA (Lin et al., 2026) formalizes *Memory Correlation Bias*: multiple memories can inherit the same upstream source and form a false majority. It estimates effective independent sources and uses provenance-aware reasoning to suppress that failure.

These works substantially overlap the broad conceptual space that IAER originally described.

## 3.4 Provenance and derivation lineage

MemLineage (Ouyang & Hou, 2026) attaches cryptographic provenance and derivation lineage to agent-memory entries and propagates ancestry through derived records. More generally, evidence-tracing and execution-provenance research treats links among observations, memories, intermediate claims, actions, and outputs as accountability infrastructure.

IAER therefore contributes neither the general provenance concept nor the first lineage-aware memory system.

## 3.5 Corrected contribution boundary

A later targeted literature reassessment did not establish that an earlier publication used the exact full IAER v0.4.3 protocol one-for-one. However, the original literature search was not sufficient to support a durable priority statement, and the surrounding conceptual and experimental components had substantial prior art.

Accordingly:

> **No priority claim is made.**

IAER is best interpreted as a controlled experimental extension that combines several already-recognized issues—repetition, dependence, memory carriage, counterevidence, and provenance—inside one configuration-specific agent-style assay.

---

# 4. Methods: original v0.4.3 study

## 4.1 Design and model configuration

The study was a behavioral-confirmatory fixed-N experiment using `qwen3.5-4b` through a local LM Studio API, with thinking disabled, temperature 0, structured JSON outputs, and the frozen v0.4.3 runner.

Thirty-two fictional binary-choice items were balanced by initial claim:

- 16 `CLAIM_A`;
- 16 `CLAIM_B`;

and by presentation order:

- 16 `A_FIRST`;
- 16 `B_FIRST`.

Fictional entities and values reduced contamination from real-world knowledge.

The hypotheses, gates, stimuli, runner, and analysis were preserved as a frozen pre-specified package before collection. Stable package hashes are embedded across the result rows. A later chronology audit did not locate a public or independently verifiable pre-collection timestamp of the preregistration artifact itself; therefore this revision does not describe v0.4.3 as publicly preregistered before collection.

## 4.2 Evidence sequence and conditions

Each core trajectory began with one independent external source, E1, with stated reliability 0.65 supporting the initial claim. A later independent counter-source, C1, with stated reliability 0.80 supported the opposing claim.

The intervening conditions were:

| Condition | Intervening memory | N |
| --- | --- | ---: |
| `source_only` | E1 only | 32 |
| `neutral_filler` | E1 plus five unrelated memory records | 32 |
| `passive_repeat` | E1 plus five explicit reviews of E1, each marked as not a new external source | 32 |
| `active_plain` | E1 plus five self-generated application traces without explicit lineage metadata | 32 |
| `active_lineage` | analogous traces marked self-generated, rooted in E1, and non-independent | 32 |
| `independent_evidence` | five genuinely independent sources supporting the initial claim | 8 |

The `neutral_filler` and `passive_repeat` conditions were matched in record count, **not in exact token/text length**.

## 4.3 Outcomes and hypotheses

The primary behavioral outcome, `retain_initial`, equaled 1 when the final belief probe selected the initially supported claim and 0 otherwise.

H1 predicted:

`passive_repeat > neutral_filler`

H2 predicted:

`active_plain > active_lineage`

Each hypothesis required both:

- paired risk difference >= +0.25; and
- Holm-adjusted two-sided exact paired McNemar p < 0.05.

## 4.4 Validity and stopping rules

Four frozen pre-specified gates protected interpretability:

1. at least 24/32 `source_only` items had to select the counterclaim;
2. at least 6/8 positive controls had to retain the initial claim;
3. all active trajectories had to contain exactly five application outputs;
4. all 168 planned keys had to be valid and complete.

Collection used fixed-N stopping with no scientific outcome-based exclusion.

## 4.5 Statistical analysis

Primary contrasts used paired risk differences and two-sided exact McNemar tests, followed by Holm correction across H1 and H2. Percentile bootstrap confidence intervals used 20,000 paired resamples with frozen seeds.

The original power note did not contain a full prospective power calculation. Later sensitivity analysis showed that N=32 is reasonably sensitive to a clean directional RD of 0.25 but substantially less sensitive when discordance occurs in both directions.

---

# 5. Original v0.4.3 results

## 5.1 Integrity and validity

All 168 planned trajectories were valid and unique. There were no unresolved failures, duplicate keys, missing keys, or extra keys.

- `source_only`: 32/32 selected the counterclaim;
- positive control: 7/8 retained the initial claim;
- all 64 active trajectories contained five application outputs;
- all planned keys were present.

All four frozen pre-specified validity gates passed.

## 5.2 H1 and H2

| Contrast | Retention | Paired RD | 95% bootstrap CI | Holm-adjusted p | Verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| H1: `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 0.6875 | [0.531, 0.844] | 9.54 × 10⁻⁷ | Supported |
| H2: `active_plain > active_lineage` | 2/32 vs 0/32 | 0.0625 | [0.000, 0.156] | 0.50 | Not supported |

For H1, 22 paired items changed in the predicted direction and none in the opposite direction.

For H2, the pre-specified medium-to-large mitigation criterion was not met. This does not establish that lineage has zero effect; it establishes that the specified mitigation hypothesis was not supported in this manipulation.

## 5.3 Provenance outcome

The explicit provenance audit identified the correct independent root evidence in 168/168 trajectories, with no false independent identifiers or missed roots. This measure was descriptive/exploratory under the frozen plan and does not establish causal provenance use in the final decision.

---

# 6. Post-publication forensic validation

A later no-new-data forensic audit:

- reconstructed the expected 168 keys;
- found zero missing, extra, or duplicate keys;
- recomputed `retain_initial` from raw final choices rather than trusting the stored derived field;
- reproduced H1 and H2 exactly;
- audited all 22 H1-discordant pairs;
- found no material computational, statistical, or pairing error.

The audit also narrowed the claim boundary.

The H1 manipulation does **not** isolate derivative dependence alone. Relative to `neutral_filler`, `passive_repeat` also changes:

- lexical repetition;
- semantic target consistency;
- target relevance/salience;
- explicit E1 references;
- prompt/token structure.

Therefore the strongest supported claim is behavioral:

> Under the frozen v0.4.3 task family and Qwen configuration, five explicitly derivative, target-consistent reviews of one initial source substantially increased retention of the initial claim relative to five unrelated memory records.

Literal independent-source counting is not established.

---

# 7. 2026-09-27 direct-configuration replication

A fresh Level B direct-configuration replication was run using the frozen v0.4.3 source materials.

The replication used:

- LM Studio 0.4.25;
- API model ID `qwen3.5-4b`;
- `Qwen3.5-4B-Q4_K_M.gguf`;
- GGUF SHA-256 `25082A7DD3776CC3C741C6347D3BD04523F05796607B3FBC32FA3A25DFA1418C`;
- thinking OFF;
- temperature 0;
- context length 8192;
- sequential execution.

The historical original GGUF hash was not preserved, so this is **not** claimed to be bit-for-bit runtime reproduction; "same direct-configuration class" is the intended scope.

## 7.1 Collection integrity

- 168/168 valid planned keys;
- zero duplicates;
- zero target-trajectory failures;
- zero target-trajectory transport retries;
- validity gates V1–V4 passed.

## 7.2 Replication results

| Contrast | Retention | Paired RD | 95% CI | Holm-adjusted p | Verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| H1: `passive_repeat > neutral_filler` | 24/32 vs 0/32 | 0.75 | [0.59375, 0.90625] | 2.38419 × 10⁻⁷ | Supported |
| H2: `active_plain > active_lineage` | 3/32 vs 0/32 | 0.09375 | [0, 0.21875] | 0.25 | Not supported |

Provenance exactness was again 168/168 and remains descriptive.

## 7.3 Interpretation

The direct replication moves H1 from a single successful collection to a **narrow behavioral effect reproduced in the same direct-configuration class under the frozen v0.4.3 protocol**.

It does not establish:

- independent-lab replication;
- cross-family generality;
- architecture-independent IAER;
- a general source-counting mechanism.

The archival release is:

`iaer-v0.4.3-level-b-replication-20260927`

---

# 8. Cross-family qualification and later program history

Later IAER work attempted to determine whether the v0.4.3 target could be meaningfully tested in other model families.

- **v0.5.0 / Phi-4-mini-instruct:** mandatory behavioral preflight failed one of four required cases; confirmatory collection stopped. No valid replication or non-replication estimate was produced.
- **v0.5.1:** exploratory interface diagnostic; not confirmatory.
- **v0.5.2 / Phi-4-mini-reasoning:** technically valid eligibility pilot but behaviorally ineligible under frozen gates; no confirmatory collection followed.
- **v0.6 / Ministral:** calibration failed before eligibility; no confirmatory IAER collection.
- **v0.7 / Ministral measurement-decoupling redesign:** integrity passed, but the frozen redesign validity gates failed and the run stopped under `REDESIGN_FAILED_STOP`. v0.7 was explicitly not an IAER replication.

Accordingly, cross-family generalization remains **unresolved**, not falsified and not established.

---

# 9. Discussion

## 9.1 What the replicated H1 establishes

Across two separate collections in the same tested Qwen configuration class, passive target-consistent derivative reviews produced a large behavioral separation from unrelated memory:

- original: 22/32 vs 0/32, RD = 0.6875;
- direct replication: 24/32 vs 0/32, RD = 0.75.

The similarity of the two effect magnitudes argues against treating the original result as a one-off execution artifact within that configuration.

## 9.2 What H1 does not establish

The experiment does not tell us which component of the manipulation caused the effect. Plausible contributors include:

- semantic repetition;
- lexical repetition;
- increased target salience;
- repeated explicit mention of E1;
- discourse conventions that signal importance;
- context-length/position effects;
- actual sensitivity to source dependence or lineage.

Because these factors were not factorially isolated, source-counting language would exceed the evidence.

## 9.3 Lineage result

The H2 lineage-mitigation hypothesis failed in both the original study and the direct replication. However, `active_plain` itself produced little retention, leaving limited room for a mitigation effect. The appropriate conclusion remains that the specified lineage intervention was **not supported**, not that provenance metadata is useless in general.

## 9.4 Relation to prior art

The post-publication literature reassessment materially changes how IAER should be positioned. Repetition-versus-independence effects, correlated memories, dependent evidence, and provenance-aware memory all predate the IAER preprint.

The IAER contribution is therefore not a foundational discovery. Its value lies in the specific controlled assay, preserved failure history, direct same-configuration replication, and explicit separation between empirical behavior and mechanistic interpretation.

---

# 10. Limitations

- **Configuration scope:** the confirmatory effect is established only for the tested `qwen3.5-4b` configuration class.
- **No independent-lab replication:** the 2026-09-27 replication was conducted within the same project.
- **No valid cross-family estimate:** later candidates failed qualification/calibration/redesign gates before a valid confirmatory cross-family comparison.
- **Synthetic task scope:** fictional binary claims improve experimental control but do not establish effects in open-ended real-world agent workflows.
- **Construct confounding:** H1 does not isolate source dependence from repetition, salience, explicit root references, and prompt structure.
- **Behavioral inference only:** correct explicit provenance classification does not prove that provenance causally governed the final choice.
- **H2 floor limitation:** low `active_plain` retention limited room to demonstrate mitigation.
- **Original sample-size planning:** N=32 was fixed without a full frozen prospective power analysis.
- **Historical preregistration wording:** the package was internally pre-specified/frozen, but a public independently verifiable pre-collection preregistration timestamp was not located.
- **Historical novelty search:** the original search was structured/scoping but incomplete and missed materially close prior work; the priority claim has therefore been withdrawn.
- **Literature reassessment is not systematic-review proof:** the later correction audit is targeted and adversarial, not a PRISMA-style exhaustive review.

---

# 11. Conclusion

The v0.4.3 study and its 2026-09-27 direct-configuration replication show a robust configuration-specific behavioral contrast: five derivative, target-consistent reviews of one initial source substantially increased retention of that source-supported claim relative to five unrelated memory records.

That finding survives post-publication data and statistical audit and was reproduced in a fresh same-configuration collection.

The result does **not** identify a literal source-counting mechanism, establish cross-family generality, or justify a claim that IAER discovered the broader phenomenon. A later prior-art reassessment found substantial earlier work on repetition, dependent evidence, correlated memory, and provenance; the historical priority claim is therefore withdrawn.

The appropriate contribution is narrower: IAER provides a transparent controlled assay, a direct same-configuration replication, an explicit construct-validity boundary, and a fail-closed record of where later generalization attempts became uninterpretable.

Further work should decompose repetition, salience, and explicit root-link structure before making mechanistic claims, and should seek independent and cross-family replication only after the measurement instrument is demonstrably valid for the candidate configuration.

---

# Data, code, correction record, and transparency

Repository:

https://github.com/ovidiuboticiu/intra-agent-evidence-recycling

Historical empirical preprint:

DOI `10.5281/zenodo.22282120`

v0.4.3 reproducibility archive:

DOI `10.5281/zenodo.22259801`

Methodological note:

DOI `10.5281/zenodo.22306245`

Relevant correction documents:

- `docs/SCIENTIFIC_INTEGRITY_PRINCIPLE.md`
- `docs/V0_4_3_FORENSIC_VALIDATION_ADDENDUM_v1_0.md`
- `docs/IAER_PRIORITY_CLAIM_WITHDRAWAL_2026-09-28.md`
- `docs/IAER_PRIOR_ART_REASSESSMENT_2026-09-28.md`

Direct-configuration replication release:

https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/iaer-v0.4.3-level-b-replication-20260927

Historical frozen artifacts are preserved. The correction process adds explicit dated/versioned records rather than silently rewriting them.

---

# Declarations

## Author contributions

Ovidiu Boticiu: conceptualization, methodology, software coordination, investigation, data curation, formal analysis, validation, visualization, writing — original draft, writing — review and editing, and project administration.

## Funding

This research received no external funding.

## Competing interests

The author declares no competing interests.

## Ethics statement

The study evaluated language-model behavior using fictional stimuli and did not involve human participants, personal data, animals, clinical interventions, or deception of research participants.

## Use of AI-assisted tools

AI-assisted tools were used for code drafting, document preparation, language editing, literature discovery, methodological critique, and post-publication audit assistance. The human author made the research decisions, authorized and executed behavioral runs, retained the raw records, and accepts responsibility for the manuscript, corrections, and reported results.

## Peer-review status

This corrected draft has not been peer reviewed.

---

# References

Boticiu, O. (2026). *Intra-Agent Evidence Recycling v0.4.3 — Behavioral Confirmatory Study*. Zenodo. https://doi.org/10.5281/zenodo.22259801

Druck, G., & Smith, E. (2026). *RAG Collapse: LLM Responses Collapse When Retrieved Documents Are Self-Authored*. arXiv:2608.22118. https://doi.org/10.48550/arXiv.2608.22118

Jain, S., & Vedam, V. N. (2026). *CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation*. arXiv:2604.05467. https://doi.org/10.48550/arXiv.2604.05467

Lin, C., Yuan, W., Wang, X., & Ngai, E. C. H. (2026). *Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration*. arXiv:2608.19701. https://doi.org/10.48550/arXiv.2608.19701

Naphade, A. (2026). Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering. *Findings of the Association for Computational Linguistics: ACL 2026*, 40293–40311. https://doi.org/10.18653/v1/2026.findings-acl.2003

Ouyang, C., & Hou, R. (2026). *MemLineage: Lineage-Guided Enforcement for LLM Agent Memory*. arXiv:2605.14421. https://doi.org/10.48550/arXiv.2605.14421

Qi, Y., Xu, X., & Li, Y. (2026). *When Not to Write Memory: Governing False Promotion from Correlated Agent Traces*. arXiv:2607.02579. https://doi.org/10.48550/arXiv.2607.02579

Ross, J. J., Koopman, B., van der Vegt, A., & Zuccon, G. (2026). *How retriever redundancy and diversity impact RAG effectiveness*. arXiv:2608.13956. https://doi.org/10.48550/arXiv.2608.13956

Schuster, J., Gautam, V., & Markert, K. (2026). *Whose Facts Win? LLM Source Preferences under Knowledge Conflicts*. arXiv:2601.03746. https://doi.org/10.48550/arXiv.2601.03746

Tan, H., Sun, F., Yang, W., Wang, Y., Cao, Q., & Cheng, X. (2024). Blinded by Generated Contexts: How Language Models Merge Generated and Retrieved Contexts When Knowledge Conflicts? *Proceedings of ACL 2024*, 6207–6227. https://doi.org/10.18653/v1/2024.acl-long.337

Toeda, T. (2026). *Memory Echo and How to Stop It: Provenance-Tagged Memory with Deterministic Output-Time Self-Citation Verification*. Zenodo. https://doi.org/10.5281/zenodo.21222332

Wan, A., Wallace, E., & Klein, D. (2024). What Evidence Do Language Models Find Convincing? *Proceedings of ACL 2024*, 7468–7484. https://doi.org/10.18653/v1/2024.acl-long.403

Wang, Y., Zhang, J., Cai, T., Liu, Z., Sun, Q., Sun, Z., Wu, Z., Dong, M., Zheng, M., Yin, X., & Zhu, Y. (2026). *From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents*. arXiv:2606.04990. https://doi.org/10.48550/arXiv.2606.04990

Xie, J., Zhang, K., Chen, J., Lou, R., & Su, Y. (2024). Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts. *ICLR 2024*. https://doi.org/10.48550/arXiv.2305.13300
