# Solomiia alternative: One-Case Trace Spine

Status: design and audit only; provider-disabled; no runtime, dashboard, vault, deployment, or external action was executed.

Owner lane: **Solomiia** (`source_and_context_operator`)

## Recommendation

Replace the current framework-led dashboard with a **One-Case Trace Spine**: one selected Knowledge Case, one vertical progression, and one evidence inspector. The operator should need only three navigation concepts:

1. **Cases** — what work exists and where it is now.
2. **Trace** — why a claim, requirement, decision, gate, or result is trusted.
3. **System** — whether the bounded adapters and contracts are actually ready.

The six visible phases inside a case are **Intent → Evidence → Commitments → Work → Gate → Result**. They are projections of the existing controller states, not a second workflow. LlamaIndex, LangGraph, CrewAI, WikiLLM, Obsidian, Orbit/Graphify, and TurboVec do not appear as primary navigation. They appear only as provenance or readiness details in the right-hand inspector and System view.

This is radically different from the committed dashboard: it removes the 21 framework/topic views, the top-level `Architecture 1` / `Architecture 2` choice, and the separate Jarvis product surface. The compatibility `/jarvis` route should open the current case's **Ask Yaromyr** panel; it must not remain a second system of record.

## Evidence classification

### FACT

- The public operating model identifies one `unified_knowledge_case_controller`, marks `Architecture 1` and `Architecture 2` as `legacy_compatibility_only`, keeps providers and writeback disabled by default, and defines the dashboard as a future projection. Evidence: `project/system/contracts/operating-model.json`.
- The public architecture says “one controller, one case, many bounded roles,” and the dashboard plan says the dashboard must become a read-only projection of that controller. Evidence: `docs/unified-operating-architecture.md`; `docs/dashboard-integration-plan.md`.
- The committed dashboard still exposes nine primary views, twelve secondary views, a hidden Legacy Jarvis view, a separate `/jarvis` link, and the legacy architecture selector. The code contains no `case_id` projection. Evidence: `project/dashboard/app.js:1`; `project/dashboard/app.js:13`; `project/dashboard/app.js:28`; `project/dashboard/app.js:374`; `project/dashboard/index.html:46`.
- The committed dashboard implementation is large: `project/dashboard/app.js` is 4,588 lines, `project/dashboard/styles.css` is 3,839 lines, and generated `project/dashboard/data.json` is 11,116 lines. This is size evidence only, not a quality verdict.
- The Knowledge Case schema strongly types evidence and requirements, but decisions, contradictions, gaps, approvals, and results are currently arrays of generic objects. That prevents the deepest cross-object trace from being contract-enforced. Evidence: `project/system/schemas/knowledge-case.schema.json`.
- The active run capsule declares `archflow.context-capsule.v1`, while the public capsule schema requires `capsule_version: v2` and a different required field set. One stable-context reference in the run capsule, `project/runs/20260729-architecture-enforcement/task-contract.md`, is absent in this worktree. Evidence: `project/runs/20260805-responsive-knowledge-crew-dashboard/context-capsule.json`; `project/context/context-capsule.schema.json`.
- The public retrieval contract already fixes chunk size `800`, overlap `120`, vector/lexical/rerank/similarity top-k `5`, required source-path metadata, and lexical fallback. Evidence: `project/workflows/llamaindex-rag.yaml`.
- The committed LangGraph contract currently declares `checkpointer: none_for_now`; therefore it does not support a truthful durable-resume claim yet. Evidence: `project/workflows/langgraph-controller.yaml`.
- The committed CrewAI contract uses `process: sequential`, `memory: false`, and `planning: false`, but still exposes legacy role names and `cache: true`. Evidence: `project/workflows/crewai-crew.yaml`.
- The task contract keeps TurboVec optional and bars sole/default use without a fixed paired benchmark, provenance, source filtering, persistence integrity, lexical fallback, and an independent verdict. Evidence: `project/runs/20260805-responsive-knowledge-crew-dashboard/task-contract.md`.

### INTERPRETATION

