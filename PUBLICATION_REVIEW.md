# Publication Review

Status: initial public folder prepared and checked.

## Checked Rules

- English-only public files.
- No API keys or credential values.
- No local absolute paths in public files.
- No private Notion page URLs in public files.
- No raw legacy files copied.
- No personal owner names copied from private task board.
- No deployment IDs or account IDs copied.
- Provider files are examples only.

## Known Non-Secret Model Reference

The public config references the local model name:

`hf.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF:Q4_K_M`

This is a public model identifier, not a secret.

## Approved And Completed Locally

- Ollama server start.
- `.env.local` creation.
- Qwythos and fallback smoke checks.
- Initial public Git commit.
- GitHub remote attachment.
- Evening automation creation.

## Still Not Installed

- LangGraph runtime package.
- CrewAI runtime package.
- LlamaIndex runtime package.
- UI dependencies.

These are documented as workflow configuration for now. Installing and running them should be a separate approved implementation step.

## Verification Run

Date: 2026-06-25

Checks completed:

- Public file list reviewed.
- ASCII-only scan passed.
- Search for local paths, private Notion links, user IDs, personal owner names, and private metadata passed.
- YAML parse passed for `project/config/model-routing.yaml`.

## Provider Check

Date: 2026-06-25

- Ollama service started.
- `ollama list` found Qwythos.
- Qwythos metadata is readable.
- Qwythos load failed during smoke test.
- `gemma4:e4b` fallback smoke test succeeded.
- `.env.local` created and ignored by Git.

## GitHub Publication Status

Date: 2026-06-25

- Local HTTPS push failed because the Codex shell did not have GitHub HTTPS credentials.
- Git SSH transport succeeded and is now the configured `origin`.
- Published commit: `b73137e`.
