# v0.4.1 — Aborted Confirmatory Attempt

**Scientific status:** ABORTED  
**Reason:** Manipulation validity failure  
**Confirmatory inference:** **Not permitted**  
**Model:** `qwen3.5-4b` via LM Studio  
**Temperature:** `0`  
**Thinking / reasoning mode:** OFF

This folder preserves the exact files and partial raw results from the first confirmatory attempt in the Intra-Agent Evidence Recycling v0.4 family.

## Confirmatory intent

v0.4.1 was designed as a held-out confirmatory replication after the exploratory v0.3.1 pilot.

It froze two co-primary behavioral hypotheses:

- **H1:** `passive_repeat > neutral_filler`
- **H2:** `active_plain > active_lineage`

Each required both:

- paired risk difference ≥ +0.25;
- Holm-adjusted exact paired McNemar p < 0.05.

The planned fixed sample was 168 valid trajectories.

## Preflight amendment

The initial v0.4 preflight failed before any experimental trajectory was collected because the simplified behavioral preflight was not task-isomorphic to the actual experimental functions.

Before confirmatory data collection, v0.4.1 amended only the preflight implementation:

- hypotheses unchanged;
- stimuli unchanged;
- N unchanged;
- q=.80 unchanged;
- statistical thresholds unchanged;
- validity gates unchanged.

The amended seven-case task-isomorphic preflight passed.

## Abort event

The confirmatory run then produced:

- **7 valid trajectories**
- **1 manipulation-failure audit row**
- **8 total JSONL rows**

The stopping event was:

```text
item = C16
condition = active_lineage
operation = O2
expected = CLAIM_B
got = CLAIM_A
```

The frozen preregistration required all five active-use operations to select INITIAL.

A valid response selecting COUNTER during an active operation was explicitly defined as a `MANIPULATION_FAILURE`, not a transport error, and the study had to stop fail-closed.

Therefore:

> **v0.4.1 is an aborted confirmatory attempt and its partial observations must not be used to test H1 or H2.**

## Partial dataset contents

The seven valid trajectories are:

| Item | Condition | retain_initial | provenance exact |
|---|---|---:|---|
| C02 | source_only | 0 | yes |
| C02 | neutral_filler | 0 | yes |
| C02 | active_plain | 0 | yes |
| C02 | independent_evidence | 1 | yes |
| C02 | passive_repeat | 1 | yes |
| C02 | active_lineage | 0 | yes |
| C16 | source_only | 0 | yes |

These values are recorded here only for audit completeness. They are **not** a confirmatory result.

## Technical integrity of the valid portion

Independent archival audit found:

- 7 valid rows;
- 1 `manipulation_failure` row;
- all valid rows use `qwen3.5-4b`;
- all valid rows use temperature `0`;
- all 7 valid provenance outputs are exact;
- **24 recorded model-call diagnostics** in valid rows;
- all 24 diagnostics have `reasoning_present=false`;
- all 24 diagnostics used `transport_attempts=1`;
- the embedded preregistration, stimuli, and rationale hashes in all valid rows match the supplied frozen files.

Raw partial-result SHA-256:

```text
6fbeb98b454a934747d5660af4e9c92e5a9a1c7612a2703179644665ace53930  results_v0_4.jsonl
```

## Known code issue retained for historical accuracy

The archived runner still contains three instances of:

```python
"strict": "true"
```

instead of the standards-correct boolean:

```python
"strict": True
```

This bug was discovered later and repaired in subsequent versions.

It is **not repaired here**, because this folder preserves the code actually used in v0.4.1.

There is no evidence that this type/compliance bug caused the C16 manipulation failure: the failure was a structurally valid `CLAIM_A` response where the frozen manipulation required `CLAIM_B`.

## Why v0.4.1 was not resumed

Rerunning C16 until the desired active-operation response appeared would have violated the frozen manipulation rule and introduced outcome-dependent selection.

The aborted attempt was therefore closed rather than "repaired" in place.

Its design failure motivated a new active-use manipulation in v0.4.2.

## Files added for GitHub archival documentation

The original supplied files are preserved byte-for-byte.

Only these archival documents are added:

- `README.md`
- `AUDIT_REPORT.md`
- `ABORT_NOTE.md`
- `POSTRUN_AUDIT_SHA256.txt`
