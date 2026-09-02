# RATIONALE — v0.5.0 cross-family replication

v0.4.3 produced a large preregistered behavioral contrast between passive
repetition and equal-sized neutral memory in qwen3.5-4b. v0.5.0 asks the next
minimal question: does that effect survive a change of model family?

Microsoft Phi-4-mini-instruct was selected because it is a dense 3.8B model,
close in scale to the 4B v0.4.3 model, but trained and released by a different
organization and model family. The selected Q4_K_M artifact fits the same local
hardware. This reduces scale and hardware changes while introducing a genuine
model-family change.

The active_plain and active_lineage conditions are omitted. Their preregistered
v0.4.3 contrast was not supported, and including them would add 320 application
calls without answering the replication question. This is a prospective design
choice, not a retrospective change to v0.4.3.

The three H1-relevant conditions retain the v0.4.3 wording and evidence
reliabilities. Fresh fictional labels prevent direct item reuse. The positive
control and counterevidence-sensitivity gates are retained.

Provenance remains descriptive. Exact provenance reporting and behavioral use
are distinct constructs; v0.5.0 does not make a mechanistic claim about the
model's internal use of source lineage.
