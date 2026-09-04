# IAER v0.4.3 — External Replication Guide v1.0

**Purpose:** enable independent researchers to reproduce or replicate the preserved v0.4.3 behavioral result without changing the frozen historical experiment.

**Scope:** IAER v0.4.3 only.  
**New IAER generation:** no.  
**Status of original project:** PAUSED after v0.7.  
**Primary empirical DOI:** `10.5281/zenodo.22282120`  
**Software/reproducibility DOI:** `10.5281/zenodo.22259801`  
**Methodological-note DOI:** `10.5281/zenodo.22306245`

---

## 1. Scientific target

The narrow v0.4.3 behavioral target is:

> Under the frozen v0.4.3 task family and Qwen configuration, five explicitly derivative, target-consistent reviews of one initial source substantially increased retention of the initial claim relative to an equal-count control containing five unrelated memory records.

The original co-primary results were:

- H1 `passive_repeat > neutral_filler`: 22/32 vs 0/32; paired RD 0.6875; Holm-adjusted exact McNemar p = 9.5367432e-7; supported.
- H2 `active_plain > active_lineage`: 2/32 vs 0/32; paired RD 0.0625; Holm-adjusted p = 0.50; not supported.

The replication target is behavioral. The original study does **not** establish that the model literally counted derivative records as independent sources.

---

## 2. What counts as reproduction versus replication

### Level A — analysis reproduction

No model calls are made.

The researcher independently verifies the archived raw data and reruns the frozen analysis:

```bash
python analyze_v0_4_3.py results_v0_4_3.jsonl
```

This tests whether the published numerical result follows from the archived raw data and analysis specification.

### Level B — direct behavioral replication

The researcher reruns the frozen v0.4.3 task, runner, stimuli, prompt logic, condition definitions, and decision rules on a Qwen configuration intended to match the original as closely as possible.

Because the original archive does not pin every model-artifact/runtime detail, this should normally be called a **direct configuration replication**, not a bit-for-bit computational replication.

### Level C — independent implementation replication

The researcher independently reimplements the frozen v0.4.3 design from the protocol rather than reusing the original runner, while preserving:

- the same conditions;
- the same sample sizes;
- the same validity gates;
- the same H1/H2 decision rules;
- the same behavioral outcome definition;
- the same no-rescue/no-threshold-change discipline.

This is stronger evidence against a shared-code implementation artifact.

### Level D — conceptual or cross-family replication

A materially different model family, prompt interface, task family, or redesigned manipulation is **not** a direct v0.4.3 replication.

For another model family, the IAER methodological note recommends qualification of the measurement instrument before target collection. Qualification failure must not be reported as a negative replication of IAER.

---

## 3. Frozen materials to preserve

The historical files under `experiments/v0_4_3/` are frozen and must not be edited for a direct replication.

Key files:

- `PREREGISTRATION_v0_4_3.md`
- `run_experiment_v0_4_3.py`
- `analyze_v0_4_3.py`
- `stimuli_v0_4_3.csv`
- `README_v0_4_3.md`
- `FREEZE_MANIFEST_v0_4_3.sha256`
- `RELEASE_MANIFEST_v0_4_3.sha256`
- `results_v0_4_3.jsonl` — original results; do not mix with replication results

The later forensic clarification is:

- `docs/V0_4_3_FORENSIC_VALIDATION_ADDENDUM_v1_0.md`

A replication should write results to a **new directory and new filenames**.

---

## 4. Public timestamp before collection

A new external replication should use a stronger prospectivity standard than the historical v0.4.3 documentation.

Before the first behavioral model call, publicly timestamp at minimum:

1. replication type: Level B or Level C;
2. exact model/configuration;
3. runtime and software versions;
4. model artifact filename and SHA-256 where available;
5. quantization / precision;
6. thinking/reasoning setting;
7. temperature and other sampling parameters;
8. frozen stimuli decision: original stimuli or prospectively frozen fresh isomorphic stimuli;
9. sample size;
10. validity gates;
11. H1/H2 decision rules;
12. retry/timeout/resume rules;
13. planned exclusions;
14. output filenames and analysis script hash.

