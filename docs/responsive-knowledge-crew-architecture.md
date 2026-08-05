# Responsive Knowledge Crew Architecture

Status: canonical public architecture
Version: 3.0
Verified baseline: 2026-08-05
Authority: `project/system/contracts/knowledge-crew-config.json`
Controller: `project/system/contracts/operating-model.json`

ArchFlow is one maintained knowledge system for onboarding employees, supporting daily work, coordinating specialist roles, validating proposed actions against current requirements, recording exact outcomes, and improving future guidance.

It is not two architectures. A PRD, ICP, market study, outreach packet, creative, design, implementation, or report is a role-owned output inside the same case lifecycle.

![Seven-layer responsive knowledge crew](../project/assets/architecture/knowledge-crew-tower.png)

*The left spine shows what each knowledge/database system contributes. The centre names all seven accountable layers. The right side names each layer's output and efficiency effect. Open the [editable labeled SVG](../project/assets/architecture/knowledge-crew-tower.svg) for full-resolution text.*

## 1. Product goal and operating invariant

The product goal is a responsive project-crew operator that:

- helps a new or existing employee understand their responsibility;
- retrieves the smallest sufficient current context for that responsibility and task;
- preserves a dependable perception of the larger project through stable context, bounded retrieval, structural pointers, and exact reads;
- selects the smallest specialist crew that owns the required outputs, checks, approval reviews, and handoffs;
- validates every consequential action against current requirements, permission, effects, rollback, verification, and readback;
- reports facts, interpretations, hypotheses, and gaps distinctly;
- promotes only reviewed reusable meaning into maintained knowledge.

The invariant is:

> A source, model, tool, role, graph transition, or successful command may propose evidence. None may silently create business truth, permission, approval, or a verified outcome.

## 2. Current truth state

| Capability | Public default | What is proved | What is not claimed |
|---|---|---|---|
| Case contracts | Enabled | Typed schemas, roles, workflow packs, validator fixtures | Production autonomy |
| Dashboard | Static and browser-local | Six primary views, local drafts, exports, responsive rendering | Authentication, durable team state, provider work |
| LlamaIndex | Optional local runtime contract | Allowlist, identity, metadata, retrieval and fallback parameters | A live index in every clone |
| TurboVec | Optional candidate | Public receipt records an isolated 0.8.0, 4-bit, 10-query synthetic trial with 9/9 checks, recall@3 1.00, and MRR 0.8167 | Fixture document count, lexical baseline, default backend, or representative production performance |
| CrewAI | Role/task contract | Configured role bindings and deterministic import/config pattern | Default provider-backed kickoff |
| LangGraph | State/control contract | Typed lifecycle, reducers, routes, interrupts, fixture validation | Persistent public checkpointer or resumed production actions |
| WikiLLM | Portable reviewed memory | Public indexes, run/decision/issue/insight pattern | Raw trace store |
| Obsidian | Optional local human workspace | Integration and security contract | Required dependency or live vault state |
| Orbit | Optional private structural adapter | A bounded adapter seam and structural-evidence contract | Knowledge authority or public private-corpus copy |
| Graphify | Generated structural reference | Repository graph/report pattern | Freshness when source commit has changed |
| Provider calls | Disabled | Zero calls in the public dashboard | Model completion |
| Writeback/external action | Disabled | Review-packet preparation only | Browser-to-Git, message, deployment, or memory write |

## 3. Seven connected layers

### L1 — Case authority and employee scope

Inputs:

- request and decision;
- employee/actor role;
- accountable owner policy;
- data class, risk, permissions, and exclusions.

Required fields:

- goal and observable done conditions;
- expected output;
- non-goals and stop conditions;
- maker and different reviewer;
- allowed operations and exact target prefixes;
- external/private/irreversible approval class;
- rollback and readback expectation.

Output: an admitted case or a named gap. Retrieval does not start for an invalid source boundary.

### L2 — Reviewed knowledge and source spine

