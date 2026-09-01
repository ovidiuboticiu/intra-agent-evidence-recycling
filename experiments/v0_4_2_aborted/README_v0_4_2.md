# RUN INSTRUCTIONS — v0.4.2

## Important
v0.4.1 is closed/aborted. Do not resume it.
Do not copy `results_v0_4.jsonl` into this folder.

## LM Studio
- qwen3.5-4b
- Enable Thinking = OFF
- server on port 1234

## Windows
- laptop plugged in
- Sleep/Hibernate disabled during execution
- screen may turn off

## Step 1 — mandatory preflight

    python run_experiment_v0_4_2.py --base-url http://localhost:1234/v1 --model auto --temperature 0 --preflight-only

Required:
    SEMANTIC_PREFLIGHT_OK

v0.4.2 has 11 preflight cases:
- 3 provenance sanity cases
- 4 task-isomorphic behavioral control cases
- 4 full five-operation active-application cases
  (active_plain + active_lineage, INITIAL=A + INITIAL=B)

ALL must pass in the same preflight run.

If any preflight case fails, do not repeatedly rerun it. Report the failure.

## Step 2 — confirmatory run

    python run_experiment_v0_4_2.py --base-url http://localhost:1234/v1 --model auto --temperature 0

New output:
    results_v0_4_2.jsonl

Planned:
    168 valid trajectories.

The runner is resumable with the exact same command.
Transport-level timeouts may be automatically retried once.

## Step 3 — after completion

    python analyze_v0_4_2.py results_v0_4_2.jsonl

Then upload `results_v0_4_2.jsonl` for independent audit.

## Frozen co-primary hypotheses
H1 passive_repeat > neutral_filler
H2 active_plain > active_lineage

Each requires:
- paired risk difference >= +0.25
- Holm-adjusted exact McNemar p < 0.05
