# ArchFlow Dashboard Operating Manual

Status: local/static dashboard operating document

## What this product is today

ArchFlow is a documentation-first, local-first framework for turning bounded project context into a reviewable knowledge report and then a governed agent-work handoff. The public repository can run by itself as a static site and contract library. It does not include a private corpus, credentials, device paths, customer information, a hosted autonomous agent service, or a live multi-user database.

The dashboard is an explanatory control surface. Jarvis is a text interface for preparing the same local reports. Neither page can make repository changes, launch a sub-agent, fetch or clone a repository, activate a provider, write a database, push Git, deploy, or write to Notion/Nexus/another external system. Those actions need an approved operator, a scoped task contract, current capability proof, and their own action-specific approval.

Start the dashboard at `/project/dashboard/#manual`. The short `/dashboard` route redirects to it. Jarvis is at `/jarvis`.

## The operating method

The product has two deliberately separate workflows:

```text
public-safe project reference or summary
  -> Knowledge Service local report
  -> human review / download
  -> Agent Control local handoff
  -> human review / download
  -> approved operator creates a scoped change
  -> validation and separate external-action approval
```

The split matters. Knowledge Service answers, “What do we know, what is missing, and what decision must this output support?” Agent Control answers, “Which bounded roles may work, with which skills/tools/sources, in which order, and who reviews the result?” Do not skip the first question by designing agents around unreviewed or unbounded context.

### Truth states

| State | Meaning | It does not mean |
|---|---|---|
| Configured | A file or browser setting exists. | A runtime ran. |
| Prepared locally | A browser-local report/packet was assembled. | A file, agent, provider call, or database write exists. |
| Reviewed | A named human accepts a bounded artifact. | A broader action is authorized. |
| Executed | A named command or runtime produced evidence. | Production approval. |
| Proved | A declared check passed within its stated scope. | Continuous availability or future safety. |
| Gated | Authority, capability, evidence, or safety is missing. | A reason to bypass the gate. |

## Admin and Guest preview

The Admin and Guest buttons are browser-local presentation modes. They are not authentication, RBAC, tenancy, individual durable memory, or a means to override any gate. The selected mode and local report context are stored only in browser localStorage on the current device and can be cleared by clearing local activity/browser storage.

| Mode | Intended use | Allowed local preparation | Held or unavailable |
|---|---|---|---|
| Admin preview | Operator learning, existing reviewed context, configuration drafting. | Knowledge report or Agent Control handoff. | Still cannot execute, write, or bypass approval. |
| Guest preview | Demonstrate the method to a public-repository user without an account. | Knowledge report first; then Agent Control from that local report. | API base/token controls, automatic model-catalog loading, repository fetching/cloning, private input, individual persistent memory. |

Enter either a public repository reference or a non-sensitive project label. A reference is a label for the report; this browser does not fetch, clone, index, inspect, or send it to a provider. Never enter a private link, local path, token, credential, raw private transcript, or customer data.

## Knowledge Service

Use Knowledge Service first whenever the operator needs a PRD, ICP brief, context capsule, evidence map, decision brief, backlog, research packet, or knowledge-update candidate.

### Required input contract

| Field | What to write | Why it is required | Stored / cannot do |
|---|---|---|---|
| Goal | One outcome and decision. | Defines a testable scope. | Browser-local report; cannot execute it. |
| Public reference or safe label | Public URL or non-sensitive name. | Identifies the subject without pretending it was read. | Browser-local report; cannot fetch it. |
| Allowed evidence | Exact approved summaries/files/categories. | Limits retrieval and claims. | Report boundary; cannot grant access. |
| Exclusions | Private, raw, stale, or out-of-scope material. | Prevents accidental ingestion. | Report boundary; cannot override a security policy. |
| Requested output | PRD, report, evidence map, role proposal, and so on. | Makes the handoff reviewable. | Proposal only. |
| Decision supported | The choice the reviewer must make. | Avoids generic “research” output. | Recorded as a review question. |
| Constraints and stop conditions | Safety, time, budget, authority, and delivery limits. | Makes escalation explicit. | Does not authorize external action. |
| Independent reviewer | Role or person accountable for review. | Keeps maker and checker separate. | Does not record a real approval. |