The source spine classifies each item as current, stale, superseded, generated, private, prohibited, or unknown. Connectivity is never authority.

Every material source carries:

- `source_path` or opaque private reference;
- `doc_id` and document hash;
- document type and public-safety state;
- authority state;
- owner;
- observed/updated date;
- `review_by`;
- `superseded_by`.

Output: source manifest, freshness/owner map, and retrieval allowlist.

### L3 — Bounded context perception

![Input and perception flow](../project/assets/architecture/context-input-flow.png)

*The input view shows how stable rules, role responsibility, current requirements, task evidence, prior receipts, and gaps pass through source admission, document identity, hybrid retrieval, exact-read validation, and a 12,000-token role-safe capsule. Open the [editable SVG](../project/assets/architecture/context-input-flow.svg).*

Whole-project perception is a cascade:

1. Stable CAG reuses project identity, authority, architecture, safety, role responsibility, and source rules.
2. LlamaIndex loads only allowlisted documents, preserves document/node identity, applies metadata filters, and routes retrieval.
3. Lexical retrieval remains the deterministic fallback.
4. TurboVec may produce compact vector candidates when its adapter, filters, pinned embedding dimension, persistence sidecar, and benchmark gate are valid.
5. Orbit and Graphify point to definitions, references, paths, and likely impact.
6. Exact source reads verify material claims and actions.
7. The capsule preserves citations, contradictions, gaps, freshness, and exact-read status.

Context budget:

| Capsule section | Budget | Content |
|---|---:|---|
| Stable CAG | 2,400 | Rules, authority, identity, source boundary |
| Role responsibility | 1,400 | Goal, inputs, outputs, tools, prohibitions, reviewer |
| Current requirements | 2,600 | Approved requirements, decisions, acceptance, contradictions |
| Task evidence | 3,200 | Retrieved nodes, exact excerpts, structural entry points |
| Prior receipts | 1,200 | Relevant verified outcomes, repairs, supersession |
| Gaps and questions | 1,200 | Unknowns, stale items, owner questions, stop triggers |
| **Maximum** | **12,000** | Compressed summaries with intact provenance |

Overflow order:

1. remove duplicate snippets;
2. replace low-authority excerpts with citations;
3. summarize prior receipts;
4. ask to narrow the case;
5. stop before dropping current requirements.

### L4 — Adaptive role crew

CrewAI expresses role and task contracts. It is deliberately not a second controller or memory system.

Public parameters:

| Parameter | Value | Reason |
|---|---|---|
| `process` | sequential by default | Clear accountability and handoffs |
| bounded parallel work | maximum 3 | Parallel extraction only when outputs/files do not overlap |
| `memory` | `false` | WikiLLM/Obsidian remain the reviewed memory spine |
| `cache` | `true` | Reuse deterministic intermediate work where safe |
| `planning` | `false` | LangGraph/task contract owns plan and state |
| default delegation | `false` | A role cannot expand its own authority |
| knowledge input | role-safe capsule only | Least-privilege context |
| provider execution | disabled | Public config is a role/task contract |

Every role task receives:

- binding, case, workflow-pack, stable role, and call-name IDs;
- role goal and required case inputs;
- one owned and expected output;
- source and requirement references;
- allowed public skills, tool-capability ceiling, and exact targets;
- a permission boundary that references `case.authority` and cannot copy or invent `allowed_actions`;
- forbidden actions;
- deterministic checks;
- typed known-gap references from the active case;
- ordered reviewer route ending at `@case_owner`;
- handoff target and fixed evidence payload;
- stop conditions.

Effective capability is always:

`case authority ∩ role tool ceiling ∩ runtime-available capabilities ∩ exact targets − role and case denials`

The dashboard and CrewAI YAML are projections of [role-catalog.json](../project/system/contracts/role-catalog.json). Materialized case work validates against [role-task-binding.schema.json](../project/system/schemas/role-task-binding.schema.json). Neither projection may introduce its own authority plane.

