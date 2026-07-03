# Agent Handout: Hybrid RAG And Jarvis Readiness

Date: 2026-07-03
Status: implementation complete for bounded hybrid retrieval and Jarvis readiness verification
Lane: LlamaIndex RAG upgrade plus Jarvis architecture-mode readiness

## Title And Purpose

This handout records the widened plan and implementation pass for the ArchFlow public knowledge system. It is for the next operator who must continue Graphify, RAG, LlamaIndex, Jarvis, dashboard, Notion, GitHub, and future tool-integration work without relying on chat history.

## Human Summary

The current reliable architecture remains public-safe first. Codex is the local operator and approval boundary. WikiLLM is the durable curated memory. Graphify is generated structural reference. LlamaIndex is the bounded retrieval layer. LangGraph controls execution paths and gates. CrewAI provides named role structure. Jarvis is the dashboard communication/control surface, with Architecture 1 for PRD/ICP output and Architecture 2 for architecture/agent-system work.

This run upgraded the LlamaIndex approved-corpus path from keyword-only proof to bounded hybrid retrieval. The script now creates stable document and chunk metadata, enforces repo-relative `source_path`, records provenance fields, keeps deterministic lexical scoring, and attempts a local vector path through the configured embedding model when the local embedder is available. In this environment the local embedder endpoint was not reachable, so the run correctly used `hybrid_fallback_lexical` and reported the fallback reason. The 20-query benchmark passed with no regression against lexical retrieval and source-path filtering passed.

Jarvis was verified through the local FastAPI health endpoint and hosted Vercel provider-disabled API endpoints. Architecture 1 PRD/ICP and Architecture 2 agent-orchestra routes both returned review packets. This proves dashboard-to-Jarvis connection and mode routing for the review-packet contract. It does not prove provider-backed automation, Railway uptime, raw voice storage, autonomous writeback, or full production execution.

The widened plan now treats external GitHub repos and tool ideas as a sequenced integration backlog, not an uncontrolled ingestion target. Graphics, Second Brain/Obsidian, audio transcription, voice, turbovec, Charlie-like OS ideas, and other knowledge-base tools should enter through approved summaries, source registries, Graphify/RAG maps, and task records only after scope and safety gates are clear. If a tool is useful but not immediately relevant, create a future task or Notion update candidate instead of forcing it into runtime.

## Current State

FACT:
- Live communication showed a prior Vercel dashboard/Jarvis connection run completed today.
- Local Jarvis `/health` now returns `status=ok`, OpenRouter selected in status, `provider_calls=0`, and writeback disabled.
- Hosted Vercel `/health` returns `status=ok`, `hosting=vercel_serverless`, OpenRouter selected in status, `provider_calls=0`, and writeback disabled.
- Hosted Architecture 1 `/api/lanes/prd-icp` returns `review_packet_created`.
- Hosted Architecture 2 `/api/lanes/agent-orchestra` returns `review_packet_created`.
- The dashboard already exposes visible `1` and `2` architecture selectors in the Jarvis surface, and the topbar exposes connected/disconnected Jarvis API state.
- E1.2 Codex proof was rerun locally through the deterministic LangGraph proof script: 11 stream events, approved final state, sanitized source boundary.
- LlamaIndex benchmark passed: 20 fixed public queries, lexical recall@5 20/20, hybrid recall@5 20/20, source-path filtering pass, no hybrid regression.

INTERPRETATION:
- Jarvis is connected for local and hosted review-packet operation.
- The knowledge system is ready for bounded retrieval-backed execution planning, but not for broad autonomous ingestion or provider-backed long jobs.
- LlamaIndex can now be called a bounded hybrid retriever because the contract, script, metadata, and benchmark path exist; vector execution is still conditional on a reachable local embedder.

HYPOTHESIS:
- The next reliability gain comes from a small Railway or equivalent always-on backend only after auth, CORS, queues, worker scope, provider secrets, and writeback policy are approved.
- Turbovec becomes useful after stable chunk IDs, embedding dimensions, source filters, benchmark repeatability, and local persistence are proven.
- NVIDIA RAG/NeMo skills may be useful later for guardrails, retriever evaluation, and RAG performance work, but they should not be activated before this repo has a clear deployment target and credentials policy.

GAP:
- Local vector embeddings did not run because the local embedder endpoint was unavailable.
- Full vector defaulting remains blocked until vector availability and the benchmark pass together.
- Provider-backed Jarvis execution, Railway uptime, durable writeback, live Nexus, raw audio storage, and autonomous dashboard-driven Notion/GitHub updates remain gated.
- Append-only Notion evidence updates were applied to E1.1.7, E1.3.9, and E1.7; no broad Notion rewrite or Done-state promotion was performed.