### Output contract

The current local report contains a stable report ID, goal, declared repository/project reference, source boundary, requested output, reviewer, constraints, and four classifications:

- **FACT** — directly supplied or independently evidenced statement.
- **INTERPRETATION** — reasoned reading of a fact; not evidence by itself.
- **HYPOTHESIS** — a testable proposition.
- **GAP** — missing evidence, authority, freshness, or capability.

It also states `review_required_not_executed` and records zero provider calls, agent launches, repository writes, database writes, and external writeback. Download the Markdown report for humans or the JSON handoff for tooling. Neither download is a repository patch.

### Knowledge files and retrieval cascade

Read the smallest relevant set in this order:

| Layer | Main configuration / knowledge file | Job |
|---|---|---|
| Public rules | `project/operating-rules.md` | Public boundary, approval policy, work communication, and proof semantics. |
| Stable context | `project/context/cag-core.yaml` and `project/context/README.md` | Reusable context assembled before task-specific material. |
| Project routing | `project/README.md` | Public mission, folder map, and local surfaces. |
| Durable memory | `wiki/index.md`, `wiki/memory.md`, `wiki/insights.md`, `wiki/log.md` | Navigation, reviewed facts, reusable interpretations, and chronological record. |
| Human rules | `wiki/rules/public-wikillm-contract.md` | What may be promoted and what must stay out. |
| Generated structure | `reference/graphify/` when present | Code/document relationship reference; never final human synthesis. |
| Bounded retrieval | `project/workflows/llamaindex-rag.yaml` | Approved corpus, chunking, hybrid candidate selection, lexical fallback. |
| Live-vault bridge | Nexus, when separately verified | Live Obsidian operations only after schema/capability discovery. |

LlamaIndex is a retrieval contract, not an instruction to ingest a whole device. The operator configures `include`, `exclude`, `chunk_size`, `chunk_overlap`, `query_mode`, `vector_top_k`, `lexical_top_k`, `rerank_top_k`, and `fallback_to_lexical` in `project/workflows/llamaindex-rag.yaml`. A retrieval score is never a factual claim. TurboVec or another vector acceleration layer remains optional and must be evaluated as a bounded performance experiment, not a source of truth.

## Agent Control

Use Agent Control only after Knowledge Service has produced a report you can review and download. The control workflow reuses the report ID and preserves its source boundary rather than copying raw source material into a new agent prompt.

### Required input contract

| Field | Why it matters |
|---|---|
| Knowledge report ID | Establishes the context and provenance handoff. |
| Goal and expected artifact | Defines a finish condition. |
| Required roles | Chooses the smallest useful role set. |
| Allowed packaged skills and methods | Prevents a broad, unreviewed tool load. |
| Allowed tools and sources | Keeps access bounded. |
| Parallel lanes and sole writer | Prevents conflicting edits. |
| Independent reviewer | Stops a maker from self-approving high-risk output. |
| Approval gates and stop conditions | Holds provider, Git, deployment, database, and external actions for explicit authority. |
| Proposed files | Makes a future change inspectable; every proposal is `created: false` until a human operator applies it. |

### Local state and stage display

The dashboard displays a sequence such as Intake, Context/Classification, Contract, Bounded Work, Review, Approval, and Packet. An active light/wiggle indicates that this browser is assembling a local review packet. A done mark means the local sequence has completed. It never means an external workflow is running.

A live state feed would need a sanitized `run_id`, `node_id`, state, timestamp, evidence reference, authority scope, and writeback state. Until those fields arrive from a verified runtime, the dashboard labels state as browser-local.

### Agent output and download

Agent Control produces a proposal with roles, allowed skills, review gate, stop conditions, and suggested files. Suggested files are marked with `created: false` and `requires_operator_review: true`. Download the Markdown report for a reviewer and JSON package for a future tooling integration. A separate approved operator must decide whether to create a run handout, update a role roster, or change a workflow YAML file.

