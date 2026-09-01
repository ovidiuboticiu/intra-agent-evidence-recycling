#!/usr/bin/env python3
import argparse, json, random
from collections import defaultdict
from pathlib import Path
from math import comb

CORE=["source_only","neutral_filler","passive_repeat","active_plain","active_lineage"]

def exact_mcnemar(desired,opposite):
    n=desired+opposite
    if n==0:
        return 1.0
    k=min(desired,opposite)
    p=2*sum(comb(n,i)*(0.5**n) for i in range(k+1))
    return min(1.0,p)

def paired_contrast(a,b):
    keys=sorted(set(a)&set(b))
    diffs=[a[k]-b[k] for k in keys]
    desired=sum(a[k]==1 and b[k]==0 for k in keys)
    opposite=sum(a[k]==0 and b[k]==1 for k in keys)
    rd=sum(diffs)/len(diffs) if diffs else float("nan")
    return keys,rd,desired,opposite,exact_mcnemar(desired,opposite)

def bootstrap_ci(a,b,seed,B=20000):
    keys=sorted(set(a)&set(b))
    if not keys:
        return (float("nan"),float("nan"))
    rng=random.Random(seed)
    n=len(keys)
    vals=[]
    for _ in range(B):
        sample=[keys[rng.randrange(n)] for _ in range(n)]
        vals.append(sum(a[k]-b[k] for k in sample)/n)
    vals.sort()
    return vals[int(.025*B)],vals[int(.975*B)-1]

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
    ap.add_argument("results",nargs="?",default="results_v0_4_3.jsonl")
    args=ap.parse_args()

    rows=[json.loads(x) for x in Path(args.results).read_text(encoding="utf-8").splitlines() if x.strip()]
    valid=[r for r in rows if r.get("status")=="valid"]
    failures=[r for r in rows if r.get("status")!="valid"]

    bykey={}
    duplicates=[]
    for r in valid:
        key=(r["item_id"],r["condition"])
        if key in bykey:
            duplicates.append(key)
        bykey[key]=r

    planned=168
    unresolved=[r for r in failures if (r["item_id"],r["condition"]) not in bykey]

    print("=== INTEGRITY ===")
    print("valid unique:",len(bykey),"/",planned)
    print("duplicate valid keys:",duplicates)
    print("audit failure rows:",len(failures))
    print("unresolved failures:",len(unresolved))

    counts=defaultdict(int)
    for r in bykey.values():
        counts[r["condition"]]+=1
    print("condition counts:",dict(counts))

    maps={}
    for c in CORE:
        maps[c]={r["item_id"]:r["retain_initial"] for r in bykey.values() if r["condition"]==c}

    # Validity gates
    source_counter=sum(1-v for v in maps["source_only"].values())
    pc=[r for r in bykey.values() if r["condition"]=="independent_evidence"]
    pc_retain=sum(r["retain_initial"] for r in pc)

    active_rows=[r for r in bykey.values() if r["condition"] in {"active_plain","active_lineage"}]
    active_complete=(
      len(active_rows)==64 and
      all(len(r.get("active_application_outputs",[]))==5 for r in active_rows)
    )

    V1=len(maps["source_only"])==32 and source_counter>=24
    V2=len(pc)==8 and pc_retain>=6
    V3=active_complete
    V4=len(bykey)==planned and not duplicates and not unresolved

    print("\n=== VALIDITY GATES ===")
    print(f"V1 source_only counter sensitivity: {source_counter}/32 ->", "PASS" if V1 else "FAIL")
    print(f"V2 independent behavior: {pc_retain}/8 ->", "PASS" if V2 else "FAIL")
    print("V3 active-trace completeness:", "PASS" if V3 else "FAIL")
    print("V4 dataset completeness:", "PASS" if V4 else "FAIL")

    # Primary tests
    _,rd1,d1,o1,p1=paired_contrast(maps["passive_repeat"],maps["neutral_filler"])
    ci1=bootstrap_ci(maps["passive_repeat"],maps["neutral_filler"],20260931)

    _,rd2,d2,o2,p2=paired_contrast(maps["active_plain"],maps["active_lineage"])
    ci2=bootstrap_ci(maps["active_plain"],maps["active_lineage"],20260932)

    adj=holm([p1,p2])
    H1=rd1>=.25 and adj[0]<.05
    H2=rd2>=.25 and adj[1]<.05

    print("\n=== CO-PRIMARY CONFIRMATORY TESTS ===")
    print(
      f"H1 passive_repeat - neutral_filler: RD={rd1:.3f}, CI={ci1}, "
      f"desired/opposite={d1}/{o1}, raw_p={p1:.6g}, Holm_p={adj[0]:.6g}, "
      f"VERDICT={'SUPPORTED' if H1 else 'NOT SUPPORTED'}"
    )
    print(
      f"H2 active_plain - active_lineage: RD={rd2:.3f}, CI={ci2}, "
      f"desired/opposite={d2}/{o2}, raw_p={p2:.6g}, Holm_p={adj[1]:.6g}, "
      f"VERDICT={'SUPPORTED' if H2 else 'NOT SUPPORTED'}"
    )

    valid_study=all([V1,V2,V3,V4])
    print("\n=== FINAL PREREGISTERED STATUS ===")
    if not valid_study:
        print("INVALID/INCONCLUSIVE: at least one validity gate failed.")
    else:
        print("VALID behavioral-confirmatory dataset.")
        print("H1:", "SUPPORTED" if H1 else "NOT SUPPORTED")
        print("H2:", "SUPPORTED" if H2 else "NOT SUPPORTED")
        print("JOINT:", "BOTH SUPPORTED" if H1 and H2 else "FULL TWO-EFFECT CONFIRMATION NOT ACHIEVED")

    print("\n=== DESCRIPTIVE RETENTION ===")
    for c in CORE+["independent_evidence"]:
        rr=[r for r in bykey.values() if r["condition"]==c]
        if not rr:
            continue
        k=sum(r["retain_initial"] for r in rr)
        implied=sum(
          (r["belief"]["confidence_chosen"] if r["belief"]["chosen_claim"]==r["initial_supported_claim"]
           else 100-r["belief"]["confidence_chosen"])
          for r in rr
        )/len(rr)
        print(f"{c}: retain {k}/{len(rr)} ({100*k/len(rr):.1f}%), mean implied support INITIAL={implied:.1f}")

    print("\n=== PROVENANCE — DESCRIPTIVE ONLY ===")
    for c in CORE+["independent_evidence"]:
        rr=[r for r in bykey.values() if r["condition"]==c]
        if not rr:
            continue
        exact=sum(bool(r["provenance_scores"]["exact_correct"]) for r in rr)
        false_ids=sum(len(r["provenance_scores"]["false_independent_ids"]) for r in rr)
        missed=sum(len(r["provenance_scores"]["missed_root_ids"]) for r in rr)
        print(f"{c}: exact={exact}/{len(rr)}, false_ids={false_ids}, missed_roots={missed}")

    print("\nNOTE: provenance results are descriptive and cannot establish a confirmed provenance-use mechanism in v0.4.3.")

if __name__=="__main__":
    main()