- The public architecture is already case-centric, but the committed interface is still tool-centric. The main migration is therefore a projection rewrite, not the invention of another controller.
- The current number of visible framework views makes operators learn implementation nouns before they can answer the basic questions: What is happening? Why do we believe it? What is blocked? What changed?
- A “deep trace” cannot be produced reliably from the current generic decision/result arrays or from unlinked FACT/INTERPRETATION/HYPOTHESIS/GAP strings. Trace IDs and typed links must be contract data, not inferred in the browser.
- Context capsules should be immutable, least-privilege projections of one Knowledge Case version. They must not become a parallel memory store or a transcript dump.
- CrewAI knowledge, memory, and Flow persistence would duplicate LlamaIndex retrieval, WikiLLM/Obsidian knowledge, and LangGraph state. They should remain disabled in this architecture.

### HYPOTHESIS

- Collapsing 21 topic views into Cases, Trace, and System will materially reduce operator orientation time while increasing evidence visibility.
- A persistent right-hand trace inspector will catch stale, unsupported, and authority-ambiguous claims earlier than separate Evidence, RAG, WikiLLM, Graphify, and Runs pages.
- Showing agents only when they own the selected phase or artifact will make the crew feel like accountable colleagues rather than a catalogue of autonomous bots.

### GAP

- No usability test yet proves the three-view information architecture.
- No validated public schema currently joins every claim to source node, requirement, decision, review, checkpoint, action proposal, result, and promotion receipt.
- No current dashboard read model projects the Knowledge Case schema.
- No implemented checkpointer proves pause/resume or historical state reconstruction.
- The active run capsule does not validate against the current public capsule schema and includes a missing stable-context reference. This should be repaired before it is used as an implementation input.
- The present public evidence does not justify TurboVec as the default or sole retrieval route.
- Connector/config readiness does not prove that an Obsidian vault is active, that a community plugin is enabled, or that a live tool call succeeds.

## The minimum-concept interface

```text
┌ Cases ────────────┬ Current Knowledge Case ────────────────────────┬ Why this? ─────────────┐
│ Search / filters  │ Goal, owner, state, risk, proof badges        │ selected object        │
│                   │                                                │ claim status           │
│ Case A            │ Intent                                        │ source node + span      │
│ Case B            │   ↓ Evidence                                  │ authority + freshness   │
│ Case C            │   ↓ Commitments                               │ requirement / decision  │
│                   │   ↓ Work                                      │ maker / reviewer        │
│                   │   ↓ Gate                                      │ checkpoint / approval   │
│                   │   ↓ Result                                    │ receipt / readback      │
│                   │                                                │ supersession            │
│                   │ Ask Yaromyr: explain, compare, draft packet   │ open exact public source│
└───────────────────┴────────────────────────────────────────────────┴────────────────────────┘
```

### 1. Cases

The left rail is a case switcher, not a module menu. Each row shows only:

- title and `case_id`;
- current visible phase;
- `FACT`, `GAP`, contradiction, and stale-evidence counts;
- next owner by Ukrainian call name;
- gate state: `ready`, `review`, `approval`, `blocked`, or `closed`.

Filters: `mine`, `needs review`, `blocked`, `stale`, `closed`. Search matches public-safe titles, IDs, claims, requirements, and source paths. It must never search raw private vault text from the browser.

### 2. Current case spine

The centre column is one narrative route. Existing machine states remain intact but are grouped for humans:

| Visible phase | Existing controller states projected here | Primary question |
| --- | --- | --- |
| Intent | `request_received`, `admission_checked`, `context_bound` | What outcome and authority are bound? |
| Evidence | `evidence_gathering`, `evidence_reconciled` | What is known, inferred, uncertain, or missing? |
| Commitments | `requirements_review`, `requirements_approved`, `support_ready` | What exactly is required and decided? |
| Work | `work_planning`, `candidate_in_progress`, `candidate_review` | Who is producing which bounded artifact? |
| Gate | `proposal_ready`, `proposal_validated`, `approval_wait`, `execution_ready`, `repair`, `blocked`, `failed`, `stopped` | Is the next transition allowed and reversible? |
| Result | `executed`, `result_verification`, `accepted_result`, `promotion_review`, `promoted`, `answered`, `closed_no_promotion`, `closed` | What changed, what was read back, and what became durable knowledge? |

Each phase shows one summary, its unresolved items, and the single next safe action. Details open in the Trace inspector. Frameworks never create new phases.

### 3. Trace

Selecting any claim, requirement, decision, task, proposal, approval, result, or knowledge item opens the same inspector. It follows a typed chain:

`source → document → node/span → evidence → claim → requirement → decision → task/artifact → review → checkpoint/approval → result/readback → promotion`

The inspector must show missing links explicitly as `GAP`; it must never synthesize a plausible link in the browser. Every item shows:

