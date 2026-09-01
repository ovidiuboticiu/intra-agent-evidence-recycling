# v0.3.1 — Calibration / Discovery Pilot

**Scientific status:** Completed calibration pilot  
**Confirmatory status:** Exploratory only — not confirmatory evidence  
**Model:** `qwen3.5-4b` via LM Studio  
**Temperature:** `0`  
**Thinking / reasoning mode:** OFF

This folder preserves the exact v0.3.1 experimental package and raw result file used in the calibration/discovery stage of the Intra-Agent Evidence Recycling project.

## Why v0.3.1 existed

v0.2 had substantial measurement limitations. v0.3 therefore redesigned the instrument rather than treating the earlier null result as a decisive test of the broader hypothesis.

The main repairs were:

- explicit `CLAIM_A` / `CLAIM_B` labels instead of ambiguous old/new terminology;
- concrete record-ID provenance auditing;
- a `source_only` baseline;
- graded counterevidence at `q = 0.55`, `0.68`, and `0.80`;
- a semantic provenance preflight;
- explicit designation as a calibration pilot.

The first v0.3 execution failed before any valid trajectory was collected because a free-text structured-output field was truncated. The technical amendment `TECHNICAL_AMENDMENT_v0_3_1.md` removed unused free-text fields before scientific data collection. No hypothesis, stimulus, condition, calibration gate, or stopping rule was changed.

## Dataset integrity

Independent post-run audit of `results_v0_3_1.jsonl` found:

- **48 / 48 valid trajectories**
- **48 / 48 unique item-condition keys**
- no missing planned item-condition keys
- no duplicate valid keys
- 8 items × 6 conditions
- all 24 active-condition trajectories contain five completed operation-call diagnostics
- all recorded **312 model-call diagnostics** have `reasoning_present = false`
- all result rows use `qwen3.5-4b`
- all result rows use `temperature = 0`
- no failure records are present in the final v0.3.1 result file

Raw results SHA-256:

```text
c5fe7f0b645d8997488dc6bedaec305409ccc0b970a3187d98ada940f1d296de  results_v0_3_1.jsonl
```

## Calibration results

### Selection of CLAIM_A

| Condition | q=.55 | q=.68 | q=.80 |
|---|---:|---:|---:|
| source_only | 7/8 | 2/8 | 0/8 |
| passive_repeat | 8/8 | 8/8 | 8/8 |
| active_plain | 8/8 | 8/8 | 8/8 |
| active_self_labeled | 8/8 | 8/8 | 7/8 |
| active_lineage | 8/8 | 8/8 | 0/8 |
| independent_evidence | 8/8 | 8/8 | 8/8 |

### Provenance exactness

| Condition | Exact | False independent IDs | Missed roots |
|---|---:|---:|---:|
| source_only | 8/8 | 0 | 0 |
| passive_repeat | 8/8 | 0 | 0 |
| active_plain | 8/8 | 0 | 0 |
| active_self_labeled | 8/8 | 0 | 0 |
| active_lineage | 6/8 | 0 | 2 |
| independent_evidence | 8/8 | 0 | 0 |

All four preregistered calibration gates passed. This made the instrument eligible for development of a later confirmatory study.

## Interpretation boundary

The striking v0.3.1 condition differences are **exploratory findings**. They must not be presented as confirmatory evidence because v0.3.1 was explicitly preregistered as a measurement-calibration pilot.

In particular:

- `passive_repeat` and `active_plain` both retained CLAIM_A at 8/8 items under q=.80;
- `active_lineage` retained CLAIM_A at 0/8 under q=.80;
- this motivated later confirmatory hypotheses, but does not itself confirm them.

## Known code issue retained for historical accuracy

The original runner uses:

```python
"strict": "true"
```

instead of the JSON/Python boolean:

```python
"strict": True
```

in three structured-output schema helpers.

This is a real type/compliance bug. It is **not repaired in this archived folder**, because the repository must preserve the code actually used.

The v0.3.1 raw outputs were nevertheless successfully parsed and matched the bounded fields used in the analysis. Therefore the bug is documented as a portability/compliance issue; there is no evidence in this dataset that it corrupted the recorded scientific fields.

See `AUDIT_REPORT.md`.

## Files

Original experimental files are preserved with their original filenames.

The additional files created only for repository documentation are:

- `README.md`
- `AUDIT_REPORT.md`
- `POSTRUN_AUDIT_SHA256.txt`

These additions do not modify the frozen experimental files or raw results.
