# RATIONALE FROM v0.2

Status of v0.2:
- 24 items × 5 conditions = 120 valid trajectories were completed.
- 5 separate technical-failure records were timeout events and were later rerun successfully.
- The preregistered active_plain > passive_repeat effect was not supported.
- However, the pilot was measurement-limited.

Observed measurement problems:
1. `old_value` / `new_value` wording was semantically ambiguous for the model.
2. `confidence_old` was sometimes interpreted as a count rather than a 0–100 belief measure.
3. The post-correction source explicitly said it "supersedes" prior evidence, creating a ceiling effect.
4. Source-count questions were not sufficiently concrete about which memory records counted as independent roots.

v0.3 therefore changes the measurement instrument, not the underlying research question.

Key repair:
- claims are named CLAIM_A and CLAIM_B, never "old" / "new";
- provenance is measured by selecting concrete evidence-record IDs;
- belief update uses graded counterevidence without the word "supersedes";
- a source-only baseline is added;
- the run is explicitly a calibration pilot, not a confirmatory hypothesis test.