## Workflow Editor

The editor is a detailed, browser-local design surface. Use it to make a proposed sequence visible before applying a repository patch.

| Field group | Configure | Effect | Persistence and limitation |
|---|---|---|---|
| Node identity | title, type, owner | Makes accountability visible. | localStorage only; does not assign a runtime. |
| Inputs and outputs | allowed sources, expected artifacts | Makes scope and handoff testable. | Downloaded packet; does not read sources. |
| Routing | condition, checkpoint, retry/revision cap, merge rule | Shows recovery and termination logic. | Draft only; does not start LangGraph. |
| Role controls | skills, tools, reviewer, output schema | Prevents persona-only agent definitions. | Draft only; does not create a worker. |
| Provider controls | provider mode, model route, approval gate | Documents a future controlled route. | Default is disabled; no browser secret or provider call. |
| Persistence and audit | memory target, trace target, run recorder | States intended durable record. | Does not write WikiLLM, database, or external tool. |

The two detailed screens have different jobs:

- **Knowledge Service / PRD-ICP Flow:** model the proposal from intake to evidence, review, approval, and client/reviewer output.
- **Agent Control / Workflow Editor:** model command classification, role contract, bounded work, independent review, merge, approval, and durable handoff.

Use **Validate** before export. Export creates a local packet, not a repository change. Use **Submit review packet** only for a separately available guarded API review; that endpoint must still report provider/writeback as disabled unless a later server-side gate is proven.

## Dashboard configuration

The configuration page exposes browser-local candidates. It is not a secret manager or production configuration system.

| Area | Versioned configuration point | Key parameters | Operational consequence |
|---|---|---|---|
| Viewer/activity | browser localStorage | viewer mode, shared report state, selected architecture | Changes only this browser's preview and handoff context. |
| Prompt candidates | dashboard Configuration page | chain name, model policy, memory policy, normal/interview/reviewer prompts | Export for review; does not change an application prompt. |
| API base | dashboard/Jarvis localStorage | same-origin or HTTP loopback origin | Can check guarded health/review endpoints; cannot hold a provider key or authorize calls. |
| LangGraph | `project/workflows/langgraph-controller.yaml` | node owner, route condition, checkpoint, revision cap, approval rule | Defines a reviewed graph contract after YAML validation. |
| LlamaIndex | `project/workflows/llamaindex-rag.yaml` | corpus boundary, chunking, hybrid retrieval, fallback | Controls candidate selection; not truth or ingestion authority. |
| CrewAI | `project/workflows/crewai-crew.yaml` | role/task examples, process/memory/cache flags | Documents a role fixture; not proof of a default runtime. |
| Roles/skills | `project/agents/agent-roster.yaml`, `project/agents/skills-by-agent.md` | role, methods/packages, outputs, forbidden actions | Defines work contracts and visibility, not agent activation. |

Never place a token, secret, personal value, local path, private URL, raw transcript, or customer document in the dashboard configuration or its download. Provider/server values remain local environment or server configuration and need separate ownership and security review.

## Jarvis operating guide

Jarvis is the conversational entry point to the same two-stage flow. Its initial response should be an architecture report in the chat, followed by a Download report or Download handoff option.

1. Choose **Guest preview** for a public demonstration or **Admin preview** for local operator drafting. This is not a login.
2. Choose **Knowledge Service**.
3. Complete Goal, public repository reference/safe project label, allowed evidence and exclusions, requested output, independent reviewer, and constraints/stop conditions.
4. Press **Prepare local report**. Read the report ID, classifications, and runtime boundary in chat.
5. Download the report. Review it with a human before promoting knowledge or designing implementation.
6. Choose **Agent Control** and reuse the local report context.
7. Describe the required roles, allowed skills/tools/sources, expected files/artifacts, independent reviewer, approval gates, and stop conditions.
8. Download the local handoff and ask an approved operator to perform any real work.

Use this prompt template for Knowledge Service:

```text
Goal:
Public repository reference or safe project label:
Allowed evidence:
Excluded/private material:
Requested output:
Decision this output must support:
Constraints and stop conditions:
Independent reviewer:
```

