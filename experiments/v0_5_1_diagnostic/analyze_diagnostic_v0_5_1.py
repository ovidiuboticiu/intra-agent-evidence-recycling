#!/usr/bin/env python3
"""Frozen descriptive analyzer for the IAER v0.5.1 exploratory diagnostic."""

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESULTS_PATH = HERE / "diagnostic_results_v0_5_1.jsonl"
REPORT_PATH = HERE / "diagnostic_report_v0_5_1.txt"
EXPECTED_MODEL = "microsoft_phi-4-mini-instruct"
EXPECTED_MODEL_SHA256 = "01999f17c39cc3074afae5e9c539bc82d45f2dd7faa3917c66cbef76fce8c0c2"
CONDITIONS = ["source_only", "independent_five"]
MODES = ["claim_label", "value_token", "explicit_odds"]


def load_items():
    with open(HERE / "stimuli_v0_5_1.csv", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def planned_keys(items):
    return {
        (item["item_id"], condition, mode)
        for item in items
        for condition in CONDITIONS
        for mode in MODES
    }


def load_rows():
    if not RESULTS_PATH.is_file():
        raise RuntimeError("RESULTS_MISSING")
    rows = []
    with open(RESULTS_PATH, encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except Exception as exc:
                raise RuntimeError(f"INVALID_JSONL line={number} error={exc!r}") from exc
    return rows


def key(row):
    return row.get("item_id"), row.get("condition"), row.get("mode")


def fraction(correct, total):
    return f"{correct}/{total} ({correct / total:.3f})" if total else "0/0 (NA)"


def summarize(rows, fields):
    groups = defaultdict(list)
    for row in rows:
        groups[tuple(row[field] for field in fields)].append(row)
    output = []
    for group in sorted(groups):
        members = groups[group]
        correct = sum(bool(row["normative_correct"]) for row in members)
        a_choices = sum(row["observed_claim"] == "CLAIM_A" for row in members)
        label = ", ".join(f"{field}={value}" for field, value in zip(fields, group))
        output.append(
            f"{label}: accuracy {fraction(correct, len(members))}; "
            f"CLAIM_A choices {fraction(a_choices, len(members))}"
        )
    return output


def transition(rows_by_key, left_mode, right_mode):
    counts = Counter()
    for item_id in sorted({item_id for item_id, _, _ in rows_by_key}):
        for condition in CONDITIONS:
            left = rows_by_key[(item_id, condition, left_mode)]["normative_correct"]
            right = rows_by_key[(item_id, condition, right_mode)]["normative_correct"]
            if not left and right:
                counts["improved"] += 1
            elif left and not right:
                counts["worsened"] += 1
            elif left and right:
                counts["both_correct"] += 1
            else:
                counts["both_wrong"] += 1
    return counts


def main():
    items = load_items()
    planned = planned_keys(items)
    rows = load_rows()
    valid = [row for row in rows if row.get("status") == "valid"]
    failures = [row for row in rows if row.get("status") != "valid"]
    counts = Counter(key(row) for row in valid)
    duplicate = sorted(k for k, count in counts.items() if count > 1)
    valid_keys = set(counts)
    missing = sorted(planned - valid_keys)
    extra = sorted(valid_keys - planned)
    unresolved_failures = sorted({key(row) for row in failures if key(row) not in valid_keys})
    identity_errors = [
        key(row)
        for row in valid
        if row.get("model") != EXPECTED_MODEL
        or row.get("model_sha256") != EXPECTED_MODEL_SHA256
        or row.get("temperature") != 0.0
        or row.get("seed") != 42
    ]
    if duplicate or missing or extra or unresolved_failures or identity_errors or len(valid) != 48:
        raise RuntimeError(
            "DIAGNOSTIC_INCOMPLETE_OR_INVALID "
            f"valid={len(valid)} duplicate={duplicate} missing={missing} extra={extra} "
            f"unresolved_failures={unresolved_failures} identity_errors={identity_errors}"
        )
    rows_by_key = {key(row): row for row in valid}
    total_correct = sum(bool(row["normative_correct"]) for row in valid)
    label_to_value = transition(rows_by_key, "claim_label", "value_token")
    value_to_explicit = transition(rows_by_key, "value_token", "explicit_odds")

    report = [
        "IAER v0.5.1 EXPLORATORY DIAGNOSTIC REPORT",
        "",
        "STATUS: COMPLETE — DESCRIPTIVE/EXPLORATORY ONLY",
        f"VALID PLANNED ROWS: {len(valid)}/48",
        f"RETAINED TECHNICAL-FAILURE ROWS: {len(failures)}",
        f"OVERALL NORMATIVE ACCURACY: {fraction(total_correct, len(valid))}",
        "",
        "BY MODE AND EVIDENCE CONDITION",
        *summarize(valid, ["mode", "condition"]),
        "",
        "BY MODE, EVIDENCE CONDITION, AND INITIAL LABEL",
        *summarize(valid, ["mode", "condition", "initial"]),
        "",
        "BY MODE AND PRESENTATION ORDER",
        *summarize(valid, ["mode", "presentation_order"]),
        "",
        "PAIRED REPRESENTATION CHANGES (16 item-condition pairs)",
        (
            "claim_label -> value_token: "
            f"improved={label_to_value['improved']}, worsened={label_to_value['worsened']}, "
            f"both_correct={label_to_value['both_correct']}, both_wrong={label_to_value['both_wrong']}"
        ),
        (
            "value_token -> explicit_odds: "
            f"improved={value_to_explicit['improved']}, worsened={value_to_explicit['worsened']}, "
            f"both_correct={value_to_explicit['both_correct']}, both_wrong={value_to_explicit['both_wrong']}"
        ),
        "",
        "INTERPRETATION BOUNDARY",
        "These are descriptive diagnostic patterns, not confirmatory tests or identified internal mechanisms.",
        "They cannot change the preregistered INVALID/INCONCLUSIVE status of v0.5.0.",
    ]
    REPORT_PATH.write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))
    print("SAVED:", REPORT_PATH.name)


if __name__ == "__main__":
    main()
