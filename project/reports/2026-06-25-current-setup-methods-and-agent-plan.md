# Current Setup Methods And Agent Plan

Date: 2026-06-25
Status: educational summary for the public ArchFlow Block 1 project

## 1. Executive Summary

ArchFlow is currently set up as a public-safe knowledge project for Block 1:

`dialogue/chat/meeting material -> structured context -> PRD -> responsibility plan -> agent-ready knowledge base`

The current setup separates four concerns:

| Concern | Current Tool | Purpose |
|---|---|---|
| Operator and approvals | Codex | Edits files, reviews safety, runs checks, publishes to GitHub. |
| Local model execution | Ollama with Qwythos | Runs local minor/background model work without cloud model keys. |
| Workflow control | LangGraph contract | Defines state, nodes, edges, gates, and revision loops. |
| Agent team structure | CrewAI contract | Defines roles, tasks, expected outputs, and accountability. |
| Retrieval/RAG | LlamaIndex contract | Defines approved corpus, indexing, retrieval, source paths, and private-source refusal. |
| Observability | LangSmith | Traces future workflow runs after API key insertion. |
| Durable memory | public WikiLLM | Stores project rules, memory, insights, decisions, runs, and issues. |

Important current boundary:

- Codex authentication is not exported as an API key.
- LangSmith is tracing only, not a model provider.
- Ollama is the only model execution provider for now.
- Cloud model APIs are not configured.
- Real API keys are stored only in ignored local env files.

## 2. Current Repository Method

The repository is public-safe by construction.

### Folder Method

| Folder | Meaning |
|---|---|
| `project/` | Active post-reset project work. |
| `history/` | Sanitized history summaries only. |
| `skills/` | Only used or set-up project skills, not the operator's whole private skill library. |
| `wiki/` | Public WikiLLM memory layer. |

### Public-Safety Method

The public project excludes:

- real API keys
- tokens
- cookies
- passwords
- private Notion URLs
- local absolute paths
- private workspace links
- raw transcripts
- raw exports
- local runtime logs
- vector indexes

The `.gitignore` blocks local env files and runtime folders. Current ignored local files include:

- `project/.env.local`
- `project/.env.langsmith.local`
- `project/local/`

### Publication Method

GitHub publication uses the working Git SSH remote.

Current remote:

`git@github.com:mcharniuk1-spec/archflow_b1_knowledge.git`

The HTTPS path previously failed because the shell had no HTTPS credentials. SSH is verified and configured.

## 3. Provider And Auth Method

Current provider mode:

```env
ARCHFLOW_PROVIDER_MODE=codex_auth_main
```

This means:

- Codex supervises and operates the project.
- Codex performs file edits, review, local checks, and Git publication.
- Codex auth is not passed into LangGraph, CrewAI, LlamaIndex, or LangSmith as a raw key.

Current Codex parameters:

```env
CODEX_OPERATOR_MODE=codex_app
CODEX_AUTH_EXPORTS_API_KEY=false
CODEX_GITHUB_PUBLICATION=codex_operated_git_ssh
```

## 4. Local Model Method: Ollama And Qwythos

Ollama is the local model server. It is used only for model execution, not project governance.

Current env:

```env
OLLAMA_BASE_URL=http://127.0.0.1:11434
OLLAMA_CHAT_MODEL=hf.co/empero-ai/Qwythos-9B-Claude-Mythos-5-1M-GGUF:Q4_K_M
OLLAMA_FALLBACK_CHAT_MODEL=gemma4:e4b
OLLAMA_EMBED_MODEL=nomic-embed-text
OLLAMA_TASK_SCOPE=minor_background_tasks
```

Current status:

- Ollama service is running locally.
- Qwythos is present in model inventory.
- Qwythos now loads and generates text.
- `gemma4:e4b` remains fallback.
- Qwythos can be verbose, so small bounded prompts and explicit stop/length controls should be used once runtime code exists.

Current allowed use:

- draft cleanup
- public text summarization
- local registry checks
- non-final background classification

Not allowed yet:

- final client output without Codex review
- raw private transcript processing without public-safety filtering
- cloud model calls

## 5. LangSmith Method

LangSmith is configured as observability only.