Use this addition for Agent Control:

```text
Use knowledge report ID:
Goal and expected artifact:
Required roles:
Allowed packaged skills and project methods:
Allowed tools and sources:
Parallel lanes and sole writer:
Independent reviewer:
Approval gates and rollback/stop condition:
Suggested files for operator review:
```

### Token, API base, model, and provider controls

- **Owner token:** visible only in Admin preview. It is held in tab memory, must never be a provider key, and is sent only to an approved same-origin/loopback guarded API route when an operator explicitly requests that route.
- **API base:** same origin or an HTTP loopback address only. This restriction prevents a local browser setting from sending packet content to an arbitrary host.
- **Model cards:** route candidates, not enabled execution. A displayed model does not prove availability, spending authority, or a provider call.
- **Public catalog:** loads only after the explicit “Load public model catalog” action in Admin preview. Guest preview does not load it automatically.
- **Provider acknowledgement:** an optional guarded API review acknowledgement, not replay protection or authorization. The optional request sends only a guarded status descriptor, not the local report body, project reference, source boundary, or chat history. Provider execution remains server-gated and must not be inferred from a local report.

## Public skill catalog

The repository packages only the following public skill contracts. It deliberately does not copy an operator's private/global skill inventory. A plain method name in the role roster is a checklist unless a task contract maps it to a reviewed package.

| Packaged skill | Purpose and trigger | Primary users | Boundaries |
|---|---|---|---|
| `arcagcom` | Coordinate active public work, claims, handoffs, and merge gates. | All public lanes. | Public-safe log only; no external authority. |
| `archflow-agent-control` | Build a role/task/gate handoff from a reviewed knowledge report. | Goal Architect, Integrator, Watchdog, dashboard control. | No agent launch, file creation, provider, or external action. |
| `archflow-architecture-operator` | Design architecture layers, roles, tools, loops, evidence, and adoption gates. | Goal/Architecture roles. | Design does not activate tools/providers. |
| `archflow-e1-runtime-guard` | Check the declared runtime spine before public Git publication. | AF Tools, publisher. | Evidence check; no deployment authority. |
| `archflow-knowledge-service` | Produce a source-bounded knowledge report before implementation design. | AF Context, AF Knowledge, PRD role. | No broad ingestion, provider, or automatic memory promotion. |
| `archflow-task-breakdown` | Turn a bounded outcome into staged tasks, gates, checks, and handoff. | AF Manager, Task Translator. | Does not create external tasks by itself. |
| `archflow1` | Apply dashboard/Jarvis/provider/Railway boundary rules. | Dashboard/Jarvis lanes. | No live-runtime claim without proof. |
| `daily-public-project-review` | Run daily public project/skill/RAG retrospective. | Scheduled review lane. | Low-churn review only. |
| `evening-skill-registry-update` | Check registry/hook drift and update only when justified. | Maintenance lane. | No automatic unsafe skill adoption. |
| `outquestions` | Capture unresolved decisions, risks, and next-stage gates. | Manager, review, knowledge, publisher. | Questions are not approvals. |
| `priority-task-operator` | Rank tasks and prepare one priority handoff. | Operator/maintenance lane. | Ranking does not grant execution authority. |
| `task-handout` | Produce readable continuity handoffs and run-closeout context. | Integrator, manager, knowledge, publisher. | Does not apply files or external updates. |

Documentation-reference counts in the dashboard are not usage counts. Public-safe execution telemetry is not implemented. The generated catalog is `project/database/skill-catalog.json` and the role catalog is `project/database/role-catalog.json`.

## Role contracts

Roles describe responsibility, not a permanently active persona or model. The full machine-readable source is `project/agents/agent-roster.yaml`; the dashboard renders every declared role with its skills, expected outputs, and forbidden actions.

