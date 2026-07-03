# Yushchenko Model Efficiency Report

Observer: Yushchenko Model Efficiency Observer

Run window: 2026-07-02 18:45 EEST

## Evidence Inspected

- `public/project/config/model-routing.yaml`
- `public/project/reports/2026-07-01-openrouter-model-routing-plan.md`
- `public/project/runs/yushchenko-model-efficiency/2026-07-02-1402-model-efficiency-report.md`
- `public/services/jarvis-api/app.py`
- `public/services/jarvis-api/README.md`
- `public/project/provider-setup.md`

## FACT

- OpenRouter remains disabled in runtime (`MODEL_PROVIDER` defaults to `none`), so no live provider inference has occurred yet.
- The frontier contract now uses OpenRouter latest aliases for auto-refresh (`~openai/gpt-latest`, `~anthropic/claude-opus-latest`) with explicit fallback pins and a dedicated qualifier path (`~anthropic/claude-fable-latest`).
- The most recent frontier council and task routing now explicitly pairs GPT-5.5-equivalent tiers with latest-Opus/Fable where task criticality justifies frontier spend, while preserving hard cost gates (`max_per_run_usd=1.99`, `daily_budget_usd=5.00`).
- A technical qualifier slot (`fable`) was added for highly specific tasks with approval gates.
- No `provider_id`/`model_list`/`pricing` evidence from live OpenRouter calls is yet available in workspace logs.

## Model Priority Update

### By Task

- `E1_kb_prd_workflow`: `~openai/gpt-latest` (currently GPT-5.5) first, then `~anthropic/claude-opus-latest`, then `gemini` for plan/review split.
- `E2_research_engine`: `~openai/gpt-latest` (currently GPT-5.5) first, then `~anthropic/claude-opus-latest`, then `gemini`.
- `E3_website_positioning`: `~anthropic/claude-opus-latest` + `~openai/gpt-latest` + `gemini`.
- `E4_content`: `~anthropic/claude-opus-latest` and `~openai/gpt-latest`.
- `E5_roi_analytics`: `~openai/gpt-latest` + `gemini` + `~anthropic/claude-opus-latest`, with `~anthropic/claude-fable-latest` gate for contested technical assumptions.
- `E6_outreach`: `~anthropic/claude-opus-latest` + `~openai/gpt-latest`.
- `E7_payment_verdict`: `~openai/gpt-latest` + `~anthropic/claude-opus-latest` + `gemini`, with `~anthropic/claude-fable-latest` gate when assumptions are technical and disputed.

### By Land-Graph Role

- `yushchenko`: frontier-efficiency and budget gate owner; now linked to task `query_shape` / `graph_node_path` fields.
- `security`: technical qualification path on technical/regulated queries.
- `jesus` and `ronaldinho`: architecture and public-facing governance review for frontier paths.

## Efficiency Assessment

Score: `4` (as currently configured, stable and controlled, but not yet measurable on live OpenRouter runtime).

Why:

- Strong governance posture and explicit role-gated routing are now in place.
- Frontier usage reduced to at most two frontier calls per strategy run (`one_to_two_calls_per_family`) to avoid overuse.
- Fable is correctly constrained to qualification-only usage and is blocked from routine execution.
- Without live runs, measured token/cost efficiency remains unavailable; only policy-level efficiency is improved.

## Required Next Step Before Live OpenRouter Activation

1. Validate resolved aliases (`~openai/gpt-latest`, `~anthropic/claude-opus-latest`, `~anthropic/claude-fable-latest`) against live `/api/v1/models` metadata before first call, then lock pricing snapshots in `runs/*/model-call-ledger.jsonl`.
2. Add one short benchmark packet per task family after activation and capture:
   - `query_shape`
   - `graph_node_path`
   - `model_id`
   - prompt/output tokens
   - latency
   - actual cost
   - pricing source
3. Keep `fable_gate` and Fable calls behind approval + overrun controls to prevent unnecessary spend.
