# Run: E1.4 KB Update Principle

Date: 2026-07-03
Project: archflow-b1-knowledge
Owner agent: Claude (Cowork)
Support agents/tools: local deterministic scripts only; no provider calls.

## Task

Define the principle for building and updating the knowledge base (E1.4).

## Inputs

- `project/operating-rules.md`
- `project/workflows/knowledge-integration.yaml`
- `wiki/memory.md`, `wiki/insights.md`
- `project/runs/2026-07-03-claude-continuation-stabilization/` packet

## Outputs

- `project/reports/2026-07-03-kb-update-principle.md`
- `project/runs/2026-07-03-kb-update-principle/agent-handout.md`

## Key Content

FACT: The report defines WikiLLM as the only durable memory, LlamaIndex as retrieval only, Graphify as generated reference, and all external surfaces (dashboard packets, Notion, Obsidian/Nexus, Telegram) as non-memory until agent review promotes content into WikiLLM with provenance.

INTERPRETATION: This closes the E1.3-to-E1.4 gap: the KB now has an explicit promotion test, per-file writing table, and traceback procedure, so a new agent can update memory correctly without chat history.

FACT: Owner acceptance was recorded on 2026-07-03. GAP: Venv-dependent validators may be environment-blocked in the Cowork sandbox; see the live log closeout entry for exact check status.

## Status

Complete and accepted by owner on 2026-07-03.

## Next Steps

- Apply the accepted E1.4 principle to E2.1 source-list planning and future evidence-card promotion.
