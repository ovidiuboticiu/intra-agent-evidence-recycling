#!/usr/bin/env python3
"""Frozen preregistered analysis for IAER v0.5.0."""

import csv
import hashlib
import json
import random
import sys
from collections import Counter
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results_v0_5_0.jsonl"
REPORT = HERE / "analysis_report_v0_5_0.txt"
EXPECTED_MODEL = "microsoft_phi-4-mini-instruct"
EXPECTED_MODEL_SHA256 = "01999f17c39cc3074afae5e9c539bc82d45f2dd7faa3917c66cbef76fce8c0c2"
EXPECTED_SMOKE_SHA256 = "487dd8fc581fe206ef6dfb021f92d42267370aa60c42e2278c350f0abadf67f7"
MODEL_FILE = (
    Path.home()
    / ".lmstudio"
    / "models"
    / "bartowski"
    / "microsoft_Phi-4-mini-instruct-GGUF"
    / "microsoft_Phi-4-mini-instruct-Q4_K_M.gguf"
)
CORE = ["source_only", "neutral_filler", "passive_repeat"]


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def exact_mcnemar(desired, opposite):
    discordant = desired + opposite
    if discordant == 0:
        return 1.0
    lower = min(desired, opposite)
    probability = 2 * sum(comb(discordant, index) * (0.5 ** discordant) for index in range(lower + 1))
    return min(1.0, probability)


def paired_contrast(a, b):
    keys = sorted(set(a) & set(b))
    differences = [a[key] - b[key] for key in keys]
    desired = sum(a[key] == 1 and b[key] == 0 for key in keys)
    opposite = sum(a[key] == 0 and b[key] == 1 for key in keys)
    risk_difference = sum(differences) / len(differences) if differences else float("nan")
    return keys, risk_difference, desired, opposite, exact_mcnemar(desired, opposite)


def bootstrap_ci(a, b, seed=20260950, repetitions=20000):
    keys = sorted(set(a) & set(b))
    if not keys:
        return float("nan"), float("nan")
    generator = random.Random(seed)
    count = len(keys)
    values = []
    for _ in range(repetitions):
        sample = [keys[generator.randrange(count)] for _ in range(count)]
        values.append(sum(a[key] - b[key] for key in sample) / count)
    values.sort()
    return values[int(0.025 * repetitions)], values[int(0.975 * repetitions) - 1]