## Widened Architecture Plan

### P0 Coordination And Safety

- Read live communication before every public project edit.
- Claim files before editing and complete the log after checks.
- Keep all public files English-only and repo-relative.
- Do not store secrets, private URLs, account IDs, raw private source, screenshots, credentials, local absolute paths, or personal identifiers.
- Treat proof-backed no-op or fallback as valid when runtime gates are unavailable.

### P1 Source Boundary And Knowledge Routing

- Route every new source through one of four states:
  - approved public file;
  - sanitized summary;
  - private source for local reasoning only;
  - blocked source.
- Keep WikiLLM as durable human/agent memory.
- Keep LlamaIndex as retrieval, not memory storage.
- Keep Graphify as generated structural map, not final synthesis.
- Use Nexus only after live schema discovery and only for approved vault actions.

### P2 LlamaIndex Hybrid RAG

- Maintain approved corpus: `project/`, `history/`, `skills/`, and `wiki/`.
- Preserve excluded zones: ignored local runtime, raw exports, private sources, secrets, temp files, and dashboard runtime output.
- Keep metadata mandatory: `source_path`, `document_type`, `updated_at`, `doc_id`, and `chunk_id`.
- Use lexical retrieval as deterministic fallback and traceability path.
- Use semantic vector retrieval only when the configured local embedder is reachable.
- Merge semantic and lexical candidates by source path plus chunk ID, then rerank with normalized blended scores.
- Run the 20-query benchmark before promoting full vector defaulting.

### P3 Turbovec

- Treat turbovec as a future vector store under LlamaIndex, not an independent memory store.
- Required before pilot:
  - stable source ID, document ID, and chunk ID;
  - fixed embedding model and dimensions;
  - public/private allowlist filters;
  - ignored local persist directory;
  - benchmark pass with vector enabled;
  - rollback to lexical retrieval.

### P4 Graphify

- Use Graphify for structural reference over bounded repos/corpora only.
- Store generated graph output under the project reference or existing graph output folder.
- Query or explain the graph before broad structure reads when graph output exists.
- Write human conclusions into WikiLLM, decisions, issues, or run notes rather than copying generated graph dumps into prompts.

### P5 Jarvis And Dashboard

- Keep Jarvis turned on as the communication/control surface for this project.
- Architecture 1 button `1`: PRD/ICP service output path. It creates review packets for source-to-PRD, ICP, evidence, backlog, and approval gates.
- Architecture 2 button `2`: agent-control and system-architecture path. It creates review packets for workflow changes, knowledge-base work, Graphify/RAG/LlamaIndex implications, approvals, and handoffs.
- Header must show Jarvis API connected/disconnected state.
- Browser-local chat and packets are useful staging surfaces but not durable memory until Codex reviews and records them.
- Voice remains browser/local text path unless storage, privacy, provider, and backend policies are approved.

### P6 E1.2 And E1.3 Proof

- E1.2 Codex proof remains the reusable deterministic proof template.
- E1.2.8 local testmeeting artifacts and sanitized OpenRouter comparison remain Review-state evidence, not owner-accepted Done-state proof.
- E1.3 remains the knowledge-base readback gate.
- After any proof rerun, update the run note, WikiLLM log, dashboard data, and handout.
- Do not let provider output override local proof without AF Review and owner acceptance.

### P7 External Tool And GitHub Repo Backlog

- Graphics/design repositories: route through design/source summaries and Graphify maps before implementation.
- Second Brain/Obsidian repositories: route through vault indexes, WikiLLM project memory, and Nexus schema discovery before live writes.
- Knowledge-base tooling repositories: classify as retrieval, memory, graph, connector, evaluation, or UI layer before adoption.
- Audio transcription and voice repositories: require privacy, storage, redaction, model/provider, and raw-media retention policy first.
- Charlie-like OS or broad operating-system ideas: keep as research architecture backlog unless a specific workflow, boundary, and proof fixture exist.
- Turbovec and other vector-store repos: evaluate only after current LlamaIndex metadata and benchmark gates are stable.
- Irrelevant or premature items should become future task candidates rather than current runtime changes.

### P8 NVIDIA Skill Spectrum Finding

