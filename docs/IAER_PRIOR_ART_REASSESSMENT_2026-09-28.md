# IAER Prior-Art Reassessment

**Date:** 2026-09-28  
**Purpose:** reassess the literature basis for the historical v0.4 IAER priority wording after publication.

## 1. Bottom line

The pre-publication literature search and weighting of the literature were not sufficient to support a durable priority claim.

The broad phenomena relevant to IAER already had substantial prior art before the 3 September 2026 empirical preprint, including:

- repetition changing LLM decisions under conflict;
- paraphrased/repeated support differing from genuinely distinct support;
- duplicate/redundant retrieval affecting model behavior;
- correlated or copied evidence being non-independent;
- self-generated or memory-carried content re-entering later decisions;
- explicit provenance/lineage mechanisms for agent memory.

For that reason, IAER now withdraws the historical "first preregistered controlled test" priority statement. This reassessment does **not** assert that any one earlier study used an identical IAER v0.4.3 protocol.

### 1.1 What was already known versus what was newly identified

The historical Version 0.4 preprint already cited and discussed several relevant works, including **Schuster et al.**, **CUE-R (Jain & Vedam)**, and **Ross et al.** The correction is therefore **not** that every close predecessor was missed. The problem is twofold:

1. some highly relevant work was identified only after publication, including **Naphade**, **GovMem**, **Memory Echo**, **MemLineage**, and **CAMA**; and
2. some close work already present in Version 0.4 was not weighted conservatively enough when the manuscript moved from a bounded search result to a "first" priority formulation.

This distinction is part of the correction record.

## 2. High-overlap prior work

| Work | Public date/status | Relevant overlap | IAER implication |
| --- | --- | --- | --- |
| Schuster, Gautam & Markert, *Whose Facts Win? LLM Source Preferences under Knowledge Conflicts*, arXiv:2601.03746 | Jan 2026 preprint | Repeating information from less credible sources can reverse model source preferences under conflict. | Repetition-driven evidence weighting was already directly demonstrated. |
| Naphade, *Rational Synthesizers or Heuristic Followers?*, Findings of ACL 2026, DOI 10.18653/v1/2026.findings-acl.2003 | 2026; peer-reviewed Findings paper | Controlled group-evidence experiments report that paraphrasing one argument can be more persuasive than distinct independent support. | Strong direct prior art against any broad claim that IAER first identified repetition-versus-independence failures. |
| Jain & Vedam, *CUE-R: Beyond the Final Answer in Retrieval-Augmented Generation*, arXiv:2604.05467 | Apr 2026 preprint | REMOVE/REPLACE/DUPLICATE interventions show duplication can be answer-redundant but behaviorally non-neutral. | Controlled duplicate-evidence interventions predate IAER. |
| Ross et al., *How retriever redundancy and diversity impact RAG effectiveness*, arXiv:2608.13956 | Aug 2026 preprint | Directly compares duplicate, paraphrased, and diverse retrieved support under controlled fictional QA. | Redundancy versus diversity was already experimentally decomposed in RAG. |
| Qi, Xu & Li, *When Not to Write Memory: Governing False Promotion from Correlated Agent Traces*, arXiv:2607.02579 | submitted 30 Jun 2026 | Explicitly treats repeated agent observations as potentially correlated rather than independent evidence and evaluates dependency-aware memory promotion. | Correlated agent-memory evidence and dependence-aware governance predate IAER publication. |
| Toeda, *Memory Echo and How to Stop It*, Zenodo DOI 10.5281/zenodo.21222332 | 6 Jul 2026 systems paper/pilot | Describes model-produced interpretation stored, retrieved later, and treated as externally grounded/independent evidence; uses provenance-tagged memory. | Very close conceptual prior art for self-generated memory re-entering later context and for provenance-based mitigation. |
| Ouyang & Hou, *MemLineage: Lineage-Guided Enforcement for LLM Agent Memory*, arXiv:2605.14421 | 14 May 2026 preprint | Attaches provenance and derivation lineage to persistent agent-memory entries and propagates ancestry through derived memories. | Provenance/lineage in agent memory was not novel to IAER. |
| Lin et al., *Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration*, arXiv:2608.19701 | 20 Aug 2026 preprint | Defines Memory Correlation Bias, where multiple memories inherit the same upstream source and create a false majority; estimates effective independent sources. | Strongly overlaps the source-dependence / false-majority framing. |

## 3. What remains specific about IAER

The reassessment does not erase the concrete IAER design. v0.4.3 combined, in one frozen configuration:

- one initial external source;
- five derivative target-consistent review records;
- an equal-count unrelated-memory control;
- a later stronger independent counter-source;
- a genuinely independent corroboration positive control;
- a separate active-use lineage contrast;
- paired fictional binary items and a fixed-N confirmatory decision rule.

A later direct-configuration replication reran the frozen design and again produced a large H1 separation. Because the historical original GGUF artifact was not hash-pinned, this is a same direct-configuration-class replication rather than bit-for-bit runtime reproduction.

However, **a specific combination of already-studied components is not, by itself, a sufficient basis for a priority claim** unless a literature review establishes that claim to an appropriate standard. The original IAER search did not meet that standard.

## 4. Construct-validity boundary

The replicated v0.4.3 H1 contrast does not isolate a single source-dependence mechanism. Compared with `neutral_filler`, `passive_repeat` simultaneously changes:

- target-consistent semantic repetition;
- lexical repetition;
- salience/relevance;
- explicit references to E1;
- derivative-memory multiplicity;
- prompt/token structure.

Therefore the strongest current inference is behavioral:

> Under the frozen Qwen configuration, five explicitly derivative, target-consistent reviews of one initial source substantially increased retention of the source-supported claim relative to five unrelated memory records.

It is **not** established that the model literally counted dependent records as independent sources.

## 5. Revised contribution boundary

Future IAER publications should not claim priority for:

- repetition bias;
- dependent-evidence effects;
- correlated-memory effects;
- provenance/lineage;
- source-independence reasoning;
- memory echo/self-reinforcement;
- the general need for construct-validity checks in LLM evaluation.

A defensible contribution statement is:

> IAER provides a pre-specified, configuration-specific controlled assay of one source re-entering a later LLM decision through derivative memory records, an archived same-configuration replication of the main behavioral contrast, and a transparent fail-closed record of later cross-family qualification attempts.

## 6. Search-status limitation

This reassessment is a targeted, adversarial literature-positioning audit. It is **not** a PRISMA systematic review and is not proof that every relevant publication has been found. Its purpose is narrower: determine whether the historical priority claim remains responsibly supportable.

Decision: **No. The priority claim is withdrawn.**

## 7. Primary-source links

- Schuster et al.: https://arxiv.org/abs/2601.03746
- Naphade: https://aclanthology.org/2026.findings-acl.2003/
- CUE-R: https://arxiv.org/abs/2604.05467
- Ross et al.: https://arxiv.org/abs/2608.13956
- GovMem: https://arxiv.org/abs/2607.02579
- Memory Echo: https://doi.org/10.5281/zenodo.21222332
- MemLineage: https://arxiv.org/abs/2605.14421
- CAMA: https://arxiv.org/abs/2608.19701
