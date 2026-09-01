# ABORT NOTE — v0.4.2

## Status

**ABORTED BEFORE CONFIRMATORY DATA COLLECTION**

## Trigger

The frozen v0.4.2 protocol required all 11 semantic/behavioral preflight cases to pass in one run.

During the actual preflight, provenance case 3 failed:

```text
expected = ["E1"]
got = []
pass = false
```

The runner therefore raised:

```text
SEMANTIC_PREFLIGHT_FAILED
```

and confirmatory collection did not start.

## Consequence

- No confirmatory `results_v0_4_2.jsonl` exists.
- Zero v0.4.2 confirmatory trajectories were collected.
- H1 and H2 were not tested.
- No data from v0.4.1 were imported or reused.
- The same preflight was not repeatedly rerun until it passed.

## What did pass

The contemporaneous console output showed that the task-isomorphic behavioral controls passed and that the repaired active-application manipulation completed all five operations in the tested `active_plain` and `active_lineage` configurations for both INITIAL=A and INITIAL=B.

This supported the manipulation redesign itself, but not the mandatory provenance gate.

## Archival caveat

The supplied v0.4.2 folder does not contain a saved preflight JSON/log.

The failure details above are derived from the contemporaneous execution capture rather than a machine-readable artifact inside this archive.

## Design consequence

v0.4.3 retained the repaired active-application manipulation but removed provenance from the behavioral study's validity gates.

Provenance remained a secondary/descriptive measurement and could not by itself support a strong mechanistic claim.