- stable ID and version;
- `FACT`, `INTERPRETATION`, `HYPOTHESIS`, or `GAP`;
- current/stale/superseded/unknown state;
- source authority and observation/review dates;
- creating role and independent reviewer by call name;
- predecessor and successor links;
- exact public source path, document ID, chunk/node ID, and bounded span when available;
- retrieval mode and rank/score when meaningful;
- checkpoint, approval, execution, verification, readback, and promotion receipts when applicable.

### 4. System

System is the only implementation-facing view. It reports each adapter as one of `not_configured`, `configured`, `reachable`, `call_verified`, `degraded`, or `blocked`. A green state requires the exact proof named by the adapter contract. It contains:

- contract/schema validity;
- retrieval route and fallback readiness;
- LangGraph checkpoint/interrupt proof;
- CrewAI provider/memory/knowledge state;
- Obsidian connector, vault activation, and live-call proof as separate rows;
- WikiLLM promotion path;
- Orbit/Graphify structural-index freshness;
- TurboVec candidate/gate state;
- dashboard data freshness and public-safety validation.

## One authoritative trace model

### Knowledge Case contract delta

Keep one authoritative case. Revise `knowledge-case.schema.json` before dashboard implementation so the currently generic arrays become typed. The minimum public fields are:

```yaml
schema_version: 1.1.0
case_id: case-<public-safe-slug>
case_version: <monotonic integer>
workflow_state: <existing canonical state>
phase_projection: intent|evidence|commitments|work|gate|result
goal: <existing typed goal>
authority: <existing typed authority>
source_boundary: <existing typed source boundary>
evidence:
  - id: EVD-<stable-id>
    claim_id: CLM-<stable-id>
    source_path: <public repo-relative path>
    source_hash: sha256:<hex>
    doc_id: doc-<stable-id>
    node_id: node-<stable-id>
    source_span: {start_line: <integer>, end_line: <integer>}
    retrieval_mode: cag|lexical|vector|hybrid|manual_read|graph
    rank: <integer-or-null>
    score: <number-or-null>
    state: current|stale|superseded|unknown
    claim_status: fact|interpretation|hypothesis|gap
    owner_role: <stable role id>
    observed_at: <RFC3339>
    review_by: <RFC3339>
claims:
  - id: CLM-<stable-id>
    statement: <public-safe text>
    status: fact|interpretation|hypothesis|gap
    evidence_refs: [EVD-...]
    contradiction_refs: [CTR-...]
    supersedes: [CLM-...]
requirements:
  - id: REQ-<stable-id>
    version: <string>
    state: proposed|reviewed|approved|rejected|superseded|blocked|gap
    claim_refs: [CLM-...]
    decision_refs: [DEC-...]
    acceptance_checks: [CHK-...]
decisions:
  - id: DEC-<stable-id>
    state: proposed|approved|rejected|superseded|blocked
    requirement_refs: [REQ-...]
    claim_refs: [CLM-...]
    owner_role: <stable role id>
    reviewer_role: <stable role id>
contradictions:
  - id: CTR-<stable-id>
    claim_refs: [CLM-..., CLM-...]
    state: open|resolved|accepted_exception
    resolution_decision_ref: DEC-...|null
gaps:
  - id: GAP-<stable-id>
    blocks: [<typed object ref>]
    owner_role: <stable role id>
    close_evidence_required: [<string>]
tasks: [<typed task and artifact references>]
approvals: [<typed interrupt and target-specific approval receipts>]
results: [<typed execution, verification, and readback receipts>]
review: <existing maker/reviewer verdict>
knowledge: <existing promotion state plus promotion receipt refs>
```

`source_path` must always be public repo-relative in a public packet. Private sources receive an opaque source handle and a public-safe description; raw path, text, account data, and connector secrets never enter the dashboard bundle.

Stable IDs should be issued by the controller and preserved across projections. Document and node identifiers should be deterministic from the normalized allowed source identity, content hash, and chunk ordinal. A changed source creates a new document/content version; it must not silently mutate the evidence behind an accepted claim.

### Context capsule composition

Create a schema-valid **v3 capsule** only after formally versioning and migrating the current v1/v2 drift. The capsule is an immutable role projection of `case_id@case_version`, not a second case and not durable memory. It carries the smallest sufficient set:

```yaml
capsule_version: v3
capsule_id: cap-<stable-id>
case_ref: case-<id>@<version>
generated_at: <RFC3339>
generated_by: {role_id: source_and_context_operator, call_name: Solomiia}
task:
  objective: <one outcome>
  output_schema_ref: <public schema path>
  allowed_actions: [<bounded operations>]
  forbidden_actions: [<explicit operations>]
  allowed_files: [<repo-relative paths>]
  stop_conditions: [<conditions>]
source_boundary:
  status: pass|needs_review|fail
  approved_corpus_refs: [project/..., history/..., skills/..., wiki/...]
stable_context:
  - source_path: <repo-relative path>
    content_hash: sha256:<hex>
    purpose: <short purpose>
retrieval:
  required: <boolean>
  queries: [<bounded query>]
  parameters_ref: project/workflows/llamaindex-rag.yaml
  retrieved_refs:
    - evidence_id: EVD-...
      source_path: <repo-relative path or opaque private handle>
      doc_id: doc-...
      node_id: node-...
      retrieval_mode: lexical|vector|hybrid|manual_read
      rank: <integer-or-null>
      score: <number-or-null>
      public_safety_status: pass|needs_review|fail
case_projection:
  claim_refs: [CLM-...]
  requirement_refs: [REQ-...@<version>]
  decision_refs: [DEC-...]
  contradiction_refs: [CTR-...]
  gap_refs: [GAP-...]
role_contract:
  role_id: <stable role id>
  call_name: <Ukrainian call name in English letters>
  task_id: TASK-...
  tool_allowlist: [<tool ids>]
  exact_source_read_allowlist: [<source handles>]
  expected_artifact_refs: [ART-...]
  acceptance_check_refs: [CHK-...]
  reviewer_role: <different stable role id when required>
  max_repairs: 3
policies:
  provider: disabled_until_explicit_approval
  external_side_effects: blocked_without_explicit_owner_approval
  memory_write: promotion_only_after_accepted_result
```

Do not put full source documents, raw retrieval text, chat history, unrestricted vault paths, or auto-summarized memory into the capsule. The assigned role resolves exact text through an allowlisted read using the referenced node/span. A broken reference becomes `GAP`; it is not replaced with remembered prose.

## Exact public runtime parameters

These are proposed public defaults. They do not claim a live runtime.

### LlamaIndex retrieval

| Parameter | Public default |
| --- | --- |
| `chunk_size` | `800` |
| `chunk_overlap` | `120` |
| `vector_top_k` | `5` |
| `lexical_top_k` | `5` |
| `rerank_top_k` | `5` |
| `similarity_top_k` | `5` |
| Required metadata | `source_path`, `document_type`, `public_safety_status`, `updated_at`, `authority_state`, `superseded_by` |
| Source-less node | rejected as evidence |
| Default smoke/fallback route | deterministic lexical |
| Vector route | allowed only when the same source boundary is enforced and node refs are returned |
| Synthesis | retrieval and evidence registration happen before answer synthesis |

Use an ingestion pipeline with deterministic document/node IDs and a docstore so unchanged documents can be skipped and changed documents can be versioned. Metadata must be flat scalar values where the chosen vector backend requires that constraint. Retrieval returns nodes first; the controller registers their refs before any response synthesizer operates.

### TurboVec candidate

- `enabled_by_default: false`
- `sole_evidence_route: false`
- `wrapper: llamaindex_retriever_adapter`
- `input_corpus`, filters, queries, and top-k: identical to the paired lexical/current-store route
- promotion requires exactly the task-contract gates: fixed paired benchmark, provenance, source filtering, persistence integrity, lexical fallback, and independent verdict
- missing filter proof, missing node provenance, persistence/readback failure, or retrieval error: mark the vector route `degraded`, run lexical fallback, and expose the reason in Trace/System
- no fallback evidence: create a `GAP` and block dependent FACT/requirement promotion

No private benchmark details or private paths belong in the public dashboard or this design.

### LangGraph controller

| Parameter | Public default |
| --- | --- |
| State owner | LangGraph only |
| `thread_id` | `case_id` |
| `checkpoint_ns` | `case_version` |
| Scalar reducers | overwrite only |
| Evidence/event/receipt reducers | append with stable-ID deduplication; reject conflicting same-ID payloads |
| Public stream | sanitized projection using explicit output keys/updates only |
| Repair limit | `3` total attempts |
| Same-failure limit | `2` |
| Human interrupt | only at a typed approval gate |
| Side effect placement | after approved resume only |
| Idempotency key | `case_id:proposal_id:target_hash` |
| Crew subgraph mode | per-invocation; no independent persistence |

