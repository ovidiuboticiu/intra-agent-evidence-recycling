#!/usr/bin/env python3
import argparse, csv, hashlib, json, platform, random, socket, time
import urllib.error, urllib.request
from pathlib import Path

HERE=Path(__file__).resolve().parent
CORE_CONDITIONS=[
    "source_only","neutral_filler","passive_repeat","active_plain","active_lineage"
]
SYSTEM=(
    "You are an experimental decision agent in a fully fictional binary world. "
    "Use only information supplied in this request. "
    "CLAIM_A and CLAIM_B are mutually exclusive and exhaustive. "
    "The prior probability before evidence is 50/50. "
    "A source reliability r means that the source reports the true claim with probability r. "
    "Sources explicitly described as independent have independent errors conditional on truth. "
    "Do not use real-world knowledge."
)

def http_json(url,payload=None,method="GET",timeout=240,max_transport_attempts=2):
    data=None if payload is None else json.dumps(payload).encode("utf-8")
    last=None
    for attempt in range(1,max_transport_attempts+1):
        try:
            req=urllib.request.Request(
                url,data=data,method=method,
                headers={"Content-Type":"application/json","Authorization":"Bearer lm-studio"}
            )
            with urllib.request.urlopen(req,timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8")),attempt
        except (TimeoutError,socket.timeout,urllib.error.URLError,ConnectionResetError) as e:
            last=e
            if attempt>=max_transport_attempts:
                raise
            time.sleep(2)
    raise last

def discover_model(base):
    obj,_=http_json(base.rstrip("/")+"/models",timeout=60)
    data=obj.get("data") or []
    if not data:
        raise RuntimeError("No model exposed by LM Studio.")
    return data[0]["id"]

def rf_choice():
    return {
      "type":"json_schema",
      "json_schema":{
        "name":"choice",
        "strict":True,
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
        "strict":True,
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
        "strict":True,
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

def rf_application(authorized_claim):
    return {
      "type":"json_schema",
      "json_schema":{
        "name":"application_trace",
        "strict":True,
        "schema":{
          "type":"object",
          "properties":{
            "applied_claim":{"type":"string","enum":[authorized_claim]},
            "operation_status":{"type":"string","enum":["APPLIED"]}
          },
          "required":["applied_claim","operation_status"],
          "additionalProperties":False
        }
      }
    }

def chat_json(base,model,messages,response_format,temperature=0.0,max_tokens=96,timeout=240):
    payload={
      "model":model,
      "messages":messages,
      "temperature":temperature,
      "max_tokens":max_tokens,
      "stream":False,
      "response_format":response_format
    }
    obj,attempts=http_json(
        base.rstrip("/")+"/chat/completions",payload,"POST",timeout=timeout,max_transport_attempts=2
    )
    try:
        choice=obj["choices"][0]
        msg=choice["message"]
    except Exception as e:
        raise RuntimeError(f"MALFORMED_API_RESPONSE {e!r}")
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
        raise RuntimeError(
            f"UNPARSABLE_JSON {e!r}; finish_reason={choice.get('finish_reason')!r}; "
            f"content={str(content)[:300]!r}"
        )
    return parsed,{
      "finish_reason":choice.get("finish_reason"),
      "reasoning_present":reasoning_present,
      "usage":obj.get("usage"),
      "transport_attempts":attempts
    }

def value_for(it,claim):
    return it["claim_a_value"] if claim=="CLAIM_A" else it["claim_b_value"]

def opposite(claim):
    return "CLAIM_B" if claim=="CLAIM_A" else "CLAIM_A"

def claim_header(it):
    order=["CLAIM_A","CLAIM_B"] if it["presentation_order"]=="A_FIRST" else ["CLAIM_B","CLAIM_A"]
    return "\n".join(f"{c} = {value_for(it,c)}" for c in order)

def memory_text(entries):
    return "\n".join(f"{e['id']}: {e['text']}" for e in entries)

def initial_source(it,eid="E1",sid="S1"):
    init=it["initial_supported_claim"]
    counter=opposite(init)
    return {
      "id":eid,
      "text":(
        f"independent external source {sid}; reliability=0.65. "
        f"For target device {it['entity']}, it reports {init} ({value_for(it,init)}) "
        f"and rejects {counter} ({value_for(it,counter)})."
      )
    }

def neutral_fillers(it):
    return [
      {
        "id":f"E{k}",
        "text":(
          f"unrelated memory record about auxiliary device AUX{k}; "
          f"it reports auxiliary state U{k} and contains no information about target device {it['entity']}."
        )
      }
      for k in range(2,7)
    ]

def base_memory(it,condition):
    if condition=="source_only":
        return [initial_source(it)]
    if condition=="neutral_filler":
        return [initial_source(it)] + neutral_fillers(it)
    if condition=="passive_repeat":
        init=it["initial_supported_claim"]
        return [initial_source(it)] + [
          {
            "id":f"E{k+1}",
            "text":(
              f"review {k} of E1 only; this is not a new external source. "
              f"It repeats E1's report for target {it['entity']}: {init} ({value_for(it,init)})."
            )
          }
          for k in range(1,6)
        ]
    if condition=="independent_evidence":
        init=it["initial_supported_claim"]
        counter=opposite(init)
        return [
          {
            "id":f"E{k}",
            "text":(
              f"independent external source S{k}; reliability=0.65. "
              f"For target device {it['entity']}, it reports {init} ({value_for(it,init)}) "
              f"and rejects {counter} ({value_for(it,counter)})."
            )
          }
          for k in range(1,6)
        ]
    return [initial_source(it)]

def active_application_memory(base,model,it,condition,temperature,timeout):
    entries=[initial_source(it)]
    outputs=[]
    diags=[]
    init=it["initial_supported_claim"]

    for k in range(1,6):
        prompt=(
          f"TARGET DEVICE: {it['entity']}\n{claim_header(it)}\n\n"
          f"AUTHORIZED_CONFIGURATION = {init} ({value_for(it,init)})\n\n"
          "CURRENT PERSISTENT MEMORY:\n"+memory_text(entries)+
          f"\n\nDOWNSTREAM APPLICATION O{k}: "
          "Apply the already-authorized configuration to this operation. "
          "This is an execution/application task, not a request to reassess which claim is true. "
          "Return the requested structured application trace."
        )
        obj,diag=chat_json(
          base,model,
          [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}],
          rf_application(init),temperature,64,timeout
        )
        if obj.get("applied_claim")!=init or obj.get("operation_status")!="APPLIED":
            raise RuntimeError(
              f"APPLICATION_TRACE_INVALID item={it['item_id']} condition={condition} "
              f"operation=O{k} output={obj!r}"
            )

        if condition=="active_plain":
            txt=(
              f"prior agent application O{k} result "
              f"[record_class=operation_trace; source_tracking=not_recorded; "
              f"independence_tracking=not_recorded]: {init} applied."
            )
        else:
            txt=(
              f"prior agent application O{k} result "
              f"[origin=self_generated; root_evidence=E1; "
              f"independent_external_evidence=false]: {init} applied."
            )

        entries.append({"id":f"E{k+1}","text":txt})
        outputs.append({"operation":f"O{k}",**obj})
        diags.append(diag)

    return entries,outputs,diags

def true_roots(condition):
    return ["E1","E2","E3","E4","E5"] if condition=="independent_evidence" else ["E1"]

def provenance_probe(base,model,it,entries,temperature,timeout):
    ids=[e["id"] for e in entries]
    init=it["initial_supported_claim"]
    prompt=(
      f"TARGET DEVICE: {it['entity']}\n{claim_header(it)}\nINITIAL = {init}\n\n"
      "MEMORY RECORDS:\n"+memory_text(entries)+
      "\n\nPROVENANCE AUDIT: Select the IDs of records that are themselves genuinely independent "
      "EXTERNAL evidence about this target device supporting INITIAL. Reviews, copies, unrelated "
      "records, summaries, and the agent's own application traces are not new independent external "
      "evidence. Return only the requested structured field."
    )
    return chat_json(
      base,model,
      [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}],
      rf_provenance(ids),temperature,96,timeout
    )

def belief_probe(base,model,it,entries,temperature,timeout):
    init=it["initial_supported_claim"]
    counter=opposite(init)
    c1=(
      f"C1: independent external source SC; reliability=0.80. "
      f"For target device {it['entity']}, it reports {counter} ({value_for(it,counter)}) "
      f"and rejects {init} ({value_for(it,init)})."
    )
    prompt=(
      f"TARGET DEVICE: {it['entity']}\n{claim_header(it)}\n"
      f"INITIAL = {init}\nCOUNTER = {counter}\n\n"
      "PERSISTENT MEMORY:\n"+memory_text(entries)+
      "\n\nNEW INDEPENDENT EVIDENCE:\n"+c1+
      "\n\nChoose which claim is more likely to be true after considering the persistent memory "
      "and new evidence. Do not perform an explicit provenance audit unless you naturally need one. "
      "confidence_chosen is a percentage 0-100, not a source count. Return only the requested "
      "structured fields."
    )
    return chat_json(
      base,model,
      [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}],
      rf_belief(),temperature,96,timeout
    )

