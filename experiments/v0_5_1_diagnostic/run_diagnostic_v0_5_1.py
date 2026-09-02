#!/usr/bin/env python3
"""Frozen exploratory diagnostic runner for IAER v0.5.1."""

import argparse
import csv
import datetime as dt
import hashlib
import json
import platform
import random
import socket
import time
import urllib.error
import urllib.request
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE_URL = "http://127.0.0.1:1234/v1"
EXPECTED_MODEL = "microsoft_phi-4-mini-instruct"
EXPECTED_MODEL_SHA256 = "01999f17c39cc3074afae5e9c539bc82d45f2dd7faa3917c66cbef76fce8c0c2"
MODEL_FILE_DEFAULT = (
    Path.home()
    / ".lmstudio"
    / "models"
    / "bartowski"
    / "microsoft_Phi-4-mini-instruct-GGUF"
    / "microsoft_Phi-4-mini-instruct-Q4_K_M.gguf"
)
RESULTS_PATH = HERE / "diagnostic_results_v0_5_1.jsonl"
CONDITIONS = ["source_only", "independent_five"]
MODES = ["claim_label", "value_token", "explicit_odds"]

SYSTEM = (
    "You are an experimental decision agent in a fully fictional binary world. "
    "Use only information supplied in this request. CLAIM_A and CLAIM_B are mutually "
    "exclusive and exhaustive. The prior probability before evidence is 50/50. "
    "A source reliability r means the source reports the true claim with probability r. "
    "Sources explicitly described as independent have independent errors conditional on truth. "
    "Do not use real-world knowledge."
)


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def http_json(url, payload=None, timeout=240, max_transport_attempts=2):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    last_error = None
    for attempt in range(1, max_transport_attempts + 1):
        try:
            request = urllib.request.Request(
                url,
                data=data,
                method="GET" if payload is None else "POST",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer lm-studio",
                },
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8")), attempt
        except (TimeoutError, socket.timeout, urllib.error.URLError, ConnectionResetError) as exc:
            last_error = exc
            if attempt == max_transport_attempts:
                raise
            time.sleep(2)
    raise last_error


def require_model(base_url):
    response, attempts = http_json(base_url.rstrip("/") + "/models", timeout=60)
    ids = [entry.get("id") for entry in response.get("data", [])]
    if EXPECTED_MODEL not in ids:
        raise RuntimeError(
            f"EXPECTED_MODEL_NOT_EXPOSED expected={EXPECTED_MODEL!r} found={ids!r}"
        )
    return attempts


def response_format(mode, item):
    if mode == "claim_label":
        field = "chosen_claim"
        enum = ["CLAIM_A", "CLAIM_B"]
    else:
        field = "chosen_value"
        enum = [item["claim_a_value"], item["claim_b_value"]]
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "diagnostic_choice",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    field: {"type": "string", "enum": enum},
                    "confidence_chosen": {"type": "number", "minimum": 0, "maximum": 100},
                },
                "required": [field, "confidence_chosen"],
                "additionalProperties": False,
            },
        },
    }


def chat_json(base_url, messages, schema, timeout=240):
    payload = {
        "model": EXPECTED_MODEL,
        "messages": messages,
        "temperature": 0.0,
        "seed": 42,
        "max_tokens": 96,
        "stream": False,
        "response_format": schema,
    }
    response, attempts = http_json(
        base_url.rstrip("/") + "/chat/completions",
        payload,
        timeout=timeout,
        max_transport_attempts=2,
    )
    try:
        choice = response["choices"][0]
        message = choice["message"]
        content = message["content"]
    except Exception as exc:
        raise RuntimeError(f"MALFORMED_API_RESPONSE {exc!r}") from exc
    if content is None or not str(content).strip():
        raise RuntimeError(
            "EMPTY_FINAL_CONTENT "
            f"reasoning_present={bool(message.get('reasoning') or message.get('reasoning_content'))} "
            f"finish_reason={choice.get('finish_reason')!r}"
        )
    try:
        parsed = json.loads(str(content).strip())
    except Exception as exc:
        raise RuntimeError(
            f"UNPARSABLE_JSON {exc!r}; finish_reason={choice.get('finish_reason')!r}; "
            f"content={str(content)[:300]!r}"
        ) from exc
    diagnostics = {
        "finish_reason": choice.get("finish_reason"),
        "reasoning_present": bool(message.get("reasoning") or message.get("reasoning_content")),
        "usage": response.get("usage"),
        "transport_attempts": attempts,
    }
    return parsed, diagnostics


