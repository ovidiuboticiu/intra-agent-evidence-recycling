# RUN INSTRUCTIONS — v0.3

## Important
v0.3 is a calibration pilot, not a confirmatory study.
Do not merge its results with v0.2.

## LM Studio
- Model: qwen3.5-4b
- Enable Thinking: OFF
- Server running on port 1234
- Keep laptop awake; screen may turn off, but Sleep/Hibernate should be disabled while running.

## 1. Preflight only
Run first:

    python run_experiment_v0_3.py --base-url http://localhost:1234/v1 --model auto --temperature 0 --preflight-only

Required:
    SEMANTIC_PREFLIGHT_OK

If preflight fails, DO NOT start the experiment.

## 2. Run experiment
Only after preflight passes:

    python run_experiment_v0_3.py --base-url http://localhost:1234/v1 --model auto --temperature 0

Output:
    results_v0_3.jsonl

There are 48 trajectories total (8 items × 6 conditions).
The runner is resumable: rerun the exact same command.

## 3. After completion
Do not interpret intermediate scientific results.
After all 48 trajectories finish, run:

    python analyze_v0_3.py results_v0_3.jsonl

Or upload results_v0_3.jsonl to ChatGPT for audited analysis.

## Fail-closed behavior
The script stops on:
- technical failure,
- malformed/empty model output,
- semantic preflight failure,
- manipulation failure.

Do not repeatedly rerun a deterministic manipulation failure. Report it instead.
