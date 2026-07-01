# 2026-07-01 OpenRouter Model Routing

## Task

Define a strategic and economical OpenRouter model-routing architecture for ArchFlow.

## Result

- Added `project/reports/2026-07-01-openrouter-model-routing-plan.md`.
- Replaced `project/config/model-routing.yaml` with a fuller routing contract.
- Kept OpenRouter runtime disabled until explicit approval and an approved local bridge or backend exists.
- Defined the frontier council: strongest available Claude, Gemini, and OpenAI models for planning, long reasoning, strategy, and review.
- Defined the execution pool: Kimi, Qwen, Mistral, DeepSeek, GLM, Llama, Perplexity, and selected optional models for bounded execution only.
- Added maker/checker rules, E1-E7 routing, budget controls, reliability controls, activation gates, and required logging fields.

## Review

An independent reviewer prompt/checklist was produced during the run and folded into the final report. The main correction was to avoid implying live provider availability and to mark model IDs as activation-time verified targets rather than permanent hard-coded truth.

## Follow-Up

Before any runtime work:

1. Get explicit approval for provider activation.
2. Build or approve a local bridge/backend.
3. Refresh OpenRouter `/api/v1/models`.
4. Store secrets only in ignored local env or provider secret storage.
5. Run model calls only on sanitized packets with budget and review logging.
