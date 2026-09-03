# Intra-Agent Evidence Recycling

**Experimental study of memory-derived evidence weighting and lineage effects in LLM agent-style systems**

## Overview

This repository documents a reproducible experimental program investigating whether repeated or self-generated memory records derived from a single epistemic source can acquire excess behavioral weight in a large language model, even when no genuinely independent evidence has been added.

The central behavioral question is:

> **Can information derived from one external source become behaviorally over-weighted after it is repeated or reused inside persistent memory?**

A secondary question asks whether explicit lineage metadata can mitigate that effect.

The project separates three kinds of claims:

- **behavioral observation** — what the model selected;
- **provenance judgment** — what the model explicitly classified as independent evidence;
- **mechanistic interpretation** — why the model behaved that way.

Behavioral resistance to counterevidence is not treated as proof that the model internally counts repeated records as independent sources.

## Current status

**Project disposition: PAUSED — instrument redesign path exhausted under v0.7.**

No v0.8 behavioral run is currently authorized or recommended. The next step is program-level scientific audit and preservation, not another model run.

| Version | Role | Status |
| --- | --- | --- |
| v0.2 | Early experimental instrument | Closed; measurement-limited |
| v0.3.1 | Calibration / discovery pilot | Completed; exploratory |
| v0.4.1 | First confirmatory attempt | **Aborted** — manipulation validity failure |
| v0.4.2 | Second confirmatory attempt | **Aborted before data collection** — provenance preflight failure |
| v0.4.3 | Behavioral-confirmatory study | **Completed and independently audited; H1 supported, H2 not supported** |
| v0.5.0 | Phi-4-mini-instruct cross-family qualification | **Invalid/inconclusive** — mandatory preflight failed |
| v0.5.1 | Exploratory response-interface diagnostic | **Completed; exploratory only** |
| v0.5.2 | Phi-4-mini-reasoning eligibility pilot | **Valid but INELIGIBLE** |
| v0.6 | Ministral staged Calibration → Eligibility → Confirmatory program | **CLOSED — CALIBRATION_FAILURE; STOP BEFORE ELIGIBILITY** |
| v0.7 | Ministral measurement-decoupling instrument redesign | **CLOSED — REDESIGN_FAILED_STOP; project PAUSED** |

See [`docs/experiment_history.md`](docs/experiment_history.md) for the full audit trail and [`docs/program_audit_v0_2_to_v0_7.md`](docs/program_audit_v0_2_to_v0_7.md) for the program-level scientific assessment.

## Only completed confirmatory IAER result: v0.4.3

v0.4.3 is the only version included in confirmatory IAER inference.

All **168/168** planned trajectories were valid and all four preregistered validity gates passed.

