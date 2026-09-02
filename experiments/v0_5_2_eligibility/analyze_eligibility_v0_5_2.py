#!/usr/bin/env python3
"""Frozen analyzer for the IAER v0.5.2 eligibility pilot."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "results_v0_5_2.jsonl"
TEXT_REPORT = HERE / "eligibility_report_v0_5_2.txt"
JSON_REPORT = HERE / "eligibility_report_v0_5_2.json"
MODEL_ID = "microsoft_phi-4-mini-reasoning"
MODEL_SHA256 = "ce8becd58f350d8ae0ec3bbb201ab36f750ffab17ab6238f39292d12ab68ea06"
CONDITIONS = ["baseline_initial", "counter_single_strong", "independent_five_initial"]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_rows() -> list[dict[str, Any]]:
    if not RESULTS_PATH.is_file():
        raise SystemExit(f"Missing {RESULTS_PATH.name}")
    rows = []
    for line_no, line in enumerate(RESULTS_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Malformed JSONL at line {line_no}: {exc}") from exc
    return rows


def ratio(correct: int, total: int) -> str:
    return f"{correct}/{total} ({correct / total:.3f})" if total else "0/0 (NA)"


def main() -> None:
    rows = load_rows()
    with (HERE / "stimuli_v0_5_2.csv").open("r", encoding="utf-8", newline="") as handle:
        items = list(csv.DictReader(handle))
    expected_keys = {(item["item_id"], condition) for item in items for condition in CONDITIONS}
    valid = [row for row in rows if row.get("status") == "valid"]
    failures = [row for row in rows if row.get("status") != "valid"]
    valid_keys = [(row.get("item_id"), row.get("condition")) for row in valid]
    key_counts = Counter(valid_keys)
    duplicate_keys = sorted(key for key, count in key_counts.items() if count != 1)
    missing_keys = sorted(expected_keys - set(valid_keys))
    extra_keys = sorted(set(valid_keys) - expected_keys)
    manifest_sha = sha256_file(HERE / "FROZEN_MANIFEST_v0_5_2.sha256")

    metadata_errors = []
    for index, row in enumerate(valid, 1):
        if row.get("model") != MODEL_ID:
            metadata_errors.append(f"row {index}: model")
        if row.get("model_sha256") != MODEL_SHA256:
            metadata_errors.append(f"row {index}: model_sha256")
        if row.get("temperature") != 0:
            metadata_errors.append(f"row {index}: temperature")
        if row.get("seed") != 42:
            metadata_errors.append(f"row {index}: seed")
        if row.get("run_meta", {}).get("manifest_sha256") != manifest_sha:
            metadata_errors.append(f"row {index}: manifest_sha256")
        if row.get("finish_reason", row.get("diagnostics", {}).get("finish_reason")) not in {None, "stop"}:
            metadata_errors.append(f"row {index}: finish_reason")

    g1 = (
        len(valid) == 36
        and not failures
        and not duplicate_keys
        and not missing_keys
        and not extra_keys
        and not metadata_errors
    )

    summaries: dict[str, Any] = {}
    overall_pass = True
    orientation_pass = True
    order_pass = True
    for condition in CONDITIONS:
        group = [row for row in valid if row.get("condition") == condition]
        overall_correct = sum(int(row.get("correct", 0)) for row in group)
        by_initial = {}
        for initial in ("CLAIM_A", "CLAIM_B"):
            subgroup = [row for row in group if row.get("initial_supported_claim") == initial]
            by_initial[initial] = {
                "correct": sum(int(row.get("correct", 0)) for row in subgroup),
                "total": len(subgroup),
            }
        by_order = {}
        for order in ("A_FIRST", "B_FIRST"):
            subgroup = [row for row in group if row.get("presentation_order") == order]
            by_order[order] = {
                "correct": sum(int(row.get("correct", 0)) for row in subgroup),
                "total": len(subgroup),
            }
        condition_overall_pass = len(group) == 12 and overall_correct >= 10
        condition_orientation_pass = all(
            value["total"] == 6 and value["correct"] >= 5 for value in by_initial.values()
        )
        condition_order_pass = all(
            value["total"] == 6 and value["correct"] >= 5 for value in by_order.values()
        )
        overall_pass &= condition_overall_pass
        orientation_pass &= condition_orientation_pass
        order_pass &= condition_order_pass
        summaries[condition] = {
            "correct": overall_correct,
            "total": len(group),
            "by_initial": by_initial,
            "by_presentation_order": by_order,
            "overall_gate_pass": condition_overall_pass,
            "orientation_gate_pass": condition_orientation_pass,
            "presentation_order_gate_pass": condition_order_pass,
        }

    gates = {
        "G1_completeness_and_integrity": g1,
        "G2_overall_condition_accuracy": bool(g1 and overall_pass),
        "G3_initial_orientation_symmetry": bool(g1 and orientation_pass),
        "G4_presentation_order_symmetry": bool(g1 and order_pass),
    }
    if not g1:
        decision = "INVALID/INCONCLUSIVE"
    elif all(gates.values()):
        decision = "ELIGIBLE"
    else:
        decision = "INELIGIBLE"

    report = {
        "experiment": "IAER",
        "version": "v0.5.2",
        "study_type": "behavioral_eligibility_pilot",
        "decision": decision,
        "valid_rows": len(valid),
        "failure_rows": len(failures),
        "missing_keys": missing_keys,
        "extra_keys": extra_keys,
        "duplicate_keys": duplicate_keys,
        "metadata_errors": metadata_errors,
        "gates": gates,
        "condition_summaries": summaries,
        "interpretation_boundary": (
            "Eligibility is not confirmation, refutation, or estimation of the IAER effect."
        ),
    }
    JSON_REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "IAER v0.5.2 BEHAVIORAL ELIGIBILITY REPORT",
        "",
        f"DECISION: {decision}",
        f"VALID PLANNED ROWS: {len(valid)}/36",
        f"RECORDED FAILURE ROWS: {len(failures)}",
        "",
        "PRESPECIFIED GATES",
    ]
    for gate, passed in gates.items():
        lines.append(f"{gate}: {'PASS' if passed else 'FAIL'}")
    lines.extend(["", "BY CONDITION"])
    for condition in CONDITIONS:
        summary = summaries[condition]
        lines.append(f"{condition}: {ratio(summary['correct'], summary['total'])}")
        for initial, values in summary["by_initial"].items():
            lines.append(f"  initial={initial}: {ratio(values['correct'], values['total'])}")
        for order, values in summary["by_presentation_order"].items():
            lines.append(f"  order={order}: {ratio(values['correct'], values['total'])}")
    if missing_keys:
        lines.extend(["", f"MISSING KEYS: {missing_keys}"])
    if extra_keys:
        lines.extend(["", f"EXTRA KEYS: {extra_keys}"])
    if duplicate_keys:
        lines.extend(["", f"DUPLICATE KEYS: {duplicate_keys}"])
    if metadata_errors:
        lines.extend(["", f"METADATA ERRORS: {metadata_errors}"])
    lines.extend([
        "",
        "INTERPRETATION BOUNDARY",
        "Eligibility is not confirmation, refutation, or estimation of the IAER effect.",
        "A fresh public preregistration is required before any v0.6.0 confirmatory run.",
    ])
    text = "\n".join(lines) + "\n"
    TEXT_REPORT.write_text(text, encoding="utf-8")
    print(text, end="")
    print(f"SAVED: {TEXT_REPORT.name}")
    print(f"SAVED: {JSON_REPORT.name}")


if __name__ == "__main__":
    main()
