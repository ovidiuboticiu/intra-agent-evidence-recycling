# IAER v0.4.3 — External Replication Kit v1.0

This index points to the public materials intended for an independent replication of the preserved IAER v0.4.3 behavioral study.

## Kit contents

1. [`EXTERNAL_REPLICATION_GUIDE_v1_0.md`](EXTERNAL_REPLICATION_GUIDE_v1_0.md)  
   Full replication scope, prospectivity rules, environment capture requirements, STOP rules, execution procedure, outcome taxonomy, and interpretation boundaries.

2. [`EXTERNAL_REPLICATION_VALIDITY_GATES_v1_0.md`](EXTERNAL_REPLICATION_VALIDITY_GATES_v1_0.md)  
   Exact frozen v0.4.3 validity-gate definitions and co-primary decision thresholds.

3. [`EXTERNAL_REPLICATION_CHECKLIST_v1_0.md`](EXTERNAL_REPLICATION_CHECKLIST_v1_0.md)  
   Compact operational checklist for before, during, and after collection.

4. [`EXTERNAL_REPLICATION_REPORT_TEMPLATE_v1_0.md`](EXTERNAL_REPLICATION_REPORT_TEMPLATE_v1_0.md)  
   Standard report structure for supported replication, valid non-replication, or invalid/inconclusive attempts.

5. [`EXTERNAL_REPLICATION_ENVIRONMENT_TEMPLATE_v1_0.json`](EXTERNAL_REPLICATION_ENVIRONMENT_TEMPLATE_v1_0.json)  
   Machine-readable environment capture template.

## Frozen source experiment

Use the preserved source materials in:

[`../experiments/v0_4_3/`](../experiments/v0_4_3/)

Do not edit or overwrite frozen historical files. External results must be written to a separate replication directory and filename.

## Persistent records

- Original empirical preprint: `10.5281/zenodo.22282120`
- Software/reproducibility archive: `10.5281/zenodo.22259801`
- Methodological note: `10.5281/zenodo.22306245`

## Current claim boundary

The strongest supported original claim is behavioral and configuration-specific: five explicitly derivative, target-consistent reviews of one initial source substantially increased retention of the initial claim relative to five unrelated memory records under the frozen v0.4.3 Qwen task/configuration.

The original study does not establish literal independent-source counting as the mechanism. A faithful direct replication inherits the original lexical-repetition, salience, prompt-length, and possible order-sensitivity limitations.

## Preferred external-replication policy

- publicly freeze the external protocol before collection;
- capture exact model/runtime artifacts where possible;
- preserve failed attempts;
- do not rerun a failed preflight until it passes;
- do not tune thresholds or prompts after target outcomes begin;
- publish raw results and analysis;
- report valid non-replications as openly as successful replications;
- separate behavioral results from mechanistic interpretation.
