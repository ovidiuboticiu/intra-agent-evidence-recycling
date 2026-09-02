#!/usr/bin/env python3
"""Frozen runner for IAER v0.5.0 cross-family replication."""

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
EXPECTED_SMOKE_SHA256 = "487dd8fc581fe206ef6dfb021f92d42267370aa60c42e2278c350f0abadf67f7"
MODEL_FILE_DEFAULT = (
    Path.home()
    / ".lmstudio"
    / "models"
    / "bartowski"
    / "microsoft_Phi-4-mini-instruct-GGUF"
    / "microsoft_Phi-4-mini-instruct-Q4_K_M.gguf"
)
CORE_CONDITIONS = ["source_only", "neutral_filler", "passive_repeat"]
PREFLIGHT_PATH = HERE / "preflight_v0_5_0.json"
RESULTS_PATH = HERE / "results_v0_5_0.jsonl"

SYSTEM = (
    "You are an experimental decision agent in a fully fictional binary world. "
    "Use only information supplied in this request. "
    "CLAIM_A and CLAIM_B are mutually exclusive and exhaustive. "
    "The prior probability before evidence is 50/50. "
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
    return ids, attempts


def response_format_belief():
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "belief",
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


def response_format_provenance(ids):
    return {
        "type": "json_schema",
        "json_schema": {
            "name": "provenance",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "independent_external_evidence_ids": {
                        "type": "array",
                        "items": {"type": "string", "enum": ids},
                        "uniqueItems": True,
                    }
                },
                "required": ["independent_external_evidence_ids"],
                "additionalProperties": False,
            },
        },
    }


def chat_json(base_url, messages, response_format, max_tokens=96, timeout=240):
    payload = {
        "model": EXPECTED_MODEL,
        "messages": messages,
        "temperature": 0.0,
        "seed": 42,
        "max_tokens": max_tokens,
        "stream": False,
        "response_format": response_format,
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


def value_for(item, claim):
    return item["claim_a_value"] if claim == "CLAIM_A" else item["claim_b_value"]


def opposite(claim):
    return "CLAIM_B" if claim == "CLAIM_A" else "CLAIM_A"


def claim_header(item):
    order = ["CLAIM_A", "CLAIM_B"] if item["presentation_order"] == "A_FIRST" else ["CLAIM_B", "CLAIM_A"]
    return "\n".join(f"{claim} = {value_for(item, claim)}" for claim in order)


def memory_text(entries):
    return "\n".join(f"{entry['id']}: {entry['text']}" for entry in entries)


def initial_source(item, evidence_id="E1", source_id="S1"):
    initial = item["initial_supported_claim"]
    counter = opposite(initial)
    return {
        "id": evidence_id,
        "text": (
            f"independent external source {source_id}; reliability=0.65. "
            f"For target device {item['entity']}, it reports {initial} ({value_for(item, initial)}) "
            f"and rejects {counter} ({value_for(item, counter)})."
        ),
    }


def neutral_fillers(item):
    return [
        {
            "id": f"E{index}",
            "text": (
                f"unrelated memory record about auxiliary device AUX{index}; "
                f"it reports auxiliary state U{index} and contains no information about "
                f"target device {item['entity']}."
            ),
        }
        for index in range(2, 7)
    ]


def build_memory(item, condition):
    if condition == "source_only":
        return [initial_source(item)]
    if condition == "neutral_filler":
        return [initial_source(item)] + neutral_fillers(item)
    if condition == "passive_repeat":
        initial = item["initial_supported_claim"]
        return [initial_source(item)] + [
            {
                "id": f"E{review + 1}",
                "text": (
                    f"review {review} of E1 only; this is not a new external source. "
                    f"It repeats E1's report for target {item['entity']}: "
                    f"{initial} ({value_for(item, initial)})."
                ),
            }
            for review in range(1, 6)
        ]
    if condition == "independent_evidence":
        initial = item["initial_supported_claim"]
        counter = opposite(initial)
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
            for index in range(1, 6)
        ]
    raise ValueError(f"UNKNOWN_CONDITION {condition!r}")


