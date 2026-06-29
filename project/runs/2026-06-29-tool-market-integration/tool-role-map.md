# Tool Role Map

| Tool | ArchFlow role | Current status |
|---|---|---|
| Codex | Operator, editor, verifier, approval boundary. | Active. |
| LangGraph | Control plane for state, routing, retries, and review gates. | Active runtime smoke passed. |
| Loop Engineering | Operating contract for loops, state, budgets, attempt caps, and maker/checker separation. | Added as L1 report-only contract. |
| CrewAI | Role/task organization inside graph-controlled runs. | Config/import check exists; no autonomous LLM execution. |
| LlamaIndex | Retrieval abstraction over approved corpus. | Active deterministic/keyword proof. |
| turbovec | Future local vector store under LlamaIndex. | Deferred. |
| WikiLLM | Canonical curated memory. | Active. |
| Cognee | Future operational recall and graph memory. | Deferred until E1.3 readback. |
| Ollama/Qwythos | Local minor/background model execution. | Configured; server state must be checked per run. |
| Mistral | Future sanitized quality pass for PRD/research/copy. | Disabled until approval and credentials. |
| LangSmith | Sanitized observability. | Configured with local ignored key and smoke traces. |
