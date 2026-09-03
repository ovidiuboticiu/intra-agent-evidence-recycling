from pathlib import Path
import csv
from collections import Counter

P=Path(__file__).resolve().parent/"stimuli_v0_7.csv"
with P.open("r",encoding="utf-8",newline="") as f:
    rows=list(csv.DictReader(f))
assert len(rows)==12
assert len({r["item_id"] for r in rows})==12
assert len({r["entity"] for r in rows})==12
vals=[x for r in rows for x in (r["claim_a_value"],r["claim_b_value"])]
assert len(vals)==24 and len(set(vals))==24
cells=Counter((r["initial_supported_claim"],r["presentation_order"]) for r in rows)
for i in ("CLAIM_A","CLAIM_B"):
    for o in ("A_FIRST","B_FIRST"):
        assert cells[(i,o)]==3, (i,o,cells[(i,o)])
print("V0.7 STIMULI: PASS")
print("rows=12; 3 per INITIAL x order cell; unique ids/entities/claim tokens")
