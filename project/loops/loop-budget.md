# Loop Budget

Status: active for planning; no cloud model execution enabled by default.

## Defaults

| Resource | Default cap | Rule |
|---|---:|---|
| Revision loops | 2 | Stop after second revision route and escalate. |
| Item retries | 3 | Stop per item after three failed attempts. |
| Parallel branches | 5 | Use only for independent extraction/review tasks. |
| Cloud model spend | 0 | Cloud models are disabled until credentials, budget, and source boundary are approved. |
| Mistral Medium passes | 0 | Enable only for final sanitized strategy/copy passes after approval. |
| Mistral Small passes | 0 | Enable only for sanitized batch/draft normalization after approval. |

## Local Model Rule

Ollama/Qwythos may be used for bounded local minor/background tasks when the server is running. `gemma4:e4b` remains the fallback.

## Escalation

Pause and write budget status when:

- a cloud model is requested
- a run would exceed the retry cap
- a broad research crawl is requested
- a persistent memory layer would ingest new source material