Current env:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
LANGSMITH_PROJECT=ArchFlow
LANGSMITH_PROJECT_ID=masked_langsmith_project_id
LANGSMITH_API_KEY=
LANGSMITH_RUN_TAGS=archflow,block1,ollama,qwythos,public-safe
LANGSMITH_TRACE_PUBLIC_SAFE_ONLY=true
```

Local key file:

`project/.env.langsmith.local`

Tracked public example:

`project/config/langsmith.env.example`

Current status:

- configured
- API key missing
- no live trace sent yet
- not a model provider

Operating rule:

LangSmith should receive only public-safe traces. Do not send raw private materials, local paths, private links, or secrets.

## 6. LangGraph Method

LangGraph is planned as the reasoning-path controller.

Current file:

`project/workflows/langgraph-controller.yaml`

Current status:

- configured as contract
- runtime package not installed
- no graph execution trace exists yet

LangGraph state fields:

- `run_id`
- `source_packet`
- `source_boundary_status`
- `retrieved_context`
- `context_digest_path`
- `prd_path`
- `task_matrix_path`
- `kb_update_path`
- `review_report_path`
- `langsmith_trace_id`
- `langsmith_trace_url`
- `approval_status`
- `gaps`

Current nodes:

| Node | Owner Agent | Purpose | Output |
|---|---|---|---|
| `intake_validate` | AF Tools | Validate source packet and safety boundary. | source boundary status |
| `retrieve_context` | AF Context | Use bounded LlamaIndex retrieval. | retrieved context |
| `write_context_digest` | AF Context | Separate facts, interpretations, hypotheses, and gaps. | context digest |
| `run_crew_prd` | AF Manager | Run PRD and responsibility planning. | PRD and responsibility matrix |
| `write_kb_update` | AF Knowledge | Convert accepted outputs into KB update. | KB update |
| `review_gate` | AF Review | Approve, revise, or block. | review report |
| `publish_or_revise` | AF Publisher | Publish or route for repair. | run summary |

Current graph logic:

1. Start at intake validation.
2. If source is safe, retrieve context.
3. If source is unsafe, go directly to review gate.
4. Write context digest.
5. Produce PRD and responsibility matrix.
6. Produce KB update.
7. Run review gate.
8. If approved, publish.
9. If revise, loop back to digest.
10. If blocked, stop.

Current graph parameters:

- checkpointer: none for now
- observability: LangSmith configured, awaiting API key
- max revision loops: 2
- human approval before publication: true
- model execution provider: Ollama only
- local model: Qwythos

## 7. CrewAI Method

CrewAI is planned as the team organizer.

Current file:

`project/workflows/crewai-crew.yaml`

Current status:

- configured as contract
- runtime package not installed
- Codex is active execution layer until installed

Current process:

```yaml
process: sequential
manager_mode: codex_operator_supervised
memory: false
cache: true
planning: false
output_log_file: project/outputs/crew-log.json
model_execution: ollama_local_qwythos
```

Current crew:

| Agent | Purpose | Main Outputs |
|---|---|---|
| AF Tools | Source and tooling analyst. | source inventory, readiness report, provider status |
| AF Context | Context analyst. | context digest, translated plan, gaps |
| AF Manager | PRD and execution manager. | PRD, responsibility matrix, milestone plan |
| AF Knowledge | KB maintainer. | KB update, memory candidates, public history summary |
| AF Review | Safety and evidence reviewer. | approval status, blocked items, required edits |
| AF Publisher | Public release operator. | git status, publication review, release notes |

Current task outputs:

- `project/outputs/templates/source-inventory.md`
- `project/outputs/templates/context-digest.md`
- `project/outputs/templates/prd.md`
- `project/outputs/templates/responsibility-matrix.md`
- `project/outputs/templates/knowledge-base-update.md`
- `project/outputs/templates/review-report.md`
- `project/runs/<date>-<run-name>.md`

## 8. LlamaIndex RAG Method

LlamaIndex is planned as the data and RAG layer.

Current file:

`project/workflows/llamaindex-rag.yaml`

Current status:

- configured as contract
- runtime package not installed
- no vector index generated

Approved corpus:

- `project/`
- `history/`
- `skills/`
- `wiki/`

Excluded corpus:

- `.git/`
- `project/.env.local`
- `project/local/`
- `raw/`
- `source_exports/`
- `secrets/`
- `private/`
- `tmp/`

Current RAG parameters:

```yaml
chunk_size: 800
chunk_overlap: 120
similarity_top_k: 5
response_mode: compact
require_source_paths: true
refuse_on_private_source: true
persist_dir: project/local/rag_index
```

RAG rule:

Every answer should be traceable to repo-relative source paths. Private sources are refused unless explicitly sanitized and approved.

## 9. WikiLLM Method

Public WikiLLM is installed inside this repository.

Current folder:

`wiki/`

Current files:

- `wiki/index.md`
- `wiki/memory.md`
- `wiki/insights.md`
- `wiki/log.md`
- `wiki/rules/public-wikillm-contract.md`
- `wiki/runs/`
- `wiki/decisions/`
- `wiki/issues/`

Purpose:

- durable public memory
- public-safe decisions
- run summaries
- reusable insights
- open issues
- project rules

Write rule for substantial work:

1. Create a run file in `wiki/runs/`.
2. Append `wiki/log.md`.
3. Add memory only for stable reusable facts.
4. Add insights only for reusable reasoning.
5. Add a decision when a durable choice is made.
6. Add an issue when a blocker remains.

## 10. Output Document Method

Current output templates:

- `source-inventory.md`
- `retrieval-log.md`
- `context-digest.md`
- `prd.md`
- `responsibility-matrix.md`
- `knowledge-base-update.md`
- `review-report.md`
- `run-summary.md`

No completed first proof-run document set exists yet.

The first proof run should use sanitized source material and produce a full output folder.

## 11. Agent Structure Options

### Option A: Current Codex-Supervised Contracts

Status: active now.

How it works:

- Codex reads the workflow contracts.
- Codex executes the steps manually or semi-manually.
- Ollama/Qwythos is used only for bounded local model tasks.
- LangSmith is prepared but not live until API key is added.

Best for:

- setup phase
- safety-sensitive changes
- public repository maintenance
- avoiding unnecessary package complexity

### Option B: Install LangGraph Runtime First

How it works:

- Add Python environment.
- Install `langgraph`.
- Convert `langgraph-controller.yaml` into executable graph code.
- Keep CrewAI and LlamaIndex as contracts at first.
- Add LangSmith tracing after API key insertion.

Best for:

- repeatable controlled runs
- visible state transitions
- review loops
- human approval gates

### Option C: Add LlamaIndex Before CrewAI

How it works:

- Install LlamaIndex and Ollama integrations.
- Build local index over approved corpus only.
- Persist index to ignored `project/local/rag_index`.
- LangGraph calls retrieval before agent/team steps.

Best for:

- source-grounded answers
- KB readback
- PRD generation from approved public/sanitized knowledge

### Option D: Add CrewAI After Graph And RAG

How it works:

- Convert `crewai-crew.yaml` into actual CrewAI agents/tasks.
- Keep process sequential first.
- Disable CrewAI memory initially.
- Use LangGraph as the outer controller and review gate.

Best for:

- clear named roles
- task accountability
- repeatable multi-agent outputs

### Option E: Add A Local UI Later

Possible UI choices:

| UI | Use |
|---|---|
| Codex chat | Current operator UI. |
| CLI scripts | Repeatable technical runs. |
| Streamlit | Simple local operator dashboard for uploading sanitized input and reviewing outputs. |
| Web app | Future client-facing or team-facing interface after proof run. |

## 12. Recommended Implementation Plan

### Phase 0: Current State

Done:

- public repo created and pushed
- Codex operator boundary defined
- Ollama/Qwythos available
- LangSmith env prepared
- WikiLLM public memory installed
- LangGraph/CrewAI/LlamaIndex contracts written

### Phase 1: API Key And Trace Readiness

1. Add LangSmith API key to `project/.env.langsmith.local`.
2. Run a small sanitized trace test.
3. Confirm trace appears in the `ArchFlow` LangSmith project.
4. Record trace ID and URL in `wiki/runs/`.

### Phase 2: LangGraph Runtime

1. Create Python project structure.
2. Install `langgraph`, `langsmith`, and Ollama/LangChain integration packages.
3. Implement graph state schema.
4. Implement nodes from `langgraph-controller.yaml`.
5. Run graph on a synthetic sanitized input.
6. Record trace and output documents.

### Phase 3: LlamaIndex RAG

1. Install LlamaIndex runtime.
2. Implement approved corpus loader.
3. Implement chunking, metadata, and local persistence.
4. Use Qwythos or local embedding provider as configured.
5. Add retrieval log output.
6. Refuse private-source retrieval by default.

### Phase 4: CrewAI Runtime

1. Install CrewAI.
2. Convert crew YAML into actual agents/tasks.
3. Keep sequential process.
4. Keep memory disabled initially.
5. Have LangGraph call CrewAI only after retrieval and digest.
6. Route all outputs through AF Review.

### Phase 5: First Proof Run

1. Use sanitized project source summary.
2. Produce all output templates.
3. Run review gate.
4. Save project run and WikiLLM run.
5. Publish only approved files.

### Phase 6: Optional UI

1. Start with CLI.
2. Add Streamlit only after one proof run works.
3. Add full web app only if repeated non-technical usage is needed.

## 13. Technology Stack To Know

### Required Now

- Git and GitHub SSH publication
- Markdown documentation
- YAML workflow contracts
- `.env` configuration patterns
- Codex operator workflow
- Ollama local model serving
- public-safety scanning
- WikiLLM memory discipline

### Required For Next Runtime Step

- Python virtual environments
- LangGraph `StateGraph`, nodes, edges, compile/invoke
- LangSmith tracing env and project routing
- Ollama chat/generate/embed APIs
- basic test scripts
- structured output validation

### Required For RAG Step

- LlamaIndex documents and nodes
- loading and ingestion pipelines
- chunking
- embeddings
- vector indexes
- query engines
- metadata filters
- source citation discipline

### Required For Crew Step

- CrewAI agents
- CrewAI tasks
- sequential vs hierarchical process
- callbacks/logging
- CrewAI memory tradeoffs
- tool permissions and safety boundaries

### Required Later

- Streamlit or lightweight web UI
- queueing and run history
- trace dashboards
- evaluation datasets
- security review for public/private boundaries

## 14. Source List

Official sources checked:

1. LangGraph overview: `https://docs.langchain.com/oss/python/langgraph/overview`
   - Used for LangGraph's role as low-level orchestration runtime, durable execution, state, persistence, and human-in-the-loop concepts.

