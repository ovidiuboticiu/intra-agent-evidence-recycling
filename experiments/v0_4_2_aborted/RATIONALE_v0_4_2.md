# RATIONALE — v0.4.2 confirmatory re-attempt

v0.4.2 preserves the two confirmatory behavioral questions but repairs the
active-use manipulation that invalidated v0.4.1.

## Why the v0.4.1 manipulation was structurally fragile
In v0.4.1 every active-use step asked the model to choose a claim again.
Across 32 items × 2 active conditions × 5 operations, this created 320
opportunities for a spontaneous belief switch before the actual counterevidence
probe. One such switch invalidated the entire fixed-N confirmatory run.

That procedure mixed two constructs:
1. reuse/application of an already selected configuration;
2. repeated epistemic re-decision.

The research question concerns whether derived memory records produced by use of
a single epistemic root acquire excess behavioral weight. Re-deciding the belief
at every use is not necessary for that manipulation.

## v0.4.2 repair
Each active operation is now a downstream APPLICATION task:
- the current configuration is explicitly authorized by the persistent state;
- the model applies that configuration to an operation;
- the response schema permits only that authorized claim;
- the resulting operation trace is stored back into memory.

Thus the active manipulation creates self-generated usage traces without turning
each step into another belief measurement.

active_plain stores the usage trace without epistemic lineage.
active_lineage stores the same usage trace with explicit root and independence metadata.

## Additional code repair
All JSON Schema response_format objects now use the boolean:
    "strict": True
not the string:
    "strict": "true"

This is a standards/portability fix and does not alter the scientific variables.

## Data separation
All 32 stimuli are new. v0.4/v0.4.1 stimuli and partial results are not reused.
