# IAER v0.6 — Model and Runtime Environment

Status: FINAL CONTENT FOR PUBLIC FREEZE A

## Candidate model

- Family: Mistral
- Base/instruct model: Ministral-3-8B-Instruct-2512
- Local distribution: GGUF
- Quantization: Q4_K_M
- Local GGUF filename: `Ministral-3-8B-Instruct-2512-Q4_k_m.gguf`
- Local GGUF size: `5198386976` bytes
- Local GGUF SHA-256: `e7480c2c16298ca644c9980e1301b6fea087f210900e69ada57ffd83d6016c02`
- Downloaded GGUF repository: `keisuke-miyako/Ministral-3-8B-Instruct-2512-gguf-q4_k_m`
- LM Studio API model identifier: `ministral-3-8b-instruct-2512`

The private absolute Windows path is intentionally omitted from the public environment record.

## Runtime

- LM Studio version: `0.4.23`
- API base: `http://127.0.0.1:1234/v1`
- Context length: `8192`
- temperature: `0`
- request seed: `42`
- maximum output tokens: `512`
- timeout: `600` seconds per transport attempt
- sequential collection only
- at most one automatic retry, and only for transport timeout/network/connection failure
- Structured Output: JSON Schema
- `strict`: boolean `true`
- no free-form rationale requested
- no chain-of-thought requested or stored

## Request independence

Each trajectory uses a fresh request message list and does not include prior experimental model outputs or LM Studio chat history.

## Technical capture

The local capture was made at `2026-09-03T17:35:40.990786Z`.
The capture script made no `/chat/completions` call. It only hashed the local GGUF and queried `/v1/models`.
`/v1/models` returned successfully and identified `ministral-3-8b-instruct-2512` as the unique Ministral candidate.
