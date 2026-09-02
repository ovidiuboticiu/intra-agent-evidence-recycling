# Rationale — IAER v0.5.2

IAER v0.4.3 found a preregistered memory-source multiplication effect in qwen3.5-4b. A first cross-family attempt, v0.5.0 with Phi-4-mini-instruct, was correctly closed as INVALID/INCONCLUSIVE when its mandatory behavioral preflight failed. No confirmatory outcomes were collected.

The subsequent v0.5.1 exploratory diagnostic found that Phi-4-mini-instruct was highly sensitive to response representation and presentation order and did not reliably aggregate five independent sources. Those diagnostics cannot alter v0.5.0 and are not confirmatory evidence.

Microsoft Phi-4-mini-reasoning is now treated as a new candidate model. Moving directly to a full confirmatory replication would risk another invalid run. Therefore v0.5.2 is a small, explicitly non-confirmatory eligibility pilot.

The pilot fixes one claim-label response interface because it is closest to the binary final-choice outcome used in v0.4.3. It does not compare several formats and then select the best performer. The conditions isolate three minimum capabilities:

1. retain a moderately supported initial belief when no counterevidence exists;
2. update to a stronger single counter-source;
3. retain the initial belief when five independent moderate sources outweigh that counter-source.

INITIAL identity and claim-presentation order are fully balanced so a label or first-position heuristic cannot satisfy the eligibility rule. The 10/12 overall and 5/6 subgroup thresholds allow one error per six-item symmetry cell while requiring consistently correct behavior.

If the candidate passes, the only authorized next inference is that a separate confirmatory design is technically and behaviorally justifiable. The v0.5.2 results themselves cannot support the substantive IAER hypotheses.