def opposite(claim):
    return "CLAIM_B" if claim == "CLAIM_A" else "CLAIM_A"


def value_for(item, claim):
    return item["claim_a_value"] if claim == "CLAIM_A" else item["claim_b_value"]


def claim_header(item):
    order = ["CLAIM_A", "CLAIM_B"] if item["presentation_order"] == "A_FIRST" else ["CLAIM_B", "CLAIM_A"]
    return "\n".join(f"{claim} = {value_for(item, claim)}" for claim in order)


def memory_entries(item, condition):
    initial = item["initial_supported_claim"]
    counter = opposite(initial)
    count = 1 if condition == "source_only" else 5
    return [
        {
            "id": f"E{index}",
            "text": (
                f"independent external source S{index}; reliability=0.65. "
                f"For target device {item['entity']}, it reports {initial} "
                f"({value_for(item, initial)}) and rejects {counter} "
                f"({value_for(item, counter)})."
            ),
        }
        for index in range(1, count + 1)
    ]


def build_prompt(item, condition, mode):
    initial = item["initial_supported_claim"]
    counter = opposite(initial)
    entries = memory_entries(item, condition)
    memory = "\n".join(f"{entry['id']}: {entry['text']}" for entry in entries)
    counterevidence = (
        f"C1: independent external source SC; reliability=0.80. "
        f"For target device {item['entity']}, it reports {counter} "
        f"({value_for(item, counter)}) and rejects {initial} "
        f"({value_for(item, initial)})."
    )
    instruction = (
        "Choose which claim is more likely to be true after considering the persistent memory "
        "and new evidence."
    )
    if mode == "explicit_odds":
        instruction += (
            " Start from prior odds 1:1 and combine every conditionally independent report "
            "multiplicatively using its likelihood ratio r/(1-r), reversing the ratio when "
            "the report supports the opposite claim."
        )
    if mode == "claim_label":
        output_instruction = "Return the chosen claim label and confidence only in the requested fields."
    else:
        output_instruction = (
            "Return the fictional value token belonging to the chosen claim and confidence only "
            "in the requested fields."
        )
    return (
        f"TARGET DEVICE: {item['entity']}\n{claim_header(item)}\n"
        f"INITIAL = {initial}\nCOUNTER = {counter}\n\n"
        "PERSISTENT MEMORY:\n"
        + memory
        + "\n\nNEW INDEPENDENT EVIDENCE:\n"
        + counterevidence
        + "\n\n"
        + instruction
        + " confidence_chosen is a percentage 0-100, not a source count. "
        + output_instruction
    )


def load_items():
    with open(HERE / "stimuli_v0_5_1.csv", encoding="utf-8", newline="") as handle:
        items = list(csv.DictReader(handle))
    expected_columns = {
        "item_id",
        "entity",
        "claim_a_value",
        "claim_b_value",
        "initial_supported_claim",
        "presentation_order",
    }
    if len(items) != 8 or not items or set(items[0]) != expected_columns:
        raise RuntimeError("INVALID_STIMULUS_SHAPE")
    for field in ["item_id", "entity", "claim_a_value", "claim_b_value"]:
        values = [row[field] for row in items]
        if len(values) != len(set(values)):
            raise RuntimeError(f"DUPLICATE_STIMULUS_FIELD {field}")
    tokens = [token for row in items for token in [row["claim_a_value"], row["claim_b_value"]]]
    if len(tokens) != len(set(tokens)):
        raise RuntimeError("DUPLICATE_CLAIM_VALUE")
    cells = {
        (initial, order): sum(
            row["initial_supported_claim"] == initial and row["presentation_order"] == order
            for row in items
        )
        for initial in ["CLAIM_A", "CLAIM_B"]
        for order in ["A_FIRST", "B_FIRST"]
    }
    if set(cells.values()) != {2}:
        raise RuntimeError(f"UNBALANCED_STIMULI {cells!r}")
    return items


