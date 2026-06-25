# Dashboard Setup And Operation Report

Date: 2026-06-25
Scope: E2.2 dashboard planning and local operator visibility for the ArchFlow Block 1 system.

## Summary

The project now has a Phase 2 local dashboard under `project/dashboard/`. It is intentionally read-only. It monitors the public project state, WikiLLM memory, configured LangGraph nodes, CrewAI agent roles, LlamaIndex corpus boundaries, LangSmith readiness, and local env/package status.

The dashboard is not the knowledge base and not the workflow runner. WikiLLM remains the durable curated memory. Codex remains the primary operator. LangSmith remains the trace and observability surface. LangGraph, CrewAI, and LlamaIndex are still configured as contracts, but their runtime packages are not yet installed in the public project runtime.

## Current Local Status

- LangGraph: configured as the workflow spine in `project/workflows/langgraph-controller.yaml`.
- CrewAI: configured as the role/task crew in `project/workflows/crewai-crew.yaml`.
- LlamaIndex: configured as the bounded retrieval layer in `project/workflows/llamaindex-rag.yaml`.
- LangSmith: configured for sanitized tracing; SDK is installed in the ignored local runtime.
- Streamlit/FastAPI: not installed; the current dashboard is static HTML/CSS/JS generated from repo files.
- Graphify: not generated yet; it should be created after runtime code exists.
- LlamaIndex vector index: not generated yet; the dashboard query is only a lexical test over approved public files.

## Dashboard Plan

Phase 1: no custom dashboard. Use Codex for operation, GitHub for files, LangSmith for traces, Obsidian for human knowledge, and WikiLLM files for durable memory.

Phase 2: local dashboard. Build a simple read-only dashboard with tabs for overview, WikiLLM memory, Graphify map links, LangGraph runs, LlamaIndex query test, CrewAI task outputs, LangSmith trace links, and env/config status.

Phase 3: full dashboard. Build a control panel only after one full proof workflow works. It should not become the primary brain. It should expose workflow inputs, approvals, trace links, run history, and config status after the system has real repeated run data.

## How To Operate

1. Regenerate dashboard data after changing workflow, wiki, report, or run files:

```bash
python3 project/scripts/generate-dashboard-data.py
```

2. Start the local server from the repository root:

```bash
python3 -m http.server 8765
```

3. Open:

```text
http://127.0.0.1:8765/project/dashboard/
```

4. Use the tabs:

- Overview: status cards, current workflow spine, phase decision, and recent activity.
- WikiLLM Memory: durable memory files, decisions, issues, and run notes.
- Graphify: current graph availability and links once generated.
- LangGraph Runs: configured nodes, owners, routing, revision loops, approval and block logic.
- LlamaIndex Query: lexical query test over approved public files.
- CrewAI Outputs: AF agent roles, goals, skills, and expected outputs.
- LangSmith: trace readiness, SDK status, source links, and safe trace rules.
- Env Config: ignored env presence, public examples, runtime package status, and RAG index status.

## How To Change Configuration

- Change workflow control in `project/workflows/langgraph-controller.yaml`.
- Change crew roles and expected outputs in `project/workflows/crewai-crew.yaml`.
- Change retrieval boundaries and indexing parameters in `project/workflows/llamaindex-rag.yaml`.
- Change model routing in `project/config/model-routing.yaml`.
- Change agent roster metadata in `project/agents/agent-roster.yaml`.
- Change dashboard rendering in `project/dashboard/app.js`.
- Change dashboard styling in `project/dashboard/styles.css`.
- Regenerate `project/dashboard/data.json` after any config or memory change.

## LangGraph Operating Model

LangGraph should be the workflow spine:

- state schema
- node routing
- revision loops
- review gates
- stop, approve, revise, and block logic

LangSmith should trace LangGraph runs. LangGraph should not own durable knowledge. It should call LlamaIndex for retrieval and write accepted outputs back to WikiLLM.

Current nodes:

- `intake_validate`
- `retrieve_context`
- `write_context_digest`
- `run_crew_prd`
- `write_kb_update`
- `review_gate`
- `publish_or_revise`

## CrewAI Operating Model

CrewAI should define who does what:

- AF Tools: source, tooling, and boundary analysis.
- AF Context: context digest and fact/interpretation/hypothesis/gap split.
- AF Manager: PRD, task matrix, milestones, and acceptance criteria.
- AF Knowledge: KB update and memory candidates.
- AF Review: public-safety, evidence, and claim review.
- AF Publisher: Git-ready release preparation.

CrewAI differs from LangGraph because CrewAI organizes agent responsibilities, while LangGraph controls when the workflow advances, loops, stops, or waits for approval. The recommended setup is LangGraph wrapping CrewAI.

## LlamaIndex Operating Model

LlamaIndex should be the runtime searchable index:

- ingest only approved public-safe docs
- chunk and embed approved text
- retrieve relevant context
- cite repo-relative source paths
- refuse private or unapproved sources

WikiLLM and LlamaIndex are not the same layer. WikiLLM says what the project knows after review. LlamaIndex helps agents find relevant text at runtime.

## Monitoring The Knowledge Base

Use WikiLLM as the canonical durable memory:

- `wiki/index.md` for read order and active layer map.
- `wiki/memory.md` for stable facts and current runtime decisions.
- `wiki/insights.md` for reusable design reasoning.
- `wiki/runs/` for execution records.
- `wiki/decisions/` for durable choices.
- `wiki/issues/` for unresolved or recently closed blockers.

The dashboard reads these files and shows recent activity, but it does not decide what is true. Substantial work should still write a run file, append `wiki/log.md`, and update memory/insights only when there is reusable future value.

## E2.2 Task Addition

Add subtask `E2.2.1 - Dashboard plan and local operator UI review` under E2.2. The subtask should cover:

- phased dashboard decision
- local dashboard implementation/review
- LangGraph/CrewAI/LlamaIndex status checks
- LangSmith trace-readiness check
- KB monitoring method
- next runtime proof actions

Acceptance criteria:

- local dashboard opens from a simple local server
- dashboard data regenerates from public project files
- workflow YAML parses
- package/env status is visible without exposing secrets
- report explains operation, configuration, monitoring, and remaining runtime gaps

## NeMo Position

NVIDIA NeMo Agent Toolkit is worth tracking as a later runtime shell because it can connect existing agent frameworks, tools, memory, observability, UI, MCP, and A2A patterns. Do not switch now. The project still needs one proof workflow with LangGraph, LlamaIndex, CrewAI, WikiLLM, and LangSmith before adding another framework layer.

## Source Notes

- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- LangSmith Studio: https://docs.langchain.com/langsmith/studio
- LangSmith observability: https://docs.langchain.com/langsmith/observability
- CrewAI crews: https://docs.crewai.com/en/concepts/crews
- LlamaIndex concepts: https://developers.llamaindex.ai/python/framework/getting_started/concepts/
- Ollama API: https://docs.ollama.com/api/introduction
- NVIDIA NeMo Agent Toolkit: https://docs.nvidia.com/nemo/agent-toolkit/latest/index.html

## Remaining Actions

1. Install LangGraph in the ignored project runtime.
2. Implement one minimal LangGraph proof run using the existing YAML contract.
3. Add bounded LlamaIndex indexing over the approved public corpus.
4. Add CrewAI execution inside the LangGraph `run_crew_prd` node.
5. Save every proof run back to `wiki/runs/` and `project/runs/`.
6. Generate Graphify after runtime code exists.
7. Upgrade the dashboard from readiness monitor to control panel only after proof data exists.