| Hypothesis | Retention | Paired RD | Holm-adjusted p | Verdict |
| --- | ---: | ---: | ---: | --- |
| H1: `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 0.6875 | 9.5367e-7 | **Supported** |
| H2: `active_plain > active_lineage` | 2/32 vs 0/32 | 0.0625 | 0.50 | **Not supported** |

The provenance audit was exact for 168/168 trajectories, but remained descriptive/exploratory as preregistered. It does not establish a confirmed provenance-use mechanism.

The strongest supported claim is therefore deliberately narrow:

> Under the frozen v0.4.3 task family and `qwen3.5-4b` configuration, five explicitly derivative reviews of one initial source substantially increased retention of the initial claim relative to an equal-sized unrelated-memory control.

The complete frozen materials and audit are in [`experiments/v0_4_3`](experiments/v0_4_3).

## Cross-family qualification after v0.4.3

### v0.5.0 — Phi-4-mini-instruct

The frozen cross-family package required a four-case behavioral validity preflight. Three cases passed; the mirrored `independent_evidence` case with INITIAL=`CLAIM_B` failed. Under the fail-closed rule, no confirmatory trajectories were collected.

Status: `INVALID/INCONCLUSIVE` for qualification, not evidence against IAER.

### v0.5.1 — exploratory diagnostic

All 48 planned diagnostic calls completed. Overall normative accuracy was 29/48 and varied substantially across response representations. Performance was much weaker on multiple-evidence integration than on the source-only condition.

Status: descriptive/exploratory only.

### v0.5.2 — Phi-4-mini-reasoning eligibility pilot

The pilot was publicly preregistered before behavioral collection. All 36 planned rows were valid.

| Condition | Correct | Requirement | Result |
| --- | ---: | ---: | --- |
| `baseline_initial` | 4/12 | at least 10/12 | FAIL |
| `counter_single_strong` | 12/12 | at least 10/12 | PASS |
| `independent_five_initial` | 2/12 | at least 10/12 | FAIL |

Decision: `INELIGIBLE`. No confirmatory IAER run followed.

Public records: [`experiments/v0_5_2_eligibility`](experiments/v0_5_2_eligibility) and the [v0.5.2 results release](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.5.2-results).

### v0.6 — Ministral calibration program

v0.6 introduced three strictly separated stages:

**Calibration → Eligibility → Confirmatory IAER**

Both prespecified Calibration interfaces were technically complete but failed the same evidence-integration control:

| Interface | `baseline_initial` | `counter_single_strong` | `independent_five_initial` | Decision |
| --- | ---: | ---: | ---: | --- |
| A | 8/8 | 8/8 | 0/8 | `INTERFACE_A_FAILED_BEHAVIORALLY` |
| B | 8/8 | 8/8 | 0/8 | `CALIBRATION_FAILURE` |

Final decision: **STOP BEFORE ELIGIBILITY**. No confirmatory IAER outcomes were collected.

A closure audit also documented that the original Freeze-A public tag omitted several calibration-specific implementation files that the publication checklist had intended to include. The original tag was not rewritten; the deviation remains visible in the repository.

See the [v0.6 results release](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.6-calibration-results).

## v0.7 — measurement-decoupling instrument redesign

v0.7 was designed to remove a major v0.6 confound: implicit Bayesian aggregation. Instead of reliability scores, the model was given an explicit rule to count **independent root sources** and assign zero new epistemic votes to records explicitly marked as derived from an existing root.

The complete v0.7 package was publicly preregistered, including the frozen ZIP asset and SHA-256, before behavioral collection.

All 48 planned calls were valid.

| Condition | Correct |
| --- | ---: |
| `two_initial_one_counter` | 12/12 |
| `one_initial_two_counter` | 11/12 |
| `derived_lure_initial_two_counter` | 7/12 |
| `three_initial_two_counter` | 12/12 |

Integrity P1 passed, but P2-P5 failed. The preregistered decision was:

> **REDESIGN_FAILED_STOP**

Across the three root-only conditions, the model was correct on 35/36 calls. In the derived-record lure condition, accuracy fell to 7/12; all five errors selected the INITIAL claim. This pattern is descriptive and potentially interesting, but v0.7 was explicitly **not** an IAER replication and cannot confirm, refute, or estimate IAER.

No rescue run is permitted under v0.7.

- [v0.7 preregistration release](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.7-instrument-preregistration)
- [v0.7 results release](https://github.com/ovidiuboticiu/intra-agent-evidence-recycling/releases/tag/v0.7-instrument-results)
- [`experiments/v0_7_instrument_redesign/V0_7_CLOSURE_REPORT.md`](experiments/v0_7_instrument_redesign/V0_7_CLOSURE_REPORT.md)

## Preprint and reproducibility archive

The citation-locked v0.4.3 manuscript is published as a public, non-peer-reviewed preprint:

> Boticiu, Ovidiu. (2026). *When One Source Returns: A Preregistered Behavioral Study of Intra-Agent Evidence Recycling* (Version 0.4) [Preprint]. Zenodo.

- Preprint DOI: [10.5281/zenodo.22282120](https://doi.org/10.5281/zenodo.22282120)
- v0.4.3 reproducibility archive: [10.5281/zenodo.22259801](https://doi.org/10.5281/zenodo.22259801)

Later v0.5-v0.7 qualification/redesign results do not alter the inferential status of that preprint.

## Experimental discipline

The project uses the following procedural principles:

- preregistration before confirmatory or qualification collection where applicable;
- fixed-N stopping;
- fail-closed execution for technical/schema/manipulation failures;
- fresh held-out stimuli after material redesigns;
- aborted and failed attempts are retained rather than deleted;
- raw results are not merged across incompatible versions;
- confirmatory thresholds are not changed after observing outcomes;
- behavioral observations, provenance judgments, and mechanistic interpretations remain distinct;
- model/task eligibility is separated from confirmatory inference;
- publication deviations are documented rather than retroactively hidden;
- a failed redesign gate is respected rather than tuned until it passes.

## Model and runtime scope

The v0.4.3 confirmatory inference is specific to `qwen3.5-4b`, LM Studio, thinking disabled, temperature 0, and the frozen fictional binary-claim task family. Its archive does not pin every runtime artifact detail, which is an acknowledged exact-replication limitation.

v0.5.x used Microsoft Phi-4-mini variants. v0.6 and v0.7 used Ministral-3-8B-Instruct-2512 GGUF Q4_K_M under a more tightly pinned local environment. Outcomes from qualification/calibration/redesign versions apply only to their exact frozen interfaces and configurations.

## Repository structure

```text
intra-agent-evidence-recycling/
├── README.md
├── CITATION.cff
├── LICENSE-CODE
├── LICENSE-DATA-DOCS.md
├── docs/
│   ├── experiment_history.md
│   └── program_audit_v0_2_to_v0_7.md
└── experiments/
    ├── v0_3_1/
    ├── v0_4_1_aborted/
    ├── v0_4_2_aborted/
    ├── v0_4_3/
    ├── v0_5_0/
    ├── v0_5_1_diagnostic/
    ├── v0_5_2_eligibility/
    ├── v0_6_ministral/
    └── v0_7_instrument_redesign/
```

## Current research disposition

**PAUSED.**

The v0.4.3 H1 effect remains a valid, configuration-specific confirmatory finding. Cross-family generalization remains unresolved because later model families did not reach a valid confirmatory IAER comparison.

The v0.7 stop rule has been reached. The project should not proceed directly to v0.8 by changing prompts or testing more models until one passes. A future restart requires a materially new measurement idea satisfying the restart criteria in [`docs/program_audit_v0_2_to_v0_7.md`](docs/program_audit_v0_2_to_v0_7.md).

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff).

Preferred manuscript citation:

> Boticiu, Ovidiu. (2026). *When One Source Returns: A Preregistered Behavioral Study of Intra-Agent Evidence Recycling* (Version 0.4) [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.22282120

Software and reproducibility archive:

> Boticiu, Ovidiu. (2026). *Intra-Agent Evidence Recycling v0.4.3 — Behavioral Confirmatory Study* (Version 0.4.3) [Software]. Zenodo. https://doi.org/10.5281/zenodo.22259801

## License

- Software code is licensed under the [MIT License](LICENSE-CODE).
- Original experimental data and documentation are licensed under [CC BY 4.0](LICENSE-DATA-DOCS.md).

Copyright © 2026 Ovidiu Boticiu.