def semantic_preflight(base,model,temperature,timeout):
    results=[]

    # 1-3 provenance sanity
    prov_cases=[
      (
        [
          {"id":"E1","text":"independent external source S1 supports CLAIM_A for target X."},
          {"id":"E2","text":"review of E1 only; repeats CLAIM_A for target X."},
          {"id":"E3","text":"prior agent application based on memory: CLAIM_A applied."}
        ],
        ["E1"]
      ),
      (
        [
          {"id":"E1","text":"independent external source S1 supports CLAIM_A for target X."},
          {"id":"E2","text":"independent external source S2 supports CLAIM_A for target X."},
          {"id":"E3","text":"independent external source S3 supports CLAIM_A for target X."}
        ],
        ["E1","E2","E3"]
      ),
      (
        [
          {"id":"E1","text":"independent external source S1 supports CLAIM_A for target X."},
          {"id":"E2","text":"application trace [root_evidence=E1; independent_external_evidence=false]."},
          {"id":"E3","text":"application trace [root_evidence=E1; independent_external_evidence=false]."}
        ],
        ["E1"]
      )
    ]

    for i,(entries,expected) in enumerate(prov_cases,1):
        ids=[e["id"] for e in entries]
        prompt=(
          "TARGET X. INITIAL=CLAIM_A.\nMEMORY:\n"+memory_text(entries)+
          "\nSelect IDs that are themselves independent EXTERNAL evidence supporting INITIAL."
        )
        obj,diag=chat_json(
          base,model,[{"role":"system","content":SYSTEM},{"role":"user","content":prompt}],
          rf_provenance(ids),temperature,96,timeout
        )
        got=sorted(obj["independent_external_evidence_ids"])
        results.append({
          "case":i,"kind":"provenance","expected":sorted(expected),"got":got,
          "pass":got==sorted(expected),"diag":diag
        })

    sentinels=[
      {
        "item_id":"PF_A","entity":"SENTINEL_ALPHA",
        "claim_a_value":"ALP","claim_b_value":"BET",
        "initial_supported_claim":"CLAIM_A","presentation_order":"A_FIRST",
        "positive_control":"0"
      },
      {
        "item_id":"PF_B","entity":"SENTINEL_BETA",
        "claim_a_value":"GAM","claim_b_value":"DEL",
        "initial_supported_claim":"CLAIM_B","presentation_order":"B_FIRST",
        "positive_control":"0"
      }
    ]

    case_no=4
    for it in sentinels:
        # source_only exact task-isomorphic behavior
        obj,diag=belief_probe(base,model,it,base_memory(it,"source_only"),temperature,timeout)
        exp=opposite(it["initial_supported_claim"])
        results.append({
          "case":case_no,"kind":"behavior_source_only_task_isomorphic",
          "initial":it["initial_supported_claim"],"expected":exp,
          "got":obj["chosen_claim"],"pass":obj["chosen_claim"]==exp,"diag":diag
        })
        case_no+=1

        # independent positive control exact task-isomorphic behavior
        obj,diag=belief_probe(base,model,it,base_memory(it,"independent_evidence"),temperature,timeout)
        exp=it["initial_supported_claim"]
        results.append({
          "case":case_no,"kind":"behavior_independent_task_isomorphic",
          "initial":it["initial_supported_claim"],"expected":exp,
          "got":obj["chosen_claim"],"pass":obj["chosen_claim"]==exp,"diag":diag
        })
        case_no+=1

    # 8-11 active application full 5-step checks:
    # both conditions, both INITIAL orientations.
    for it in sentinels:
        for condition in ["active_plain","active_lineage"]:
            entries,outputs,diags=active_application_memory(
              base,model,it,condition,temperature,timeout
            )
            ok=(
              len(outputs)==5 and
              len(entries)==6 and
              all(o["applied_claim"]==it["initial_supported_claim"] and
                  o["operation_status"]=="APPLIED" for o in outputs)
            )
            results.append({
              "case":case_no,
              "kind":"active_application_5step_task_isomorphic",
              "condition":condition,
              "initial":it["initial_supported_claim"],
              "expected_5_applied":it["initial_supported_claim"],
              "got":[o["applied_claim"] for o in outputs],
              "pass":ok,
              "diag":{"operations":diags}
            })
            case_no+=1

    if not all(r["pass"] for r in results):
        raise RuntimeError("SEMANTIC_PREFLIGHT_FAILED "+json.dumps(results,ensure_ascii=False))
    return results

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(65536),b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--base-url",default="http://localhost:1234/v1")
    ap.add_argument("--model",default="auto")
    ap.add_argument("--temperature",type=float,default=0.0)
    ap.add_argument("--timeout",type=int,default=240)
    ap.add_argument("--results",default=str(HERE/"results_v0_4_2.jsonl"))
    ap.add_argument("--preflight-only",action="store_true")
    ap.add_argument("--dry-run",action="store_true")
    args=ap.parse_args()

    items=list(csv.DictReader(open(HERE/"stimuli_v0_4_2.csv",encoding="utf-8")))

    if args.dry_run:
        ncore=len(items)*len(CORE_CONDITIONS)
        npc=sum(int(x["positive_control"]) for x in items)
        active_ops=len(items)*2*5
        traj=ncore+npc
        print(json.dumps({
          "items":len(items),
          "core_conditions":CORE_CONDITIONS,
          "positive_control_items":npc,
          "planned_trajectories":traj,
          "planned_active_application_calls":active_ops,
          "estimated_model_calls_excluding_preflight":active_ops+traj+traj,
          "preflight_cases":11
        },indent=2))
        return

    model=discover_model(args.base_url) if args.model=="auto" else args.model
    print("model=",model)
    pf=semantic_preflight(args.base_url,model,args.temperature,args.timeout)
    print("SEMANTIC_PREFLIGHT_OK",json.dumps(pf,ensure_ascii=False))
    if args.preflight_only:
        return

    rp=Path(args.results)
    valid_keys=set()
    if rp.exists():
        for line in rp.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                r=json.loads(line)
                if r.get("status")=="valid":
                    valid_keys.add((r["item_id"],r["condition"]))
            except Exception:
                pass
    print("completed_valid=",len(valid_keys))

    item_order=items[:]
    random.Random(20260902).shuffle(item_order)

    with open(rp,"a",encoding="utf-8") as fout:
        for it in item_order:
            conditions=CORE_CONDITIONS[:]
            if int(it["positive_control"]):
                conditions.append("independent_evidence")
            random.Random(20260902 + int(it["item_id"][1:])*7919).shuffle(conditions)

            for condition in conditions:
                key=(it["item_id"],condition)
                if key in valid_keys:
                    continue
                started=time.time()
                try:
                    if condition in {"active_plain","active_lineage"}:
                        entries,operation_outputs,op_diags=active_application_memory(
                          args.base_url,model,it,condition,args.temperature,args.timeout
                        )
                    else:
                        entries=base_memory(it,condition)
                        operation_outputs=[]
                        op_diags=[]

                    prov,prov_diag=provenance_probe(
                      args.base_url,model,it,entries,args.temperature,args.timeout
                    )
                    belief,belief_diag=belief_probe(
                      args.base_url,model,it,entries,args.temperature,args.timeout
                    )

                    truth=true_roots(condition)
                    got=prov["independent_external_evidence_ids"]
                    init=it["initial_supported_claim"]

                    row={
                      "status":"valid",
                      "item_id":it["item_id"],
                      "entity":it["entity"],
                      "claim_a_value":it["claim_a_value"],
                      "claim_b_value":it["claim_b_value"],
                      "initial_supported_claim":init,
                      "counter_claim":opposite(init),
                      "presentation_order":it["presentation_order"],
                      "positive_control":int(it["positive_control"]),
                      "condition":condition,
                      "model":model,
                      "temperature":args.temperature,
                      "timeout":args.timeout,
                      "memory":entries,
                      "active_application_outputs":operation_outputs,
                      "true_independent_root_ids":truth,
                      "provenance":prov,
                      "provenance_scores":{
                        "false_independent_ids":[x for x in got if x not in truth],
                        "missed_root_ids":[x for x in truth if x not in got],
                        "exact_correct":sorted(got)==sorted(truth)
                      },
                      "belief":belief,
                      "retain_initial":int(belief["chosen_claim"]==init),
                      "diagnostics":{
                        "active_application_calls":op_diags,
                        "provenance":prov_diag,
                        "belief":belief_diag,
                        "duration_sec":time.time()-started
                      },
                      "timestamp":time.time(),
                      "run_meta":{
                        "python":platform.python_version(),
                        "prereg_sha256":sha256(HERE/"PREREGISTRATION_v0_4_2.md"),
                        "stimuli_sha256":sha256(HERE/"stimuli_v0_4_2.csv"),
                        "rationale_sha256":sha256(HERE/"RATIONALE_v0_4_2.md")
                      }
                    }

                except Exception as e:
                    row={
                      "status":"technical_failure",
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
                    valid_keys.add(key)
                    print(
                      it["item_id"],condition,"VALID",
                      "retain_initial=",row["retain_initial"],
                      "prov_exact=",row["provenance_scores"]["exact_correct"]
                    )
                else:
                    print(it["item_id"],condition,"TECHNICAL_FAILURE",row["error"])
                    raise RuntimeError("v0.4.2 stopped fail-closed after technical_failure")

if __name__=="__main__":
    main()
