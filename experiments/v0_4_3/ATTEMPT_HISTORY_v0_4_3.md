# CONFIRMATORY ATTEMPT HISTORY

## v0.4.1
ABORTED after 7 valid trajectories because the active-lineage manipulation asked
the model to re-decide the claim at every use step. C16 switched spontaneously at O2,
triggering the preregistered manipulation-failure rule.

## v0.4.2
ABORTED before data collection because one semantic provenance preflight case failed:
the model returned an empty root set in a lineage-marked memory even though E1 was the
true root. Behavioral controls and all 20 active-application operations passed.

## Consequence for v0.4.3
The active-use repair from v0.4.2 is retained.
Provenance is still collected, but it is no longer a validity gate and is not used to
justify a confirmatory mechanistic claim.
No prior confirmatory-attempt stimulus is reused.
