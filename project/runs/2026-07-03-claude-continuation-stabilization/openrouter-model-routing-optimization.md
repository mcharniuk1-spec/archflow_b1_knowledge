# OpenRouter Model Routing Optimization - 2026-07-03

Status: planning and routing recommendation only. Provider runtime remains disabled.

Source checked: `https://openrouter.ai/api/v1/models` on 2026-07-03.

## Current Rule

FACT:
- Browser JavaScript must not receive provider keys.
- OpenRouter provider calls are disabled by default.
- Existing budget rule is 5.00 USD daily cap and 1.99 USD per-run hard stop.
- Hosted Jarvis API returns review packets with provider calls 0.

INTERPRETATION:
- OpenRouter should be a server-side or local-bridge execution option only after owner approval, source screening, model-list refresh, ledger, and budget guard.

## Recommended Routing

### Default

Use `MODEL_PROVIDER=none`.

Use Codex for operator work, Git edits, public-safety review, and final promotion.

### Cheap Structured Execution

Use only after provider approval and for sanitized packets:

- `qwen/qwen3.6-plus`: strong cost/context tradeoff for source-scope comparison, PRD/ICP synthesis, and long packet review.
- `openai/gpt-5.4-mini`: structured reasoning and schema repair when a cheaper OpenAI-family model is enough.
- `poolside/laguna-xs-2.1`: very cheap coding-agent candidate for bounded code review or patch suggestions; must be maker/checker-gated.

### Long-Context And Agentic Planning

Use only for material planning or complex architecture review:

- `anthropic/claude-sonnet-5`: high-stakes coding, agent, and professional review.
- `google/gemini-3.1-pro-preview`: long-context multimodal review and alternative synthesis.
- `z-ai/glm-5.2`: 1M-context project-level software-engineering and broad code/UI planning candidate.

### High-Stakes Final Review

Use only when a decision affects strategy, public claims, provider activation, payment test, or production promotion:

- `openai/gpt-5.5`
- `anthropic/claude-fable-5` or `~anthropic/claude-fable-latest`
- `anthropic/claude-sonnet-5`

Run at most one frontier final review unless there is a clear contradiction or owner asks for a council.

### Coding And Implementation Suggestions

Use only after source packet is sanitized:

- `moonshotai/kimi-k2.7-code`
- `z-ai/glm-5.2`
- `poolside/laguna-xs-2.1`
- `anthropic/claude-sonnet-5` for high-risk code review only

## Mandatory Ledger

Every provider call must write a local reviewed ledger entry with:

- timestamp;
- lane;
- model ID;
- prompt version;
- source packet ID;
- input type;
- raw private source sent: true/false;
- estimated input/output tokens;
- estimated spend;
- actual provider calls count;
- budget remaining;
- reviewer verdict;
- durable-write permission: true/false.

## Stop Rules

Stop before provider call if:

- no owner approval;
- no fresh model-list check;
- no sanitized source packet;
- no public-safety screen;
- no budget cap;
- no ledger path;
- no reviewer assigned;
- task can be done by Codex/local deterministic script.

## Config Recommendation

Do not replace `project/config/model-routing.yaml` wholesale yet. It is a policy contract, not an active provider config. The next implementation pass should add a small `activation_snapshot` section only after a real approved provider activation lane begins.
