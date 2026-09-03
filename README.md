# Intra-Agent Evidence Recycling

**Experimental study of memory-derived evidence weighting and lineage effects in LLM agent-style systems**

## Overview

This repository documents a reproducible experimental project investigating whether repeated or self-generated memory records derived from a single epistemic source can acquire excess behavioral weight in a large language model, and whether explicit lineage metadata can reduce that effect.

The central behavioral question is:

> **Can information derived from one external source become behaviorally over-weighted after it is repeated or reused inside persistent memory, even when no genuinely independent evidence has been added?**

A second question concerns mitigation:

> **Does explicit lineage metadata — for example, identifying a self-generated record as derived from `E1` and as not independently evidential — reduce this excess behavioral weight?**

The study does **not** assume that repeated records are internally represented by the model as independent sources. Behavioral effects and provenance understanding are treated as separate constructs.

## Current status

| Version | Role | Status |
| --- | --- | --- |
| v0.2 | Early experimental instrument | Closed; measurement-limited |
| v0.3.1 | Calibration / discovery pilot | Completed; exploratory |
| v0.4.1 | First confirmatory attempt | **Aborted** — manipulation validity failure |
| v0.4.2 | Second confirmatory attempt | **Aborted before data collection** — provenance preflight failure |
| v0.4.3 | Behavioral-confirmatory study | **Completed and independently audited** |
| v0.5.0 | Cross-family replication attempt with Phi-4-mini-instruct | **Invalid/inconclusive** — mandatory behavioral preflight failed; no confirmatory outcomes collected |
| v0.5.1 | Exploratory response-interface diagnostic | **Completed; exploratory only** — strong representation sensitivity and unreliable evidence aggregation |
| v0.5.2 | Preregistered Phi-4-mini-reasoning eligibility pilot | **Valid but INELIGIBLE** — integrity passed; behavioral eligibility gates failed |

See [`docs/experiment_history.md`](docs/experiment_history.md) for the full audit trail.

The only completed confirmatory result remains v0.4.3. The v0.5.x studies are qualification and diagnostic studies and do not alter the v0.4.3 result.

## v0.4.3 confirmatory result

All **168/168** planned trajectories are valid, with no duplicate, missing, extra, or unresolved keys. All four preregistered validity gates pass.

