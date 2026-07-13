# Tool Adoption Gates

## Required gate

1. Name one problem the current stack cannot solve adequately.
2. Verify the primary source, maintainer, license, release/version, and platform fit.
3. Run SkillSpector or an equivalent static and semantic review. Record whether the semantic pass actually ran.
4. Inspect install scripts, hooks, network use, secrets, write scope, deletion capability, telemetry, and transitive dependencies.
5. Pin the version or commit and preserve a rollback path.
6. Test in a disposable, sanitized fixture with provider calls disabled where possible.
7. Compare against the current baseline using the declared metrics.
8. Require independent review before access to a vault, external system, provider key, or production runtime.
9. Record `adopt`, `trial`, `defer`, or `reject` with evidence and revisit date.

## Current classifications

| Candidate | Decision | Reason / graduation gate |
|---|---|---|
| Loop Engineering | Adopt at L1 | Existing bounded contract; graduate only with measured L2 fixture reliability. |
| Goal Engineering | Adopt as a contract | Adds persistent objective, independent verifier, budget, lifecycle, and kill switches. |
| LangGraph | Adopt as state owner | Avoid duplicate orchestration control in CrewAI or ad hoc prompts. |
| CrewAI | Trial inside LangGraph | Use named task teams only when it beats simpler worker functions on evaluation. |
| `destructive_command_guard` | Trial later | Defense in depth; requires completed security scan, pinned release, hook-diff review, fixture tests, and proof that platform approvals remain authoritative. |
| `claude-obsidian` methods | Selective adopt | Reuse index-first retrieval, hot/current cache, provenance, reconciliation, and write propagation. Reject permission bypass and uncontrolled background writes. |
| `mcp-obsidian` | Defer as fallback | Nexus and filesystem access already cover the role. Consider a read-only sanitized-vault fallback only after a proven gap; never expose delete by default. |
| Cognee | Trial later | Evaluate operational graph/vector recall after canonical WikiLLM readback and source IDs are stable. It must not become a second source of truth. |
| TurboVec | Trial later | Benchmark only after stable embeddings, dimension, metadata filters, persistence, license/security, and lexical baseline exist. |
| Google ADK / agents-cli | Reference, then trial | Strong build/eval/deploy/govern/observe patterns; current project is OpenRouter-first and should not add a second orchestrator without a measured use case. |
| NVIDIA signed skills | Adopt governance pattern | Prefer task-specific signed/evaluated skills; do not install the entire catalog. Verify signature and benchmark per selected skill. |
| NeMo Agent Toolkit | Reference, then trial | Useful evaluation, profiling, observability, and optimization lane when a runnable provider-backed agent exists. |
| LTX-2 | Defer to media role | Heavy video/audio generation lane; requires hardware, model-license, cost, privacy, and website story-board gates. |
| Omma | Defer to 3D prototype | External prototyping surface; require sanitized assets, export/lock-in review, accessibility and performance fallback. |
| Legora | Adopt as product reference | Its layered context, capability, interface, and governance model is an architectural comparison, not an implementation dependency. |
| LaTeX/Typst toolchain | Trial for publishing | Add only as a deterministic document-build skill with citation, font, accessibility, and PDF validation. |

## Automatic rejects

- `curl | bash` or equivalent unreviewed installer in the live workspace;
- `--dangerously-skip-permissions` or permission-bypass background agents;
- whole-device or whole-vault ingestion without a bounded corpus;
- external MCP access with broad write/delete authority by default;
- a framework that duplicates canonical state, memory, or orchestration without benchmark evidence;
- a tool whose claimed benefit cannot be tested against a current baseline.