Acceptable public timestamp mechanisms include an immutable Zenodo/OSF record or a public GitHub release/tag created before collection.

Do not change thresholds, prompts, stimuli, retry rules, or model choice after observing target outcomes within the same registered replication.

---

## 5. Environment capture

Before collection, record at minimum:

```text
replication_id
replication_type
replicator_name_or_team
collection_date_utc
operating_system
hardware_cpu
hardware_gpu_if_any
ram
lm_studio_version_or_runtime
model_display_name
model_artifact_filename
model_artifact_sha256_if_available
quantization_or_precision
context_length
thinking_or_reasoning_setting
temperature
other_sampling_parameters
api_base_url
runner_sha256
analysis_sha256
stimuli_sha256
protocol_or_preregistration_url
```

If an exact model-artifact hash cannot be obtained, state that limitation explicitly.

---

## 6. Same-configuration direct replication procedure

### 6.1 Prepare an isolated replication directory

Do not write into the frozen original result file.

Recommended structure:

```text
replications/
└── external_<team>_<date>/
    ├── REPLICATION_PROTOCOL.md
    ├── MODEL_ENVIRONMENT_CAPTURE.json
    ├── results_external_v0_4_3.jsonl
    ├── analysis_external.txt
    ├── REPLICATION_REPORT.md
    └── SHA256SUMS.txt
```

### 6.2 Verify frozen source files

Before collection, verify the available v0.4.3 manifests.

On systems with `sha256sum`:

```bash
cd experiments/v0_4_3
sha256sum -c FREEZE_MANIFEST_v0_4_3.sha256
```

Record the verification result.

### 6.3 Configure the original task environment

The historical runner instructions specify:

- model label: `qwen3.5-4b`;
- LM Studio OpenAI-compatible local server;
- port `1234`;
- Enable Thinking = OFF;
- temperature = 0;
- Windows laptop plugged in and sleep/hibernate disabled during the run.

A replicator may use another operating system if the deviation is declared. Do not call such a run bit-for-bit identical.

### 6.4 Mandatory behavioral preflight

Original command:

```bash
python run_experiment_v0_4_3.py --base-url http://localhost:1234/v1 --model auto --temperature 0 --preflight-only
```

Required historical terminal outcome:

```text
BEHAVIORAL_PREFLIGHT_OK
```

The preflight has 8 cases covering source-only, independent-evidence, active-plain, and active-lineage mirrored across INITIAL=A/B.

All 8 must pass in one preflight run.

**STOP rule:** if the preflight fails, do not repeatedly rerun it until it passes and do not proceed to target collection under the same registered replication. Report the attempt as `INVALID/INCONCLUSIVE — PREFLIGHT FAILURE`.

### 6.5 Confirmatory collection

Historical command:

```bash
python run_experiment_v0_4_3.py --base-url http://localhost:1234/v1 --model auto --temperature 0
```

The original runner writes `results_v0_4_3.jsonl`. For external replication, use an isolated copy or wrapper so the output is written under a new replication-specific filename and cannot overwrite the historical file.

Planned total:

```text
168 valid trajectories
```

The historical runner is resumable using the same command and does not print scientific outcomes during collection.

### 6.6 Analysis

Run the frozen analysis logic on the replication result file, or an independently implemented equivalent analysis registered before outcome inspection.

The original co-primary decision rules are:

- H1: `passive_repeat > neutral_filler`
- H2: `active_plain > active_lineage`

For each hypothesis:

- paired RD must be at least +0.25;
- Holm-adjusted exact paired McNemar p must be < 0.05.

All validity gates must pass before the H1/H2 result is interpreted.

---

## 7. Replication outcome taxonomy

Use the following terminology.

### `REPLICATION_SUPPORTED`

Use only if:

- integrity and validity gates pass;
- the target comparison is fully collected;
- the frozen H1 rule is met.

Report the observed effect size and exact p-value; do not report only the categorical label.

### `VALID_NON_REPLICATION`

Use only if:

- integrity and validity gates pass;
- the target comparison is fully collected;
- the frozen H1 rule is not met.

This is interpretable evidence against replication under the exact tested configuration. It is not automatically evidence against IAER in every model or task family.

### `INVALID/INCONCLUSIVE`