| Hypothesis | Retention | Paired RD | Holm-adjusted p | Verdict |
| --- | ---: | ---: | ---: | --- |
| H1: `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 0.6875 | 9.5367e-7 | **Supported** |
| H2: `active_plain > active_lineage` | 2/32 vs 0/32 | 0.0625 | 0.50 | **Not supported** |

The provenance audit was exact for 168/168 trajectories, but remains descriptive/exploratory as preregistered. It cannot establish a confirmed provenance-use mechanism.

The complete frozen materials, raw results, release manifest, and audit report are in [`experiments/v0_4_3`](experiments/v0_4_3).

## Preprint

The citation-locked manuscript is published as a public, non-peer-reviewed preprint:

> Boticiu, Ovidiu. (2026). *When One Source Returns: A Preregistered Behavioral Study of Intra-Agent Evidence Recycling* (Version 0.4) [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.22282120

- Preprint DOI: [10.5281/zenodo.22282120](https://doi.org/10.5281/zenodo.22282120)
- Reproducibility archive: [10.5281/zenodo.22259801](https://doi.org/10.5281/zenodo.22259801)

## Cross-family qualification after v0.4.3

### v0.5.0 — Phi-4-mini-instruct

The frozen package and technical checks passed, but one of four mandatory behavioral preflight cases failed. Under the fail-closed rule, v0.5.0 was declared `INVALID/INCONCLUSIVE`, and no confirmatory outcomes were collected.

### v0.5.1 — exploratory diagnostic

The diagnostic completed all 48 planned calls. Overall normative accuracy was 29/48 and varied substantially across the `claim_label`, `value_token`, and `explicit_odds` response representations. These findings are descriptive and exploratory; they cannot identify an internal mechanism or change the status of v0.5.0.

### v0.5.2 — Phi-4-mini-reasoning eligibility pilot

The pilot was [publicly preregistered](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.5.2-preregistration) before behavioral collection. All 36 planned trajectories were valid, with no failure, missing, extra, duplicate, or metadata-mismatched rows.

| Condition | Correct | Prespecified requirement | Result |
| --- | ---: | ---: | --- |
| `baseline_initial` | 4/12 | at least 10/12 | FAIL |
| `counter_single_strong` | 12/12 | at least 10/12 | PASS |
| `independent_five_initial` | 2/12 | at least 10/12 | FAIL |

The preregistered decision was `INELIGIBLE`: this exact model/interface/configuration cannot proceed to an IAER v0.6.0 confirmatory run. This is a valid negative screening result, not a technical failure. The complete outcome is archived in [`experiments/v0_5_2_eligibility`](experiments/v0_5_2_eligibility) and in the [public results release](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.5.2-results).

These qualification outcomes neither confirm nor refute cross-family generalization of the IAER effect.

## Research design

The experiments use fictional binary claims about fictional devices, limiting contamination by real-world knowledge.

Core conditions:

- `source_only` — one independent external source supports the initial claim;
- `neutral_filler` — the same source plus unrelated memory records;
- `passive_repeat` — the same source plus repeated reviews of that source;
- `active_plain` — the source plus self-generated downstream application traces without explicit epistemic lineage;
- `active_lineage` — the same traces with explicit root-source and non-independence metadata;
- `independent_evidence` — multiple genuinely independent external sources, used as a positive control.

A later independent counter-source is introduced, and the model's final choice is measured. The primary behavioral outcome is whether the model retains the initially supported claim after receiving stronger counterevidence.

## Experimental discipline

The project follows these procedural rules:

- preregistration before confirmatory data collection;
- fixed-N stopping;
- fail-closed execution for technical or schema failures;
- fresh held-out stimuli for materially revised confirmatory attempts;
- aborted attempts are retained rather than deleted;
- raw results are not merged across incompatible versions;
- confirmatory thresholds are not changed after observing results;
- behavioral observations, provenance judgments, and mechanistic interpretations remain distinct.

## Model and runtime scope

The v0.4.3 result is specific to:

- model label: `qwen3.5-4b`;
- LM Studio local server;
- temperature: `0`;
- thinking/reasoning mode: OFF;
- structured outputs through JSON Schema.

Generalization requires replication across additional models, runtimes, prompts, and task families.

The v0.5.0 and v0.5.1 studies used Microsoft Phi-4-mini-instruct. The v0.5.2 eligibility pilot used Microsoft Phi-4-mini-reasoning Q4_K_M. Their outcomes apply only to their frozen task interfaces and configurations.

## Repository structure

```text
intra-agent-evidence-recycling/
├── README.md
├── CITATION.cff
├── LICENSE-CODE
├── LICENSE-DATA-DOCS.md
├── docs/
│   └── experiment_history.md
└── experiments/
    ├── v0_3_1/
    ├── v0_4_1_aborted/
    ├── v0_4_2_aborted/
    ├── v0_4_3/
    ├── v0_5_0/
    ├── v0_5_1_diagnostic/
    └── v0_5_2_eligibility/
```

## Reproducibility

The repository allows another researcher to determine:

1. what hypotheses and decision thresholds were frozen before collection;
2. which exact stimuli and model configuration were used;
3. how every condition was constructed;
4. how failures and aborted attempts were handled;
5. how the final statistics were computed;
6. whether the complete release still matches its SHA-256 manifest.

## Interpretation policy

The project distinguishes between:

- **behavioral observation** — what the model selected;
- **provenance judgment** — what the model explicitly classified as independent evidence;
- **mechanistic interpretation** — why the model behaved that way.

Only the first two are directly observed. Mechanistic explanations remain hypotheses unless separately validated.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). GitHub can render it through the repository's **Cite this repository** control.

Preferred manuscript citation:

> Boticiu, Ovidiu. (2026). *When One Source Returns: A Preregistered Behavioral Study of Intra-Agent Evidence Recycling* (Version 0.4) [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.22282120

Software and reproducibility archive:

> Boticiu, Ovidiu. (2026). *Intra-Agent Evidence Recycling v0.4.3 — Behavioral Confirmatory Study* (Version 0.4.3) [Software]. Zenodo. https://doi.org/10.5281/zenodo.22259801

## License

- Software code is licensed under the [MIT License](LICENSE-CODE).
- Original experimental data and documentation are licensed under [CC BY 4.0](LICENSE-DATA-DOCS.md).

Copyright © 2026 Ovidiu Boticiu.
