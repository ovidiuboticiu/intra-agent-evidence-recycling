# ABORT NOTE — v0.4.1

## Status

**ABORTED — MANIPULATION VALIDITY FAILURE**

## Event

The runner stopped during:

```text
item: C16
condition: active_lineage
operation: O2
initial / expected: CLAIM_B
returned: CLAIM_A
```

## Why this invalidated the confirmatory run

The preregistered active manipulation required every one of the five active-use operations to retain the initially supported claim.

A valid response selecting the counter-claim was explicitly classified as a scientific `MANIPULATION_FAILURE`.

The frozen validity gate V4 required:

> No unresolved MANIPULATION_FAILURE.

Therefore v0.4.1 could no longer become a valid confirmatory dataset once the C16/O2 event occurred.

## Data policy

- The seven valid trajectories remain in the repository as historical raw data.
- They are not combined with later versions.
- H1 and H2 are not tested using this partial dataset.
- C16 is not rerun until a preferred answer appears.
- The failure is treated as a design-validity event, not as evidence for or against the substantive hypotheses.

## Design lesson

The v0.4.1 active manipulation asked the model to make a fresh epistemic choice at each of five reuse operations.

That mixed two constructs:

1. applying/reusing information;
2. re-evaluating the truth of the claim.

A later version redesigned the active operation as a downstream application task so that use of memory could be manipulated without turning each use step into a new belief-choice probe.