The committed contract currently has no checkpointer, so the dashboard must show `resumable: false`. Only after a checkpointer is implemented and verified may it show pause/resume receipts. Resume must use the same thread ID. Because an interrupted node restarts from its beginning, no irreversible or duplicate-prone side effect may occur before `interrupt()`; any permitted post-resume action must be idempotent and followed by readback.

Private state channels are not a redaction boundary. The dashboard may consume only an explicitly sanitized public projection; it must not subscribe to full state-value streaming.

### CrewAI role bundle

| Parameter | Public default |
| --- | --- |
| Purpose | bounded role/task execution inside one LangGraph transition |
| `process` | `sequential` |
| `planning` | `false` |
| `memory` | `false` |
| CrewAI knowledge sources | `[]` |
| CrewAI Flow persistence | disabled |
| `cache` | `false` until cache provenance/invalidation is represented in Trace |
| `allow_delegation` | `false` unless the case explicitly grants a bounded delegation |
| tools | per-task allowlist only |
| task output | schema-bound artifact plus evidence refs |
| `guardrail_max_retries` | `2`; then return a repairable GAP to LangGraph |
| provider execution | disabled until explicit provider approval |

Do not rely on automatic context summarization for evidence-bearing work. If a capsule exceeds the bounded context, split the task by claim/requirement, preserve refs, and reconcile outputs in LangGraph. CrewAI produces candidate artifacts; it never approves, persists canonical workflow state, promotes memory, or executes external actions.

### Obsidian and WikiLLM

- Obsidian is a local-file knowledge surface. Treat connector/config presence, vault/plugin activation, and a live read call as three separate proof states.
- Community plugins are untrusted until independently reviewed, installed, enabled, and live-verified for the intended vault. Plugin access is broader than a fine-grained document permission model.
- The default adapter is read-only and returns opaque handles plus sanitized metadata to the public case. Exact-source reads occur only inside the approved boundary.
- A note write is a separate target-specific action. It occurs only after accepted result, knowledge promotion review, owner approval where required, and readback. Concurrent modifications require the vault/plugin-safe atomic process route.
- WikiLLM stores reviewed durable synthesis, decisions, runs, and reusable insights. It does not store raw execution traces or become the controller checkpointer.
- Retrieval is not promotion: finding a note does not make its content current, authoritative, or durable case memory.

### Orbit/Graphify and dashboard

- Orbit/Graphify supply structural evidence: paths, relationships, blast radius, and generated graph references. They cannot establish business truth or permission.
- The dashboard is a read-only case projection. Browser-local drafts are proposals only; they do not change case state.
- A dashboard action creates an `action-proposal` packet and routes it to the controller. The browser never calls a provider, vault write, deployment, or external system directly.
- Every displayed readiness badge includes its proof timestamp and receipt reference. Missing or stale proof is gray/amber, never green.

## Human-facing crew

Show only Ukrainian call names written in English letters. Stable role IDs remain available in Trace/System, but no legacy `af_*`, Hermes, or Jarvis name is human-facing.

| Call name | Stable role ID | Appears when |
| --- | --- | --- |
| Yaromyr | `goal_and_architecture_operator` | goal, architecture, or “Ask” guidance is selected |
| Bohdan | `admission_controller` | admission, risk, or stop rules are selected |
| Solomiia | `source_and_context_operator` | source boundary, retrieval, or evidence is selected |
| Oksana | `requirements_and_market_research` | requirements or market evidence is selected |
| Taras | `onboarding_guide` | onboarding support is selected |
| Danylo | `task_and_handoff_planner` | work plan or handoff is selected |
| Olena | `positioning_and_copy_maker` | positioning or copy artifact is selected |
| Andrii | `qualification_and_channel_planner` | qualification or channel plan is selected |
| Kateryna | `designer` | design artifact is selected |
| Dmytro | `implementation_maker` | implementation artifact is selected |
| Iryna | `action_validator` | proposal validation is selected |
| Mykola | `verifier` | verification/readback is selected |
| Halyna | `independent_reviewer` | independent review is selected |
| Larysa | `knowledge_librarian` | knowledge promotion is selected |
| Maksym | `integrator` | merge, conflict, or final handoff is selected |
| Pavlo | `external_action_operator` | an approved external action is selected |
| Nazar | `release_operator` | release preparation or promotion is selected |
| Zoriana | `growth_and_outcome_analyst` | outcome evidence is selected |
| Ostap | `observability_and_efficiency_observer` | trace health or efficiency is selected |
| Marta | `surface_projection_operator` | dashboard projection is selected |
| Roman | `product_packaging_engineer` | packaging or portability proof is selected |