- Relevant future candidates found: NVIDIA RAG Blueprint, NeMo retriever, RAG eval/perf skills, Nemotron retrieval recipes, and Nemotron speech.
- Not activated now: GPU/NIM deployment, hosted NVIDIA endpoints, NeMo Guardrails, RAGAS evaluation, speech runtime, cuDF, cuOpt, CUDA-Q, and GPU host setup.
- Reason: the current repo needs bounded LlamaIndex reliability, source filters, and benchmark evidence before GPU/provider/NIM deployment.
- Future gate: create a separate evaluation task if NVIDIA RAG/NeMo tools become necessary for guardrails, retrieval eval, reranking, speech, or production-scale retrieval.

### P9 Notion, Git, And Transfer

- Notion update was append-only and evidence-backed:
  - RAG contract upgraded to bounded hybrid with lexical fallback.
  - Benchmark passed locally with vector unavailable and explicit fallback.
  - Jarvis local and hosted review-packet routes passed for Architecture 1 and Architecture 2.
  - Railway/provider/writeback/voice remain gated.
- Git path:
  - stay on `main`;
  - review dirty diff;
  - run public safety, workflow validation, runtime guard, dashboard checks, and diff check;
  - commit only scoped files;
  - push main only after checks pass and the owner-approved push path is available.
- Transfer package:
  - this handout;
  - WikiLLM run note;
  - live communication completion entry;
  - updated dashboard data;
  - local benchmark report in ignored runtime path.

## Files Changed Or Expected

- `project/scripts/llamaindex-approved-corpus.py`
- `project/scripts/llamaindex-rag-benchmark.py`
- `project/workflows/llamaindex-rag.yaml`
- `project/workflows/knowledge-integration.yaml`
- `project/agentic-stack.md`
- `project/README.md`
- `project/scripts/generate-dashboard-data.py`
- `project/dashboard/app.js`
- `project/runs/E1.2/2026-06-26-full-test/e1_2_langgraph_output.json`
- `project/runs/E1.2/2026-06-26-full-test/e1_2_stream_events.jsonl`
- `project/runs/2026-07-03-hybrid-rag-jarvis-readiness/agent-handout.md`
- `wiki/runs/2026-07-03-hybrid-rag-jarvis-readiness.md`
- `wiki/log.md`
- `wiki/memory.md`
- `project/dashboard/data.json`
- `project/live/communication/agent-communication-log.md`

## Validation

Passed:

- `project/local/venv/bin/python project/scripts/llamaindex-approved-corpus.py`
- `project/local/venv/bin/python project/scripts/llamaindex-approved-corpus.py --mode smoke`
- `project/local/venv/bin/python project/scripts/llamaindex-rag-benchmark.py`
- local Jarvis `/health`
- hosted Jarvis `/health`
- hosted Architecture 1 PRD/ICP lane
- hosted Architecture 2 agent-orchestra lane
- append-only Notion updates to E1.1.7, E1.3.9, and E1.7
- `project/local/venv/bin/python project/scripts/e1_2_full_test.py`
- `python3 -m py_compile project/scripts/llamaindex-approved-corpus.py project/scripts/llamaindex-rag-benchmark.py project/scripts/generate-dashboard-data.py`
- `node --check project/dashboard/app.js`

Still required before final push:

- regenerate dashboard data;
- parse dashboard JSON;
- workflow validation;
- pre-push runtime guard;
- public safety scan;
- `git diff --check`;
- final live communication completion entry.

## Agent Continuation Prompt

Continue the ArchFlow public hybrid RAG and Jarvis readiness lane from this handout. First read `project/operating-rules.md`, the live communication files, `project/workflows/llamaindex-rag.yaml`, `project/scripts/llamaindex-approved-corpus.py`, `project/scripts/llamaindex-rag-benchmark.py`, `project/agentic-stack.md`, `project/dashboard/app.js`, and `wiki/log.md`.

Goal: finish validation, regenerate dashboard data, update WikiLLM log/memory, optionally perform append-only Notion sync through an approved connector, commit and push main if checks pass, and leave the next Railway/provider/writeback lane clearly gated.

Constraints: do not ingest private files; do not start provider-backed Jarvis; do not deploy Railway; do not write to Notion/GitHub/Telegram unless the approved path is available; do not store secrets, private URLs, local paths, raw transcripts, screenshots, or account IDs.

Stop condition: stop before full vector defaulting, provider calls, live writeback, production promotion, raw voice storage, or broad external repo ingestion unless a separate approved task explicitly opens that gate.

## Safety Boundary

This run stores only public-safe architecture, retrieval, benchmark, and readiness facts. It does not store raw private prompt text, raw transcripts, private source documents, credentials, local absolute paths, private URLs, account IDs, screenshots, or provider secrets.
