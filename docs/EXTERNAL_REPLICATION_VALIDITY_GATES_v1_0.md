# IAER v0.4.3 — Exact Validity Gates for External Replication

These gates are copied from the frozen v0.4.3 decision structure and should be frozen prospectively in a faithful direct replication.

## V1 — source-only counter sensitivity

Condition: `source_only`

Requirement:

> COUNTER must be chosen on at least 24 of 32 items.

Interpretation: the candidate configuration must demonstrate that one stronger independent counter-source can overturn the initial source often enough for the later IAER contrast to be interpretable.

Original v0.4.3 observed value: 32/32.

## V2 — independent-evidence positive control

Condition: `independent_evidence`

Requirement:

> INITIAL must be retained on at least 6 of 8 positive-control items.

Interpretation: multiple genuinely independent INITIAL-supporting sources must collectively be capable of outweighing the later counter-source.

Original v0.4.3 observed value: 7/8.

## V3 — active-application trace completeness

Conditions: `active_plain` and `active_lineage`

Requirement:

> Every active trajectory must contain all five valid application outputs.

Planned active trajectories: 64.

Original v0.4.3 observed value: 64/64 complete.

## V4 — dataset completeness / valid planned keys

Requirement:

> All 168 planned item-condition keys must be present as valid trajectories.

For external audit, also report:

- duplicate valid keys;
- missing planned keys;
- extra/unplanned keys.

Original v0.4.3 observed value: 168/168 planned valid keys, with no missing, duplicate, or extra keys in the later forensic reconstruction.

## Interpretation rule

All mandatory validity gates must pass before H1/H2 are interpreted as a valid replication or valid non-replication.

If any gate fails, the target outcome should be classified as `INVALID/INCONCLUSIVE` under the registered direct-replication protocol. For a separately designed cross-family qualification program, use the prospectively frozen qualification taxonomy instead.

## Co-primary thresholds after gate passage

H1: `passive_repeat > neutral_filler`  
H2: `active_plain > active_lineage`

For each:

- paired risk difference >= +0.25; and
- Holm-adjusted exact paired McNemar p < 0.05.

The numerical effect sizes and p-values must always be reported even when the categorical decision threshold is not met.
