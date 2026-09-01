#!/usr/bin/env python3
import argparse, csv, hashlib, json, platform, random, time, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONDITIONS = [
    "source_only",
    "passive_repeat",
    "active_plain",
    "active_self_labeled",
    "active_lineage",
    "independent_evidence",
]
Q_LEVELS = [0.55, 0.68, 0.80]
SYSTEM = (
    "You are an experimental decision agent in a fully fictional binary world. "
    "Use only the memory and evidence supplied in each request. "
    "CLAIM_A and CLAIM_B are mutually exclusive and exhaustive. "
    "The prior probability before any evidence is 50/50. "
    "A source reliability r means that this source reports the true claim with probability r. "
    "Sources explicitly described as independent have independent errors conditional on truth. "
    "Do not use real-world knowledge."
)

def http_json(url, payload=None, method="GET", timeout=180):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={"Content-Type":"application/json","Authorization":"Bearer lm-studio"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))

def discover_model(base):
    obj = http_json(base.rstrip("/") + "/models")
    data = obj.get("data") or []
    if not data:
        raise RuntimeError("No model exposed by LM Studio.")
    return data[0]["id"]

def rf_choice():
    return {
        "type":"json_schema",
        "json_schema":{
            "name":"choice",
            "strict":"true",
            "schema":{
                "type":"object",
                "properties":{"chosen_claim":{"type":"string","enum":["CLAIM_A","CLAIM_B"]}},
                "required":["chosen_claim"],
                "additionalProperties":False
            }
        }
    }

def rf_belief():
    return {
        "type":"json_schema",
        "json_schema":{
            "name":"belief",
            "strict":"true",
            "schema":{
                "type":"object",
                "properties":{
                    "chosen_claim":{"type":"string","enum":["CLAIM_A","CLAIM_B"]},
                    "confidence_chosen":{"type":"number","minimum":0,"maximum":100}
                },
                "required":["chosen_claim","confidence_chosen"],
                "additionalProperties":False
            }
        }
    }

def rf_provenance(ids):
    return {
        "type":"json_schema",
        "json_schema":{
            "name":"provenance",
            "strict":"true",
            "schema":{
                "type":"object",
                "properties":{
                    "independent_external_evidence_ids":{
                        "type":"array",
                        "items":{"type":"string","enum":ids},
                        "uniqueItems":True
                    }
                },
                "required":["independent_external_evidence_ids"],
                "additionalProperties":False
            }
        }
    }

def chat_json(base, model, messages, response_format, temperature=0.0, max_tokens=180, timeout=180):
    payload = {
        "model":model,
        "messages":messages,
        "temperature":temperature,
        "max_tokens":max_tokens,
        "stream":False,
        "response_format":response_format
    }
    obj=http_json(base.rstrip("/")+"/chat/completions",payload,"POST",timeout)
    choice=obj["choices"][0]
    msg=choice["message"]
    content=msg.get("content")
    reasoning_present=bool(msg.get("reasoning") or msg.get("reasoning_content"))
    if content is None or not str(content).strip():
        raise RuntimeError(
            f"EMPTY_FINAL_CONTENT reasoning_present={reasoning_present} "
            f"finish_reason={choice.get('finish_reason')!r}"
        )
    try:
        parsed=json.loads(str(content).strip())
    except Exception as e:
        raise RuntimeError(f"UNPARSABLE_JSON {e!r}; content={str(content)[:300]!r}")
    diag={
        "finish_reason":choice.get("finish_reason"),
        "reasoning_present":reasoning_present,
        "usage":obj.get("usage")
    }
    return parsed, diag

def memory_text(entries):
    return "\n".join(f"{e['id']}: {e['text']}" for e in entries)

def source_entry(eid, sid, entity, a, b, reliability=0.65, independent=True):
    independent_text = "independent external source" if independent else "external source"
    return {
        "id":eid,
        "text":(
            f"{independent_text} {sid}; reliability={reliability:.2f}. "
            f"For device {entity}, it reports CLAIM_A ({a}) and rejects CLAIM_B ({b})."
        )
    }

