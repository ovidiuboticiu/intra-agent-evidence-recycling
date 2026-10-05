# Historical byte-integrity correction — 2026-10-05

## Scope

A post-publication adversarial audit found five historical text artifacts whose committed Git blobs used LF line endings while their preserved freeze/post-run SHA-256 manifests corresponded to CRLF bytes.

The affected files were:

- `experiments/v0_3_1/results_v0_3_1.jsonl`
- `experiments/v0_3_1/stimuli_v0_3.csv`
- `experiments/v0_4_1_aborted/results_v0_4.jsonl`
- `experiments/v0_4_1_aborted/stimuli_v0_4.csv`
- `experiments/v0_4_2_aborted/stimuli_v0_4_2.csv`

For every affected file, converting only LF line endings back to CRLF reproduced the exact SHA-256 already recorded in the corresponding historical manifest.

## Correction

The five files were restored to the manifest-matching CRLF byte representation. Exact `.gitattributes` rules now mark those paths `-text` so Git does not normalize them on checkout.

No JSONL record, CSV field, experimental result, label, or numerical value was changed. This is a byte-preservation correction.

Run:

```bash
python tools/verify_historical_byte_integrity.py
```

Expected result:

```text
PASS historical byte integrity {'files': 5}
```

## Scientific effect

This correction does not change the v0.4.3 H1/H2 results or any later qualification result. It repairs historical archive fidelity only.

## Historical v0.4.3 release wording

The original GitHub v0.4.3 release body is preserved as a historical record and uses wording such as "preregistered" and "independently audited." Current project documentation applies narrower wording:

- v0.4.3 is described as **pre-specified/frozen** where a public or independently verifiable pre-collection preregistration timestamp cannot be established;
- audit/recomputation claims are described according to what is actually recoverable from the artifacts and should not be read as external independent replication or external peer review.

The original behavioral numbers remain reported because they survive the current artifact-level checks; the stronger historical provenance/priority wording is not relied upon.
