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

See [`docs/experiment_history.md`](docs/experiment_history.md) for the full audit trail.

## v0.4.3 confirmatory result

All **168/168** planned trajectories are valid, with no duplicate, missing, extra, or unresolved keys. All four preregistered validity gates pass.

| Hypothesis | Retention | Paired RD | Holm-adjusted p | Verdict |
| --- | ---: | ---: | ---: | --- |
| H1: `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 0.6875 | 9.5367e-7 | **Supported** |
| H2: `active_plain > active_lineage` | 2/32 vs 0/32 | 0.0625 | 0.50 | **Not supported** |

The provenance audit was exact for 168/168 trajectories, but remains descriptive/exploratory as preregistered. It cannot establish a confirmed provenance-use mechanism.

The complete frozen materials, raw results, release manifest, and audit report are in [`experiments/v0_4_3`](experiments/v0_4_3).

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
    └── v0_4_3/
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

Suggested citation:

> Boticiu, Ovidiu. *Intra-Agent Evidence Recycling*, version 0.4.3, 2026. <https://github.com/ovidiuboticiu/intra-agent-evidence-recycling>.

## License

- Software code is licensed under the [MIT License](LICENSE-CODE).
- Original experimental data and documentation are licensed under [CC BY 4.0](LICENSE-DATA-DOCS.md).

Copyright © 2026 Ovidiu Boticiu.