Permission modes are explicit: read/draft only; exact-target local mutation; frozen-candidate review; verification without repair; knowledge candidate only; browser-local projection; observation only; exact-approved external action; or exact-approved Git action.

### L5 — Specialist research and delivery

The architecture includes ten adaptive workflow packs:

| Pack | Core responsibility | Typical roles | Required output |
|---|---|---|---|
| Employee onboarding | Orient, support, validate first action | Taras, Solomiia, Danylo, Iryna, Halyna, Larysa | Orientation, first mission, answer, escalation, learning candidate |
| Requirements research | Evidence to reviewed requirements | Oksana, Solomiia, Yaromyr, Halyna, Larysa | Evidence cards, pain chain, PRD/ICP projection, acceptance and gaps |
| Daily task planning | Requirement to bounded mission | Danylo, Maksym, Iryna, Mykola | Mission, dependencies, review route, blocker questions |
| Outreach | Qualify before message or send | Andrii, Oksana, Olena, Halyna, Pavlo | Company/person verdict, channel packet, message, no-send reason |
| Content and copy | Evidence to public-safe narrative | Olena, Oksana, Kateryna, Halyna, Nazar | Copy, caption, creative brief, claim/rights table |
| Design | Requirement to editable accessible visual | Kateryna, Marta, Dmytro, Mykola, Halyna | Direction, editable source, responsive artifact, accessibility evidence |
| Implementation | Bounded approved change | Dmytro, Maksym, Iryna, Mykola, Halyna | Candidate patch, tests, readback, repair record |
| Reporting | Evidence to decision-ready delivery | Zoriana, Ostap, Olena, Halyna, Larysa | Executive summary, evidence table, verdict, gaps, recommendation |
| Knowledge maintenance | Accepted result to reusable meaning | Larysa, Solomiia, Halyna, Ostap | Promotion, index, supersession, freshness task |
| Release/external action | One exact approved action | Pavlo, Nazar, Iryna, Mykola, Halyna | Preflight, one action, receipt, readback or blocked record |

The controller starts with one pack and adds a role only if it owns a required output, check, approval review, or handoff.

### L6 — Graph control, validation, and review

![Output, validation, and receipt flow](../project/assets/architecture/output-receipt-flow.png)

*Specialist candidates enter the same requirements/authority gate. The right side distinguishes employee handoff, report, verified artifact, exact action, result receipt, and maintained knowledge. Open the [editable SVG](../project/assets/architecture/output-receipt-flow.svg).*

LangGraph owns:

- typed case state and valid transitions;
- conditional routes;
- bounded parallel branches;
- reducers;
- checkpoint/resume when an approved runtime is configured;
- approval interrupts;
- bounded repair loops;
- terminal states.

It does not own source truth or approval.

Reducers:

| Field | Reducer |
|---|---|
| Evidence, claims, contradictions, gaps, artifacts | append unique by ID |
| Approvals, results, receipts | append only |
| Requirements and decisions | replace same ID only with a higher version |
| Tasks | replace same ID only after a valid transition |
| Workflow state | replace after a valid transition |

Persistence:

| Environment | Checkpointer |
|---|---|
| Public static demo | none |
| Local single user | SQLite only after migration and recovery proof |
| Team runtime | PostgreSQL only after tenancy, backup, and recovery proof |
| Thread key | `case_id` |
| Specialist subgraphs | per invocation by default |

Interrupts:

- requirement-owner decision;
- external-action approval;
- private-source request;
- irreversible change;
- material contradiction.

Interrupt payloads are JSON-serializable summaries without secrets. An interrupted node restarts on resume, so side effects occur after the interrupt and use an `action_id` replay guard.

Validation order:

1. approved requirement coverage;
2. actor, operation, exact target, and data class;
3. side effects, reversibility, rollback, verification, and readback;
4. deterministic maker checks;
5. independent reviewer verdict;
6. target-specific owner approval when required;
7. one action;
8. exact target readback.

Repair policy: maximum three attempts and maximum two repeats of the same failure.

### L7 — Receipts, outcomes, and maintained knowledge

