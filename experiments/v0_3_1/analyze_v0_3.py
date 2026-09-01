#!/usr/bin/env python3
import argparse, json
from collections import defaultdict
from pathlib import Path

CONDITIONS=[
    "source_only","passive_repeat","active_plain",
    "active_self_labeled","active_lineage","independent_evidence"
]
Q=["0.55","0.68","0.80"]

def pct(n,d):
    return 100*n/d if d else float("nan")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("results",nargs="?",default="results_v0_3_1.jsonl")
    args=ap.parse_args()

    rows=[]
    for line in Path(args.results).read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))

    valid=[r for r in rows if r.get("status")=="valid"]
    failures=[r for r in rows if r.get("status")!="valid"]
    print(f"valid trajectories: {len(valid)}/48")
    print(f"failure records: {len(failures)}")

    by=defaultdict(list)
    for r in valid:
        by[r["condition"]].append(r)

    print("\nBELIEF RETENTION: % selecting CLAIM_A")
    print("condition\tq=.55\tq=.68\tq=.80")
    for c in CONDITIONS:
        vals=[]
        for q in Q:
            rr=by[c]
            k=sum(r["belief_by_correction_reliability"][q]["chosen_claim"]=="CLAIM_A" for r in rr)
            vals.append(f"{k}/{len(rr)} ({pct(k,len(rr)):.1f}%)" if rr else "NA")
        print(c+"\t"+"\t".join(vals))

    print("\nPROVENANCE EXACT-CORRECT")
    for c in CONDITIONS:
        rr=by[c]
        k=sum(bool(r["provenance_scores"]["exact_correct"]) for r in rr)
        fp=sum(len(r["provenance_scores"]["false_independent_ids"]) for r in rr)
        miss=sum(len(r["provenance_scores"]["missed_root_ids"]) for r in rr)
        print(f"{c}: exact {k}/{len(rr)}; false IDs={fp}; missed roots={miss}")

    # Gates
    def count_claim(c,q,claim):
        rr=by[c]
        return sum(r["belief_by_correction_reliability"][q]["chosen_claim"]==claim for r in rr)

    g1 = (
        len(by["source_only"])==8 and
        count_claim("source_only","0.55","CLAIM_A")>=6 and
        count_claim("source_only","0.80","CLAIM_B")>=6
    )
    g2 = len(by["independent_evidence"])==8 and count_claim("independent_evidence","0.80","CLAIM_A")>=6
    g3 = len(by["independent_evidence"])==8 and sum(
        r["provenance_scores"]["exact_correct"] for r in by["independent_evidence"]
    )>=6
    g4 = len(valid)==48 and not failures

    print("\nCALIBRATION GATES")
    print("G1 dynamic range:", "PASS" if g1 else "FAIL")
    print("G2 positive-control sensitivity:", "PASS" if g2 else "FAIL")
    print("G3 provenance positive control:", "PASS" if g3 else "FAIL")
    print("G4 transport/integrity:", "PASS" if g4 else "FAIL")
    print("OVERALL:", "PASS -> eligible to design confirmatory v0.4" if all([g1,g2,g3,g4])
          else "FAIL -> revise instrument; do not claim hypothesis test")

if __name__=="__main__":
    main()
