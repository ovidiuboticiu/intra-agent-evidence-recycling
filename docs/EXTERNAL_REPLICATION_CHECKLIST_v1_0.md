# IAER v0.4.3 — External Replication Checklist v1.0

Use this checklist before, during, and after an external replication.

## Before collection

- [ ] Select replication level: A / B / C / D.
- [ ] Choose same-configuration direct replication or a separately qualified cross-family study.
- [ ] Freeze the exact model/configuration.
- [ ] Record runtime/software version.
- [ ] Record model artifact filename and SHA-256 if available.
- [ ] Record quantization/precision.
- [ ] Record thinking/reasoning setting.
- [ ] Record temperature and all other sampling parameters.
- [ ] Decide original versus fresh isomorphic stimuli.
- [ ] Freeze sample size.
- [ ] Freeze H1/H2 decision rules.
- [ ] Freeze the exact V1-V4 validity gates.
- [ ] Freeze retry/timeout/resume policy.
- [ ] Freeze planned exclusions.
- [ ] Compute hashes for runner, analysis, stimuli, and protocol.
- [ ] Publish a timestamped protocol before the first behavioral call.
- [ ] Create an isolated output directory; never overwrite the historical `results_v0_4_3.jsonl`.
- [ ] Verify the available v0.4.3 freeze manifest.

## Mandatory preflight

- [ ] Run exactly one registered mandatory preflight.
- [ ] Confirm 8/8 required cases pass.
- [ ] Confirm terminal result `BEHAVIORAL_PREFLIGHT_OK`.
- [ ] If preflight fails, STOP.
- [ ] Do not repeatedly rerun a failed preflight until it passes.
- [ ] Record failed preflight as `INVALID/INCONCLUSIVE — PREFLIGHT FAILURE`.

## During collection

- [ ] Preserve the registered model/configuration.
- [ ] Preserve the registered runner/prompts/stimuli.
- [ ] Do not inspect scientific outcomes to decide whether to continue.
- [ ] Do not change thresholds after seeing outcomes.
- [ ] Do not switch models within the registered replication.
- [ ] Preserve technical failures and retries.
- [ ] If resumed, use the registered resume policy and document the interruption.
- [ ] Target the planned 168 valid trajectories for a faithful full v0.4.3 replication.

## Before interpretation — exact validity gates

- [ ] V1: `source_only` chooses COUNTER on at least 24/32 items.
- [ ] V2: `independent_evidence` retains INITIAL on at least 6/8 positive-control items.
- [ ] V3: all 64 active trajectories contain all five valid application outputs.
- [ ] V4: all 168 planned item-condition keys are present as valid trajectories.
- [ ] Audit duplicate valid keys.
- [ ] Audit missing planned keys.
- [ ] Audit extra/unplanned keys.
- [ ] If any mandatory gate fails, do not interpret H1/H2 as replication/non-replication.
- [ ] Run the registered analysis only after collection integrity is established.

## Report H1/H2

- [ ] H1 passive_repeat retained INITIAL: ___ / 32.
- [ ] H1 neutral_filler retained INITIAL: ___ / 32.
- [ ] H1 paired RD reported.
- [ ] H1 exact paired McNemar p reported.
- [ ] H1 Holm-adjusted p reported.
- [ ] H2 active_plain retained INITIAL: ___ / 32.
- [ ] H2 active_lineage retained INITIAL: ___ / 32.
- [ ] H2 paired RD reported.
- [ ] H2 exact paired McNemar p reported.
- [ ] H2 Holm-adjusted p reported.
- [ ] All effect sizes are reported even if categorical threshold fails.

## Final classification

Choose one:

- [ ] `REPLICATION_SUPPORTED`
- [ ] `VALID_NON_REPLICATION`
- [ ] `INVALID/INCONCLUSIVE`
- [ ] `CONFIGURATION_INELIGIBLE` (cross-family qualification only)

## Interpretation discipline

- [ ] Behavioral observation is separated from provenance judgment.
- [ ] Behavioral observation is separated from mechanistic claim.
- [ ] No claim is made that derivative records were literally counted as independent sources unless a separate mechanism design tests that claim.
- [ ] Known lexical-repetition/salience/prompt-length confounds are disclosed.
- [ ] Presentation-order sensitivity is disclosed where relevant.
- [ ] Environment/model-artifact matching limitations are disclosed.

## Archive after collection

- [ ] Publish the frozen protocol.
- [ ] Publish environment capture.
- [ ] Publish raw results.
- [ ] Publish analysis output/code.
- [ ] Publish deviation log.
- [ ] Publish final report.
- [ ] Compute SHA-256 for all released files.
- [ ] Preserve invalid/failed attempts rather than deleting them.
- [ ] Link original empirical DOI `10.5281/zenodo.22282120`.
- [ ] Link software DOI `10.5281/zenodo.22259801`.
- [ ] Link methodological-note DOI `10.5281/zenodo.22306245`.
