#!/usr/bin/env python3
import argparse, json, math, random
from collections import defaultdict
from pathlib import Path
from math import comb

CORE=["source_only","neutral_filler","passive_repeat","active_plain","active_lineage"]

def exact_mcnemar(b,c):
    n=b+c
    if n==0: return 1.0
    k=min(b,c)
    p=2*sum(comb(n,i)*(0.5**n) for i in range(k+1))
    return min(1.0,p)

def paired_contrast(a,b):
    # returns mean(a-b), desired discordance a=1,b=0, opposite a=0,b=1
    keys=sorted(set(a)&set(b))
    diffs=[a[k]-b[k] for k in keys]
    desired=sum(a[k]==1 and b[k]==0 for k in keys)
    opposite=sum(a[k]==0 and b[k]==1 for k in keys)
    rd=sum(diffs)/len(diffs) if diffs else float("nan")
    return keys,rd,desired,opposite,exact_mcnemar(desired,opposite)

def bootstrap_ci(a,b,seed=20260901,B=20000):
    keys=sorted(set(a)&set(b))
    if not keys: return (float("nan"),float("nan"))
    rng=random.Random(seed)
    vals=[]
    n=len(keys)
    for _ in range(B):
        sample=[keys[rng.randrange(n)] for _ in range(n)]
        vals.append(sum(a[k]-b[k] for k in sample)/n)
    vals.sort()
    return vals[int(.025*B)], vals[int(.975*B)-1]

