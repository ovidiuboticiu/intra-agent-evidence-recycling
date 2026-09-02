# IAER v0.5.1 diagnostic — frozen model environment

The diagnostic uses the same local model identity and inference configuration
as the closed v0.5.0 preregistered attempt.

## Model identity

- Publisher/build: Bartowski Microsoft Phi-4-mini-instruct GGUF
- Quantization: Q4_K_M
- File: `microsoft_Phi-4-mini-instruct-Q4_K_M.gguf`
- API identifier: `microsoft_phi-4-mini-instruct`
- File size shown by LM Studio: 2.49 GB
- Model SHA-256:
  `01999f17c39cc3074afae5e9c539bc82d45f2dd7faa3917c66cbef76fce8c0c2`

## LM Studio load configuration

- LM Studio version: 0.4.23
- Context length: 8192
- GPU offload: 2 layers
- CPU thread pool size: 6
- Evaluation batch size: 2048
- Physical batch size: 512
- Maximum concurrent predictions: 1
- Unified KV cache: off
- Context checkpoints: 32
- Reasoning budget message: blank
- RoPE frequency base/scale: automatic
- Offload KV cache to GPU: on
- Keep model in memory: on
- mmap: on
- seed: 42
- speculative decoding: off
- chat template: model default
- flash attention: on
- K/V cache quantization: off

## Request configuration

- Base URL: `http://127.0.0.1:1234/v1`
- Temperature: 0
- Seed: 42
- Streaming: off
- Maximum completion tokens: 96
- Strict structured JSON schema
- One retry permitted only for defined transport failures

