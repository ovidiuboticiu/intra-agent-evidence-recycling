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
|---|---|---|
| v0.2 | Early experimental instrument | Closed; measurement-limited |
| v0.3.1 | Calibration / discovery pilot | Completed |
| v0.4.1 | First confirmatory attempt | **Aborted** — manipulation validity failure |
| v0.4.2 | Second confirmatory attempt | **Aborted before data collection** — provenance preflight failure |
| v0.4.3 | Behavioral-confirmatory study | **In progress** |

See [`docs/experiment_history.md`](docs/experiment_history.md) for the full audit trail.

## Research design

The experiments use fictional binary claims about fictional devices, limiting contamination by real-world knowledge.

Core conditions:

- `source_only` — one independent external source supports the initial claim;
- `neutral_filler` — the same source plus unrelated memory records;
- `passive_repeat` — the same source plus repeated reviews of that source;
- `active_plain` — the source plus self-generated downstream application traces without explicit epistemic lineage;
- `active_lineage` — the same traces with explicit root-source and non-independence metadata;
- `independent_evidence` — multiple genuinely independent external sources, used as a positive control.

A later independent counter-source is then introduced, and the model's final choice is measured.

The primary behavioral outcome is whether the model **retains the initially supported claim** after receiving stronger counterevidence.

## Confirmatory hypotheses in v0.4.3

### H1 — Memory-source multiplication

`passive_repeat` should retain the initial claim more often than the length-matched `neutral_filler` control.

Confirmatory support requires both:

- paired risk difference ≥ **+0.25**;
- Holm-adjusted exact paired McNemar **p < 0.05**.

### H2 — Lineage mitigation

`active_plain` should retain the initial claim more often than `active_lineage`.

The same confirmatory thresholds apply.

## Provenance: secondary in v0.4.3

Earlier work suggested a possible dissociation between explicit provenance judgments and behavioral evidence weighting. However, provenance auditing proved less stable than the behavioral task itself.

For that reason, v0.4.3 still records provenance outputs, but they are:

- descriptive / exploratory;
- not a validity gate;
- not part of H1 or H2;
- not sufficient, by themselves, to establish a confirmed "provenance-use gap".

A dedicated provenance study would be required for a strong mechanistic claim.

## Experimental discipline

This project follows several procedural rules:

- **pre-registration before confirmatory data collection;**
- **fixed-N stopping;**
- **fail-closed execution** for technical or schema failures;
- **fresh held-out stimuli** for each new confirmatory attempt;
- aborted attempts are retained and documented rather than deleted;
- raw results are not merged across incompatible versions;
- technical amendments are documented explicitly;
- confirmatory thresholds are not changed after observing results;
- pilot findings are not presented as confirmatory evidence.

## Model and local runtime

Current experimental family:

- **Model:** `qwen3.5-4b`
- **Runtime:** LM Studio local server
- **Temperature:** `0`
- **Thinking / reasoning mode:** OFF
- structured outputs via JSON Schema
- current code passes `strict` as a JSON/Python boolean (`True`)

The study is therefore specific to this model/configuration unless replicated elsewhere.

## Repository structure

```text
intra-agent-evidence-recycling/
├── README.md
├── .gitignore
├── docs/
│   └── experiment_history.md
└── experiments/
    ├── v0_3_1/
    ├── v0_4_1_aborted/
    ├── v0_4_2_aborted/
    └── v0_4_3/
```

Each experiment folder should eventually contain, where applicable:

- preregistration;
- stimuli;
- runner;
- analysis script;
- raw JSONL results;
- freeze manifest / hashes;
- amendments or abort notes;
- version-specific README.

## Reproducibility

The repository should allow another researcher to determine:

1. what hypothesis was frozen before data collection;
2. which exact stimuli were used;
3. which model/runtime configuration was used;
4. how each condition was constructed;
5. how technical failures were handled;
6. how the final statistics were computed;
7. which versions were exploratory, confirmatory, or aborted.

## Interpretation policy

The project distinguishes between:

- **behavioral observation** — what the model selected;
- **provenance judgment** — what the model explicitly classified as independent evidence;
- **mechanistic interpretation** — why the model behaved that way.

Only the first two are directly observed. Mechanistic explanations remain hypotheses unless separately validated.

## Publication status

This repository is currently a private research workspace.

No result from the ongoing v0.4.3 study should be described as confirmed until:

1. the fixed-N collection is complete;
2. the preregistered analysis is run;
3. the raw results are independently audited;
4. the final status of H1 and H2 is determined.

A later public release may be accompanied by a preprint and an archived reproducibility package.

## Citation

A formal citation file will be added when the first public reproducibility release is frozen.

## License

No license has been assigned yet. A license should be selected before public release.
