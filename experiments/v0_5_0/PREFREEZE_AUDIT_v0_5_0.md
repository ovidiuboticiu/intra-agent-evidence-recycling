# PREFREEZE AUDIT — IAER v0.5.0

Audit completed before behavioral preflight and confirmatory collection.

## Model and technical compatibility

- Exact model file SHA-256 recorded and embedded in the runner.
- LM Studio model identifier is explicit; auto-selection is prohibited because
  multiple models are exposed by the local server.
- Neutral structured-output smoke test: PASS.
- Smoke test used temperature 0, seed 42, strict JSON schema, one completion,
  no scientific manipulation, and no confirmatory item.
- Finish reason was `stop`; reasoning tokens were 0; no transport retry occurred.

## Design construction

- 32 unique item IDs.
- 32 unique fictional entity labels.
- 64 unique fictional claim-value labels.
- INITIAL balanced 16/16.
- presentation balanced 16/16.
- all four INITIAL × presentation cells contain exactly 8 items.
- 8 positive-control items, exactly 2 in each cell.
- exact expected keyset: 104 trajectories.
- expected confirmatory API calls: 208, plus 4 behavioral-preflight calls.

## Cross-version freshness audit

Exact entity and claim-value tokens were compared with the published stimulus
files from:

- `experiments/v0_3_1/stimuli_v0_3.csv`
- `experiments/v0_4_1_aborted/stimuli_v0_4.csv`
- `experiments/v0_4_2_aborted/stimuli_v0_4_2.csv`
- `experiments/v0_4_3/stimuli_v0_4_3.csv`

Result:

- entity-token overlap: 0;
- claim-value-token overlap: 0.

The published Git blob identifiers used for the first three comparisons were
`d8262be40953d570f7cd8a35d7e794d98ade48a5`,
`7974542c0b88fb9cb713bf9b0c73c5eb4973d9df`, and
`34e546e3210ef0dc74181d8534ba98daa75905e9`. The v0.4.3 stimulus SHA-256 was
`1fc82a4b8555445b54b6b2c7882531e75c21bc0565d1fe57b2a3cae0eee6736e`.

## Prompt and analysis audit

- The source_only, neutral_filler, passive_repeat, independent_evidence,
  counterevidence, belief-probe, and provenance-probe wording is retained from
  frozen v0.4.3.
- active_plain and active_lineage are prospectively omitted.
- H1-R is the only confirmatory hypothesis.
- The support rule fixes both RD >= +0.25 and two-sided exact paired McNemar
  p < 0.05.
- No Holm adjustment is used because the confirmatory family contains one test.
- The analysis refuses to compute scientific outcomes until all 104 exact
  planned keys are complete and valid.
- The runner prints no belief outcomes during confirmatory collection.
- Provenance remains explicitly descriptive/exploratory.

## Immutability boundary

Files listed in `FREEZE_MANIFEST_v0_5_0.sha256` become immutable when that
manifest is generated. Preflight, raw results, technical-failure rows, and
derived analysis reports are append-only or generated records and must never be
hand-edited.
