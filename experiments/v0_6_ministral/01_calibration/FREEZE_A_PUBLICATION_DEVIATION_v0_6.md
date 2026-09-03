# IAER v0.6 — Freeze A Publication Deviation

## Status

This note records a publication-process deviation discovered during final archival closure. It is intentionally added after the Calibration outcomes and does not alter, replace, or backdate the original preregistration tag.

## What was publicly frozen before behavioral collection

Before Calibration, GitHub release/tag `v0.6-calibration-preregistration` was created and resolved to commit `76af1a5c4e1fcc9f96d1d93a51fb5516693444d5`.

That tagged commit publicly contained the `00_program_protocol/` directory, including the staged Calibration → Eligibility → Confirmatory design, model identity, configuration, calibration gates, A→B→STOP rule, eligibility gates, confirmatory hypothesis, fixed-N logic, and fail-closed rules.

## What was intended but not included in the tagged commit

The Freeze-A publication checklist also intended to publish the exact Calibration prompt specification, stimuli, configuration JSON, runner, analyzer, Calibration-specific protocol/preregistration, Freeze-A SHA-256 manifest, and program commitment manifest containing ELI/CON stimulus commitments.

Those files existed locally in the pre-run package and were used unchanged for the reported runs, but they were not actually present in the public preregistration tag.

## Secondary local specification inconsistency

The locally frozen `INTERFACES_v0_6.json` retained an older summary sentence: `If A fails, run B on Calibration.`

The authoritative program protocol, Calibration protocol, Calibration-specific preregistration, and runner used the stricter rule: A integrity failure -> INVALID/INCONCLUSIVE and STOP; A integrity PASS plus behavioral-gate failure -> B authorized.

This stale summary line did not affect the realized experiment because Interface A had C1 integrity PASS (24/24 valid, zero failure rows) before its behavioral gate failure. Nevertheless, it is archived as an internal specification inconsistency and must not be silently corrected in the historical frozen file.

## Consequence

The public preregistration was **incomplete relative to the declared Freeze-A publication plan**.

The archived local files and their hashes document the materials that were used, but a post-outcome archival commit cannot retroactively provide the same evidentiary value as a public pre-outcome freeze.

Accordingly, the Calibration stopping decision is retained; the 48 calibration calls are valid descriptive calibration data; the project must NOT claim that the full Calibration implementation was completely publicly preregistered before outcomes; no Eligibility or Confirmatory IAER collection was performed; the v0.4.3 confirmatory result is unaffected; and any future redesign must use a new version and a genuinely complete public freeze before behavioral collection.

## Remediation

The exact local frozen materials, raw A/B results, analyzer reports, this deviation note, and a final archival SHA-256 manifest are preserved in the final closure archive. The original tag remains unchanged. No history is rewritten.
