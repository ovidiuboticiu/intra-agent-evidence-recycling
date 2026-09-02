# IAER v0.5.1 diagnostic

This is a frozen **exploratory diagnostic**, not a confirmatory replication.
It follows the preregistered failure of the v0.5.0 behavioral preflight and
does not alter, rerun, or rescue v0.5.0.

## Question

Why did Microsoft Phi-4-mini-instruct fail the mirrored positive-control case
with `INITIAL=CLAIM_B`?

The diagnostic separates three candidate explanations:

1. response-label asymmetry (`CLAIM_A` versus `CLAIM_B`);
2. difficulty integrating multiple probabilistic sources;
3. a broader instability not isolated by either manipulation.

## Design

- 8 new fictional items;
- balanced INITIAL label and claim presentation order;
- 2 evidence conditions per item;
- 3 response/instruction modes per condition;
- 48 total model calls;
- no provenance calls;
- temperature 0 and seed 42;
- results are descriptive/exploratory only.

## Run order

Keep LM Studio running with `microsoft_phi-4-mini-instruct` loaded.

1. Run `00_VERIFY_DIAGNOSTIC_PACKAGE.bat`.
2. Run `01_RUN_EXPLORATORY_DIAGNOSTIC.bat` once.
3. Run `02_ANALYZE_EXPLORATORY_DIAGNOSTIC.bat` only after collection reports
   48 valid rows.

The collection runner prints progress but not decisions. It writes
`diagnostic_results_v0_5_1.jsonl`. The analyzer writes
`diagnostic_report_v0_5_1.txt`.

## Integrity and stopping

Frozen inputs are listed in `FREEZE_MANIFEST_v0_5_1.sha256`. The runner stops
fail-closed on a technical or schema failure. A completed valid decision is
never rerun. Infrastructure-interrupted collection may resume with unchanged
files; valid keys are skipped and failure rows are retained.

