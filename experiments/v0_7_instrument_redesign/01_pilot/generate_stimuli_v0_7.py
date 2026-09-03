from pathlib import Path
import csv, random

SEED = 2026090307
OUT = Path(__file__).resolve().parent / "stimuli_v0_7.csv"

ONSETS = ["BX","CZ","DQ","FX","GZ","JQ","KX","LZ","MQ","NX","PZ","QX","RX","SZ","TQ","VX","WZ","XQ"]
VOWELS = ["A","E","I","O","U","Y"]
CODAS = ["B","C","F","G","H","J","Q","W","Y","Z"]

def token(rng, used, length=2):
    while True:
        t="".join(rng.choice(ONSETS)+rng.choice(VOWELS)+rng.choice(CODAS) for _ in range(length))
        if t not in used:
            used.add(t); return t

def value(rng, used):
    chars="23456789BCDFGHJKMNPQRTVWXYZ"
    while True:
        t="".join(rng.choice(chars) for _ in range(5))
        if t not in used:
            used.add(t); return t

def main():
    rng=random.Random(SEED)
    used_e=set(); used_v=set()
    assignments=[(i,o) for i in ["CLAIM_A","CLAIM_B"] for o in ["A_FIRST","B_FIRST"] for _ in range(3)]
    rng.shuffle(assignments)
    rows=[]
    for n,(initial,order) in enumerate(assignments,1):
        rows.append({
            "item_id":f"R7I{n:03d}",
            "entity":token(rng,used_e),
            "claim_a_value":value(rng,used_v),
            "claim_b_value":value(rng,used_v),
            "initial_supported_claim":initial,
            "presentation_order":order
        })
    with OUT.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()),lineterminator="\n")
        w.writeheader(); w.writerows(rows)

if __name__=="__main__":
    main()
