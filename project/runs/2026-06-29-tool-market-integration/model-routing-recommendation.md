# Model Routing Recommendation

## Current Default

Codex is the operator and reviewer. Ollama is the local model execution layer for bounded minor/background work. Qwythos is the intended local model and `gemma4:e4b` remains fallback.

## Future Mistral Gate

Mistral is disabled by default until:

- credentials are approved and stored outside public files
- input packet is sanitized
- model ID and prompt version are logged
- budget cap is set
- AF Review runs after output

## Suggested Future Roles

| Model family | Role |
|---|---|
| Mistral Small | Batch normalization, extraction schema filling, draft ICP/copy variants. |
| Mistral Medium | Final strategy, PRD, ICP, proposal, or website-copy quality pass after evidence is fixed. |
| Mistral OCR | Document preparation only after a live model-name/privacy preflight. |

## Forbidden Inputs

- raw private transcripts
- private Notion exports
- credentials or env files
- unsanitized client material
- private LinkedIn/profile data
