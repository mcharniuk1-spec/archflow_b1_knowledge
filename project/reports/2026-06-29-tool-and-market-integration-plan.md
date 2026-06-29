# Tool And Market Integration Plan

Date: 2026-06-29
Status: accepted as planning update; gated tools not activated

## Summary

The June 29 reports strengthen the current E1-E7 plan instead of replacing it. E1 still proves the internal KB/PRD workflow. E2 becomes a market evidence engine. E3-E4 convert approved evidence into positioning and content. E5 measures funnel and ROI quality. E6-E7 test real demand through conversations and payment or firm paid intent.

## Tool Decisions

| Tool | Decision | Gate |
|---|---|---|
| Loop Engineering | Adopt now as operating discipline. | L1 report-only, state schema, attempt caps, maker/checker split. |
| Cognee | Defer to sandbox after E1.3 readback. | Approved artifacts only; compare recall against WikiLLM. |
| turbovec | Defer to vector pilot after metadata exists. | Stable source IDs, embeddings, 20-query benchmark, ignored local index. |
| Mistral | Optional future quality pass. | Credentials, sanitized inputs, budget cap, model metadata logging, AF Review. |
| Ollama/Qwythos | Continue as local minor/background model path. | Server running and bounded prompts; `gemma4:e4b` fallback. |

## Market Decisions

FACT: First ICP hypothesis is product/software/AI service agencies and adjacent service firms.

INTERPRETATION: The first sellable pain is not "make a PRD"; it is reducing ambiguity, PM/BA cleanup, rework, scope creep, weak handoffs, and lost decision memory.

HYPOTHESIS: The first entry offer should be a Client Discovery-to-Backlog Pack.

GAP: No external buyer demand is validated yet.

## E2 Research Engine

Use `project/workflows/market-research-engine.yaml`.

Execution stages:

1. Hypothesis and exclusions.
2. Account universe.
3. Parallel public signal extraction.
4. Pain scoring.
5. Live role verification.
6. Message synthesis.
7. Fact-check gate.
8. Learning loop.

Parallel branches are allowed only for extraction work. Synthesis, review, memory promotion, external writes, and outreach remain sequential.

## Demand Rule

Validated demand means paid diagnostic, prepayment, approved paid start, or firm paid intent with source packet, timeline, scope, and budget-owner path. Attention signals are not demand.
