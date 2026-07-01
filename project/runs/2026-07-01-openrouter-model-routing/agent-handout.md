# Agent Handout: OpenRouter Model Routing

## Title And Purpose

This handout records the OpenRouter model-routing architecture for future ArchFlow agents.

## Human Summary

ArchFlow now has a durable model-routing plan for future OpenRouter use. The plan keeps OpenRouter disabled today and treats cloud execution as approval-gated, server-side work only.

The new architecture uses the strongest Claude, Gemini, and OpenAI models as a frontier council for planning, long reasoning, strategy, architecture, public-claim review, and payment verdicts. Cheaper models such as Kimi, Qwen, Mistral, DeepSeek, GLM, Llama, Perplexity, MiniMax, Mercury, Grok, and Gemma are assigned to bounded execution work that must be checked before publication or memory promotion.

## Current State

Status: complete after validation.

Main artifacts:

- `project/config/model-routing.yaml`
- `project/reports/2026-07-01-openrouter-model-routing-plan.md`
- `wiki/runs/2026-07-01-openrouter-model-routing.md`
- `wiki/memory.md`
- `wiki/insights.md`
- `wiki/log.md`

OpenRouter runtime state: disabled.

## Agent Continuation Prompt

```text
You are continuing ArchFlow model-routing work. Read project/config/model-routing.yaml and project/reports/2026-07-01-openrouter-model-routing-plan.md first. Treat OpenRouter as disabled unless the owner explicitly approves activation and a local bridge or backend exists. Before any runtime wiring, refresh the OpenRouter model list, verify exact model IDs and pricing, keep secrets out of public files and frontend code, and enforce budget, logging, public-safety, and human-approval gates. Do not let execution-pool models self-approve public claims, memory writes, outreach, architecture, pricing, or payment verdicts.
```

## Execution Trace

FACT: The live communication log was read and updated before edits.

FACT: An independent reviewer subagent produced a reviewer prompt/checklist covering provider boundaries, cost discipline, maker/checker separation, E1-E7 fit, public safety, unsupported model-name risk, frontier-model overuse, budget controls, and reliability controls.

FACT: The model-routing YAML now includes activation gates, frontier council routing, execution pool roles, E1-E7 task routing, budget controls, reliability controls, quality gates, and required logging fields.

INTERPRETATION: The safest architecture is not one best model. It is a tiered system where expensive models are reserved for expensive decisions and cheaper models perform bounded work.

GAP: The exact OpenRouter model IDs and prices must be rechecked at activation time.

## Decisions

- Keep Codex as operator and approval boundary.
- Keep OpenRouter disabled until explicit approval and a server-side bridge/backend exists.
- Use Claude, Gemini, and OpenAI together for material strategy and review.
- Use cheaper execution models first for bulk extraction, drafting, classification, code variants, and source discovery.
- Require human approval before provider activation, external writes, memory promotion, outreach, publication, or payment verdicts.

## Validation

- Pass: `ruby -e "require 'yaml'; YAML.load_file('public/project/config/model-routing.yaml'); puts 'model-routing yaml ok'"`
- Pass after owner-name false-positive cleanup: `python3 public/scripts/public_safety_scan.py`
- Pending at handout creation: final communication log completion.

## Next Actions

1. If model runtime is approved later, design the local bridge/backend before any API call.
2. Refresh OpenRouter `/api/v1/models`.
3. Convert the YAML task routing into LangGraph route nodes only after approval.
4. Add deterministic schema validators for model outputs before using execution-pool models at scale.

## Safety Boundary

Do not store API keys, private source text, private URLs, local absolute paths, account IDs, screenshots, raw transcripts, provider secrets, or frontend-callable model credentials in public files.