| Role group | Roles | Typical output | Expansion condition |
|---|---|---|---|
| Goal and integration | Goal Architect, Terra Integrator, Luna Worker, Architecture Operator | goal contract, integrated architecture, evidence packet, design/benchmark pack | bounded task contract, sole writer, independent reviewer. |
| Control and tools | Hermes Watchdog, AF Tools, AF Context, AF Manager | risk classification, tool readiness, context digest, PRD/task matrix | no provider/tool activation without current proof. |
| Product delivery | AF Discovery, AF PRD Architect, AF Task Translator, AF Research, AF Knowledge | discovery packet, PRD, task packet, evidence cards, memory candidate | use only approved sources and role-specific skills. |
| Communication and market | AF Copy, AF ABM Channel, AF Growth Evidence, AF Product Packaging Engineer | source-grounded copy, reviewed outreach packet, cohort evidence, installability package | no autonomous sending, invented metrics, or productization claim. |
| Review and publication | GloomyLord, AF Review, AF Publisher, Model-Efficiency Observer | visual proof, verdict, release packet, efficiency report | independent review, public safety, owner approval for release/action. |

Each role may use only the packages and method checklists named in its task contract. It may widen tool access only after a reviewed use case, provenance/license/security assessment, sandbox fixture, rollback path, updated role mapping, and independent AF Review.

## Data Lab and database boundary

The Data Lab queries generated `project/dashboard/data.json` with a deliberately small read-only SQL-like grammar: `SELECT columns FROM skills|roles|workflow_nodes|sources|runs LIMIT n`. It is not SQL, does not connect to a server, cannot join/mutate tables, and cannot access a private corpus.

| Storage layer | What it holds now | Write authority |
|---|---|---|
| Generated public catalog | skills, roles, workflow nodes, source links, public run summaries | data generator only. |
| Browser-local drafts | editor changes, local reports, local review packets | this browser only. |
| Private runtime store | not exposed in this public console | gated private operator runtime. |
| Future multi-user database | not implemented | requires authentication, tenancy, RBAC, audit, retention, backup, recovery, and migration proof. |

## FAQ

### Does the dashboard run agents continuously?

No. The animated state is a browser-local packet-preparation preview. A continuous monitor or agent runtime must publish current, verifiable event evidence before the UI may describe it as live.

### Can a guest create a knowledge base for a repository?

A guest can prepare and download a local Knowledge Service report for a public reference/safe summary. The current static page does not fetch, clone, ingest, or persist that repository. A real knowledge-base setup requires a separate approved corpus and operator runtime.

### Can Agent Control create files or sub-agents?

No. It proposes a role/task/file architecture. An approved operator may later create a scoped change after review, communication-file claim, checks, and any needed approval.

### How do I change the RAG setup?

Change the bounded LlamaIndex YAML, run the smallest relevant validation/fixture, record evidence, regenerate dashboard data, and have an independent reviewer assess the change. Do not treat vector search or TurboVec as a substitute for source governance.

### Where do I put my private project information?

Not in the public repository, dashboard, Jarvis download, or static browser configuration. Keep private material in an approved private boundary and create a sanitized, source-bounded handoff if an operator later needs it.

### Is the public skill list the complete local skill library?

No. It is the complete portable public allowlist for this repository. Private/device-specific skills are intentionally excluded until their provenance, license, portability, safety, and project use case are reviewed.

### What must be checked before a public Git push?

Run the public safety scan, workflow validation, JavaScript syntax check, dashboard static smoke, Jarvis contract/owner-guard smoke, generated JSON parse, and runtime guard. Then record the result in a run handout and obtain/confirm the separate Git-push authority.

## Local setup

From the public repository root:

```bash
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 8765
```

Open `http://127.0.0.1:8765/project/dashboard/#manual`. For the current verification command set, see `project/dashboard/README.md`. Regenerate `project/dashboard/data.json` whenever public workflows, role/skill contracts, reports, runs, or WikiLLM material changes.

## Current limitations

- Authentication and individual member memory are not implemented.
- Provider execution, durable spend ledger, and real external writeback are not implemented/proven by the static UI.
- The dashboard does not include a strategic planning page.
- A route/configuration file or a browser control is not proof of a continuously healthy hosted service.
- The public catalog intentionally excludes private skills and private knowledge.
