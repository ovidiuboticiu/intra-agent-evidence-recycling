#!/usr/bin/env python3
"""Frozen runner for the IAER v0.5.2 eligibility pilot."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import platform
import random
import socket
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


HERE = Path(__file__).resolve().parent
VERSION = "v0.5.2"
API_BASE = "http://127.0.0.1:1234/v1"
MODEL_ID = "microsoft_phi-4-mini-reasoning"
MODEL_FILENAME = "microsoft_Phi-4-mini-reasoning-Q4_K_M.gguf"
MODEL_SHA256 = "ce8becd58f350d8ae0ec3bbb201ab36f750ffab17ab6238f39292d12ab68ea06"
TEMPERATURE = 0
SEED = 42
ORDER_SEED = 20260902
MAX_TOKENS = 2048
TIMEOUT = 600
CONDITIONS = ["baseline_initial", "counter_single_strong", "independent_five_initial"]
RESULTS_PATH = HERE / "results_v0_5_2.jsonl"
MANIFEST_PATH = HERE / "FROZEN_MANIFEST_v0_5_2.sha256"
STIMULI_PATH = HERE / "stimuli_v0_5_2.csv"

SYSTEM = (
    "You are an experimental decision agent in a fully fictional binary world. "
    "Use only information supplied in this request. CLAIM_A and CLAIM_B are mutually "
    "exclusive and exhaustive. The prior probability before evidence is 50/50. "
    "A source reliability r means the source reports the true claim with probability r. "
    "Sources explicitly described as independent have independent errors conditional on truth. "
    "Do not use real-world knowledge."
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8 * 1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest() -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, filename = line.split("  ", 1)
        entries.append((digest.lower(), filename))
    return entries


def verify_frozen_files() -> None:
    failures = []
    for expected, filename in load_manifest():
        path = HERE / filename
        if not path.is_file():
            failures.append(f"MISSING {filename}")
            continue
        actual = sha256_file(path)
        if actual != expected:
            failures.append(f"HASH_MISMATCH {filename}: expected={expected} actual={actual}")
    if failures:
        raise RuntimeError("FROZEN_FILE_VERIFICATION_FAILED: " + "; ".join(failures))


def load_stimuli() -> list[dict[str, str]]:
    with STIMULI_PATH.open("r", encoding="utf-8", newline="") as handle:
        items = list(csv.DictReader(handle))
    required = {
        "item_id", "entity", "claim_a_value", "claim_b_value",
        "initial_supported_claim", "presentation_order",
    }
    if len(items) != 12 or not items or set(items[0]) != required:
        raise RuntimeError("STIMULUS_DESIGN_INVALID: expected 12 rows and exact columns")
    if len({item["item_id"] for item in items}) != 12:
        raise RuntimeError("STIMULUS_DESIGN_INVALID: duplicate item_id")
    if sum(item["initial_supported_claim"] == "CLAIM_A" for item in items) != 6:
        raise RuntimeError("STIMULUS_DESIGN_INVALID: INITIAL orientation not balanced")
    if sum(item["presentation_order"] == "A_FIRST" for item in items) != 6:
        raise RuntimeError("STIMULUS_DESIGN_INVALID: presentation order not balanced")
    cells = {
        (initial, order): sum(
            item["initial_supported_claim"] == initial and item["presentation_order"] == order
            for item in items
        )
        for initial in ("CLAIM_A", "CLAIM_B")
        for order in ("A_FIRST", "B_FIRST")
    }
    if set(cells.values()) != {3}:
        raise RuntimeError(f"STIMULUS_DESIGN_INVALID: crossing={cells}")
    return items


def find_model_file() -> Path:
    root = Path.home() / ".lmstudio" / "models"
    matches = [p for p in root.rglob("*.gguf") if p.name.lower() == MODEL_FILENAME.lower()]
    if len(matches) != 1:
        raise RuntimeError(f"MODEL_FILE_COUNT_INVALID: expected 1, found {len(matches)}")
    return matches[0]


def http_json(
    method: str,
    url: str,
    payload: dict[str, Any] | None = None,
    timeout: int = TIMEOUT,
) -> tuple[dict[str, Any], int]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    last_error: Exception | None = None
    for attempt in (1, 2):
        request = Request(url, data=body, method=method)
        request.add_header("Accept", "application/json")
        request.add_header("Authorization", "Bearer lm-studio")
        if body is not None:
            request.add_header("Content-Type", "application/json")
        try:
            with urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8")), attempt
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
        except (TimeoutError, socket.timeout, URLError, ConnectionResetError) as exc:
            last_error = exc
            if attempt == 2:
                raise RuntimeError(f"TRANSPORT_RETRY_EXHAUSTED: {exc}") from exc
            time.sleep(2)
    raise RuntimeError(f"UNREACHABLE_TRANSPORT_STATE: {last_error}")


def verify_environment() -> tuple[Path, str, list[dict[str, str]]]:
    verify_frozen_files()
    items = load_stimuli()
    model_path = find_model_file()
    actual_model_sha = sha256_file(model_path)
    if actual_model_sha != MODEL_SHA256:
        raise RuntimeError(
            f"MODEL_SHA256_MISMATCH: expected={MODEL_SHA256} actual={actual_model_sha}"
        )
    models, attempts = http_json("GET", f"{API_BASE}/models", timeout=60)
    model_ids = [entry.get("id") for entry in models.get("data", [])]
    if MODEL_ID not in model_ids:
        raise RuntimeError(f"API_MODEL_NOT_FOUND: expected={MODEL_ID} available={model_ids}")
    print("FROZEN PACKAGE: PASS")
    print(f"FROZEN FILES CHECKED: {len(load_manifest())}")
    print(f"MODEL SHA256: PASS {actual_model_sha}")
    print(f"API MODEL: PASS {MODEL_ID}")
    print(f"ELIGIBILITY DESIGN: PASS (12 items, 36 planned calls)")
    print(f"MODEL LIST TRANSPORT ATTEMPTS: {attempts}")
    return model_path, actual_model_sha, items


def opposite(claim: str) -> str:
    return "CLAIM_B" if claim == "CLAIM_A" else "CLAIM_A"


def value_for(item: dict[str, str], claim: str) -> str:
    return item["claim_a_value"] if claim == "CLAIM_A" else item["claim_b_value"]


def claim_header(item: dict[str, str]) -> str:
    claims = ["CLAIM_A", "CLAIM_B"]
    if item["presentation_order"] == "B_FIRST":
        claims.reverse()
    return "\n".join(f"{claim} = {value_for(item, claim)}" for claim in claims)


def source_record(item: dict[str, str], source_id: str, evidence_id: str, claim: str, reliability: float) -> str:
    other = opposite(claim)
    return (
        f"{evidence_id}: independent external source {source_id}; reliability={reliability:.2f}. "
        f"For target device {item['entity']}, it reports {claim} ({value_for(item, claim)}) "
        f"and rejects {other} ({value_for(item, other)})."
    )


def build_prompt(item: dict[str, str], condition: str) -> tuple[str, str]:
    initial = item["initial_supported_claim"]
    counter = opposite(initial)
    if condition == "baseline_initial":
        memory = [source_record(item, "S1", "E1", initial, 0.65)]
        new_evidence = "No additional evidence is supplied."
        expected = initial
    elif condition == "counter_single_strong":
        memory = [source_record(item, "S1", "E1", initial, 0.65)]
        new_evidence = source_record(item, "SC", "C1", counter, 0.80)
        expected = counter
    elif condition == "independent_five_initial":
        memory = [
            source_record(item, f"S{k}", f"E{k}", initial, 0.65)
            for k in range(1, 6)
        ]
        new_evidence = source_record(item, "SC", "C1", counter, 0.80)
        expected = initial
    else:
        raise RuntimeError(f"UNKNOWN_CONDITION: {condition}")

    prompt = (
        f"TARGET DEVICE: {item['entity']}\n{claim_header(item)}\n"
        f"INITIAL = {initial}\nCOUNTER = {counter}\n\n"
        "PERSISTENT MEMORY:\n" + "\n".join(memory) + "\n\n"
        "NEW INDEPENDENT EVIDENCE:\n" + new_evidence + "\n\n"
        "Choose which claim is more likely to be true after considering all supplied evidence. "
        "confidence_chosen is a percentage from 0 to 100, not a source count. "
        "Return only the requested structured fields."
    )
    return prompt, expected


def response_format() -> dict[str, Any]:
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "iaer_v0_5_2_eligibility_choice",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "chosen_claim": {"type": "string", "enum": ["CLAIM_A", "CLAIM_B"]},
                    "confidence_chosen": {"type": "number", "minimum": 0, "maximum": 100},
                },
                "required": ["chosen_claim", "confidence_chosen"],
                "additionalProperties": False,
            },
        },
    }


def collect_one(item: dict[str, str], condition: str) -> tuple[dict[str, Any], dict[str, Any]]:
    prompt, expected = build_prompt(item, condition)
    payload = {
        "model": MODEL_ID,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
        "temperature": TEMPERATURE,
        "seed": SEED,
        "max_tokens": MAX_TOKENS,
        "stream": False,
        "response_format": response_format(),
    }
    response, attempts = http_json("POST", f"{API_BASE}/chat/completions", payload)
    try:
        choice = response["choices"][0]
        message = choice["message"]
        content = message["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError("MALFORMED_API_RESPONSE") from exc
    if choice.get("finish_reason") != "stop":
        raise RuntimeError(f"NON_STOP_FINISH_REASON: {choice.get('finish_reason')!r}")
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("EMPTY_FINAL_CONTENT")
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"UNPARSABLE_JSON: {content[:300]!r}") from exc
    if set(parsed) != {"chosen_claim", "confidence_chosen"}:
        raise RuntimeError(f"SCHEMA_KEYS_INVALID: {parsed}")
    if parsed["chosen_claim"] not in {"CLAIM_A", "CLAIM_B"}:
        raise RuntimeError(f"CHOSEN_CLAIM_INVALID: {parsed}")
    confidence = parsed["confidence_chosen"]
    if isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not 0 <= confidence <= 100:
        raise RuntimeError(f"CONFIDENCE_INVALID: {parsed}")
    diag = {
        "transport_attempts": attempts,
        "finish_reason": choice.get("finish_reason"),
        "reasoning_content_present": bool(message.get("reasoning") or message.get("reasoning_content")),
        "usage": response.get("usage"),
        "raw_final_content": content,
    }
    return {**parsed, "expected_claim": expected}, diag


def read_existing_rows() -> tuple[list[dict[str, Any]], set[tuple[str, str]]]:
    rows: list[dict[str, Any]] = []
    valid_keys: set[tuple[str, str]] = set()
    if not RESULTS_PATH.exists():
        return rows, valid_keys
    for line_no, line in enumerate(RESULTS_PATH.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"EXISTING_RESULTS_MALFORMED line={line_no}") from exc
        rows.append(row)
        if row.get("status") != "valid":
            raise RuntimeError("RECORDED_FAILURE_EXISTS: frozen collection must not resume")
        key = (row.get("item_id"), row.get("condition"))
        if key in valid_keys:
            raise RuntimeError(f"DUPLICATE_VALID_KEY: {key}")
        valid_keys.add(key)
    return rows, valid_keys


def append_row(row: dict[str, Any]) -> None:
    with RESULTS_PATH.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def collect() -> None:
    _, actual_model_sha, items = verify_environment()
    existing_rows, valid_keys = read_existing_rows()
    expected_keys = {(item["item_id"], condition) for item in items for condition in CONDITIONS}
    if not valid_keys <= expected_keys:
        raise RuntimeError("EXISTING_RESULTS_CONTAIN_UNPLANNED_KEYS")
    print(f"EXISTING VALID ROWS: {len(existing_rows)}")
    print("BEGINNING/RESUMING BLINDED ELIGIBILITY COLLECTION")

    schedule = [(item, condition) for item in items for condition in CONDITIONS]
    random.Random(ORDER_SEED).shuffle(schedule)
    manifest_sha = sha256_file(MANIFEST_PATH)

    for sequence, (item, condition) in enumerate(schedule, 1):
        key = (item["item_id"], condition)
        if key in valid_keys:
            continue
        started = time.monotonic()
        started_utc = utc_now()
        try:
            output, diagnostics = collect_one(item, condition)
            row = {
                "status": "valid",
                "sequence": sequence,
                "item_id": item["item_id"],
                "entity": item["entity"],
                "claim_a_value": item["claim_a_value"],
                "claim_b_value": item["claim_b_value"],
                "initial_supported_claim": item["initial_supported_claim"],
                "counter_claim": opposite(item["initial_supported_claim"]),
                "presentation_order": item["presentation_order"],
                "condition": condition,
                "expected_claim": output["expected_claim"],
                "chosen_claim": output["chosen_claim"],
                "confidence_chosen": output["confidence_chosen"],
                "correct": int(output["chosen_claim"] == output["expected_claim"]),
                "model": MODEL_ID,
                "model_filename": MODEL_FILENAME,
                "model_sha256": actual_model_sha,
                "api_base": API_BASE,
                "temperature": TEMPERATURE,
                "seed": SEED,
                "max_tokens": MAX_TOKENS,
                "timeout_seconds": TIMEOUT,
                "started_at_utc": started_utc,
                "completed_at_utc": utc_now(),
                "duration_seconds": round(time.monotonic() - started, 3),
                "diagnostics": diagnostics,
                "run_meta": {
                    "python": platform.python_version(),
                    "platform": platform.platform(),
                    "manifest_sha256": manifest_sha,
                    "preregistration_sha256": sha256_file(HERE / "PREREGISTRATION_v0_5_2.md"),
                    "stimuli_sha256": sha256_file(STIMULI_PATH),
                    "rationale_sha256": sha256_file(HERE / "RATIONALE_v0_5_2.md"),
                },
            }
        except Exception as exc:
            row = {
                "status": "technical_failure",
                "sequence": sequence,
                "item_id": item["item_id"],
                "condition": condition,
                "model": MODEL_ID,
                "model_sha256": actual_model_sha,
                "temperature": TEMPERATURE,
                "seed": SEED,
                "started_at_utc": started_utc,
                "completed_at_utc": utc_now(),
                "duration_seconds": round(time.monotonic() - started, 3),
                "error_type": type(exc).__name__,
                "error": str(exc),
                "run_meta": {"manifest_sha256": manifest_sha},
            }
            append_row(row)
            print(f"{sequence:02d}/36 {item['item_id']} {condition} TECHNICAL_FAILURE")
            raise RuntimeError("ELIGIBILITY_PILOT_STOPPED_FAIL_CLOSED; do not resume") from exc

        append_row(row)
        valid_keys.add(key)
        print(f"{sequence:02d}/36 {item['item_id']} {condition} VALID")

    print(f"ELIGIBILITY COLLECTION COMPLETE: {len(valid_keys)} / 36 valid keys")
    print(f"SAVED: {RESULTS_PATH.name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("verify", "collect"))
    args = parser.parse_args()
    if args.command == "verify":
        verify_environment()
    else:
        collect()


if __name__ == "__main__":
    main()
