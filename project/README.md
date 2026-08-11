# ArchFlow Public Tool

This directory contains the generic, public-safe operating contracts behind the ArchFlow Knowledge Operator. It is designed to be cloned by an individual or a small team and adapted to their own approved sources. It does not reconstruct the creator's workspace, project history, personal memory, deployment metadata, or credentials.

## Product mission

ArchFlow turns one bounded objective and exact source boundary into an inspectable path from research to definition, action, independent review, result readback, and maintained knowledge.

The system is useful when teams need to answer more than “what did the model say?” It makes the following chain explicit:

```text
objective and decision
  -> allowed evidence and gaps
  -> functional owner and portable skills
  -> typed state and stop conditions
  -> candidate plus deterministic checks
  -> independent verdict
  -> optional approved action and readback
  -> reviewed solution or action memory
```

## Public package map

| Path | Purpose |
|---|---|
| `dashboard/` | Responsive documentation, project, role/skill, setup, evidence, schema, and Communication Center UI |
| `agents/` | Canonical functional role roster, smallest-responsible role packs, and skill bindings |
| `assets/architecture/` | Four editable visual schemas and raster previews |
| `benchmarks/` | Fixed synthetic fixtures, raw denominators, results, and limitations |
| `config/` | Provider states and public environment-name contracts; never credential values |
| `context/` | Compact stable context and exact source-boundary rules |
| `database/` | Run, event, review, receipt, role, skill, solution-memory, and action-memory schemas |
| `goals/` and `loops/` | Observable objective, retry, budget, stop, and recovery contracts |
| `scripts/` | Generation, validation, retrieval, auth, benchmark, and browser checks |
| `system/` | Provider-disabled reference fixtures and canonical operating-model validation |
| `workflows/` | LangGraph, CrewAI, LlamaIndex, and knowledge-integration contracts |

Historical run archives, live coordination logs, private notes, deployment receipts, raw captures, and local graph indexes are deliberately not product data. A clean checkout may include empty templates for future local runs, but no prior operator history is required to use the tool.

The canonical V3 projection resolves 21 functional roles, four smallest-responsible role packs, and ten portable skill packages. These are reusable contracts, not stored identities or continuously running workers.

## Runtime responsibilities

- **LangGraph contract:** owns typed state, routing, reducers, interrupts, retry caps, and terminal states.
- **Functional roles:** own bounded outputs. The roster is configuration; it is not a claim that 21 agents are continuously running.
- **Portable skills:** provide reusable procedures and safety boundaries. A skill never grants a key, target, or authority by itself.
- **LlamaIndex contract:** retrieves only manifest-approved documents, returns source paths, and falls back to deterministic lexical search.
- **CrewAI contract:** may materialize a reviewed subset of role and task contracts; it is not the canonical state owner.
- **Knowledge Operator and Jarvis:** prepare and display browser-local packets. They do not silently execute providers or external actions.

## First verified path

```bash
python3 scripts/generate-dashboard-data.py
python3 scripts/validate-dashboard-data.py
python3 scripts/benchmark-actionable-agents.py
python3 scripts/browser-v3-smoke.py
python3 -m http.server 8765 --directory ..
```

From the repository root, the equivalent commands use the `project/` prefix and the dashboard opens at `http://127.0.0.1:8765/project/dashboard/`.

## Safety and authority

The zero-key public core makes provider calls and external writes zero by construction. Optional authentication, provider adapters, observability, Git, deployment, publication, and writeback are separate server-side or operator-controlled extensions. Each needs its own environment configuration, negative test, exact target, approval, rollback, replay protection, and readback.

Do not add personal identifiers, customer material, raw transcripts, private URLs, local absolute paths, credential values, or old project history to the corpus manifest. Promote only reviewed reusable meaning with source lineage, owner, freshness, and supersession.

Start with the root [README](../README.md), [quickstart](../docs/quickstart.md), and [dashboard manual](../docs/dashboard-operating-manual.md).