A successful command is not a result. Required receipts can include admission, retrieval, verification, approval, action, readback, and promotion.

The result record names exact artifacts, observed state, verification, readback, rollback state, and remaining gaps.

Knowledge promotion:

1. search for duplicates;
2. identify reusable meaning;
3. preserve source, requirement, decision, and result lineage;
4. assign owner and review date;
5. supersede old knowledge instead of silently deleting it;
6. run retrieval regression;
7. promote, reject, or close without promotion.

## 4. Named role catalog

Call names are Ukrainian names written with English letters. They improve human coordination; stable role IDs remain the machine contract.

| Call name | Role | Owns | Cannot do |
|---|---|---|---|
| Yaromyr | Goal and Architecture Operator | Objective, done conditions, states, gates | Expand permission or self-verify high risk |
| Bohdan | Admission Controller | Risk, profile, minimum roles, stop rules | Edit the project or activate a provider |
| Solomiia | Source and Context Operator | Allowlist, CAG, retrieval, capsule | Ingest broadly or promote knowledge |
| Oksana | Requirements and Market Research | Evidence, market/pain, requirements, acceptance | Approve requirements, infer demand, execute |
| Taras | Onboarding Guide | Role projection, answer, first mission, escalation | Invent truth or inherit permission |
| Danylo | Task and Handoff Planner | Dependencies, task packet, checks, questions | Create unowned shared edits |
| Olena | Positioning and Copy Maker | Positioning, message, caption, claim table | Invent proof, send, publish |
| Andrii | Qualification and Channel Planner | Company/person fit, currentness, channel, send checklist | Send or infer pain from signals |
| Kateryna | Designer | Brief, hierarchy, editable artifact, accessibility | Approve claims, publish, self-review |
| Dmytro | Implementation Maker | Claimed files, change, checks, repairs | Expand scope or provide final review |
| Iryna | Action Validator | Requirements, permission, effects, rollback, verdict | Execute or infer approval |
| Mykola | Verifier | Deterministic checks, regressions, readback | Silently repair or declare unsupported completion |
| Halyna | Independent Reviewer | Approve, revise, block; calibrated claims | Repair candidate or self-approve |
| Larysa | Knowledge Librarian | Duplicates, lineage, promotion, supersession, freshness | Promote raw traces, secrets, unsupported claims |
| Maksym | Integrator | Lane claims, merge order, conflicts, receipts, handoff | Hide blockers or infer permission |
| Pavlo | External Action Operator | One approved action, preflight, receipt, readback | Reuse approval or chain actions |
| Nazar | Release Operator | Release prep, evidence, owner-approved Git action | Deploy/publish without approval |
| Zoriana | Growth and Outcome Analyst | Event ledger, denominators, observed/modeled split | Treat attention as demand |
| Ostap | Observability and Efficiency Observer | Drift, usage evidence, reproducibility gaps | Activate providers or claim completion |
| Marta | Surface Projection Operator | Read-only views, local packets, truthful labels | Own source truth or write back |
| Roman | Product Packaging Engineer | Clean clone, least privilege, lifecycle proof | Productize without evidence |

The executable source is [role-catalog.json](../project/system/contracts/role-catalog.json).

## 5. Research and delivery methods

### Source and claim discipline

- Source-authority triage grades primary/current/reviewed versus secondary/historical/unverified.
- `FACT / INTERPRETATION / HYPOTHESIS / GAP` prevents reasoning from being presented as observation.
- Triangulation requires independent support for material claims.
- Disconfirmation searches for evidence that would change or reject a conclusion.
- A claim table records statement, status, source, owner, freshness, counter-evidence, and allowed use.

### Market, pain, and requirement research

- Jobs-to-be-Done defines situation, progress, and current alternative.
- Forcing-moment analysis separates push, pull, habit, and anxiety.
- Five Whys and pain-chain analysis trace symptom → mechanism → decision impact.
- A ninety-day story turns desired progress into observable milestones and responsibilities.
- Market/account evidence separates target universe, company fit, person-role currentness, trigger, and demand proof.
- Requirements-to-acceptance converts evidence into versioned requirements, non-goals, exceptions, and objective checks.