def load_items():
    with open(HERE / "stimuli_v0_5_0.csv", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def expected_keys(items):
    keys = set()
    for item in items:
        for condition in CORE:
            keys.add((item["item_id"], condition))
        if item["positive_control"] == "1":
            keys.add((item["item_id"], "independent_evidence"))
    return keys


def verify_manifest():
    manifest = HERE / "FREEZE_MANIFEST_v0_5_0.sha256"
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        expected, relative = line.split("  ", 1)
        path = HERE / relative
        if not path.is_file() or sha256(path) != expected:
            return False, relative
    return True, None


def render_report():
    lines = []

    def emit(text=""):
        lines.append(str(text))

    if not RESULTS.is_file():
        emit("ANALYSIS REFUSED: results_v0_5_0.jsonl is missing.")
        return "\n".join(lines) + "\n", 2

    rows = []
    malformed = []
    for line_number, line in enumerate(RESULTS.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception as exc:
            malformed.append((line_number, repr(exc)))

    valid = [row for row in rows if row.get("status") == "valid"]
    failures = [row for row in rows if row.get("status") != "valid"]
    key_counts = Counter((row.get("item_id"), row.get("condition")) for row in valid)
    duplicates = sorted(key for key, count in key_counts.items() if count > 1)
    by_key = {(row["item_id"], row["condition"]): row for row in valid}
    planned = expected_keys(load_items())
    observed = set(by_key)
    missing = sorted(planned - observed)
    extra = sorted(observed - planned)
    unresolved_failures = [
        row for row in failures if (row.get("item_id"), row.get("condition")) not in observed
    ]

    emit("=== INTEGRITY — BLINDED COMPLETENESS CHECK ===")
    emit(f"valid unique keys: {len(observed)}/104")
    emit(f"technical-failure audit rows: {len(failures)}")
    emit(f"malformed rows: {malformed}")
    emit(f"duplicate valid keys: {duplicates}")
    emit(f"missing planned keys: {missing}")
    emit(f"extra valid keys: {extra}")
    emit(f"unresolved technical failures: {len(unresolved_failures)}")

    complete = (
        len(observed) == 104
        and observed == planned
        and not malformed
        and not duplicates
        and not extra
        and not unresolved_failures
    )
    if not complete:
        emit()
        emit("ANALYSIS REFUSED: V3 completeness failed. No scientific outcomes were computed.")
        return "\n".join(lines) + "\n", 2

    condition_counts = Counter(row["condition"] for row in by_key.values())
    maps = {
        condition: {
            row["item_id"]: row["retain_initial"]
            for row in by_key.values()
            if row["condition"] == condition
        }
        for condition in CORE
    }
    source_counter = sum(1 - value for value in maps["source_only"].values())
    positive_rows = [row for row in by_key.values() if row["condition"] == "independent_evidence"]
    positive_retain = sum(row["retain_initial"] for row in positive_rows)

    v1 = len(maps["source_only"]) == 32 and source_counter >= 24
    v2 = len(positive_rows) == 8 and positive_retain >= 6
    v3 = complete and condition_counts == {
        "source_only": 32,
        "neutral_filler": 32,
        "passive_repeat": 32,
        "independent_evidence": 8,
    }

    package_ok, bad_file = verify_manifest()
    smoke_ok = (
        (HERE / "technical_smoke_result_v0_5_0.json").is_file()
        and sha256(HERE / "technical_smoke_result_v0_5_0.json") == EXPECTED_SMOKE_SHA256
    )
    preflight_ok = False
    preflight_path = HERE / "preflight_v0_5_0.json"
    if preflight_path.is_file():
        preflight = json.loads(preflight_path.read_text(encoding="utf-8"))
        preflight_ok = (
            preflight.get("passed") is True
            and len(preflight.get("cases", [])) == 4
            and preflight.get("model") == EXPECTED_MODEL
            and preflight.get("model_sha256") == EXPECTED_MODEL_SHA256
        )
    row_identity_ok = all(
        row.get("model") == EXPECTED_MODEL
        and row.get("model_sha256") == EXPECTED_MODEL_SHA256
        and row.get("temperature") == 0.0
        and row.get("seed") == 42
        for row in by_key.values()
    )
    model_file_ok = MODEL_FILE.is_file() and sha256(MODEL_FILE) == EXPECTED_MODEL_SHA256
    v4 = package_ok and smoke_ok and preflight_ok and row_identity_ok and model_file_ok

    emit()
    emit("=== VALIDITY GATES ===")
    emit(f"V1 source_only counter sensitivity: {source_counter}/32 -> {'PASS' if v1 else 'FAIL'}")
    emit(f"V2 independent-evidence sensitivity: {positive_retain}/8 -> {'PASS' if v2 else 'FAIL'}")
    emit(f"V3 exact dataset completeness: {'PASS' if v3 else 'FAIL'}")
    emit(f"V4 frozen identity and integrity: {'PASS' if v4 else 'FAIL'}")
    if bad_file:
        emit(f"V4 first package mismatch: {bad_file}")

    all_valid = v1 and v2 and v3 and v4
    if not all_valid:
        emit()
        emit("FINAL PREREGISTERED STATUS: INVALID/INCONCLUSIVE")
        emit("At least one validity gate failed. H1-R was not tested confirmatorily.")
        return "\n".join(lines) + "\n", 1

    _, rd, desired, opposite, p_value = paired_contrast(
        maps["passive_repeat"], maps["neutral_filler"]
    )
    ci_low, ci_high = bootstrap_ci(
        maps["passive_repeat"], maps["neutral_filler"]
    )
    supported = rd >= 0.25 and p_value < 0.05

    emit()
    emit("=== SINGLE CONFIRMATORY TEST ===")
    emit("H1-R: passive_repeat > neutral_filler")
    emit(f"paired risk difference: {rd:.6f}")
    emit(f"paired bootstrap 95% CI: [{ci_low:.6f}, {ci_high:.6f}]")
    emit(f"discordant desired/opposite: {desired}/{opposite}")
    emit(f"two-sided exact paired McNemar p: {p_value:.12g}")
    emit(f"effect threshold RD >= 0.25: {'PASS' if rd >= 0.25 else 'FAIL'}")
    emit(f"significance threshold p < 0.05: {'PASS' if p_value < 0.05 else 'FAIL'}")
    emit(f"H1-R VERDICT: {'SUPPORTED' if supported else 'NOT SUPPORTED'}")

    emit()
    emit("=== DESCRIPTIVE RETENTION ===")
    for condition in CORE + ["independent_evidence"]:
        condition_rows = [row for row in by_key.values() if row["condition"] == condition]
        retained = sum(row["retain_initial"] for row in condition_rows)
        implied = sum(
            row["belief"]["confidence_chosen"]
            if row["belief"]["chosen_claim"] == row["initial_supported_claim"]
            else 100 - row["belief"]["confidence_chosen"]
            for row in condition_rows
        ) / len(condition_rows)
        emit(
            f"{condition}: retain {retained}/{len(condition_rows)} "
            f"({100 * retained / len(condition_rows):.1f}%), "
            f"mean implied support INITIAL={implied:.2f}"
        )

    emit()
    emit("=== PROVENANCE — DESCRIPTIVE/EXPLORATORY ONLY ===")
    for condition in CORE + ["independent_evidence"]:
        condition_rows = [row for row in by_key.values() if row["condition"] == condition]
        exact = sum(bool(row["provenance_scores"]["exact_correct"]) for row in condition_rows)
        false_ids = sum(len(row["provenance_scores"]["false_independent_ids"]) for row in condition_rows)
        missed = sum(len(row["provenance_scores"]["missed_root_ids"]) for row in condition_rows)
        emit(
            f"{condition}: exact={exact}/{len(condition_rows)}, "
            f"false_ids={false_ids}, missed_roots={missed}"
        )
    emit("Provenance results cannot establish a confirmed provenance-use mechanism.")

    emit()
    emit("=== DESCRIPTIVE CROSS-STUDY REFERENCE ===")
    emit("Frozen v0.4.3 H1 RD: 0.687500")
    emit(f"v0.5.0 minus v0.4.3 RD: {rd - 0.6875:.6f}")
    emit("This comparison is descriptive and is not an additional confirmatory test.")

    emit()
    emit("=== FINAL PREREGISTERED STATUS ===")
    emit("VALID behavioral-confirmatory replication dataset.")
    emit(f"H1-R: {'SUPPORTED' if supported else 'NOT SUPPORTED'}")
    return "\n".join(lines) + "\n", 0


def main():
    report, exit_code = render_report()
    print(report, end="")
    if exit_code in {0, 1}:
        REPORT.write_text(report, encoding="utf-8")
        print(f"REPORT SAVED: {REPORT.name}")
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
