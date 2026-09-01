# RATIONALE — v0.4 confirmatory replication

v0.3.1 was explicitly a calibration/discovery pilot. It showed a usable behavioral
dynamic range and motivated two candidate effects for independent confirmation:

1. memory-source multiplication:
   repeated/derived memory records from a single epistemic root may increase behavioral
   resistance to counterevidence even when those records are not independent evidence;

2. lineage mitigation:
   explicitly marking self-generated records with their root evidence and non-independence
   may reduce that excess behavioral weight.

v0.4 is a new-data confirmatory replication. No v0.3.1 item is reused.

Important design improvements:
- 32 held-out fictional items;
- initial supported claim is balanced between CLAIM_A and CLAIM_B;
- display order of CLAIM_A / CLAIM_B is balanced;
- condition order is independently randomized per item;
- a neutral_filler control matches the number of memory records without repeating the
  target claim;
- active_plain receives neutral non-provenance metadata so that the lineage contrast is
  less confounded by record formatting/length;
- one counterevidence strength (0.80) is frozen from the discovery pilot;
- only bounded structured outputs are collected;
- two co-primary hypotheses are tested with exact paired tests and Holm family-wise
  correction;
- minimum effect sizes are required in addition to statistical significance.

This study confirms effects only for qwen3.5-4b under the frozen configuration.
Cross-model generalization is a separate later study.