A public signal is not pain; attention is not demand; a modeled scenario is not an observed result.

### Outreach

Company qualification and person qualification are different gates. An outreach packet includes current company-fit evidence, current person/role evidence, stage reconciliation, public evidence grade, pain → mechanism → question chain, source-grounded message, channel/send checklist, and exact approval or no-send reason.

The planner and copy maker never send. Pavlo may send only one exact approved message and must read back the result.

### Copy, creative, design, and implementation

Copy and design share one approved brief and claim table. Creative work includes the content job, audience, evidence-backed hierarchy, approved/prohibited claims, rights boundary, channel dimensions, editable source, phone-scale/wrapping/contrast/accessibility checks, publication packet, and rollback.

The designer produces three substantially different directions before convergence when material judgment is required. The maker supplies an editable artifact and responsive implementation. The verifier checks exact breakpoints, wrapping, forms, perimeter spacing, keyboard path, contrast, reduced motion, and visual regression. The independent reviewer reviews the frozen candidate; the maker performs repairs.

### Reporting

Reports distinguish observed versus modeled, numerator and denominator, current versus stale, configured versus tested versus live, eligible versus approved versus executed versus accepted, and the remaining gap/next safe action.

## 6. Employee onboarding and daily work

![Employee onboarding and teamwork](../project/assets/architecture/onboarding-teamwork-flow.png)

*The top row is the employee journey, the middle row shows specialist responsibilities, and the bottom row shows daily control, manager interrupts, maker/reviewer repair, and the maintained knowledge loop. Open the [editable SVG](../project/assets/architecture/onboarding-teamwork-flow.svg).*

First 30 minutes:

1. Read role purpose, owned outputs, forbidden actions, source boundary, and escalation.
2. Trace one current requirement to its source, owner, freshness, and acceptance.
3. Complete one reversible mission with a different reviewer and exact readback.

Daily mission card:

- why this work matters;
- one observable output;
- current requirement version;
- allowed and excluded evidence;
- owner, maker, reviewer;
- exact files/targets;
- checks;
- blocker/stop condition;
- next handoff.

Taras provides deterministic contextual guidance in the public dashboard. In a live approved runtime, the same role may receive a role-safe perception capsule. Taras cannot become a separate source of truth, monitor employees, grant permission, or bypass the manager/reviewer interrupt.

Onboarding outcome measures ask whether the employee can explain why, find the governing source, distinguish fact from gap, perform the safe action, escalate uncertainty, and record readback.

## 7. Skill lifecycle and cleaning

Lifecycle:

`discovered → quarantined → inspected → deduplicated → normalized → fixture-tested → reviewed → allowlisted → assigned → observed → updated → deprecated → removed`

Required checks cover identity/provenance, license, static risk, instruction injection, secrets/paths, duplicate scope, role fit, sandbox fixture, failure/rollback, version pin, and independent review.

Skill Spectre is the static package-inspection job before allowlisting. Public evidence currently records low-risk static scans for two ArchFlow skills; semantic scanning is not proved. A clean scan never authorizes automatic installation.

“Video Spectre” is represented only as the reusable inspection pattern—inventory, isolate, scan, normalize, fixture-test, compare, approve, roll back—for media or large generated-skill packs. No public tool execution is claimed without a receipt.

Skills update after repeated use/failure or an upstream version change. Automatic installation and automatic rewrite remain disabled.

## 8. Dashboard as the non-technical operating surface

| View | Job |
|---|---|
| Today | Current mission, role, evidence boundary, reviewer, next safe action, and Taras guidance |
| Work | Create and drive one browser-local mission and export its review packet |
| Knowledge | Explain layers, tools, parameters, diagrams, methods, and skill lifecycle |
| Team | Search all roles and inspect adaptive workflow packs and handoffs |
| Review | Trace evidence to requirements, validation, independent review, receipts, and promotion |
| Set up | Configure bounded source, LlamaIndex, TurboVec, checkpointer, and loopback proposals |

