# Final Audit Report — Intra-Agent Evidence Recycling v0.4.3

Audit date: 2026-09-01 UTC  
Audit mode: read-only inspection and independent recomputation  
Raw-data policy: no retrospective modification of frozen code, preregistration, stimuli, or raw results

## Verdict

The v0.4.3 dataset is complete and valid under the preregistered gates. The frozen analysis reproduces successfully. H1 is supported; H2 is not supported. The joint two-effect confirmation criterion is not achieved.

No critical or major integrity discrepancy was found.

## File integrity

- The supplied archive contains one project directory and ten files, with no symlinks or path-traversal entries.
- The original `FREEZE_MANIFEST_v0_4_3.sha256` verifies all eight files that it lists.
- That original manifest is a pre-collection freeze: it intentionally does not hash the later raw-results file.
- The raw dataset SHA-256 is `5af33c11104bdd18dce9e945d5f2fce885f93c6cb1322f9b2f2469c38082cc54`.
- Every result row embeds preregistration, stimuli, and rationale hashes matching the frozen files.
- The GitHub-ready release preserves every supplied file byte-for-byte and adds a separate post-collection release manifest.

## Dataset audit

| Check | Result |
| --- | --- |
| JSONL rows | 168 |
| Valid rows | 168 |
| Technical-failure rows | 0 |
| Duplicate valid keys | 0 |
| Missing planned keys | 0 |
| Extra unplanned keys | 0 |
| Core conditions | 32 rows each |
| Positive control | 8 prespecified rows |
| Active trajectories | 64/64 with exactly five valid application outputs |
| Provenance score recomputation | 168/168 exact; no stored-score mismatch |
| Retention recomputation | 168/168 consistent with final belief choice |

The 32 stimuli are balanced as frozen: 16 `CLAIM_A` and 16 `CLAIM_B` initial claims; 16 `A_FIRST` and 16 `B_FIRST` presentations. Each core condition inherits the same balance.

## Collection-trace audit

- Model label: `qwen3.5-4b` in all 168 rows.
- Temperature: `0.0` in all rows.
- Timeout: `240` seconds in all rows.
- Python version recorded: `3.14.6` in all rows.
- Collection interval: 2026-09-01 16:38:45 to 19:39:51 UTC.
- The row order exactly matches the runner's deterministic seeded item-and-condition schedule.
- All 656 recorded model calls have `transport_attempts=1`, `finish_reason=stop`, and `reasoning_present=false`.
- Recorded call usage totals 216,903 prompt tokens, 15,998 completion tokens, and 232,901 tokens overall.
- Summed trajectory duration is 10,991.338 seconds; timestamps and durations form one continuous sequence apart from approximately 0.358 seconds of total inter-row write overhead.

These checks support internal consistency with the frozen runner. They are not a cryptographic attestation of the external runtime.

## Preregistered validity gates

| Gate | Requirement | Observed | Verdict |
| --- | --- | ---: | --- |
| V1 | `source_only` selects COUNTER on at least 24/32 | 32/32 | Pass |
| V2 | `independent_evidence` retains INITIAL on at least 6/8 | 7/8 | Pass |
| V3 | All 64 active trajectories contain five application outputs | 64/64 | Pass |
| V4 | All 168 planned keys have valid final records | 168/168 | Pass |

## Co-primary confirmatory analysis

The frozen script uses paired risk differences, two-sided exact paired McNemar tests, and Holm adjustment across the two co-primary p-values. Independent recomputation agrees exactly.

| Hypothesis | Marginal retention | Discordant pairs desired/opposite | RD | Bootstrap 95% CI | Raw p | Holm p | Thresholds met? |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| H1 `passive_repeat > neutral_filler` | 22/32 vs 0/32 | 22/0 | 0.6875 | [0.53125, 0.84375] | 4.7683716e-7 | 9.5367432e-7 | Yes |
| H2 `active_plain > active_lineage` | 2/32 vs 0/32 | 2/0 | 0.0625 | [0.0, 0.15625] | 0.50 | 0.50 | No |

Preregistered decision rules require both RD at least +0.25 and Holm-adjusted p below 0.05. Therefore:

- H1: supported.
- H2: not supported.
- Joint status: full two-effect confirmation not achieved.

## Descriptive results

| Condition | Retain INITIAL | Mean implied support for INITIAL |
| --- | ---: | ---: |
| `source_only` | 0/32 (0.0%) | 20.1 |
| `neutral_filler` | 0/32 (0.0%) | 15.5 |
| `passive_repeat` | 22/32 (68.8%) | 63.6 |
| `active_plain` | 2/32 (6.2%) | 21.4 |
| `active_lineage` | 0/32 (0.0%) | 15.0 |
| `independent_evidence` | 7/8 (87.5%) | 84.7 |

The provenance audit identifies the correct independent external evidence set in 168/168 trajectories, with zero false IDs and zero missed roots. Per the preregistration, this remains secondary/descriptive and does not rescue H2 or prove an internal provenance-use gap.

## Limitations and noncritical audit notes

1. The eight mandatory behavioral preflight outputs were printed by the runner but were not archived as a separate log. The runner structurally performs and passes preflight before collection; however, the exact preflight responses cannot be independently re-inspected from this folder.
2. Exact non-reuse of stimuli from v0.4.1 and v0.4.2 cannot be independently verified without those earlier stimulus sets. The v0.4.3 package itself is internally unique and balanced.
3. The model label is recorded, but the package does not pin the precise model artifact hash, quantization, LM Studio version, or runtime build. Exact computational replication therefore requires additional environment metadata.
4. The frozen V4 implementation checks total unique valid keys, duplicates, and unresolved failures but does not itself compare the observed key set to a constructed expected key set. The final audit performed that stricter comparison and found an exact 168/168 match, so this robustness gap does not affect the present verdict.
5. The directional wording of H1/H2 does not specify one- versus two-sided McNemar testing in prose. The frozen pre-collection analysis script resolves the ambiguity by implementing the more conservative two-sided exact test.

## Claims supported by this release

Supported: under this frozen task family and configuration, repeating five explicitly derivative reviews of one initial source substantially increased retention of the initial claim relative to five unrelated filler records.

Not supported: this study did not confirm a medium-to-large reduction in retention from adding explicit lineage metadata to self-generated application traces.

Not established: a general mechanism across models, a confirmed internal provenance-use gap, or effectiveness of lineage metadata outside this exact manipulation and task family.
