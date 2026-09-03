# IAER v0.7 — Raw Data Location Clarification

This is a post-outcome archival clarification. It does not modify the frozen preregistration, raw data, analyzer output, closure report, or release tags.

## Raw JSONL

The exact raw behavioral file is:

`results_v0_7.jsonl`

SHA-256:

`e42a9d30a14c99800df1853b0f8b70ecd66c4a1edcfe4c82d9773c3a97b33bdf`

The raw JSONL is distributed inside the public results-release asset:

- release tag: `v0.7-instrument-results`
- asset: `iaer_v0_7_closure_final.zip`
- asset SHA-256: `120c7d37d4327797ccdcb141f27bf01726298cc86cb1e86d70f182ddd7c4c943`
- path inside the closure archive: `iaer_v0_7_closure_final/results/results_v0_7.jsonl`

## Repository representation

The repository `results/` directory contains the analyzer reports and a standalone SHA-256 record for the raw JSONL rather than a second copy of the raw JSONL itself.

`ARCHIVAL_MANIFEST_v0_7.sha256` should therefore be read as the manifest of the **closure archive contents**, not as a claim that every listed archive member is separately duplicated as an ordinary GitHub repository file.

The release asset is the canonical complete closure bundle. Its GitHub-reported digest was verified to match the locally computed SHA-256.

This clarification is intended only to remove ambiguity about file location and does not change any scientific result or interpretation.