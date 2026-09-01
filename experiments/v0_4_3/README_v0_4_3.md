# RUN INSTRUCTIONS — v0.4.3 BEHAVIORAL-CONFIRMATORY

## Do not resume earlier attempts
v0.4.1 and v0.4.2 are closed.
Do not copy their result files into this folder.

## LM Studio
- qwen3.5-4b
- Enable Thinking = OFF
- local server on port 1234

## Windows
- laptop plugged in
- Sleep/Hibernate disabled while running
- screen may turn off

## 1. Mandatory behavioral preflight

    python run_experiment_v0_4_3.py --base-url http://localhost:1234/v1 --model auto --temperature 0 --preflight-only

Required:
    BEHAVIORAL_PREFLIGHT_OK

There are 8 cases:
- source_only and independent_evidence for INITIAL=A
- source_only and independent_evidence for INITIAL=B
- active_plain and active_lineage full five-step application for INITIAL=A
- active_plain and active_lineage full five-step application for INITIAL=B

All 8 must pass in one run.
Do not repeatedly rerun a failed preflight.

## 2. Confirmatory collection

    python run_experiment_v0_4_3.py --base-url http://localhost:1234/v1 --model auto --temperature 0

Output:
    results_v0_4_3.jsonl

Planned total:
    168 valid trajectories.

The runner is resumable with the exact same command.
During collection the terminal prints only VALID/technical status, not scientific outcomes.

## 3. Final analysis

    python analyze_v0_4_3.py results_v0_4_3.jsonl

Then upload results_v0_4_3.jsonl for independent audit.

## Frozen co-primary hypotheses
H1 passive_repeat > neutral_filler
H2 active_plain > active_lineage

Each requires:
- paired RD >= +0.25
- Holm-adjusted exact McNemar p < 0.05

Provenance is descriptive only in v0.4.3.