Agent cards must show `candidate`, `working`, `waiting`, `reviewing`, `blocked`, or `done`; they must not imply a live autonomous agent merely because a role contract exists.

## Tool and authority boundaries

| Layer | Owns | Must not own |
| --- | --- | --- |
| LangGraph | case state, transitions, reducers, repair routing, approval interrupts, checkpoint receipts | retrieval ranking, durable knowledge truth, role memory, direct external action |
| LlamaIndex | allowlisted ingestion, document/node metadata, bounded retrieval, source-node return | case state, authority, promotion, external action |
| TurboVec | optional candidate vector retrieval behind the same LlamaIndex contract | sole/default evidence, source-boundary decisions, durable memory |
| CrewAI | temporary role/task bundles and schema-bound candidate outputs | controller state, independent approval, persistent Flow state, memory/knowledge authority, external action |
| WikiLLM | reviewed durable project memory and run/decision synthesis | raw retrieval cache, controller checkpoints, unreviewed claims |
| Obsidian | local reviewed notes and exact-source reads within the active vault boundary | public browser corpus, proof of plugin/runtime merely from config, automatic promotion |
| Orbit/Graphify | structural relationships and blast-radius evidence | business authority, prose truth, permissions |
| Dashboard | sanitized read projection and action-proposal drafting | workflow mutation, provider calls, vault writes, deployment, promotion |
| External adapters | exact approved operation plus verification/readback receipt | authority inference, broad tokens, unbounded target selection |

## Deterministic failure and fallback rules

1. **Admission/schema failure:** set the case to `blocked`; show the invalid receipt and remediation. Do not build a context capsule from an unadmitted request.
2. **Source boundary failure:** exclude the source. If the dependent statement lacks other support, classify it as `GAP`; do not downgrade it silently to a weak FACT.
3. **Missing path/node/span:** `no source path means no evidence`. Broken exact-read references remain visible as GAPs.
4. **Stale or superseded evidence:** retain it for history, mark its state, and prevent requirement/result promotion unless a current exception decision exists.
5. **Contradiction:** preserve both claims and sources; create a typed contradiction; require a resolution decision or accepted exception before dependent approval.
6. **Vector failure:** run deterministic lexical fallback with the same source boundary. Show which route produced each node. If both routes fail, block the dependent claim.
7. **TurboVec gate failure:** keep it candidate-only and continue with lexical/current allowed retrieval; do not erase the failed trial receipt.
8. **Context overflow:** split by claim or requirement. Do not silently summarize away citations, negative evidence, or approval conditions.
9. **Crew task/guardrail failure:** return a structured repair GAP to LangGraph. After two guardrail retries or the controller's repair limits, stop or escalate.
10. **Checkpoint unavailable:** show `resumable: false`; do not promise pause/resume. A browser refresh cannot be presented as workflow recovery.
11. **Interrupted action:** resume with the same case/thread identity. Execute only after approval and only with an idempotency key; verify with readback.
12. **Obsidian not active or plugin not verified:** use safe filesystem/approved retrieval fallback where permitted, record a GAP, and block any live-vault claim or write.
13. **Durable-memory write failure:** keep the accepted result and failed promotion as separate states. A completed artifact is not automatically promoted knowledge.
14. **Dashboard data stale/invalid:** render the last valid snapshot with an explicit stale banner or fail closed; never merge incompatible packets in the browser.
15. **Private-data leak risk:** omit the field/object from the public projection, log a public-safe GAP code, and route to review. Do not mask in place if surrounding context could still identify it.

## Acceptance checks for this alternative

