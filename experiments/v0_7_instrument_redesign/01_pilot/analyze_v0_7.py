#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import csv,json,hashlib

HERE=Path(__file__).resolve().parent
P=HERE/"results_v0_7.jsonl"
C=HERE/"config_v0_7.json"
CONDS=["two_initial_one_counter","one_initial_two_counter",
       "derived_lure_initial_two_counter","three_initial_two_counter"]

def hfile(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""):h.update(c)
    return h.hexdigest()

cfg=json.loads(C.read_text(encoding="utf-8"))
rows=[json.loads(x) for x in P.read_text(encoding="utf-8").splitlines() if x.strip()]
valid=[r for r in rows if r.get("status")=="valid"]
fail=[r for r in rows if r.get("status")!="valid"]
keys=[(r.get("item_id"),r.get("condition")) for r in valid]
expected={(f"R7I{i:03d}",c) for i in range(1,13) for c in CONDS}
dups=[k for k,n in Counter(keys).items() if n!=1]
missing=sorted(expected-set(keys));extra=sorted(set(keys)-expected)
mp=HERE/cfg["manifest_filename"]; msha=hfile(mp) if mp.exists() else None
meta=[]
for n,r in enumerate(valid,1):
    checks=[
      r.get("model")==cfg["model_id"],r.get("model_sha256")==cfg["model_sha256"],
      r.get("temperature")==0,r.get("seed")==42,
      r.get("diagnostics",{}).get("finish_reason")=="stop",
      r.get("run_meta",{}).get("manifest_sha256")==msha
    ]
    if not all(checks): meta.append(n)
p1=(len(valid)==48 and not fail and not dups and not missing and not extra and not meta)

summ={}
p2=p3=p4=True
for cond in CONDS:
    g=[r for r in valid if r.get("condition")==cond]
    co=sum(int(r.get("correct",0)) for r in g)
    bi={}
    bo={}
    for ini in ["CLAIM_A","CLAIM_B"]:
        s=[r for r in g if r.get("initial_supported_claim")==ini]
        bi[ini]=(sum(int(r.get("correct",0)) for r in s),len(s))
    for o in ["A_FIRST","B_FIRST"]:
        s=[r for r in g if r.get("presentation_order")==o]
        bo[o]=(sum(int(r.get("correct",0)) for r in s),len(s))
    c2=(len(g)==12 and co>=11)
    c3=all(t==6 and c>=5 for c,t in bi.values())
    c4=all(t==6 and c>=5 for c,t in bo.values())
    p2 &= c2;p3 &= c3;p4 &= c4
    summ[cond]={"correct":co,"total":len(g),"by_initial":bi,"by_order":bo,
                "condition_accuracy_pass":c2,"initial_symmetry_pass":c3,"order_symmetry_pass":c4}
r3=summ.get("derived_lure_initial_two_counter",{})
p5=(r3.get("correct",0)>=11 and r3.get("initial_symmetry_pass") and r3.get("order_symmetry_pass"))
gates={"P1_integrity":p1,"P2_condition_accuracy":bool(p1 and p2),
       "P3_initial_symmetry":bool(p1 and p3),"P4_order_symmetry":bool(p1 and p4),
       "P5_derived_lure":bool(p1 and p5)}
if not p1: decision="INVALID/INCONCLUSIVE"
elif all(gates.values()): decision="INSTRUMENT_CANDIDATE_VIABLE"
else: decision="REDESIGN_FAILED_STOP"
report={"program":"IAER v0.7","stage":"measurement_decoupling_pilot",
        "decision":decision,"valid_rows":len(valid),"failure_rows":len(fail),
        "missing":missing,"extra":extra,"duplicates":dups,"metadata_error_rows":meta,
        "gates":gates,"condition_summaries":summ,
        "interpretation_boundary":"v0.7 tests instrument usability only; it does not confirm, refute, or estimate IAER."}
(HERE/"report_v0_7.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
lines=[f"IAER v0.7 DECISION: {decision}",f"VALID ROWS: {len(valid)}/48",f"FAILURE ROWS: {len(fail)}",""]
lines += [f"{k}: {'PASS' if v else 'FAIL'}" for k,v in gates.items()]
lines += ["","BY CONDITION"]
for cond,s in summ.items():
    lines.append(f"{cond}: {s['correct']}/{s['total']}")
    for k,(c,t) in s["by_initial"].items():lines.append(f"  initial={k}: {c}/{t}")
    for k,(c,t) in s["by_order"].items():lines.append(f"  order={k}: {c}/{t}")
lines += ["","INTERPRETATION BOUNDARY",
          "v0.7 tests instrument usability only; it does not confirm, refute, or estimate IAER."]
txt="\n".join(lines)+"\n"
(HERE/"report_v0_7.txt").write_text(txt,encoding="utf-8")
print(txt,end="")
