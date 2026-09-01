# TECHNICAL / VALIDATION AMENDMENT v0.4.1
Date: 2026-08-31

## Trigger
The frozen v0.4 preflight stopped before any experimental trajectory was written.
Provenance cases 1-3 passed. The simplified behavioral case "one 0.65 source vs one
0.80 counter-source" returned CLAIM_A when the preflight expected CLAIM_B.
The five-independent-source positive control passed.

## Implementation defect discovered
The two behavioral preflight cases were not task-isomorphic to the confirmatory
experiment. They used hand-written simplified prompts instead of the actual
`base_memory()` and `belief_probe()` functions. Therefore they did not validate
the exact prompt/evidence structure used by the experiment.

This amendment does NOT reinterpret the failed preflight as a scientific result.

## Changes
No experimental hypothesis, item, condition, sample size, counterevidence strength,
effect-size threshold, alpha, Holm correction, validity gate, model, temperature,
or confirmatory analysis is changed.

Only the preflight implementation is changed:
1. Provenance sanity cases are retained.
2. Behavioral sanity checks now call the exact same `base_memory()` and
   `belief_probe()` functions used by experimental trajectories.
3. Two held-out sentinel items are used:
   - one with INITIAL=CLAIM_A,
   - one with INITIAL=CLAIM_B.
4. Each sentinel tests both:
   - source_only vs q=.80 counterevidence -> expected COUNTER;
   - five independent .65 sources vs q=.80 counterevidence -> expected INITIAL.
5. Thus v0.4.1 has 7 total preflight cases.

## Decision rule
All 7 cases must pass in one preflight run.
If any task-isomorphic behavioral case fails, DO NOT start the confirmatory experiment.
At that point the q=.80 measurement design must be reconsidered rather than repeatedly
rerunning the preflight until it passes.

## Data status
No valid v0.4 confirmatory trajectory existed at amendment time.
The failed v0.4 preflight is retained as an audit event but is not scientific data.