def holm(ps):
    m=len(ps)
    order=sorted(range(m),key=lambda i:ps[i])
    adj=[None]*m
    running=0.0
    for rank,i in enumerate(order):
        val=min(1.0,(m-rank)*ps[i])
        running=max(running,val)
        adj[i]=running
    return adj

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("results",nargs="?",default="results_v0_4.jsonl")
    args=ap.parse_args()

    rows=[json.loads(l) for l in Path(args.results).read_text(encoding="utf-8").splitlines() if l.strip()]
    valid=[r for r in rows if r.get("status")=="valid"]
    failures=[r for r in rows if r.get("status")!="valid"]

    bykey={}
    duplicates=[]
    for r in valid:
        k=(r["item_id"],r["condition"])
        if k in bykey: duplicates.append(k)
        bykey[k]=r

    planned=32*5+8
    print("=== INTEGRITY ===")
    print("valid unique trajectories:",len(bykey),"/",planned)
    print("duplicate valid keys:",duplicates)
    print("audit failure records:",len(failures))
    unresolved=[r for r in failures if (r["item_id"],r["condition"]) not in bykey]
    print("unresolved failures:",len(unresolved))

    # Expected condition counts
    counts=defaultdict(int)
    for r in bykey.values(): counts[r["condition"]]+=1
    print("condition counts:",dict(counts))

    # Build paired outcomes
    maps={}
    for c in CORE:
        maps[c]={r["item_id"]:r["retain_initial"] for r in bykey.values() if r["condition"]==c}

    # Controls
    source_counter=sum(1-v for v in maps["source_only"].values())
    pc=[r for r in bykey.values() if r["condition"]=="independent_evidence"]
    pc_retain=sum(r["retain_initial"] for r in pc)
    pc_prov=sum(bool(r["provenance_scores"]["exact_correct"]) for r in pc)
    V1=len(maps["source_only"])==32 and source_counter>=24
    V2=len(pc)==8 and pc_retain>=6
    V3=len(pc)==8 and pc_prov>=6
    V4=not any(r.get("status")=="manipulation_failure" and
               (r["item_id"],r["condition"]) not in bykey for r in failures)
    V5=len(bykey)==planned and not unresolved and not duplicates

    print("\n=== VALIDITY GATES ===")
    print(f"V1 source_only counter sensitivity: {source_counter}/32 ->", "PASS" if V1 else "FAIL")
    print(f"V2 independent behavior: {pc_retain}/8 ->", "PASS" if V2 else "FAIL")
    print(f"V3 independent provenance: {pc_prov}/8 ->", "PASS" if V3 else "FAIL")
    print("V4 manipulation integrity:", "PASS" if V4 else "FAIL")
    print("V5 completeness:", "PASS" if V5 else "FAIL")

    # Provenance interpretation gate
    prov_by={}
    total_exact=0
    total_n=0
    each_ok=True
    print("\n=== PROVENANCE ACCURACY ===")
    for c in CORE:
        rr=[r for r in bykey.values() if r["condition"]==c]
        k=sum(bool(r["provenance_scores"]["exact_correct"]) for r in rr)
        prov_by[c]=(k,len(rr))
        total_exact+=k; total_n+=len(rr)
        rate=k/len(rr) if rr else 0
        if rate<.70: each_ok=False
        print(f"{c}: {k}/{len(rr)} ({100*rate:.1f}%)")
    overall=total_exact/total_n if total_n else 0
    mech_gate=overall>=.85 and each_ok
    print(f"overall core: {total_exact}/{total_n} ({100*overall:.1f}%)")
    print("provenance-use interpretation gate:", "PASS" if mech_gate else "FAIL")

    # Co-primary
    _,rd1,b1,c1,p1=paired_contrast(maps["passive_repeat"],maps["neutral_filler"])
    ci1=bootstrap_ci(maps["passive_repeat"],maps["neutral_filler"],20260911)
    _,rd2,b2,c2,p2=paired_contrast(maps["active_plain"],maps["active_lineage"])
    ci2=bootstrap_ci(maps["active_plain"],maps["active_lineage"],20260912)
    adj=holm([p1,p2])
    H1=(rd1>=.25 and adj[0]<.05)
    H2=(rd2>=.25 and adj[1]<.05)

    print("\n=== CO-PRIMARY CONFIRMATORY TESTS ===")
    print(f"H1 passive_repeat - neutral_filler: RD={rd1:.3f}, 95% bootstrap CI={ci1}, "
          f"discord desired/opposite={b1}/{c1}, raw p={p1:.6g}, Holm p={adj[0]:.6g}, "
          f"VERDICT={'SUPPORTED' if H1 else 'NOT SUPPORTED'}")
    print(f"H2 active_plain - active_lineage: RD={rd2:.3f}, 95% bootstrap CI={ci2}, "
          f"discord desired/opposite={b2}/{c2}, raw p={p2:.6g}, Holm p={adj[1]:.6g}, "
          f"VERDICT={'SUPPORTED' if H2 else 'NOT SUPPORTED'}")

    valid_study=all([V1,V2,V3,V4,V5])
    print("\n=== FINAL PREREGISTERED STATUS ===")
    if not valid_study:
        print("INVALID/INCONCLUSIVE: one or more validity gates failed.")
    else:
        print("VALID confirmatory dataset.")
        print("H1:", "SUPPORTED" if H1 else "NOT SUPPORTED")
        print("H2:", "SUPPORTED" if H2 else "NOT SUPPORTED")
        if H1 and H2:
            print("JOINT RESULT: BOTH CO-PRIMARY HYPOTHESES SUPPORTED.")
        else:
            print("JOINT RESULT: FULL TWO-EFFECT CONFIRMATION NOT ACHIEVED.")
        print("Mechanistic 'provenance-use gap' language:",
              "PERMITTED" if mech_gate else "NOT PERMITTED")

    print("\n=== DESCRIPTIVE RETENTION ===")
    for c in CORE+["independent_evidence"]:
        rr=[r for r in bykey.values() if r["condition"]==c]
        if rr:
            k=sum(r["retain_initial"] for r in rr)
            conf=sum(
                (r["belief"]["confidence_chosen"] if r["belief"]["chosen_claim"]==r["initial_supported_claim"]
                 else 100-r["belief"]["confidence_chosen"])
                for r in rr
            )/len(rr)
            print(f"{c}: retain {k}/{len(rr)} ({100*k/len(rr):.1f}%), "
                  f"mean implied support INITIAL={conf:.1f}")

if __name__=="__main__":
    main()
