# MODEL AND ENVIRONMENT RECORD — v0.5.0

## Model artifact

- Original weights: `microsoft/Phi-4-mini-instruct`
- GGUF quantizer/repository: `bartowski/microsoft_Phi-4-mini-instruct-GGUF`
- Local filename: `microsoft_Phi-4-mini-instruct-Q4_K_M.gguf`
- Format: GGUF
- Architecture reported by LM Studio: `phi3`
- Quantization: `Q4_K_M`
- Size shown by LM Studio: 2.49 GB
- SHA-256: `01999f17c39cc3074afae5e9c539bc82d45f2dd7faa3917c66cbef76fce8c0c2`

## Runtime

- Operating system: Windows 11
- LM Studio: 0.4.23
- Python observed in technical smoke test: 3.14.6
- API identifier: `microsoft_phi-4-mini-instruct`
- API endpoint: `http://127.0.0.1:1234/v1`

## Load settings

- context length: 8192
- GPU offload: 2
- CPU thread pool: 6
- evaluation batch size: 2048
- physical batch size: 512
- maximum concurrent predictions: 1
- Unified KV Cache: OFF
- context checkpoints: 32
- reasoning budget message: blank
- RoPE base and scale: Auto
- KV cache GPU offload: ON
- keep model in memory: ON
- mmap: ON
- seed: 42
- speculative decoding: OFF
- chat template: default embedded template
- Flash Attention: ON
- K/V cache quantization: OFF

## API generation settings

- temperature: 0
- seed: 42
- streaming: false
- maximum output tokens: 96
- timeout: 240 seconds
- strict JSON-schema structured output

## Pre-freeze technical compatibility test

- timestamp UTC: 2026-09-02T13:35:37.257552+00:00
- PASS
- exact API model identifier found
- strict JSON returned the expected fields
- finish reason: stop
- reasoning tokens: 0
- transport attempts: 1 for model listing, 1 for completion
- archived result SHA-256:
  `487dd8fc581fe206ef6dfb021f92d42267370aa60c42e2278c350f0abadf67f7`
