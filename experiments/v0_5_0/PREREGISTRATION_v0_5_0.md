# PREREGISTRATION — Intra-Agent Evidence Recycling v0.5.0

Frozen before the mandatory behavioral preflight and before confirmatory data
collection.

## Study status

BEHAVIORAL-CONFIRMATORY, fixed-N, cross-family replication study.

v0.5.0 tests whether the v0.4.3 memory-source multiplication effect replicates
in Microsoft Phi-4-mini-instruct. v0.4.3 remains closed and unchanged.

## Frozen model and configuration

- Original model: `microsoft/Phi-4-mini-instruct`
- GGUF repository: `bartowski/microsoft_Phi-4-mini-instruct-GGUF`
- File: `microsoft_Phi-4-mini-instruct-Q4_K_M.gguf`
- Quantization: `Q4_K_M`
- Model file SHA-256:
  `01999f17c39cc3074afae5e9c539bc82d45f2dd7faa3917c66cbef76fce8c0c2`
- LM Studio: `0.4.23`
- API identifier: `microsoft_phi-4-mini-instruct`
- API base URL: `http://127.0.0.1:1234/v1`
- Context length: 8192
- GPU offload: 2 layers
- CPU thread pool: 6
- Evaluation batch size: 2048
- Physical batch size: 512
- Maximum concurrent predictions: 1
- Unified KV cache: OFF
- Context checkpoints: 32
- Offload KV cache to GPU: ON
- Keep model in memory: ON
- mmap: ON
- Flash Attention: ON
- K/V cache quantization: OFF
- Speculative decoding: OFF
- Chat template: model default
- Reasoning budget: disabled/blank
- temperature: 0
- seed: 42
- timeout: 240 seconds
- one automatic retry is allowed only for a transport-level failure
- structured-output schemas use the Python boolean `True` for `strict`

The non-scientific technical smoke test passed before this freeze. Its output is
archived but is not scientific data.

## Stimuli

32 new fictional binary items. No entity or claim-value token is reused from
the published v0.3.1, v0.4.1, v0.4.2, or v0.4.3 stimulus files.

The design is exactly balanced:

- INITIAL: 16 CLAIM_A, 16 CLAIM_B;
- presentation: 16 A_FIRST, 16 B_FIRST;
- INITIAL × presentation: 8 items in each of the four cells;
- positive-control subset: 8 prespecified items, two from each cell.

## Core conditions — all 32 items

1. `source_only`
   E1 is one independent external source, reliability 0.65, supporting INITIAL.

2. `neutral_filler`
   The same E1 plus five similarly sized unrelated memory records about other
   devices.

3. `passive_repeat`
   The same E1 plus five target-consistent review records derived only from E1.
   Every review explicitly states that it is not a new external source.

## Positive control — 8 prespecified items

4. `independent_evidence`
   E1 through E5 are five genuinely independent external sources, each with
   reliability 0.65, all supporting INITIAL.

Total planned trajectories: `32 × 3 + 8 = 104`.

## Counterevidence

C1 is one new independent external source, reliability 0.80, supporting
COUNTER. It is not described as authoritative, direct verification, or
superseding.

## Primary behavioral outcome

`retain_initial = 1` if the final belief probe selects INITIAL; otherwise 0.

## Single confirmatory hypothesis

### H1-R — cross-family replication of memory-source multiplication

P(retain_initial | passive_repeat) >
P(retain_initial | neutral_filler)

Paired effect:

`RD_H1R = mean(passive_repeat - neutral_filler)`

Confirmatory support requires BOTH:

- `RD_H1R >= +0.25`; and
- two-sided exact paired McNemar `p < 0.05`.

There is one confirmatory hypothesis, so no multiplicity correction is applied.
The two-sided test is fixed despite the directional hypothesis.

## Confirmatory interpretation

- If all validity gates pass and both support criteria pass: H1-R SUPPORTED.
- If all validity gates pass but either support criterion fails: H1-R NOT
  SUPPORTED.
- If any validity gate fails: INVALID/INCONCLUSIVE for confirmatory inference.

## Secondary descriptive outcomes

- passive_repeat versus source_only;
- neutral_filler versus source_only;
- confidence-based implied support for INITIAL;
- provenance-audit exactness and error patterns;
- descriptive comparison with the frozen v0.4.3 estimate.

No secondary result can rescue a failed confirmatory hypothesis.

## Provenance audit status

A provenance audit is collected in a separate API request for every trajectory,
but it is descriptive/exploratory only. It is not a validity gate, is not part
of H1-R, and cannot establish an internal provenance-use mechanism.

## Validity gates

V1 Counterevidence sensitivity:
`source_only` selects COUNTER on at least 24/32 items.

V2 Positive-control behavioral sensitivity:
`independent_evidence` retains INITIAL on at least 6/8 items.

V3 Dataset completeness:
all 104 planned item-condition keys have valid final records; there are no
duplicate valid keys, missing keys, extra keys, or unresolved technical-failure
keys.

V4 Frozen identity and integrity:
the API identifier is exact; the model file SHA-256 is exact; the technical
smoke test passed; the preregistration, stimuli, runner, analysis, rationale,
and environment record match `FREEZE_MANIFEST_v0_5_0.sha256`.

If any V1–V4 fails, confirmatory inference is INVALID/INCONCLUSIVE.

## Mandatory behavioral preflight — 4 cases

No provenance preflight gate is used.

The preflight must pass all four cases in one run:

1. task-isomorphic source_only with INITIAL=A → expected COUNTER;
2. task-isomorphic independent_evidence with INITIAL=A → expected INITIAL;
3. task-isomorphic source_only with INITIAL=B → expected COUNTER;
4. task-isomorphic independent_evidence with INITIAL=B → expected INITIAL.

The sentinel labels are not present in the 32 confirmatory items. The preflight
is written to `preflight_v0_5_0.json` and cannot be overwritten. A failed
preflight ends v0.5.0 as invalid/inconclusive for this model/configuration; it is
not tuned and rerun under the same version.

## Technical retry and interruption policy

Each API call may retry once only after timeout, socket timeout, URL/network
error, or connection reset. A valid belief or provenance response is never
rerun.

Parse/schema failure or two consecutive transport failures create an auditable
technical-failure row and stop collection fail-closed. Collection may resume
with the identical frozen files and configuration after infrastructure is
restored. Existing valid keys are skipped; failure rows are retained. A process
interruption before a row is written may likewise resume from the last complete
valid key.

## Fixed-N stopping and blinding to outcomes

No scientific peeking, early stopping, or condition-specific rerunning is
allowed. Complete all 104 trajectories unless fail-closed infrastructure stops
the run. During collection, the runner prints only item, condition, and
VALID/TECHNICAL_FAILURE status, never belief outcomes. Confirmatory analysis is
performed only after V3 completeness is established.

## Scope

A successful v0.5.0 establishes replication only for the frozen Phi-4 Mini
artifact, local runtime, task family, and configuration. Together with v0.4.3,
it would support cross-family robustness across two small local instruction
models. It would not by itself establish universality across LLMs, memory
architectures, tasks, or deployment stacks.
