from __future__ import annotations

import hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

EXPECTED={
    "experiments/v0_3_1/results_v0_3_1.jsonl":"c5fe7f0b645d8997488dc6bedaec305409ccc0b970a3187d98ada940f1d296de",
    "experiments/v0_3_1/stimuli_v0_3.csv":"224f910339a7766e43c107fd9f1ea86a2be01ce22c730e64e08bb89298db4e18",
    "experiments/v0_4_1_aborted/results_v0_4.jsonl":"6fbeb98b454a934747d5660af4e9c92e5a9a1c7612a2703179644665ace53930",
    "experiments/v0_4_1_aborted/stimuli_v0_4.csv":"ed7e23f488ffa16d40074c3c629655fc3d17eca073fd07bb4be0a8ea11b0d861",
    "experiments/v0_4_2_aborted/stimuli_v0_4_2.csv":"43e6e9d7cacc3ae7a52410e8831cc5859115123de68916d2443314cf41c22a8a",
}

failures=[]
for rel,expected in EXPECTED.items():
    path=ROOT/rel
    got=hashlib.sha256(path.read_bytes()).hexdigest()
    if got!=expected:
        failures.append((rel,got,expected))

if failures:
    for rel,got,expected in failures:
        print("FAIL",rel,got,"!=",expected)
    raise SystemExit(1)

print("PASS historical byte integrity",{"files":len(EXPECTED)})
