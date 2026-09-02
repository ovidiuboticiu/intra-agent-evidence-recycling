# IAER v0.5.1 — frozen exploratory diagnostic plan

Frozen after observing the v0.5.0 preregistered preflight failure and before
running any v0.5.1 diagnostic calls.

## Status and scope

This is an exploratory diagnostic. It is not a confirmatory hypothesis test,
has no inferential alpha threshold, and cannot change the status of v0.5.0.
Its purpose is to inform a later, separately preregistered replication.

## Fixed model and decoding

- API identifier: `microsoft_phi-4-mini-instruct`
- GGUF: Bartowski Microsoft Phi-4-mini-instruct Q4_K_M
- model SHA-256:
  `01999f17c39cc3074afae5e9c539bc82d45f2dd7faa3917c66cbef76fce8c0c2`
- temperature: `0`
- seed: `42`
- structured JSON schema: strict boolean `true`
- no explicit reasoning payload requested

## Items and balance

Eight new fictional binary items are used. Each of the four cells defined by
INITIAL (`CLAIM_A`, `CLAIM_B`) and presentation order (`A_FIRST`, `B_FIRST`)
contains two items. Entity names and claim-value tokens do not occur in the
v0.5.0 confirmatory stimuli or preflight sentinels.

## Evidence conditions

Each item is evaluated under both conditions:

1. `source_only`: one independent source of reliability 0.65 supports INITIAL,
   then one new independent source of reliability 0.80 supports COUNTER.
   Normative expected choice: COUNTER.
2. `independent_five`: five conditionally independent sources of reliability
   0.65 support INITIAL, then one new independent source of reliability 0.80
   supports COUNTER. Normative expected choice: INITIAL.

## Response/instruction modes

Each item-condition pair is evaluated under all three modes:

1. `claim_label`: reproduce the v0.5.0 choice representation, returning
   `CLAIM_A` or `CLAIM_B`.
2. `value_token`: use the same qualitative instruction but return the fictional
   value token rather than the claim label.
3. `explicit_odds`: return the fictional value token after an explicit
   instruction to combine conditionally independent evidence using likelihood
   ratios.

Total planned calls: `8 × 2 × 3 = 48`.

The task order is deterministically shuffled with diagnostic order seed 510.

## Descriptive outputs

The frozen analyzer reports exact counts and proportions for:

- overall normative accuracy;
- accuracy by mode and evidence condition;
- accuracy by INITIAL label and presentation order;
- `CLAIM_A` choice frequency after mapping all outputs back to claim identity;
- item-paired changes from `claim_label` to `value_token`;
- item-paired changes from `value_token` to `explicit_odds`.

No p-values, confidence intervals, or confirmatory conclusions are produced.

## Interpretation guide

- Better mirrored performance in `value_token` than `claim_label` would be
  consistent with response-label asymmetry.
- Better performance in `explicit_odds` than `value_token`, especially for
  `independent_five`, would be consistent with an evidence-integration or
  instruction-following limitation.
- Persistent asymmetry across all modes would indicate that neither simple
  explanation is sufficient.

These patterns are descriptive clues, not identified internal mechanisms.

## Technical policy

Each request may retry once only for timeout, connection reset, socket, or URL
transport errors. A valid response is never rerun. A schema/parse failure or
two consecutive transport failures writes an auditable failure row and stops
collection. Resumption is permitted only for infrastructure recovery with the
same frozen files and configuration.

