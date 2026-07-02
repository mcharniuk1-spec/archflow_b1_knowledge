# Model Efficiency Advice

Purpose: reusable advice for ArchFlow agents choosing models, spending tokens, and deciding when to escalate from cheap execution models to frontier review.

## Standing Advice

1. Use Codex and deterministic scripts before model calls when the task is file inspection, schema validation, YAML parsing, public-safety scanning, or simple formatting.
2. Treat OpenRouter as disabled unless an approved backend or local bridge exists.
3. Use cheap execution models first for extraction, classification, drafting, source discovery, and code variants.
4. Use the Claude, Gemini, and OpenAI frontier council only when the result affects strategy, architecture, public claims, memory promotion, outreach, pricing, or payment verdicts.
5. Never let an execution-pool model self-approve its own output.
6. Log model ID, task, role, source IDs, prompt version, estimated input tokens, estimated output tokens, estimated cost, reviewer, and human gate status.
7. If token or cost data is missing, report it as missing. Do not estimate after the fact unless the source log supports it.
8. For bulk E2 research, audit a sample with a frontier reviewer instead of reviewing every low-value item.
9. For E7 payment verdicts, do not optimize for cheapness; use strong review because a wrong verdict costs more than model tokens.
10. If OpenRouter model IDs or pricing are stale, stop and refresh the provider model list before recommending activation.
11. When no runtime evidence exists, say "No active OpenRouter runtime evidence found" and list the evidence files inspected.
12. If provider context/window behavior changes, log `context_window_tokens`, `prompt_tokens`, and `actual_output_tokens` to separate runtime-configuration overhead from quality effects.
13. Keep local deterministic proof ledgers separate from provider-backed ledgers; do not use a zero-cost local proof to imply OpenRouter activation.

## Efficiency Scoring

Use this simple score in reports:

- `5`: cheap model or deterministic check solved the task with clear evidence and no escalation needed.
- `4`: cheap model solved most of the task and a small review pass was justified.
- `3`: model choice was acceptable but logging, prompt scope, or review threshold needs improvement.
- `2`: frontier model was used where a cheaper model or script should have been used.
- `1`: model output affected claims, memory, outreach, architecture, or payment without adequate review.

## Report Advice

Every observer report should include:

- actual models used
- what each model was used for
- evidence source
- token and cost fields if recorded
- efficiency score
- overuse or under-review risks
- cheaper substitute if appropriate
- escalation recommendation if quality or risk requires it
- missing logging fields
- next action