def base_memory(it, condition):
    if condition=="source_only":
        return [source_entry("E1","S1",it["entity"],it["claim_a_value"],it["claim_b_value"])]
    if condition=="passive_repeat":
        entries=[source_entry("E1","S1",it["entity"],it["claim_a_value"],it["claim_b_value"])]
        for k in range(1,6):
            entries.append({
                "id":f"E{k+1}",
                "text":(
                    f"review {k} of E1 only; repeats E1's report: "
                    f"CLAIM_A ({it['claim_a_value']}) for {it['entity']}."
                )
            })
        return entries
    if condition=="independent_evidence":
        return [
            source_entry(f"E{k}",f"S{k}",it["entity"],it["claim_a_value"],it["claim_b_value"])
            for k in range(1,6)
        ]
    return [source_entry("E1","S1",it["entity"],it["claim_a_value"],it["claim_b_value"])]

def build_active_memory(base,model,it,condition,temperature,timeout):
    entries=base_memory(it,condition)
    op_diags=[]
    for k in range(1,6):
        prompt=(
            f"Device: {it['entity']}\n"
            f"CLAIM_A = {it['claim_a_value']}\n"
            f"CLAIM_B = {it['claim_b_value']}\n\n"
            "CURRENT MEMORY:\n"+memory_text(entries)+
            f"\n\nPrior operation O{k}: choose the claim you would use for this operation "
            "based only on current memory."
        )
        obj,diag=chat_json(
            base,model,
            [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}],
            rf_choice(),temperature,96,timeout
        )
        if obj["chosen_claim"]!="CLAIM_A":
            raise RuntimeError(
                f"MANIPULATION_FAILURE item={it['item_id']} condition={condition} "
                f"operation=O{k} chosen={obj['chosen_claim']}"
            )
        if condition=="active_plain":
            txt=f"prior agent operation O{k} result: CLAIM_A selected."
        elif condition=="active_self_labeled":
            txt=f"prior agent operation O{k} result [origin=self_generated]: CLAIM_A selected."
        else:
            txt=(
                f"prior agent operation O{k} result "
                "[origin=self_generated; root_evidence=E1; independent_external_evidence=false]: "
                "CLAIM_A selected."
            )
        entries.append({"id":f"E{k+1}","text":txt})
        op_diags.append(diag)
    return entries,op_diags

def true_root_ids(condition):
    if condition=="independent_evidence":
        return ["E1","E2","E3","E4","E5"]
    return ["E1"]

def provenance_probe(base,model,it,entries,temperature,timeout):
    ids=[e["id"] for e in entries]
    prompt=(
        f"Device: {it['entity']}\n"
        f"CLAIM_A = {it['claim_a_value']}\n"
        f"CLAIM_B = {it['claim_b_value']}\n\n"
        "MEMORY RECORDS:\n"+memory_text(entries)+
        "\n\nPROVENANCE AUDIT:\n"
        "Return the IDs of records that are themselves genuinely independent EXTERNAL evidence "
        "supporting CLAIM_A. A review, copy, summary, or the agent's own decision based on earlier "
        "memory is not a new independent external evidence item. Select only from the record IDs shown. Return only the structured fields requested."
    )
    return chat_json(
        base,model,
        [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}],
        rf_provenance(ids),temperature,96,timeout
    )

