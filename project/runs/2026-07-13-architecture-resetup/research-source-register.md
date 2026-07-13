# Research Source Register

All entries are architecture inputs, not proof that a tool is installed or suitable for production.

## Agent architecture and safety

| Source | Primary use | Decision |
|---|---|---|
| [Loop Engineering](https://github.com/cobusgreyling/loop-engineering) | Loop maturity, state, maker/checker, scheduling, worktrees, skills, context, audit/cost. | Adopt current L1 discipline. |
| [Goal Engineering](https://github.com/cobusgreyling/goal-engineering) | Objective, done condition, verifier, state, budgets, kill switches, readiness levels. | Adopt as G1 contract. |
| [Destructive Command Guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Pre-tool command policy and defense in depth. | Trial only after completed security and hook review. |
| [Google agents-cli](https://github.com/google/agents-cli) | Build, evaluate, deploy, govern, observe agent lifecycle and skills. | Reference; trial only for a Google-specific need. |
| [Google ADK Python](https://github.com/google/adk-python) | Code-first agents, tool confirmation, multi-agent composition, sessions, memory, evaluation, deployment. | Reference; avoid duplicate state owner. |
| [Google ADK Samples](https://github.com/google/adk-samples) | Official implementation examples across languages, tools, and agent patterns. | Reference only; select per fixture. |
| [Google Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) | Historical templates for CI/CD, evaluation, observability, deployment, and RAG. | Superseded for new projects by agents-cli; useful migration reference. |
| [Google MCP Toolbox for Databases](https://github.com/googleapis/mcp-toolbox) | Least-privilege database tools and MCP integration patterns. | Reference for data-role contracts; not needed in the current public architecture. |
| [A2A protocol](https://github.com/a2aproject/A2A) | Interoperability between separately deployed agent applications. | Defer until a real cross-runtime boundary exists. |
| [Google Cloud generative-ai samples](https://github.com/GoogleCloudPlatform/generative-ai) | Official notebooks and examples across Gemini Enterprise Agent Platform. | Discovery/reference only; not an install target. |
| [Google agentic AI architecture guides](https://docs.cloud.google.com/architecture/agentic-ai-overview) | Production architecture and workload patterns. | Reference. |
| [NVIDIA Agent Skills](https://github.com/NVIDIA/skills) | Signed skill cards, evaluation datasets, benchmarks, task-specific catalog. | Adopt governance pattern; select skills only. |
| [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) | Static and semantic external skill review. | Required gate when it completes; timed out in this run. |
| [NVIDIA NeMo Agent Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | Multi-agent interoperability, evaluation, profiling, observability, optimization. | Reference; future trial. |
| [NVIDIA RAG Blueprint](https://github.com/NVIDIA-AI-Blueprints/rag) | Reference RAG pipeline, deployment, ingestion, retrieval, and evaluation surface. | Reference/benchmark candidate only; current bounded LlamaIndex path stays default. |
| [NVIDIA NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | Input, dialog, retrieval, execution, and output rails for LLM applications. | Future application-safety trial after a provider-backed runtime exists. |
| [NVIDIA NeMo Retriever](https://github.com/NVIDIA/NeMo-Retriever) | Document content/metadata extraction and retrieval services. | Defer until a GPU-backed corpus and workload justify it. |

## Knowledge, Obsidian, graph, and retrieval

| Source | Primary use | Decision |
|---|---|---|
| [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Index-first retrieval, hot context, hybrid search, source ingestion, reconciliation, advisory locks. | Selective method adoption only. |
| [mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) | REST-based note read/search/patch/append/delete. | Defer; Nexus/filesystem already cover the role. |
| [Cognee](https://github.com/topoteretes/cognee) | Operational graph/vector agent memory, recall, provenance, evaluation. | Bounded future trial after canonical readback. |
| [TurboVec](https://github.com/RyanCodrai/turbovec) | Rust/Python compact vector index based on TurboQuant. | Benchmark candidate, not current default. |
| [LLM Survey Papers Collection](https://github.com/KalyanKS-NLP/LLM-Survey-Papers-Collection) | Discovery index for surveys across RAG, agents, evaluation, safety, prompting, post-training, and domains. | Keep as curated routing map; verify primary papers. |

## Media and product references

| Source | Primary use | Decision |
|---|---|---|
| [LTX-2](https://github.com/Lightricks/LTX-2) | Video/audio generation and media workflows. | Media-role-only future trial. |
| [Omma](https://omma.build/) | Agent-assisted 3D scene and interactive website prototyping. | Future sanitized prototype only. |
| [Legora](https://legora.com/) | Layered agent, data/integration, context/knowledge, capability, interface, security/governance product reference. | Architecture and UX reference. |

## Research limits

- No third-party repository was installed or executed.
- SkillSpector scans were attempted but did not return inside the bounded review window; no scanned-safe verdict exists.
- The Google/NVIDIA set is a curated responsibility-based control-plane shortlist, not every repository in either organization. An exhaustive organization-wide audit would be unstable, expensive, and mostly irrelevant to ArchFlow roles.
- Current websites and repository pages can change; version, license, release, and security details must be refreshed before adoption.
- The market package is desk research, not primary buyer validation.