Use when a mandatory integrity, preflight, schema, completeness, manipulation, or validity requirement fails.

Do **not** convert this category into a negative replication.

### `CONFIGURATION_INELIGIBLE`

Use for a prospective cross-family qualification program in which the model/interface technically runs but fails frozen prerequisite behavioral gates before target IAER collection.

This category is neither support nor evidence against the target effect.

---

## 8. Required report contents

Every external replication report should include:

1. replicator/team identity or declared pseudonymous identity;
2. public pre-collection protocol URL and timestamp;
3. exact code commit/tag used;
4. all relevant SHA-256 hashes;
5. model artifact and runtime details;
6. preflight outcome;
7. planned versus completed trajectory counts;
8. missing/duplicate/extra key audit;
9. H1 and H2 pair counts;
10. paired risk differences;
11. exact McNemar p-values;
12. Holm-adjusted p-values;
13. validity-gate outcomes;
14. deviations from the registered plan;
15. technical failures/retries;
16. final classification from Section 7;
17. explicit separation of behavioral result from mechanistic interpretation.

Use `docs/EXTERNAL_REPLICATION_REPORT_TEMPLATE_v1_0.md` for a standardized report.

---

## 9. Blinding and independence

Because the original result is public, a fully outcome-blind replication is no longer generally possible.

Researchers should nevertheless reduce discretionary bias by:

- freezing the protocol before collection;
- avoiding adaptive prompt/model changes after target outcomes begin;
- using deterministic scripts for scoring;
- preserving all failed attempts;
- publishing raw trajectory-level data;
- separating collection from interpretation where possible;
- using an independently written analysis script as an additional audit when feasible.

Contact with the original author is acceptable for technical clarification, but outcome-sensitive design decisions should be resolved prospectively and publicly documented.

---

## 10. Original-stimulus versus fresh-stimulus replication

### Original frozen stimuli

Advantages:

- closest direct comparison to v0.4.3;
- minimizes item-set differences.

Limitation:

- tests the same item family and therefore does not establish stimulus generalization.

### Fresh isomorphic stimuli

Advantages:

- tests whether the effect survives a new item set;
- reduces dependence on idiosyncratic original items.

Requirements:

- stimulus-generation rules must be frozen before target outcomes;
- balance constraints must match the intended original design;
- the fresh stimuli must not be tuned after seeing target results;
- this should be reported as a fresh-stimulus replication rather than exact item replication.

For maximum evidential value, a replication program can preregister both original-stimulus and fresh-stimulus phases while keeping their inferences separate.

---

## 11. Important known limitations inherited from v0.4.3

A faithful replication inherits the original design limitations:

- derivative multiplicity is not isolated from lexical repetition;
- passive repetition also increases target-consistent salience;
- final prompt length differs between `passive_repeat` and `neutral_filler`;
- presentation order may moderate magnitude;
- exact external runtime/model artifact was not fully pinned in the historical study.

A direct replication can test whether the **behavioral contrast** reproduces. It cannot, by itself, resolve these mechanism-level confounds.

A future mechanism experiment should be a separately registered new design, not a rescue modification of this replication.

---

## 12. Recommended publication policy for replications

Publish all integrity-valid attempts, including valid non-replications.

At minimum preserve:

- protocol/pre-registration;
- environment capture;
- code/version hashes;
- raw results;
- analysis output;
- deviations;
- final report.

If possible, assign a persistent identifier such as a Zenodo DOI and link the replication to:

- `10.5281/zenodo.22282120` — original empirical preprint;
- `10.5281/zenodo.22259801` — original software/reproducibility archive;
- `10.5281/zenodo.22306245` — methodological note.

---

## 13. Interpretation boundary

A successful direct replication would strengthen confidence that the v0.4.3 behavioral contrast is reproducible under a closely matched configuration.

A valid non-replication would materially reduce confidence in configuration-level reproducibility and would be scientifically important.

An invalid preflight, calibration failure, or configuration-ineligibility result does not adjudicate the target effect.

No replication outcome should be interpreted as proof of an internal source-counting mechanism without a design that prospectively separates derivative dependence from repetition, salience, order, and prompt-length effects.
