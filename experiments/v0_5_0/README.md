# Intra-Agent Evidence Recycling v0.5.0

Frozen cross-family replication package for the preregistered v0.4.3
memory-source multiplication effect.

## Scientific question

Does fivefold passive repetition of one 0.65-reliable source increase retention
of its claim, relative to an equal-sized neutral-memory control, in
Phi-4-mini-instruct after conflicting 0.80-reliable evidence arrives?

## Frozen design

- 32 new paired items;
- 3 core conditions per item;
- 8 prespecified independent-evidence positive controls;
- 104 planned trajectories;
- one confirmatory hypothesis;
- provenance audit descriptive only;
- fixed model artifact and SHA-256;
- mandatory four-case preflight before collection.

## File order and use

1. Read `PREREGISTRATION_v0_5_0.md`.
2. Verify the package using `00_VERIFY_FROZEN_PACKAGE.bat`.
3. Run `01_RUN_BEHAVIORAL_PREFLIGHT.bat` exactly once.
4. If and only if preflight prints PASS, run
   `02_RUN_CONFIRMATORY_EXPERIMENT.bat`.
5. After all 104 trajectories are valid, run `03_ANALYZE_RESULTS.bat`.

Do not edit any frozen file after `FREEZE_MANIFEST_v0_5_0.sha256` is created.
Runtime outputs (`preflight_v0_5_0.json`, `results_v0_5_0.jsonl`, and the
analysis report) are new records and must not be edited.

## Important separation

The archived technical smoke test is not scientific data. The behavioral
preflight is a validity gate. The 104 trajectories are confirmatory data.
