# IAER v0.4.3 — External Replication Report Template v1.0

> Use this template for a direct or independently implemented replication of the frozen v0.4.3 behavioral study. Delete instructional comments before publication only if the removed text is purely editorial; do not delete failed stages, deviations, or negative results.

## 1. Replication identity

- Replication ID:
- Replicator / team:
- Affiliation (optional):
- Contact:
- Date/time collection began (UTC):
- Date/time collection ended (UTC):
- Replication type:
  - [ ] Level A — analysis reproduction
  - [ ] Level B — direct behavioral replication
  - [ ] Level C — independent implementation replication
  - [ ] Level D — conceptual / cross-family study

## 2. Public pre-collection protocol

- Registration / frozen protocol URL:
- Public timestamp:
- Git commit/tag/release:
- Protocol SHA-256:
- Was the protocol public before the first behavioral call? Yes / No
- If no, explain:

## 3. Model and runtime environment

- Operating system:
- CPU:
- GPU:
- RAM:
- Runtime / LM Studio version:
- Model display name:
- Model artifact filename:
- Model artifact SHA-256:
- Quantization / precision:
- Context length:
- Thinking / reasoning setting:
- Temperature:
- Other sampling parameters:
- API base URL:

## 4. Frozen source material

- Repository commit/tag used:
- `run_experiment_v0_4_3.py` SHA-256:
- `analyze_v0_4_3.py` SHA-256:
- stimuli SHA-256:
- `FREEZE_MANIFEST_v0_4_3.sha256` verification result:
- Stimulus mode:
  - [ ] original frozen stimuli
  - [ ] fresh prospectively frozen isomorphic stimuli
- If fresh stimuli, provide generation rules and archive URL:

## 5. Planned analysis and decision rules

Confirm before collection:

- Planned N: 168 valid trajectories / other: ______
- H1: `passive_repeat > neutral_filler`
- H2: `active_plain > active_lineage`
- Paired RD threshold: >= +0.25
- Holm-adjusted exact paired McNemar threshold: p < 0.05
- Validity gates preserved from frozen protocol: Yes / No
- Planned exclusions:
- Retry policy:
- Timeout policy:
- Resume policy:

If any item differs from the frozen protocol, describe the deviation before reporting outcomes.

## 6. Mandatory preflight

- Preflight command or equivalent:
- Preflight started UTC:
- Preflight completed UTC:
- Cases passed: ___ / 8
- Terminal result:
  - [ ] `BEHAVIORAL_PREFLIGHT_OK`
  - [ ] failed
- Were any failed preflights rerun before proceeding? Yes / No
- If yes, explain and classify the replication accordingly:

### Preflight disposition

- [ ] PASS — target collection permitted
- [ ] INVALID/INCONCLUSIVE — PREFLIGHT FAILURE; target collection stopped

## 7. Collection integrity

- Planned valid trajectories:
- Completed valid trajectories:
- Invalid trajectories:
- Duplicate keys:
- Missing planned keys:
- Extra/unplanned keys:
- Technical failures:
- Calls with retry > 1:
- Reasoning/thinking content detected:
- Collection interrupted/resumed? Yes / No
- If resumed, describe:

## 8. Validity gates

Use the exact frozen definitions summarized in `EXTERNAL_REPLICATION_VALIDITY_GATES_v1_0.md`.

| Gate | Frozen requirement | Observed | Pass/Fail |
| --- | --- | --- | --- |
| V1 — source-only counter sensitivity | `source_only`: COUNTER on at least 24/32 items | | |
| V2 — independent-evidence positive control | `independent_evidence`: retain INITIAL on at least 6/8 items | | |
| V3 — active trace completeness | all 64 active trajectories contain all five valid application outputs | | |
| V4 — dataset completeness | all 168 planned item-condition keys present as valid trajectories | | |

Additional exact-key audit:

- Duplicate valid keys:
- Missing planned keys:
- Extra/unplanned keys:

Overall validity disposition:

- [ ] all gates pass
- [ ] one or more gates fail → target inference not permitted

## 9. Co-primary results

### H1 — `passive_repeat > neutral_filler`

- passive_repeat retained INITIAL: ___ / 32
- neutral_filler retained INITIAL: ___ / 32
- paired RD:
- discordant desired/opposite:
- exact two-sided McNemar p:
- Holm-adjusted p:
- Frozen-rule verdict:
  - [ ] supported
  - [ ] not supported

### H2 — `active_plain > active_lineage`

- active_plain retained INITIAL: ___ / 32
- active_lineage retained INITIAL: ___ / 32
- paired RD:
- discordant desired/opposite:
- exact two-sided McNemar p:
- Holm-adjusted p:
- Frozen-rule verdict:
  - [ ] supported
  - [ ] not supported

## 10. Secondary/descriptive results

- Provenance exactness:
- Confidence summaries:
- Presentation-order summaries:
- INITIAL-label summaries:
- Other registered secondary analyses:
- Post-hoc analyses clearly marked as such:

Do not convert post-hoc subgroup analyses into confirmatory claims.

## 11. Deviations from registered plan

List every deviation, including apparently harmless ones.

| Deviation | When discovered | Outcome-sensitive? | Consequence |
| --- | --- | --- | --- |
| | | | |

If none: `No deviations recorded.`

## 12. Final replication classification

Choose exactly one primary classification:

- [ ] `REPLICATION_SUPPORTED`
- [ ] `VALID_NON_REPLICATION`
- [ ] `INVALID/INCONCLUSIVE`
- [ ] `CONFIGURATION_INELIGIBLE` (cross-family qualification only)

Rationale:

## 13. Interpretation boundary

### What this replication supports

Write a narrow behavioral statement tied to the tested configuration.

### What this replication does not establish

At minimum address:

- literal independent-source counting mechanism;
- generalization across model families;
- isolation from lexical repetition / salience / prompt length;
- any untested runtime or artifact equivalence.

## 14. Files and persistent archive

- Raw results filename:
- Raw results SHA-256:
- Environment capture filename/hash:
- Analysis output filename/hash:
- Replication report filename/hash:
- Archive/DOI URL:
- Repository URL:

## 15. Related IAER records

- Original empirical preprint: `10.5281/zenodo.22282120`
- Original software/reproducibility archive: `10.5281/zenodo.22259801`
- Methodological note: `10.5281/zenodo.22306245`
- Forensic clarification: `docs/V0_4_3_FORENSIC_VALIDATION_ADDENDUM_v1_0.md`

## 16. Declaration

> We report this replication according to the prospectively frozen protocol identified above. We have preserved failed or invalid stages, disclosed deviations, and separated behavioral findings from mechanistic interpretation.

Name / team:

Date:
