# v0.4.2 — Aborted Before Confirmatory Data Collection

**Scientific status:** ABORTED BEFORE DATA COLLECTION  
**Reason:** Mandatory semantic-provenance preflight failure  
**Confirmatory inference:** **Not permitted**  
**Model:** `qwen3.5-4b` via LM Studio  
**Temperature:** `0`  
**Thinking / reasoning mode:** OFF

This folder preserves the frozen v0.4.2 confirmatory re-attempt package.

Unlike v0.4.1, v0.4.2 did **not** begin confirmatory experimental collection. The mandatory preflight failed, so no `results_v0_4_2.jsonl` was generated.

## Purpose of v0.4.2

v0.4.2 retained the two behavioral co-primary hypotheses:

- **H1:** `passive_repeat > neutral_filler`
- **H2:** `active_plain > active_lineage`

It repaired the active-use manipulation that invalidated v0.4.1.

Instead of asking the model to decide which claim was true at every reuse operation, the new manipulation supplied an already authorized configuration and required the model to apply it in a downstream task.

This separated:

1. application/reuse of an existing configuration; from
2. repeated epistemic re-decision.

## Code compliance repair

v0.4.2 also repaired the Structured Output type bug inherited from earlier versions.

The supplied runner contains **4** schema occurrences using:

```python
"strict": True
```

and **0** occurrences of the historical string form:

```python
"strict": "true"
```

Therefore the known `strict` type bug was repaired before this attempt.

## Fresh stimulus set

Independent archival inspection confirms:

- 32 new fictional items;
- INITIAL: 16 CLAIM_A / 16 CLAIM_B;
- presentation order: 16 A_FIRST / 16 B_FIRST;
- 8 prespecified positive-control items.

The planned confirmatory dataset remained **168 valid trajectories**.

## Mandatory preflight

The frozen protocol required all 11 preflight cases to pass in one run:

- 3 provenance semantic sanity cases;
- 4 task-isomorphic behavioral control cases;
- 4 full five-operation active-application cases.

The confirmatory dataset could not start unless all 11 passed.

## Observed abort event

The contemporaneous console capture from the actual preflight showed:

```text
case = 3
kind = provenance
expected = ["E1"]
got = []
pass = false
```

The case contained one genuine independent external root `E1` plus lineage-marked self-generated application traces derived from E1.

The other displayed behavioral and active-application preflight cases passed, including the five-step active checks for both INITIAL orientations.

Because case 3 failed, the runner raised:

```text
SEMANTIC_PREFLIGHT_FAILED
```

and no confirmatory trajectories were collected.

## Important archival limitation

The supplied ZIP contains **no machine-readable preflight result log**.

The runner prints the preflight object to the terminal but does not persist it to a file. Therefore the exact case-3 failure above is historical execution evidence reconstructed from the contemporaneous console capture, not independently recoverable from this ZIP alone.

This limitation is documented rather than silently filled in.

## Why the study was not repeatedly rerun

The preflight existed to validate the measurement/manipulation before scientific data collection.

Repeatedly rerunning it until the model happened to return the desired provenance answer would weaken the validity of the gate.

Accordingly, v0.4.2 was closed before data collection.

## Scientific interpretation

v0.4.2 provides no confirmatory evidence for or against H1 or H2.

What it established methodologically was narrower:

- the repaired active-application manipulation passed the observed active preflight checks;
- the explicit provenance instrument remained less stable;
- provenance measurement and behavioral confirmation should therefore be separated in the next design.

That decision led to v0.4.3, where provenance remained descriptive but no longer invalidated the behavioral-confirmatory study.

## Frozen-package integrity

`FREEZE_MANIFEST_v0_4_2.sha256` verifies all listed files successfully.

Original uploaded archive SHA-256:

```text
dfee2a70bed29c8c1bf4fd0ff5d65351654e0f7cae578a04c6489620e634d719
```

## Files added only for repository archival

The supplied experimental files are preserved byte-for-byte.

This GitHub-ready folder adds only:

- `README.md`
- `AUDIT_REPORT.md`
- `ABORT_NOTE.md`
- `POSTRUN_AUDIT_SHA256.txt`