There is no standalone Jarvis brain. `/jarvis` redirects to the embedded Today guidance.

Browser storage is for drafts/examples only. The dashboard fetches fixed public JSON contracts, accepts no secrets, allows only its own origin or HTTP loopback as a bridge proposal, does not contact the bridge automatically, exports JSON review packets, and never activates a provider or writes externally.

Default parameters:

```json
{
  "llamaindex": {
    "chunk_size": 800,
    "chunk_overlap": 120,
    "lexical_top_k": 5,
    "vector_top_k": 5,
    "rerank_top_k": 5,
    "final_source_limit": 8,
    "require_source_paths": true,
    "require_exact_read_for_action": true,
    "fallback_to_lexical": true
  },
  "turbovec": {
    "candidate": false,
    "bit_width": 4,
    "default_backend_changed": false
  },
  "langgraph": {
    "public_checkpointer": "none",
    "thread_id": "case_id"
  },
  "crewai": {
    "process": "sequential",
    "memory": false,
    "cache": true,
    "planning": false,
    "maximum_parallel_tasks": 3
  },
  "provider": "disabled",
  "writeback": "disabled"
}
```

## 9. Public, local, private, and secret boundaries

| Class | Examples | Storage |
|---|---|---|
| Public portable | Contracts, schemas, synthetic fixtures, docs, editable diagrams | Git |
| Local generated | Indexes, embeddings, graph outputs, browser drafts, checkpoints | Ignored runtime |
| Private knowledge | Internal sources, decisions, mappings, private vault notes | Approved local/private system |
| Secrets | Tokens, credentials, cookies, passwords | App-native auth or OS keychain only |

The public repository never requires a private vault. Optional local Obsidian/Orbit adapters return only bounded references and sanitized reviewed conclusions across the boundary.

Obsidian community plugins are privileged local code. Review source, restrict and pin the plugin set, back up the vault, and preserve restricted-mode fallback. See [Obsidian plugin security](https://obsidian.md/help/plugin-security).

## 10. Verification and release gates

```bash
python3 project/system/validate_system.py
python3 project/scripts/generate-dashboard-data.py
node --check project/dashboard/app.js
python3 project/scripts/dashboard-static-smoke.py --skip-browser
```

Full browser smoke:

```bash
python3 project/scripts/dashboard-static-smoke.py
```

Release requires parsed JSON/YAML/SVG, passing validator fixtures, all six rendered routes, no clipped or overlaid interface text, no horizontal page overflow, keyboard-visible forms, independent review, exact Git target approval, and remote readback after push.

## 11. Primary framework references

- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [LangGraph subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
- [LlamaIndex ingestion pipeline](https://docs.llamaindex.ai/en/v0.10.17/module_guides/loading/ingestion_pipeline/root.html)
- [LlamaIndex documents and nodes](https://docs.llamaindex.ai/en/v0.10.19/module_guides/loading/documents_and_nodes/root.html)
- [LlamaIndex router retriever](https://docs.llamaindex.ai/en/stable/api_reference/retrievers/router/)
- [CrewAI documentation](https://docs.crewai.com/)
- [Obsidian plugin security](https://obsidian.md/help/plugin-security)
- [TurboVec repository](https://github.com/RyanCodrai/turbovec)

## 12. Known gaps

- TurboVec needs a representative fixed 20-query benchmark and independent review before a default change.
- The public dashboard has no live checkpointer, provider, durable identity, team tenancy, or writeback.
- SQLite/PostgreSQL modes need target-environment migration and recovery proof.
- Orbit and Obsidian live state cannot be inferred from the portable repository.
- Generated Graphify evidence must be regenerated after source changes.
- Skill Spectre semantic scanning and a public Video Spectre execution are not proved.
- Dashboard configuration remains a proposal until an approved runtime validates and reads back exact settings.
