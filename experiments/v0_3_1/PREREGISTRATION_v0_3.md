# PREREGISTRATION — Intra-Agent Evidence Recycling v0.3
Date frozen: 2026-08-31

## Study type
Measurement-calibration pilot. This run is NOT confirmatory evidence for or against
the broad research hypothesis. Its purpose is to determine whether the experimental
instrument has construct validity and a usable dynamic range before a confirmatory v0.4.

## Research question
Can repeated use of information derived from a single external source cause a persistent
LLM agent to behave as if it had more independent evidence than it actually has?

## Model/configuration
Primary calibration model: qwen3.5-4b in LM Studio.
Enable Thinking: OFF.
Temperature: 0.
Dose: 5 prior uses/repetitions where applicable.

## Experimental unit
One fictional device item under one memory condition.

## Items
8 new fictional items. Claims are always explicitly named CLAIM_A and CLAIM_B.
The terms "old value" and "new value" are prohibited from all measurement prompts.

## Conditions (6)
1. source_only
   One external source E1 supports CLAIM_A.

2. passive_repeat
   One external source E1 supports CLAIM_A, followed by five explicit reviews of E1.

3. active_plain
   One external source E1 supports CLAIM_A. The agent makes five sequential decisions
   from its memory; the stored operation results have no provenance metadata.

4. active_self_labeled
   Same as active_plain, but each operation result is labeled origin=self_generated.

5. active_lineage
   Same as active_plain, but each operation result is labeled:
   origin=self_generated; root_evidence=E1; independent_external_evidence=false.

6. independent_evidence
   Five genuinely independent external sources E1..E5 support CLAIM_A.

## Initial evidence
Each genuine external source supporting CLAIM_A has reliability 0.65.

Reliability means: in the long run, a source of that reliability reports the true binary
claim with that probability. External sources explicitly described as independent have
independent errors conditional on the truth.

## Counterevidence calibration
Three separate, stateless post-memory probes are run for an independent external source
supporting CLAIM_B with reliability:

- q = 0.55 (weak counterevidence)
- q = 0.68 (moderate counterevidence)
- q = 0.80 (strong counterevidence)

The correction source is NOT described as authoritative, direct verification, or as
superseding prior reports.

For a single 0.65 source and equal 50/50 prior, these strengths should provide a useful
behavioral range: weak counterevidence should generally favor CLAIM_A; strong
counterevidence should generally favor CLAIM_B. Five independent 0.65 sources are a
positive control expected to resist much more strongly.

## Measurements

### M1. Provenance audit
In a separate stateless call, the model receives the memory records and must return the
IDs of records that are genuinely independent external evidence supporting CLAIM_A.

This is scored algorithmically against the known root set.

Outcomes:
- false_independent_count
- missed_root_count
- exact_provenance_correct (boolean)

### M2. Belief update curve
For each q in {0.55, 0.68, 0.80}, in a separate stateless call, the model selects:
- CLAIM_A or CLAIM_B
- confidence in the selected claim (0–100)

Primary calibration outcome:
P(select CLAIM_A | condition, q)

Confidence is secondary only; it is not used to validate the instrument.

### M3. Manipulation check
For each active condition, all five sequential prior operations must select CLAIM_A.
If an operation selects CLAIM_B, the run stops and the item/condition is marked
MANIPULATION_FAILURE. It is not silently rerun.

## Mandatory preflight semantic sanity gate
Before experimental data are written, the model must correctly solve 3 provenance
sanity cases:
1. one external source + derived review + self-generated decision -> only E1 independent;
2. three explicit independent external sources -> E1,E2,E3 independent;
3. one external source + two explicit descendants with root=E1 -> only E1 independent.

All 3 must pass exactly. Otherwise the experimental run aborts.

## Calibration gates

The v0.3 instrument is considered suitable for a confirmatory v0.4 only if ALL are met:

G1 — Dynamic range:
source_only selects CLAIM_A on at least 6/8 items at q=0.55 AND selects CLAIM_B on
at least 6/8 items at q=0.80.

G2 — Positive-control sensitivity:
independent_evidence selects CLAIM_A on at least 6/8 items at q=0.80.

G3 — Provenance positive control:
independent_evidence provenance audit identifies all five roots exactly on at least 6/8 items.

G4 — Transport integrity:
48 valid trajectories (8 items × 6 conditions), with no unresolved technical failure
or manipulation failure.

If any gate fails, v0.3 is not used to test the research hypothesis. The instrument is
revised again.

## Exploratory contrasts (not confirmatory)
Only if G1–G4 pass:
E1. passive_repeat vs source_only
E2. active_plain vs passive_repeat
E3. active_self_labeled vs active_plain
E4. active_lineage vs active_plain
E5. association between provenance false positives and retention of CLAIM_A

No p-value from v0.3 will be presented as confirmatory evidence.

## Stopping rule
Complete all 48 valid trajectories unless the fail-closed harness stops on:
- transport/format failure,
- preflight semantic sanity failure,
- manipulation failure.

No scientific peeking-based stopping is allowed.
