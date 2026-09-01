# RUN INSTRUCTIONS — v0.4 CONFIRMATORY

## Before running
LM Studio:
- qwen3.5-4b
- Enable Thinking = OFF
- server on port 1234

Windows:
- laptop plugged in
- Sleep/Hibernate disabled during execution
- screen may turn off

Do NOT copy any old results file into this folder.

## Step 1 — mandatory preflight

    python run_experiment_v0_4.py --base-url http://localhost:1234/v1 --model auto --temperature 0 --preflight-only

Required:
    SEMANTIC_PREFLIGHT_OK

There are five cases. All must show pass=true.

## Step 2 — confirmatory run

    python run_experiment_v0_4.py --base-url http://localhost:1234/v1 --model auto --temperature 0

Expected new output file:
    results_v0_4.jsonl

Planned total:
    168 valid trajectories

The run is resumable with the same command.

The runner may retry an individual API call once after a transport timeout/network error.
If a trajectory still fails, or a manipulation check fails, the program stops fail-closed.

## Important
Do not inspect scientific outcomes during collection. Terminal lines include technical
validation fields; do not use them to stop the study.

## Step 3 — after all 168 trajectories

    python analyze_v0_4.py results_v0_4.jsonl

Then upload `results_v0_4.jsonl` for independent audit.

## Confirmatory success
Two co-primary hypotheses:
H1 passive_repeat > neutral_filler
H2 active_plain > active_lineage

Both use paired exact McNemar tests with Holm correction and each also requires an
absolute paired risk difference >= 0.25.