2. CrewAI crews docs: `https://docs.crewai.com/en/concepts/crews`
   - Used for crew concepts: agents, tasks, process, memory, cache, planning, callbacks, tracing, and YAML-first configuration.

3. LlamaIndex high-level concepts: `https://developers.llamaindex.ai/python/framework/getting_started/concepts/`
   - Used for RAG concepts: loading, documents/nodes, indexing, querying, storing, local models, embeddings, and observability.

4. LangSmith observability: `https://docs.langchain.com/langsmith/observability`
   - Used for LangSmith's role as tracing, monitoring, feedback, and observability layer.

5. LangSmith trace setup: `https://docs.langchain.com/langsmith/trace-with-langchain`
   - Used for env variables: `LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_ENDPOINT`, and `LANGSMITH_PROJECT`; also used for project routing and local-model trace naming.

6. Ollama API introduction: `https://docs.ollama.com/api/introduction`
   - Used for local API base URL and model interaction concept.

7. Local project files:
   - `project/config/model-routing.yaml`
   - `project/workflows/langgraph-controller.yaml`
   - `project/workflows/crewai-crew.yaml`
   - `project/workflows/llamaindex-rag.yaml`
   - `project/langsmith-setup.md`
   - `wiki/index.md`
   - `wiki/memory.md`

## 15. Current Gaps

- LangSmith API key is not inserted yet.
- LangGraph runtime is not installed.
- CrewAI runtime is not installed.
- LlamaIndex runtime is not installed.
- No actual vector index exists.
- No real LangSmith trace exists.
- No first proof-run output set exists.

## 16. Recommended Next Approval

Recommended next approval:

```text
Approve Phase 1: add LangSmith API key locally and run one sanitized LangSmith trace test with Ollama/Qwythos only.
```

Do not install LangGraph, CrewAI, or LlamaIndex until the trace path is verified.