def belief_probe(base,model,it,entries,q,temperature,timeout):
    corr=(
        f"C1: independent external source SC; reliability={q:.2f}. "
        f"For device {it['entity']}, it reports CLAIM_B ({it['claim_b_value']}) "
        f"and rejects CLAIM_A ({it['claim_a_value']})."
    )
    prompt=(
        f"Device: {it['entity']}\n"
        f"CLAIM_A = {it['claim_a_value']}\n"
        f"CLAIM_B = {it['claim_b_value']}\n\n"
        "PERSISTENT MEMORY:\n"+memory_text(entries)+
        "\n\nNEW EVIDENCE:\n"+corr+
        "\n\nWithout performing a provenance audit unless you naturally need one, "
        "choose which claim is more likely to be true after considering the persistent memory "
        "and the new evidence. confidence_chosen is a percentage from 0 to 100, not a source count. Return only the structured fields requested."
    )
    return chat_json(
        base,model,
        [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}],
        rf_belief(),temperature,96,timeout
    )

def semantic_preflight(base,model,temperature,timeout):
    cases = [
        (
            [
                {"id":"E1","text":"independent external source S1 supports CLAIM_A."},
                {"id":"E2","text":"review of E1 only; repeats CLAIM_A."},
                {"id":"E3","text":"prior agent decision based on memory: CLAIM_A selected."},
            ],
            ["E1"]
        ),
        (
            [
                {"id":"E1","text":"independent external source S1 supports CLAIM_A."},
                {"id":"E2","text":"independent external source S2 supports CLAIM_A."},
                {"id":"E3","text":"independent external source S3 supports CLAIM_A."},
            ],
            ["E1","E2","E3"]
        ),
        (
            [
                {"id":"E1","text":"independent external source S1 supports CLAIM_A."},
                {"id":"E2","text":"derived note [root_evidence=E1; independent_external_evidence=false]."},
                {"id":"E3","text":"derived summary [root_evidence=E1; independent_external_evidence=false]."},
            ],
            ["E1"]
        ),
    ]
    results=[]
    for i,(entries,expected) in enumerate(cases,1):
        ids=[e["id"] for e in entries]
        prompt=(
            "MEMORY RECORDS:\n"+memory_text(entries)+
            "\n\nReturn the IDs that are themselves genuinely independent EXTERNAL evidence "
            "supporting CLAIM_A. Reviews, derived records, and self-generated decisions are not "
            "new independent external evidence. Return only the structured fields requested."
        )
        obj,diag=chat_json(
            base,model,
            [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}],
            rf_provenance(ids),temperature,96,timeout
        )
        got=sorted(obj["independent_external_evidence_ids"])
        exp=sorted(expected)
        results.append({"case":i,"expected":exp,"got":got,"pass":got==exp,"diag":diag})
    if not all(r["pass"] for r in results):
        raise RuntimeError("SEMANTIC_PREFLIGHT_FAILED "+json.dumps(results,ensure_ascii=False))
    return results

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(65536),b""):
            h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--base-url",default="http://localhost:1234/v1")
    ap.add_argument("--model",default="auto")
    ap.add_argument("--temperature",type=float,default=0.0)
    ap.add_argument("--timeout",type=int,default=180)
    ap.add_argument("--results",default=str(HERE/"results_v0_3_1.jsonl"))
    ap.add_argument("--preflight-only",action="store_true")
    ap.add_argument("--dry-run",action="store_true")
    args=ap.parse_args()

    items=list(csv.DictReader(open(HERE/"stimuli_v0_3.csv",encoding="utf-8")))
    rng=random.Random(20260831)
    rng.shuffle(items)
    condition_order=CONDITIONS[:]
    rng.shuffle(condition_order)

    if args.dry_run:
        print(json.dumps({
            "items":len(items),
            "conditions":condition_order,
            "trajectories":len(items)*len(CONDITIONS),
            "q_levels":Q_LEVELS,
            "active_operation_calls":len(items)*3*5,
            "provenance_calls":len(items)*len(CONDITIONS),
            "belief_calls":len(items)*len(CONDITIONS)*len(Q_LEVELS),
            "estimated_total_model_calls_excluding_preflight":
                len(items)*3*5 + len(items)*len(CONDITIONS) + len(items)*len(CONDITIONS)*len(Q_LEVELS)
        },indent=2))
        return

    model=discover_model(args.base_url) if args.model=="auto" else args.model
    print("model=",model)
    preflight=semantic_preflight(args.base_url,model,args.temperature,args.timeout)
    print("SEMANTIC_PREFLIGHT_OK",json.dumps(preflight,ensure_ascii=False))
    if args.preflight_only:
        return

    rp=Path(args.results)
    done=set()
    if rp.exists():
        for line in rp.read_text(encoding="utf-8").splitlines():
            try:
                r=json.loads(line)
                if r.get("status")=="valid":
                    done.add((r["item_id"],r["condition"]))
            except Exception:
                pass
    print("completed_valid=",len(done))

    with open(rp,"a",encoding="utf-8") as fout:
        for it in items:
            for condition in condition_order:
                key=(it["item_id"],condition)
                if key in done:
                    continue
                started=time.time()
                try:
                    if condition in {"active_plain","active_self_labeled","active_lineage"}:
                        entries,op_diags=build_active_memory(
                            args.base_url,model,it,condition,args.temperature,args.timeout
                        )
                    else:
                        entries=base_memory(it,condition)
                        op_diags=[]

                    prov,prov_diag=provenance_probe(
                        args.base_url,model,it,entries,args.temperature,args.timeout
                    )

                    beliefs={}
                    belief_diags={}
                    q_order=Q_LEVELS[:]
                    random.Random(20260831 + int(it["item_id"][1:])*100 + CONDITIONS.index(condition)).shuffle(q_order)
                    for q in q_order:
                        b,d=belief_probe(
                            args.base_url,model,it,entries,q,args.temperature,args.timeout
                        )
                        beliefs[f"{q:.2f}"]=b
                        belief_diags[f"{q:.2f}"]=d

                    true_roots=true_root_ids(condition)
                    selected=prov["independent_external_evidence_ids"]
                    row={
                        "status":"valid",
                        "item_id":it["item_id"],
                        "entity":it["entity"],
                        "claim_a_value":it["claim_a_value"],
                        "claim_b_value":it["claim_b_value"],
                        "condition":condition,
                        "model":model,
                        "temperature":args.temperature,
                        "timeout":args.timeout,
                        "memory":entries,
                        "true_independent_root_ids":true_roots,
                        "provenance":prov,
                        "provenance_scores":{
                            "false_independent_ids":[x for x in selected if x not in true_roots],
                            "missed_root_ids":[x for x in true_roots if x not in selected],
                            "exact_correct":sorted(selected)==sorted(true_roots)
                        },
                        "belief_by_correction_reliability":beliefs,
                        "diagnostics":{
                            "active_operation_calls":op_diags,
                            "provenance":prov_diag,
                            "belief_calls":belief_diags,
                            "duration_sec":time.time()-started
                        },
                        "timestamp":time.time(),
                        "run_meta":{
                            "python":platform.python_version(),
                            "prereg_sha256":sha256(HERE/"PREREGISTRATION_v0_3.md"),
                            "stimuli_sha256":sha256(HERE/"stimuli_v0_3.csv"),
                            "rationale_sha256":sha256(HERE/"RATIONALE_FROM_v0_2.md")
                        }
                    }
                except Exception as e:
                    err=str(e)
                    status="manipulation_failure" if "MANIPULATION_FAILURE" in err else "technical_failure"
                    row={
                        "status":status,
                        "item_id":it["item_id"],
                        "condition":condition,
                        "model":model,
                        "temperature":args.temperature,
                        "timeout":args.timeout,
                        "error":repr(e),
                        "duration_sec":time.time()-started,
                        "timestamp":time.time()
                    }

                fout.write(json.dumps(row,ensure_ascii=False)+"\n")
                fout.flush()

                if row["status"]=="valid":
                    print(it["item_id"],condition,"VALID")
                else:
                    print(it["item_id"],condition,row["status"].upper(),row["error"])
                    raise RuntimeError("v0.3 stopped fail-closed after "+row["status"])

if __name__=="__main__":
    main()
