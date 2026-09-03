#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, os, random, socket, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

HERE=Path(__file__).resolve().parent
STIMULI=HERE/"stimuli_v0_7.csv"
CONFIG=HERE/"config_v0_7.json"
SPEC=HERE/"PROMPT_SPEC_v0_7.json"
AUTH=HERE/"PUBLIC_FREEZE_AUTHORIZATION_v0_7.json"
CONDS=["two_initial_one_counter","one_initial_two_counter",
       "derived_lure_initial_two_counter","three_initial_two_counter"]

def hfile(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()

def loadj(p): return json.loads(p.read_text(encoding="utf-8"))
def opp(x): return "CLAIM_B" if x=="CLAIM_A" else "CLAIM_A"
def val(item,c): return item["claim_a_value"] if c=="CLAIM_A" else item["claim_b_value"]
def utc(): return datetime.now(timezone.utc).isoformat().replace("+00:00","Z")

def http(method,url,payload=None,timeout=600):
    body=None if payload is None else json.dumps(payload).encode()
    last=None
    for attempt in (1,2):
        req=Request(url,data=body,method=method)
        req.add_header("Accept","application/json")
        req.add_header("Authorization","Bearer lm-studio")
        if body is not None:req.add_header("Content-Type","application/json")
        try:
            with urlopen(req,timeout=timeout) as r:
                return json.loads(r.read().decode()),attempt
        except HTTPError as e:
            raise RuntimeError(f"HTTP {e.code}: "+e.read().decode(errors="replace"))
        except (TimeoutError,socket.timeout,URLError,ConnectionResetError) as e:
            last=e
            if attempt==2: raise RuntimeError(f"TRANSPORT_RETRY_EXHAUSTED: {e}")
            time.sleep(2)
    raise RuntimeError(str(last))

def find_model_file(cfg):
    root=Path.home()/".lmstudio"/"models"
    matches=[p for p in root.rglob("*.gguf") if p.name.lower()==cfg["model_filename"].lower()]
    if len(matches)!=1:
        raise RuntimeError(f"MODEL_FILE_COUNT_INVALID expected=1 found={len(matches)}")
    p=matches[0]
    if p.stat().st_size != int(cfg["model_size_bytes"]):
        raise RuntimeError("MODEL_SIZE_MISMATCH")
    if hfile(p) != cfg["model_sha256"]:
        raise RuntimeError("MODEL_SHA256_MISMATCH")
    return p

def load_stimuli():
    with STIMULI.open("r",encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    if len(rows)!=12: raise RuntimeError("STIMULI_N_INVALID")
    return rows

def claim_header(item):
    cs=["CLAIM_A","CLAIM_B"]
    if item["presentation_order"]=="B_FIRST": cs.reverse()
    return "\n".join(f"{c} = {val(item,c)}" for c in cs)

def root_line(rid,claim,item):
    return f"ROOT SOURCE {rid}: independent; supports {claim} ({val(item,claim)})."

def derived_line(did,root,claim,item):
    return (f"DERIVED RECORD {did}: root_source_id={root}; supports {claim} "
            f"({val(item,claim)}); adds_new_epistemic_vote=false.")

def build(item,cond,spec):
    ini=item["initial_supported_claim"]; ctr=opp(ini)
    if cond=="two_initial_one_counter":
        rec=[root_line("I1",ini,item),root_line("I2",ini,item),root_line("C1",ctr,item)]
        exp=ini
    elif cond=="one_initial_two_counter":
        rec=[root_line("I1",ini,item),root_line("C1",ctr,item),root_line("C2",ctr,item)]
        exp=ctr
    elif cond=="derived_lure_initial_two_counter":
        rec=[root_line("I1",ini,item)]
        rec += [derived_line(f"D{k}","I1",ini,item) for k in range(1,6)]
        rec += [root_line("C1",ctr,item),root_line("C2",ctr,item)]
        exp=ctr
    elif cond=="three_initial_two_counter":
        rec=[root_line("I1",ini,item),root_line("I2",ini,item),root_line("I3",ini,item),
             root_line("C1",ctr,item),root_line("C2",ctr,item)]
        exp=ini
    else: raise RuntimeError("UNKNOWN_CONDITION")
    rule="\n".join(f"{n+1}. {x}" for n,x in enumerate(spec["epistemic_rule"]))
    prompt=(f"TARGET DEVICE: {item['entity']}\n{claim_header(item)}\n"
            f"INITIAL={ini}\nCOUNTER={ctr}\n\nEPISTEMIC RULE:\n{rule}\n\n"
            "RECORDS:\n"+"\n".join(rec)+"\n\n"+spec["semantic_instruction"])
    return prompt,exp

def verify(cfg):
    if not AUTH.is_file():
        raise RuntimeError("PUBLIC_FREEZE_NOT_AUTHORIZED")
    auth=loadj(AUTH)
    if auth.get("authorized") is not True:
        raise RuntimeError("PUBLIC_FREEZE_NOT_AUTHORIZED")
    required_auth=["github_release_tag","github_commit_sha","archive_asset_sha256"]
    for k in required_auth:
        v=auth.get(k)
        if not isinstance(v,str) or not v.strip() or "[" in v:
            raise RuntimeError(f"PUBLIC_FREEZE_AUTH_INCOMPLETE: {k}")
    if len(auth["github_commit_sha"]) != 40:
        raise RuntimeError("PUBLIC_FREEZE_COMMIT_SHA_INVALID")
    if len(auth["archive_asset_sha256"]) != 64:
        raise RuntimeError("PUBLIC_FREEZE_ARCHIVE_SHA_INVALID")

    if cfg.get("freeze_status")!="FROZEN":
        raise RuntimeError("CONFIG_NOT_FROZEN")
    mp=HERE/cfg["manifest_filename"]
    if not mp.is_file():
        raise RuntimeError("MANIFEST_MISSING")
    base=HERE.parent
    for line in mp.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        dig,rel=line.split("  ",1)
        p=base/rel
        if not p.is_file() or hfile(p)!=dig:
            raise RuntimeError(f"FROZEN_FILE_MISMATCH {rel}")

    find_model_file(cfg)

    models,_=http("GET",cfg["api_base"].rstrip("/")+"/models",timeout=60)
    ids=[x.get("id") for x in models.get("data",[])]
    if cfg["model_id"] not in ids:
        raise RuntimeError("API_MODEL_ID_MISSING")
    return load_stimuli()

def append(row):
    p=HERE/"results_v0_7.jsonl"
    with p.open("a",encoding="utf-8",newline="\n") as f:
        f.write(json.dumps(row,separators=(",",":"),ensure_ascii=False)+"\n");f.flush();os.fsync(f.fileno())

def main():
    if not CONFIG.is_file(): raise SystemExit("Missing config_v0_7.json")
    cfg=loadj(CONFIG); spec=loadj(SPEC); items=verify(cfg)
    p=HERE/"results_v0_7.jsonl"
    existing=[];keys=set()
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip():continue
            r=json.loads(line);existing.append(r)
            if r.get("status")!="valid": raise RuntimeError("RECORDED_FAILURE_EXISTS")
            k=(r["item_id"],r["condition"])
            if k in keys: raise RuntimeError("DUPLICATE_KEY")
            keys.add(k)
    schedule=[(i,c) for i in items for c in CONDS]
    random.Random(cfg["order_seed"]).shuffle(schedule)
    print("IAER v0.7 MEASUREMENT-DECOUPLING PILOT")
    print("Existing valid rows:",len(keys))
    print("BLINDED COLLECTION; CHOICES/CORRECTNESS WILL NOT BE PRINTED")
    for seq,(item,cond) in enumerate(schedule,1):
        key=(item["item_id"],cond)
        if key in keys: continue
        started=utc();t0=time.monotonic()
        prompt,expected=build(item,cond,spec)
        payload={
          "model":cfg["model_id"],
          "messages":[{"role":"system","content":spec["system"]},{"role":"user","content":prompt}],
          "temperature":cfg["temperature"],"seed":cfg["seed"],"max_tokens":cfg["max_tokens"],
          "stream":False,
          "response_format":{"type":"json_schema","json_schema":{
             "name":"iaer_v0_7_choice","strict":True,"schema":spec["response_schema"]}}
        }
        try:
            resp,attempts=http("POST",cfg["api_base"].rstrip("/")+"/chat/completions",payload,int(cfg["timeout_seconds"]))
            ch=resp["choices"][0]
            if ch.get("finish_reason")!="stop": raise RuntimeError("NON_STOP_FINISH_REASON")
            content=ch["message"]["content"]
            parsed=json.loads(content)
            if set(parsed)!={"chosen_claim"} or parsed["chosen_claim"] not in {"CLAIM_A","CLAIM_B"}:
                raise RuntimeError("SCHEMA_CONTENT_INVALID")
            row={"status":"valid","sequence":seq,"item_id":item["item_id"],"entity":item["entity"],
                 "initial_supported_claim":item["initial_supported_claim"],
                 "presentation_order":item["presentation_order"],"condition":cond,
                 "expected_claim":expected,"chosen_claim":parsed["chosen_claim"],
                 "correct":int(parsed["chosen_claim"]==expected),
                 "model":cfg["model_id"],"model_sha256":cfg["model_sha256"],
                 "temperature":cfg["temperature"],"seed":cfg["seed"],
                 "started_at_utc":started,"elapsed_seconds":round(time.monotonic()-t0,3),
                 "diagnostics":{"transport_attempts":attempts,"finish_reason":ch.get("finish_reason"),
                                "usage":resp.get("usage"),
                                "user_prompt_sha256":hashlib.sha256(prompt.encode()).hexdigest()},
                 "run_meta":{"manifest_sha256":hfile(HERE/cfg["manifest_filename"]),
                             "prompt_spec_sha256":hfile(SPEC)}}
            append(row);keys.add(key);print(f"progress {len(keys)}/48")
        except Exception as e:
            append({"status":"failure","sequence":seq,"item_id":item["item_id"],"condition":cond,
                    "error_type":type(e).__name__,"error":str(e),"started_at_utc":started,
                    "elapsed_seconds":round(time.monotonic()-t0,3)})
            raise
    print("COLLECTION COMPLETE: 48/48 VALID PLANNED KEYS")
    print("Run frozen analyzer next.")

if __name__=="__main__": main()