def planned_tasks(items):
    tasks = [
        {"item": item, "condition": condition, "mode": mode}
        for item in items
        for condition in CONDITIONS
        for mode in MODES
    ]
    random.Random(510).shuffle(tasks)
    if len(tasks) != 48:
        raise RuntimeError("INVALID_TASK_COUNT")
    return tasks


def verify_manifest():
    manifest = HERE / "FREEZE_MANIFEST_v0_5_1.sha256"
    if not manifest.is_file():
        raise RuntimeError("FREEZE_MANIFEST_MISSING")
    checked = 0
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        path = HERE / relative
        if not path.is_file():
            raise RuntimeError(f"FROZEN_FILE_MISSING {relative}")
        got = sha256(path)
        if got != expected:
            raise RuntimeError(f"FROZEN_FILE_HASH_MISMATCH {relative} expected={expected} got={got}")
        checked += 1
    return checked


def verify_environment(base_url, model_file):
    checked = verify_manifest()
    items = load_items()
    tasks = planned_tasks(items)
    model_file = Path(model_file)
    if not model_file.is_file():
        raise RuntimeError(f"MODEL_FILE_NOT_FOUND {model_file}")
    model_hash = sha256(model_file)
    if model_hash != EXPECTED_MODEL_SHA256:
        raise RuntimeError(
            f"MODEL_HASH_MISMATCH expected={EXPECTED_MODEL_SHA256} got={model_hash}"
        )
    model_attempts = require_model(base_url)
    print("DIAGNOSTIC PACKAGE: PASS")
    print("FROZEN FILES CHECKED:", checked)
    print("MODEL SHA256: PASS", model_hash)
    print("API MODEL: PASS", EXPECTED_MODEL)
    print("DIAGNOSTIC DESIGN: PASS (8 items, 48 planned calls)")
    print("MODEL LIST TRANSPORT ATTEMPTS:", model_attempts)
    return items, tasks, model_hash


