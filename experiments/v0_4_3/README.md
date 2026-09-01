# Intra-Agent Evidence Recycling — v0.4.3

Behavioral-confirmatory fixed-N study of whether an agent reuses derivative memory records as if they add evidential weight, and whether explicit lineage metadata mitigates that behavior.

## Final status

All 168 planned trajectories are present and valid. All four preregistered validity gates pass.

| Test | Retention | Paired RD | Exact McNemar p | Holm p | Preregistered verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| H1: `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 0.6875 | 4.7683716e-7 | 9.5367432e-7 | Supported |
| H2: `active_plain > active_lineage` | 2/32 vs 0/32 | 0.0625 | 0.50 | 0.50 | Not supported |

H1 supports a behavioral memory-source multiplication effect in this task family and configuration. H2 does not confirm the preregistered medium-to-large lineage-mitigation effect. Full two-effect confirmation was not achieved.

The provenance audit was exact for 168/168 trajectories. As preregistered, this result is descriptive/exploratory only and cannot establish a confirmed provenance-use mechanism.

## Reproduce the frozen analysis

Requires Python 3 and only the standard library.

```bash
python analyze_v0_4_3.py results_v0_4_3.jsonl
```

Verify the pre-collection freeze:

```bash
sha256sum -c FREEZE_MANIFEST_v0_4_3.sha256
```

Verify the complete release, including raw results and audit additions:

```bash
sha256sum -c RELEASE_MANIFEST_v0_4_3.sha256
```

## Repository map

- `PREREGISTRATION_v0_4_3.md` — frozen hypotheses, thresholds, gates, and scope.
- `run_experiment_v0_4_3.py` — frozen collection runner.
- `analyze_v0_4_3.py` — frozen preregistered analysis.
- `stimuli_v0_4_3.csv` — 32 fictional balanced items.
- `results_v0_4_3.jsonl` — raw trajectory-level results.
- `FREEZE_MANIFEST_v0_4_3.sha256` — original pre-collection manifest; preserved unchanged.
- `AUDIT_REPORT_v0_4_3.md` — final independent file, data, and analysis audit.
- `RELEASE_MANIFEST_v0_4_3.sha256` — complete post-collection release manifest.
- `README_v0_4_3.md` — original frozen run instructions; preserved unchanged.

## Scope

The confirmatory inference is limited to `qwen3.5-4b`, LM Studio, thinking disabled, temperature 0, and the frozen fictional binary-claim task family. Generalization requires independent replication across models, runtimes, prompts, and task families.

No license is included in this archive. Repository publication is possible without one, but reuse permissions remain unspecified until the owner selects a license.
