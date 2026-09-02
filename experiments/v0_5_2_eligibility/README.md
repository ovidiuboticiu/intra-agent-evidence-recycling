# IAER v0.5.2 — Phi-4-mini-reasoning eligibility pilot

This is a frozen, fixed-N behavioral eligibility pilot. It is **not** a confirmatory replication of the IAER v0.4.3 findings.

## Purpose

Determine whether Microsoft Phi-4-mini-reasoning Q4_K_M can reliably execute the task-isomorphic binary evidence-integration interface required for a future, separately preregistered cross-family replication.

## Frozen target

- API model identifier: `microsoft_phi-4-mini-reasoning`
- GGUF: `microsoft_Phi-4-mini-reasoning-Q4_K_M.gguf`
- Model SHA-256: `ce8becd58f350d8ae0ec3bbb201ab36f750ffab17ab6238f39292d12ab68ea06`
- LM Studio API: `http://127.0.0.1:1234/v1`
- Temperature: `0`
- Seed: `42`
- Context length configured in LM Studio: `8192`

## Design

- 12 new balanced fictional items
- 3 task-isomorphic conditions per item
- 36 planned calls
- fixed response representation: `chosen_claim` plus `confidence_chosen`
- no response-format selection after outcomes

See `PREREGISTRATION_v0_5_2.md` for the complete decision rule.

## Required execution order

1. Publish the complete frozen folder and attached ZIP in a GitHub **pre-release** before behavioral collection.
2. Record the release tag and ZIP SHA-256 in the public release notes.
3. Keep LM Studio running with the frozen model showing `READY`.
4. Double-click `00_VERIFY_FROZEN_PACKAGE.bat`. It must print `FROZEN PACKAGE: PASS`.
5. Double-click `01_RUN_ELIGIBILITY_PILOT.bat` exactly once. Do not inspect or analyze partial outcomes.
6. After `ELIGIBILITY COLLECTION COMPLETE: 36 / 36`, double-click `02_ANALYZE_RESULTS.bat`.
7. Archive the raw JSONL, text report, and JSON report without editing them.

## Files created during execution

- `results_v0_5_2.jsonl`
- `eligibility_report_v0_5_2.txt`
- `eligibility_report_v0_5_2.json`

The collection script is resumable after a power interruption only when no failure row was written for the interrupted key. A valid completed key is never rerun. A recorded failure stops the pilot fail-closed.