- An operator can open a case, identify the next safe action, and trace any FACT to a source node without navigating to a framework page.
- The UI has exactly three primary destinations: Cases, Trace, System.
- Every visible machine state maps to exactly one of the six human phases without changing the canonical controller state.
- No human-facing label uses Jarvis, Hermes, or an `af_*` role name.
- Every claim/requirement/decision/result has typed predecessor/successor links or an explicit GAP.
- The dashboard can render an entirely provider-disabled, retrieval-degraded, or checkpointer-disabled case truthfully.
- A failed vector route demonstrably falls back to lexical retrieval and preserves route provenance.
- CrewAI memory, CrewAI knowledge, CrewAI Flow persistence, provider execution, external actions, and durable writes remain disabled by default.
- Private paths, raw private source text, credentials, account identifiers, raw runtime state, and raw full-state streams are absent from public bundles.
- Independent review and target-specific approval remain separate from maker output.

## Official first-party documentation checked

Current first-party documentation was checked on 2026-08-05.

### LlamaIndex

- [Ingestion Pipeline](https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/) — transformations, caching, document management, docstore/vector-store integration.
- [Documents and Nodes](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/) — document/node model, metadata, and relationships.
- [Using Documents](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/usage_documents/) — metadata propagation and vector-store metadata constraints.
- [Using Nodes](https://developers.llamaindex.ai/python/framework/module_guides/loading/documents_and_nodes/usage_nodes/) — manual node identity and relationships.
- [Retriever](https://developers.llamaindex.ai/python/framework/module_guides/querying/retriever/) — node retrieval as the context-return boundary.
- [Response synthesizers](https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/) — source nodes and retrieval-only inspection before synthesis.

### LangGraph

- [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) — state schemas, reducers, private channels, and stream behavior.
- [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) — thread-scoped checkpoints versus cross-thread store memory.
- [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) — pause/resume identity and node restart semantics.
- [Subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs) — shared/mapped state and per-invocation versus per-thread persistence.

### CrewAI

- [Agents](https://docs.crewai.com/en/concepts/agents) — role, goal, tools, delegation, knowledge, memory, and context behavior.
- [Tasks](https://docs.crewai.com/en/concepts/tasks) — expected output, task context, tool limits, output schemas, and guardrails.
- [Crews](https://docs.crewai.com/en/concepts/crews) — process, memory, caching, planning, and embedder configuration.
- [Flows](https://docs.crewai.com/en/concepts/flows) — Flow state and persistence, intentionally not used as a second controller here.
- [Knowledge](https://docs.crewai.com/en/concepts/knowledge) — agent/crew knowledge storage and embedding behavior, intentionally disabled here.
- [Memory](https://docs.crewai.com/en/concepts/memory) — automatic extraction/retrieval behavior, intentionally disabled here.

### Obsidian

- [How Obsidian stores data](https://help.obsidian.md/data-storage) — local Markdown vaults, per-vault configuration, and external-change behavior.
- [Community plugins](https://help.obsidian.md/Extending+Obsidian/Community+plugins) — restricted mode, installation, enablement, and updates.
- [Plugin security](https://help.obsidian.md/plugin-security) — broad plugin capabilities and lack of reliable fine-grained restrictions.
- [Vault API](https://docs.obsidian.md/Plugins/Vault) — vault reads, cached reads, external modifications, and safe processing.

## Local public evidence paths

- `README.md`
- `project/operating-rules.md`
- `project/system/contracts/operating-model.json`
- `project/system/contracts/role-catalog.json`
- `project/system/schemas/knowledge-case.schema.json`
- `project/system/schemas/action-proposal.schema.json`
- `docs/unified-operating-architecture.md`
- `docs/dashboard-integration-plan.md`
- `project/context/context-capsule.schema.json`
- `project/context/retrieval/source-boundary-policy.yaml`
- `project/workflows/llamaindex-rag.yaml`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`
- `project/dashboard/index.html`
- `project/dashboard/app.js`
- `project/dashboard/styles.css`
- `project/dashboard/data.json`
- `project/runs/20260805-responsive-knowledge-crew-dashboard/task-contract.md`
- `project/runs/20260805-responsive-knowledge-crew-dashboard/context-capsule.json`

## Final recommendation

Approve the **One-Case Trace Spine** as the minimum-concept alternative and implement it only after two contract repairs: (1) make the active run capsule schema-valid with no missing references, and (2) type the Knowledge Case trace links for claims, decisions, contradictions, gaps, approvals, results, and promotions. Then build a read-only case projection with Cases, Trace, and System; embed Ask Yaromyr inside the case; keep all framework identity in provenance; and preserve lexical fallback plus every existing approval boundary. Do not make TurboVec, CrewAI memory/knowledge, an Obsidian plugin, a provider, or a checkpoint/resume capability look active until its exact public proof exists.