def load_existing_rows():
    if not RESULTS_PATH.exists():
        return []
    rows = []
    with open(RESULTS_PATH, encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except Exception as exc:
                raise RuntimeError(f"INVALID_EXISTING_JSONL line={number} error={exc!r}") from exc
    return rows


def task_key(item_id, condition, mode):
    return item_id, condition, mode


def map_output_to_claim(parsed, mode, item):
    if mode == "claim_label":
        observed = parsed.get("chosen_claim")
        if observed not in {"CLAIM_A", "CLAIM_B"}:
            raise RuntimeError(f"INVALID_CHOSEN_CLAIM {parsed!r}")
        return observed
    observed_value = parsed.get("chosen_value")
    mapping = {
        item["claim_a_value"]: "CLAIM_A",
        item["claim_b_value"]: "CLAIM_B",
    }
    if observed_value not in mapping:
        raise RuntimeError(f"INVALID_CHOSEN_VALUE {parsed!r}")
    return mapping[observed_value]


def run_collection(base_url, model_file, timeout):
    items, tasks, model_hash = verify_environment(base_url, model_file)
    del items
    existing = load_existing_rows()
    valid_keys = set()
    for row in existing:
        if row.get("status") != "valid":
            continue
        key = task_key(row.get("item_id"), row.get("condition"), row.get("mode"))
        if key in valid_keys:
            raise RuntimeError(f"DUPLICATE_VALID_EXISTING_KEY {key!r}")
        valid_keys.add(key)
    print("EXISTING VALID ROWS:", len(valid_keys))
    print("BEGINNING/RESUMING BLINDED DIAGNOSTIC COLLECTION")
    with open(RESULTS_PATH, "a", encoding="utf-8", newline="\n") as handle:
        for sequence, task in enumerate(tasks, start=1):
            item = task["item"]
            condition = task["condition"]
            mode = task["mode"]
            key = task_key(item["item_id"], condition, mode)
            if key in valid_keys:
                continue
            started = time.time()
            try:
                prompt = build_prompt(item, condition, mode)
                parsed, diagnostics = chat_json(
                    base_url,
                    [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
                    response_format(mode, item),
                    timeout=timeout,
                )
                confidence = parsed.get("confidence_chosen")
                if isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not 0 <= confidence <= 100:
                    raise RuntimeError(f"INVALID_CONFIDENCE {parsed!r}")
                observed = map_output_to_claim(parsed, mode, item)
                initial = item["initial_supported_claim"]
                expected = opposite(initial) if condition == "source_only" else initial
                row = {
                    "study": "IAER v0.5.1 diagnostic",
                    "status": "valid",
                    "timestamp_utc": utc_now(),
                    "sequence": sequence,
                    "item_id": item["item_id"],
                    "entity": item["entity"],
                    "initial": initial,
                    "presentation_order": item["presentation_order"],
                    "condition": condition,
                    "mode": mode,
                    "expected_claim": expected,
                    "observed_claim": observed,
                    "normative_correct": observed == expected,
                    "raw_response": parsed,
                    "diagnostics": diagnostics,
                    "model": EXPECTED_MODEL,
                    "model_sha256": model_hash,
                    "temperature": 0.0,
                    "seed": 42,
                    "duration_sec": time.time() - started,
                    "freeze_manifest_sha256": sha256(HERE / "FREEZE_MANIFEST_v0_5_1.sha256"),
                    "python": platform.python_version(),
                    "platform": platform.platform(),
                }
            except Exception as exc:
                row = {
                    "study": "IAER v0.5.1 diagnostic",
                    "status": "technical_failure",
                    "timestamp_utc": utc_now(),
                    "sequence": sequence,
                    "item_id": item["item_id"],
                    "entity": item["entity"],
                    "initial": item["initial_supported_claim"],
                    "presentation_order": item["presentation_order"],
                    "condition": condition,
                    "mode": mode,
                    "error": repr(exc),
                    "model": EXPECTED_MODEL,
                    "model_sha256": model_hash,
                    "duration_sec": time.time() - started,
                }
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                handle.flush()
                print(f"{sequence:02d}/48 {item['item_id']} {condition} {mode} TECHNICAL_FAILURE")
                raise RuntimeError(
                    "COLLECTION_STOPPED_FAIL_CLOSED. Preserve results and repair only infrastructure."
                ) from exc
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            handle.flush()
            valid_keys.add(key)
            print(f"{sequence:02d}/48 {item['item_id']} {condition} {mode} VALID")
    print("DIAGNOSTIC COLLECTION COMPLETE:", len(valid_keys), "/ 48 valid keys")
    print("SAVED:", RESULTS_PATH.name)


def dry_run():
    items = load_items()
    tasks = planned_tasks(items)
    print("ITEMS:", len(items))
    print("TASKS:", len(tasks))
    print("CONDITIONS:", CONDITIONS)
    print("MODES:", MODES)
    print("BALANCED CELLS: 2 items per INITIAL x presentation-order cell")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=["verify", "run", "dry-run"])
    parser.add_argument("--base-url", default=BASE_URL)
    parser.add_argument("--model-file", default=str(MODEL_FILE_DEFAULT))
    parser.add_argument("--timeout", type=int, default=240)
    args = parser.parse_args()
    if args.phase == "verify":
        verify_environment(args.base_url, args.model_file)
    elif args.phase == "run":
        run_collection(args.base_url, args.model_file, args.timeout)
    else:
        dry_run()


if __name__ == "__main__":
    main()