def true_roots(condition):
    if condition == "independent_evidence":
        return ["E1", "E2", "E3", "E4", "E5"]
    return ["E1"]


def provenance_probe(base_url, item, entries, timeout=240):
    ids = [entry["id"] for entry in entries]
    initial = item["initial_supported_claim"]
    prompt = (
        f"TARGET DEVICE: {item['entity']}\n{claim_header(item)}\nINITIAL = {initial}\n\n"
        "MEMORY RECORDS:\n"
        + memory_text(entries)
        + "\n\nPROVENANCE AUDIT: Select the IDs of records that are themselves genuinely independent "
        "EXTERNAL evidence about this target device supporting INITIAL. Reviews, copies, unrelated "
        "records, summaries, and the agent's own application traces are not new independent external "
        "evidence. Return only the requested structured field."
    )
    parsed, diagnostics = chat_json(
        base_url,
        [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        response_format_provenance(ids),
        max_tokens=96,
        timeout=timeout,
    )
    got = parsed.get("independent_external_evidence_ids")
    if not isinstance(got, list) or len(got) != len(set(got)) or any(value not in ids for value in got):
        raise RuntimeError(f"INVALID_PROVENANCE_OUTPUT {parsed!r}")
    return parsed, diagnostics


def belief_probe(base_url, item, entries, timeout=240):
    initial = item["initial_supported_claim"]
    counter = opposite(initial)
    counterevidence = (
        f"C1: independent external source SC; reliability=0.80. "
        f"For target device {item['entity']}, it reports {counter} ({value_for(item, counter)}) "
        f"and rejects {initial} ({value_for(item, initial)})."
    )
    prompt = (
        f"TARGET DEVICE: {item['entity']}\n{claim_header(item)}\n"
        f"INITIAL = {initial}\nCOUNTER = {counter}\n\n"
        "PERSISTENT MEMORY:\n"
        + memory_text(entries)
        + "\n\nNEW INDEPENDENT EVIDENCE:\n"
        + counterevidence
        + "\n\nChoose which claim is more likely to be true after considering the persistent memory "
        "and new evidence. Do not perform an explicit provenance audit unless you naturally need one. "
        "confidence_chosen is a percentage 0-100, not a source count. Return only the requested "
        "structured fields."
    )
    parsed, diagnostics = chat_json(
        base_url,
        [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        response_format_belief(),
        max_tokens=96,
        timeout=timeout,
    )
    if parsed.get("chosen_claim") not in {"CLAIM_A", "CLAIM_B"}:
        raise RuntimeError(f"INVALID_BELIEF_CLAIM {parsed!r}")
    confidence = parsed.get("confidence_chosen")
    if isinstance(confidence, bool) or not isinstance(confidence, (int, float)) or not 0 <= confidence <= 100:
        raise RuntimeError(f"INVALID_BELIEF_CONFIDENCE {parsed!r}")
    return parsed, diagnostics


def load_items():
    path = HERE / "stimuli_v0_5_0.csv"
    with open(path, encoding="utf-8", newline="") as handle:
        items = list(csv.DictReader(handle))
    if len(items) != 32:
        raise RuntimeError(f"STIMULUS_COUNT expected=32 got={len(items)}")
    required = {
        "item_id",
        "entity",
        "claim_a_value",
        "claim_b_value",
        "initial_supported_claim",
        "presentation_order",
        "positive_control",
    }
    if set(items[0]) != required:
        raise RuntimeError(f"STIMULUS_COLUMNS expected={sorted(required)} got={sorted(items[0])}")
    for field in ["item_id", "entity", "claim_a_value", "claim_b_value"]:
        values = [item[field] for item in items]
        if len(values) != len(set(values)):
            raise RuntimeError(f"STIMULUS_DUPLICATE_FIELD {field}")
    all_claim_values = [value for item in items for value in [item["claim_a_value"], item["claim_b_value"]]]
    if len(all_claim_values) != len(set(all_claim_values)):
        raise RuntimeError("STIMULUS_DUPLICATE_CLAIM_VALUE")
    cells = {}
    positive_cells = {}
    for initial in ["CLAIM_A", "CLAIM_B"]:
        for presentation in ["A_FIRST", "B_FIRST"]:
            key = (initial, presentation)
            cells[key] = sum(
                item["initial_supported_claim"] == initial and item["presentation_order"] == presentation
                for item in items
            )
            positive_cells[key] = sum(
                item["initial_supported_claim"] == initial
                and item["presentation_order"] == presentation
                and item["positive_control"] == "1"
                for item in items
            )
    if set(cells.values()) != {8} or set(positive_cells.values()) != {2}:
        raise RuntimeError(f"STIMULUS_BALANCE cells={cells!r} positive_cells={positive_cells!r}")
    if any(item["positive_control"] not in {"0", "1"} for item in items):
        raise RuntimeError("STIMULUS_POSITIVE_CONTROL_ENCODING")
    return items


def planned_keys(items):
    keys = set()
    for item in items:
        for condition in CORE_CONDITIONS:
            keys.add((item["item_id"], condition))
        if item["positive_control"] == "1":
            keys.add((item["item_id"], "independent_evidence"))
    if len(keys) != 104:
        raise RuntimeError(f"PLANNED_KEY_COUNT expected=104 got={len(keys)}")
    return keys


def verify_manifest():
    manifest = HERE / "FREEZE_MANIFEST_v0_5_0.sha256"
    if not manifest.exists():
        raise RuntimeError("FREEZE_MANIFEST_MISSING")
    checked = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        expected, relative = line.split("  ", 1)
        path = HERE / relative
        if not path.is_file():
            raise RuntimeError(f"FROZEN_FILE_MISSING {relative}")
        got = sha256(path)
        if got != expected:
            raise RuntimeError(f"FROZEN_HASH_MISMATCH {relative} expected={expected} got={got}")
        checked.append(relative)
    if not checked:
        raise RuntimeError("FREEZE_MANIFEST_EMPTY")
    return checked


def verify_smoke_result():
    path = HERE / "technical_smoke_result_v0_5_0.json"
    if sha256(path) != EXPECTED_SMOKE_SHA256:
        raise RuntimeError("TECHNICAL_SMOKE_HASH_MISMATCH")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("scientific_data") is not False or data.get("passed") is not True:
        raise RuntimeError("TECHNICAL_SMOKE_NOT_PASSING")
    if data.get("expected_model") != EXPECTED_MODEL:
        raise RuntimeError("TECHNICAL_SMOKE_MODEL_MISMATCH")
    if data.get("diagnostics", {}).get("reasoning_present") is not False:
        raise RuntimeError("TECHNICAL_SMOKE_REASONING_PRESENT")


def verify_environment(base_url, model_file):
    checked = verify_manifest()
    verify_smoke_result()
    model_file = Path(model_file)
    if not model_file.is_file():
        raise RuntimeError(f"MODEL_FILE_NOT_FOUND {model_file}")
    model_hash = sha256(model_file)
    if model_hash != EXPECTED_MODEL_SHA256:
        raise RuntimeError(
            f"MODEL_HASH_MISMATCH expected={EXPECTED_MODEL_SHA256} got={model_hash}"
        )
    ids, model_attempts = require_model(base_url)
    load_items()
    print("FROZEN PACKAGE: PASS")
    print("FROZEN FILES CHECKED:", len(checked))
    print("MODEL SHA256: PASS", model_hash)
    print("API MODEL: PASS", EXPECTED_MODEL)
    print("STIMULUS DESIGN: PASS (32 items, 104 planned trajectories)")
    print("MODEL LIST TRANSPORT ATTEMPTS:", model_attempts)
    return ids


def preflight_cases():
    return [
        {
            "item": {
                "item_id": "PF5_A",
                "entity": "SENTINEL_OMICRON",
                "claim_a_value": "KAFU",
                "claim_b_value": "ZERI",
                "initial_supported_claim": "CLAIM_A",
                "presentation_order": "A_FIRST",
                "positive_control": "0",
            },
            "condition": "source_only",
            "expected": "CLAIM_B",
        },
        {
            "item": {
                "item_id": "PF5_A",
                "entity": "SENTINEL_OMICRON",
                "claim_a_value": "KAFU",
                "claim_b_value": "ZERI",
                "initial_supported_claim": "CLAIM_A",
                "presentation_order": "A_FIRST",
                "positive_control": "0",
            },
            "condition": "independent_evidence",
            "expected": "CLAIM_A",
        },
        {
            "item": {
                "item_id": "PF5_B",
                "entity": "SENTINEL_SIGMA",
                "claim_a_value": "BREG",
                "claim_b_value": "WONU",
                "initial_supported_claim": "CLAIM_B",
                "presentation_order": "B_FIRST",
                "positive_control": "0",
            },
            "condition": "source_only",
            "expected": "CLAIM_A",
        },
        {
            "item": {
                "item_id": "PF5_B",
                "entity": "SENTINEL_SIGMA",
                "claim_a_value": "BREG",
                "claim_b_value": "WONU",
                "initial_supported_claim": "CLAIM_B",
                "presentation_order": "B_FIRST",
                "positive_control": "0",
            },
            "condition": "independent_evidence",
            "expected": "CLAIM_B",
        },
    ]


def run_preflight(base_url, model_file, timeout):
    if PREFLIGHT_PATH.exists():
        raise RuntimeError(
            "PREFLIGHT_FILE_ALREADY_EXISTS. Do not rerun or overwrite the behavioral preflight."
        )
    verify_environment(base_url, model_file)
    rows = []
    for number, case in enumerate(preflight_cases(), start=1):
        started = time.time()
        item = case["item"]
        condition = case["condition"]
        try:
            memory = build_memory(item, condition)
            belief, diagnostics = belief_probe(base_url, item, memory, timeout=timeout)
            got = belief["chosen_claim"]
            row = {
                "case": number,
                "status": "valid",
                "item_id": item["item_id"],
                "condition": condition,
                "initial": item["initial_supported_claim"],
                "expected": case["expected"],
                "got": got,
                "pass": got == case["expected"],
                "belief": belief,
                "memory": memory,
                "diagnostics": diagnostics,
                "duration_sec": time.time() - started,
            }
        except Exception as exc:
            row = {
                "case": number,
                "status": "technical_failure",
                "item_id": item["item_id"],
                "condition": condition,
                "initial": item["initial_supported_claim"],
                "expected": case["expected"],
                "pass": False,
                "error": repr(exc),
                "duration_sec": time.time() - started,
            }
            rows.append(row)
            break
        rows.append(row)

    passed = len(rows) == 4 and all(row["pass"] for row in rows)
    record = {
        "study": "IAER v0.5.0",
        "phase": "mandatory behavioral preflight",
        "scientific_data": False,
        "validity_gate": True,
        "timestamp_utc": utc_now(),
        "model": EXPECTED_MODEL,
        "model_sha256": EXPECTED_MODEL_SHA256,
        "temperature": 0.0,
        "seed": 42,
        "timeout": timeout,
        "passed": passed,
        "cases": rows,
        "frozen_manifest_sha256": sha256(HERE / "FREEZE_MANIFEST_v0_5_0.sha256"),
        "python": platform.python_version(),
        "platform": platform.platform(),
    }
    PREFLIGHT_PATH.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("\n=== MANDATORY BEHAVIORAL PREFLIGHT ===")
    for row in rows:
        print(
            f"CASE {row['case']}: {row['condition']} initial={row['initial']} "
            f"expected={row['expected']} got={row.get('got', 'TECHNICAL_FAILURE')} "
            f"-> {'PASS' if row['pass'] else 'FAIL'}"
        )
    print("PREFLIGHT RESULT:", "PASS" if passed else "FAIL — v0.5.0 INVALID/INCONCLUSIVE")
    print("SAVED:", PREFLIGHT_PATH.name)
    if not passed:
        raise RuntimeError("BEHAVIORAL_PREFLIGHT_FAILED; do not run confirmatory collection")


def require_passing_preflight():
    if not PREFLIGHT_PATH.is_file():
        raise RuntimeError("PREFLIGHT_MISSING; run 01_RUN_BEHAVIORAL_PREFLIGHT.bat first")
    record = json.loads(PREFLIGHT_PATH.read_text(encoding="utf-8"))
    if record.get("passed") is not True or len(record.get("cases", [])) != 4:
        raise RuntimeError("PREFLIGHT_NOT_PASSING; confirmatory collection is prohibited")
    if record.get("model") != EXPECTED_MODEL or record.get("model_sha256") != EXPECTED_MODEL_SHA256:
        raise RuntimeError("PREFLIGHT_IDENTITY_MISMATCH")
    if record.get("frozen_manifest_sha256") != sha256(HERE / "FREEZE_MANIFEST_v0_5_0.sha256"):
        raise RuntimeError("PREFLIGHT_MANIFEST_MISMATCH")
    return sha256(PREFLIGHT_PATH)


def read_existing_results(expected_keys):
    valid_keys = set()
    failure_count = 0
    if not RESULTS_PATH.exists():
        return valid_keys, failure_count
    for line_number, line in enumerate(RESULTS_PATH.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except Exception as exc:
            raise RuntimeError(f"MALFORMED_EXISTING_RESULT line={line_number} error={exc!r}") from exc
        key = (row.get("item_id"), row.get("condition"))
        if key not in expected_keys:
            raise RuntimeError(f"EXTRA_EXISTING_KEY line={line_number} key={key!r}")
        if row.get("status") == "valid":
            if key in valid_keys:
                raise RuntimeError(f"DUPLICATE_VALID_KEY line={line_number} key={key!r}")
            if row.get("model") != EXPECTED_MODEL or row.get("model_sha256") != EXPECTED_MODEL_SHA256:
                raise RuntimeError(f"EXISTING_RESULT_IDENTITY_MISMATCH line={line_number}")
            valid_keys.add(key)
        else:
            failure_count += 1
    return valid_keys, failure_count


def append_row(row):
    with open(RESULTS_PATH, "a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        handle.flush()


def run_confirmatory(base_url, model_file, timeout):
    verify_environment(base_url, model_file)
    preflight_sha = require_passing_preflight()
    items = load_items()
    expected_keys = planned_keys(items)
    valid_keys, prior_failures = read_existing_results(expected_keys)
    print("EXISTING VALID TRAJECTORIES:", len(valid_keys), "/ 104")
    print("RETAINED TECHNICAL-FAILURE ROWS:", prior_failures)

    item_order = items[:]
    random.Random(20260905).shuffle(item_order)
    for item in item_order:
        conditions = CORE_CONDITIONS[:]
        if item["positive_control"] == "1":
            conditions.append("independent_evidence")
        random.Random(20260905 + int(item["item_id"][1:]) * 7919).shuffle(conditions)
        for condition in conditions:
            key = (item["item_id"], condition)
            if key in valid_keys:
                continue
            started = time.time()
            try:
                memory = build_memory(item, condition)
                provenance, provenance_diagnostics = provenance_probe(
                    base_url, item, memory, timeout=timeout
                )
                belief, belief_diagnostics = belief_probe(
                    base_url, item, memory, timeout=timeout
                )
                true = true_roots(condition)
                got = provenance["independent_external_evidence_ids"]
                initial = item["initial_supported_claim"]
                row = {
                    "status": "valid",
                    "item_id": item["item_id"],
                    "entity": item["entity"],
                    "claim_a_value": item["claim_a_value"],
                    "claim_b_value": item["claim_b_value"],
                    "initial_supported_claim": initial,
                    "counter_claim": opposite(initial),
                    "presentation_order": item["presentation_order"],
                    "positive_control": int(item["positive_control"]),
                    "condition": condition,
                    "model": EXPECTED_MODEL,
                    "model_sha256": EXPECTED_MODEL_SHA256,
                    "temperature": 0.0,
                    "seed": 42,
                    "timeout": timeout,
                    "memory": memory,
                    "true_independent_root_ids": true,
                    "provenance": provenance,
                    "provenance_scores": {
                        "false_independent_ids": [value for value in got if value not in true],
                        "missed_root_ids": [value for value in true if value not in got],
                        "exact_correct": sorted(got) == sorted(true),
                    },
                    "belief": belief,
                    "retain_initial": int(belief["chosen_claim"] == initial),
                    "diagnostics": {
                        "provenance": provenance_diagnostics,
                        "belief": belief_diagnostics,
                        "duration_sec": time.time() - started,
                    },
                    "timestamp_utc": utc_now(),
                    "timestamp_unix": time.time(),
                    "run_meta": {
                        "python": platform.python_version(),
                        "platform": platform.platform(),
                        "preflight_sha256": preflight_sha,
                        "freeze_manifest_sha256": sha256(HERE / "FREEZE_MANIFEST_v0_5_0.sha256"),
                        "prereg_sha256": sha256(HERE / "PREREGISTRATION_v0_5_0.md"),
                        "stimuli_sha256": sha256(HERE / "stimuli_v0_5_0.csv"),
                        "rationale_sha256": sha256(HERE / "RATIONALE_v0_5_0.md"),
                        "environment_sha256": sha256(HERE / "MODEL_ENVIRONMENT_v0_5_0.md"),
                    },
                }
            except Exception as exc:
                row = {
                    "status": "technical_failure",
                    "item_id": item["item_id"],
                    "condition": condition,
                    "model": EXPECTED_MODEL,
                    "model_sha256": EXPECTED_MODEL_SHA256,
                    "temperature": 0.0,
                    "seed": 42,
                    "timeout": timeout,
                    "error": repr(exc),
                    "duration_sec": time.time() - started,
                    "timestamp_utc": utc_now(),
                    "timestamp_unix": time.time(),
                }
            append_row(row)
            if row["status"] != "valid":
                print(item["item_id"], condition, "TECHNICAL_FAILURE")
                raise RuntimeError(
                    "COLLECTION_STOPPED_FAIL_CLOSED. Preserve results and repair only infrastructure."
                )
            valid_keys.add(key)
            print(item["item_id"], condition, "VALID", f"({len(valid_keys)}/104)")

    valid_keys, failures = read_existing_results(expected_keys)
    if valid_keys == expected_keys:
        print("\nCONFIRMATORY COLLECTION COMPLETE: 104/104 VALID UNIQUE KEYS")
        print("TECHNICAL-FAILURE AUDIT ROWS RETAINED:", failures)
        print("You may now run 03_ANALYZE_RESULTS.bat")
    else:
        raise RuntimeError(
            f"COLLECTION_INCOMPLETE valid={len(valid_keys)} expected=104"
        )


def dry_run():
    items = load_items()
    keys = planned_keys(items)
    print(
        json.dumps(
            {
                "items": len(items),
                "core_conditions": CORE_CONDITIONS,
                "positive_control_items": sum(item["positive_control"] == "1" for item in items),
                "planned_trajectories": len(keys),
                "model_calls_per_trajectory": 2,
                "planned_confirmatory_model_calls": len(keys) * 2,
                "behavioral_preflight_cases": 4,
            },
            indent=2,
        )
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phase", choices=["verify", "preflight", "run", "dry-run"])
    parser.add_argument("--base-url", default=BASE_URL)
    parser.add_argument("--model-file", default=str(MODEL_FILE_DEFAULT))
    parser.add_argument("--timeout", type=int, default=240)
    args = parser.parse_args()

    if args.phase == "verify":
        verify_environment(args.base_url, args.model_file)
    elif args.phase == "preflight":
        run_preflight(args.base_url, args.model_file, args.timeout)
    elif args.phase == "run":
        run_confirmatory(args.base_url, args.model_file, args.timeout)
    else:
        dry_run()


if __name__ == "__main__":
    main()
