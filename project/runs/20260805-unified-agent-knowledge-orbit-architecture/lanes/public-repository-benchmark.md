# Public Repository Benchmark for an Operable Knowledge Agent

Date: 2026-08-05
Mode: QUICK research brief, adapted to software-repository research
Access date for every external source: 2026-08-05
Status: maker-lane recommendation; integration and independent review remain pending

AI disclosure: this brief was produced with AI-assisted research tools. Repository claims were checked against current first-party repository pages or official documentation. No repository was cloned, executed, or security-audited in this lane.

## Research question and scope

> Which current public repositories and official documentation patterns offer the strongest reusable precedents for an operable, local-first, source-grounded onboarding and action-support agent with bounded roles, retrieval, review gates, private configuration, contributor guidance, architecture visuals, examples, tests, and a clean-clone quickstart?

**FACT:** The active ArchFlow public repository already establishes a provider-disabled clean-clone demo, a public/private boundary, browser-local review packets, bounded retrieval, maker/reviewer separation, and explicit truth states. The relevant local sources are `README.md`, `docs/quickstart.md`, `docs/architecture.md`, `docs/security-and-data-boundaries.md`, `CONTRIBUTING.md`, `SECURITY.md`, `project/operating-rules.md`, and the admitted run contract.

**In scope:** official LangGraph, LlamaIndex, CrewAI, and Obsidian repositories/docs; four current open-source knowledge assistants; repository and documentation information architecture; deterministic examples/tests; visual grammar; an incremental adaptation path.

**Out of scope:** copying third-party implementation or artwork, evaluating model quality, running the reviewed systems, dependency installation, provider activation, private corpus ingestion, dashboard implementation, deployment, and license or security certification.

**Method:** inspect the default-branch repository map and official documentation; accept a repository claim only when the current first-party surface supports it; distinguish reusable patterns from ArchFlow-specific interpretation; disclose contradictions and unverified areas. All eight reviewed projects are implementation precedents, not endorsements or drop-in dependencies.

## Executive finding

**INTERPRETATION:** No single reviewed repository satisfies the complete ArchFlow contract. The strongest public design is a deliberate composition:

1. Use LangGraph's typed state, deterministic/agentic step split, persistence, and human interrupt model for the controller contract.
2. Use LlamaIndex's core-versus-integration separation and retrieval/evaluation documentation map for bounded source access.
3. Use CrewAI's file-based role/task declarations as authoring ergonomics, while adding ArchFlow authority, evidence, reviewer, and forbidden-action fields.
4. Use Obsidian's separate development-vault rule, minimal plugin manifest, build/lint workflow, and release compatibility files for the local adapter.
5. Use Khoj's multi-client/self-hosting route, Dify's visible workflow and end-to-end repository separation, AnythingLLM's component boundaries and explicit telemetry disclosure, and Open WebUI's scoped knowledge/RBAC model as product-operability references.

**HYPOTHESIS:** ArchFlow will be more trustworthy and easier to adopt if the first clean-clone success is a small provider-disabled onboarding fixture that produces a cited answer, a requirement-validation result, a review receipt, and a blocked-action receipt in under ten minutes. A large visual builder or full multi-user platform should follow only after that invariant is stable.

## Verified precedent matrix

| Precedent | Verified current pattern | Reusable ArchFlow pattern | Evidence strength |
|---|---|---|---|
| [LangGraph repository](https://github.com/langchain-ai/langgraph), [overview](https://docs.langchain.com/oss/python/langgraph/overview), [Graph API](https://docs.langchain.com/oss/python/langgraph/use-graph-api), [core tests](https://github.com/langchain-ai/langgraph/tree/main/libs/langgraph/tests) | **FACT:** The repository separates `docs/`, `examples/`, and `libs/`. Official docs describe mixing deterministic and agentic steps, typed state, persistence, human-in-the-loop control, and graph compilation checks. Core tests include interruption, persistence, retry, state, migration, serialization allowlist, subgraph, and time-travel coverage. | Make the controller a typed state machine; keep authority checks deterministic; make pause/resume and review transitions testable; keep runtime tests beside the controller package. | Strong: current repository plus current official docs and test tree. |
| [LlamaIndex repository](https://github.com/run-llama/llama_index), [framework docs](https://developers.llamaindex.ai/python/framework/), [local-model starter](https://developers.llamaindex.ai/python/framework/getting_started/starter_example_local/), [representative core test](https://github.com/run-llama/llama_index/blob/main/llama-index-core/tests/node_parser/test_markdown_element.py) | **FACT:** The repository separates core, integrations, instrumentation, utilities, docs, and scripts. The documentation navigation separates agents, RAG loading/indexing/querying/storing, evaluation, privacy/security, observability, and integrations. The repository README explicitly says official docs are updated more frequently. Core tests use mock models for deterministic parser checks. | Keep retrieval core small; isolate adapters; document ingestion, retrieval, evaluation, privacy, and observability separately; use mock/provider-disabled tests; publish authority and supersession markers because README/docs can drift. | Strong: current repository, docs map, and test file; the README/docs freshness contradiction is explicit. |
| [CrewAI repository](https://github.com/crewAIInc/crewAI), [quickstart](https://docs.crewai.com/en/quickstart), [Flows](https://docs.crewai.com/en/concepts/flows), [Crews](https://docs.crewai.com/en/concepts/crews), [tests](https://github.com/crewAIInc/crewAI/tree/main/lib/crewai/tests) | **FACT:** CrewAI distinguishes precise, stateful Flows from role-oriented Crews. Its current quickstart scaffolds a source package, per-agent configuration, crew/task configuration, state, and a saved artifact. Its tests include flow persistence, resumability, visualization, human feedback, guardrails, crew, task, knowledge, security, and skill areas. | Store roles and tasks as reviewable files; let one controller own state/order; retain explicit output paths; test persistence, review, and guardrails. | Strong: current repository, docs, and test tree. |
| [Obsidian sample plugin](https://github.com/obsidianmd/obsidian-sample-plugin), [build guide](https://docs.obsidian.md/Plugins/Getting%20started/Build%20a%20plugin), [manifest reference](https://docs.obsidian.md/Reference/Manifest), [submission guide](https://docs.obsidian.md/Plugins/Releasing/Submit%20your%20plugin), [plugin checklist](https://docs.obsidian.md/oo/plugin) | **FACT:** The official template keeps source, manifest, compatibility versions, build, lint, and release workflow visible. Official docs require development in a separate test vault to reduce data-loss risk and define manifest/release assets. The current package scripts expose build and lint but no test command. | Build the Obsidian adapter as a thin, versioned package; test only against a disposable fixture vault; treat release metadata and compatibility as contracts; add tests beyond the sample template. | Strong for template/build/release; explicit GAP for testing because the sample has no test script. |
| [Khoj repository](https://github.com/khoj-ai/khoj), [self-hosting](https://docs.khoj.dev/get-started/setup/), [chat and references](https://docs.khoj.dev/features/chat/), [development](https://docs.khoj.dev/contributing/development/), [privacy](https://docs.khoj.dev/privacy/) | **FACT:** Khoj's repository exposes `documentation/`, `src/`, `tests/`, Docker configuration, and a Python project. Official docs support self-hosting, local/offline model routes, Obsidian/Desktop/Web clients, synced knowledge, and reference notes in answers. Privacy docs disclose that relevant context may reach a cloud model when that model is selected and disclose telemetry. | Offer one local core with optional clients; keep citations visible; put privacy effects next to model choice; document install, upgrade, uninstall, and contribution checks. | Strong: current repository and official operations/privacy docs. |
| [Dify repository](https://github.com/langgenius/dify) | **FACT:** The current repository visibly separates API, web, CLI, agent runtime, Docker, docs, SDKs, packages, and end-to-end tests. Its README provides a Docker Compose quickstart, an `.env.example` path, workflow/RAG/agent/observability capabilities, and advanced configuration routing. | Make runtime components legible at the repository root; include an end-to-end test lane; give config a documented template and one canonical index. | Moderate-to-strong: current first-party repository/README; no runtime execution in this review. |
| [AnythingLLM repository](https://github.com/Mintplex-Labs/anything-llm), [self-hosted terms](https://github.com/Mintplex-Labs/anything-llm/blob/master/TERMS_SELF_HOSTED.md) | **FACT:** The repository separates frontend, server, collector, Docker, embed, browser extension, and related components. It describes local-first document/agent workflows, source citations, multiple users in the Docker edition, and telemetry with an opt-out. The self-hosted terms describe user-managed infrastructure and an air-gap route when local providers are used. | Separate collection from retrieval/runtime and UI; document persistence, telemetry, and opt-out behavior in the quickstart rather than hiding it in policy pages. | Strong for current repository/component and disclosure patterns; product claims were not independently performance-tested. |
| [Open WebUI repository](https://github.com/open-webui/open-webui), [Workspace model](https://docs.openwebui.com/features/workspace/), [Knowledge](https://docs.openwebui.com/features/workspace/knowledge/), [permissions](https://docs.openwebui.com/features/authentication-access/rbac/permissions/) | **FACT:** The repository visibly separates backend, frontend source, docs, scripts, static assets, tests, environment example, troubleshooting, and multiple deployment profiles. Official docs distinguish focused RAG, full context, semantic query, exact/line retrieval, scoped knowledge, export/sync, and RBAC. The permissions guide warns that authoring/importing executable tools is equivalent to root-level server access and recommends least privilege. | Expose semantic and lexical retrieval as distinct tools; preserve path/line evidence; scope knowledge by role; classify executable tools as high authority; add troubleshooting and deployment profiles only after local proof. | Strong: current repository and official knowledge/security docs. |

## Cross-source synthesis

### 1. Controller, roles, and gates

**FACT:** LangGraph explicitly supports deterministic and agentic steps plus human state inspection; CrewAI recommends state/order in a Flow while crews perform bounded work; both repositories expose substantial tests for state, persistence, interruption, feedback, and guardrails ([LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview), [CrewAI quickstart](https://docs.crewai.com/en/quickstart), [LangGraph tests](https://github.com/langchain-ai/langgraph/tree/main/libs/langgraph/tests), [CrewAI tests](https://github.com/crewAIInc/crewAI/tree/main/lib/crewai/tests)).

**INTERPRETATION:** ArchFlow should not expose “agents” as independent personas. It should expose one admitted workflow whose role steps are data-driven contracts. Each role contract needs: purpose, inputs, allowed sources, allowed tools, forbidden actions, required output schema, reviewer, evidence fields, stop condition, and promotion authority. The controller, not the role, owns transition and retry state.

**GAP:** CrewAI's role/goal/backstory ergonomics do not by themselves express ArchFlow's public/private boundary, claim authority, freshness, contradiction state, or external-action approval. Those fields must remain ArchFlow extensions rather than inferred framework behavior.

### 2. Retrieval and source grounding

**FACT:** LlamaIndex documents ingestion, indexing, querying, storage, evaluation, local models, privacy, and observability as separate areas. Open WebUI documents semantic query, exact/line retrieval, scoped knowledge, and citations as complementary behaviors. Khoj documents reference notes in answers and local/client knowledge sync ([LlamaIndex docs](https://developers.llamaindex.ai/python/framework/), [Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/), [Khoj chat](https://docs.khoj.dev/features/chat/)).

**INTERPRETATION:** The public implementation should expose two retrieval primitives rather than one opaque “RAG” call:

- `search_concept`: semantic candidate retrieval, always returning source ID, repo-relative path, chunk/section identity, and score.
- `find_exact`: lexical/path/line retrieval for identifiers, requirement IDs, decisions, versions, and contradiction checks.

Synthesis should accept evidence only after the source-boundary and authority filter. A citation proves where text came from; it does not prove that the source is current, approved, authoritative, or non-contradictory.

**HYPOTHESIS:** A two-step `semantic candidate -> exact source read` trace will be easier to audit and test than a single synthesized-answer call, especially for onboarding questions and requirement validation.

### 3. Local-first and private configuration

**FACT:** Khoj, AnythingLLM, Dify, and Open WebUI all document self-hosted or local operating routes, but their quickstarts vary in prerequisites, environment configuration, local/cloud options, and telemetry. Obsidian explicitly requires a separate development vault to protect primary data ([Khoj self-hosting](https://docs.khoj.dev/get-started/setup/), [AnythingLLM repository](https://github.com/Mintplex-Labs/anything-llm), [Dify repository](https://github.com/langgenius/dify), [Open WebUI repository](https://github.com/open-webui/open-webui), [Obsidian build guide](https://docs.obsidian.md/Plugins/Getting%20started/Build%20a%20plugin)).

**INTERPRETATION:** “Local-first” should be an observable profile, not a slogan. The default ArchFlow profile should:

- start with `provider_mode: disabled`;
- accept only a bundled synthetic fixture;
- write runtime data to an ignored local directory;
- treat `.env.example` as names and comments only, never values;
- fail closed when a private adapter target is missing or outside the allowlist;
- disclose telemetry as `none`, `disabled`, or `enabled` with a verification method;
- require a disposable test vault for the Obsidian adapter;
- include upgrade, uninstall, data-location, backup, and rollback instructions before any “operable” claim.

**GAP:** This benchmark does not verify an active local runtime, Orbit behavior, or an Obsidian adapter. Those belong to the private integration lane and integrator tests.

### 4. Repository navigation and contributor trust

**FACT:** The mature repositories consistently expose a root README, source packages, docs, contribution guidance, CI/config, and tests; several also expose `SECURITY.md`, examples, troubleshooting, releases, and environment templates. LlamaIndex explicitly warns that its README can lag official docs ([LlamaIndex repository](https://github.com/run-llama/llama_index)).

**INTERPRETATION:** ArchFlow needs one source-of-truth marker on every architecture/config document: `status`, `authority`, `updated_at`, `supersedes`, and `verified_by`. Navigation should separate what the system is, how to run it, how to adapt it, and what is merely planned.

## Anti-patterns to reject

1. **Provider keys before first success.** Current LangGraph and CrewAI tutorials commonly demonstrate provider-backed agents, while ArchFlow's first-run acceptance test must remain deterministic and provider-disabled ([LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart), [CrewAI quickstart](https://docs.crewai.com/en/quickstart)).
2. **Persona-only role files.** Role, goal, and backstory are useful authoring aids, but they are not authority, scope, evidence, review, or stop contracts ([CrewAI Crews](https://docs.crewai.com/en/concepts/crews)).
3. **Treating persistence as permission or correctness.** Checkpoints and resumability preserve state; they do not authorize an external action or validate a claim ([LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence)).
4. **Treating a citation as truth.** RAG and reference notes improve traceability but do not establish source authority, owner, freshness, or contradiction resolution ([Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/), [Khoj chat](https://docs.khoj.dev/features/chat/)).
5. **Unbounded sync or whole-device ingestion.** Knowledge sync is a product capability in several assistants, not permission to broaden the ArchFlow corpus. Every adapter needs an explicit include/exclude manifest and dry-run receipt ([Khoj upload routes](https://docs.khoj.dev/data-sources/share_your_data/), [Open WebUI Knowledge](https://docs.openwebui.com/features/workspace/knowledge/)).
6. **Executable tools presented as ordinary skills.** Open WebUI's official RBAC guide treats tool authoring/import as root-equivalent. ArchFlow must visually and contractually separate instructions, read-only retrieval, deterministic transforms, and executable/external tools ([Open WebUI permissions](https://docs.openwebui.com/features/authentication-access/rbac/permissions/)).
7. **Hidden telemetry or cloud-context effects.** Khoj and AnythingLLM disclose telemetry and model-dependent privacy behavior. ArchFlow should place those disclosures beside setup and model selection, not only in policy text ([Khoj privacy](https://docs.khoj.dev/privacy/), [AnythingLLM repository](https://github.com/Mintplex-Labs/anything-llm)).
8. **Using the Obsidian sample as a complete quality bar.** It is a good build/release template, but its current package scripts have build and lint without tests. ArchFlow needs fixture-vault unit and integration tests ([sample package](https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/package.json)).
9. **Copying mature-platform breadth.** Dify, AnythingLLM, and Open WebUI have large frontend/backend/deployment surfaces. Their component separation is reusable; their full feature breadth is not the correct initial ArchFlow scope ([Dify repository](https://github.com/langgenius/dify), [AnythingLLM repository](https://github.com/Mintplex-Labs/anything-llm), [Open WebUI repository](https://github.com/open-webui/open-webui)).
10. **README and docs without authority states.** LlamaIndex's own README points users to more current docs. ArchFlow should encode supersession rather than expect readers to infer it ([LlamaIndex repository](https://github.com/run-llama/llama_index)).
11. **Screenshots as architecture source.** A screenshot is proof of appearance at one moment, not an editable or testable architecture. Store diagram source plus generated SVG and alt text.
12. **Copying third-party visual assets or code patterns without review.** This benchmark recommends concepts only. Any code reuse requires a separate provenance, license, security, and maintenance review.

## Proposed public repository map

**INTERPRETATION:** Preserve the existing public site and `project/` evidence during migration. Add a clean implementation surface first; do not perform a disruptive root rewrite in the architecture run.

```text
.
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── CHANGELOG.md
├── .env.example                 # names/comments only; no usable secrets
├── pyproject.toml               # one install, CLI, test, lint entry point
├── src/
│   └── archflow_knowledge_agent/
│       ├── cli/                 # provider-disabled demo and operator commands
│       ├── contracts/           # state, role, source, receipt schemas
│       ├── controller/          # admitted state graph and deterministic gates
│       ├── retrieval/           # lexical, semantic adapter interface, provenance
│       ├── knowledge/           # claims, requirements, decisions, contradictions
│       ├── review/              # maker/reviewer, policy, promotion checks
│       ├── adapters/
│       │   ├── filesystem/      # allowlisted, read-only default
│       │   └── obsidian/        # thin adapter; fixture vault in tests only
│       └── receipts/            # run, review, blocked-action records
├── config/
│   ├── profiles/                # public, provider-disabled profiles
│   ├── schemas/                 # machine-readable validation
│   └── examples/                # redacted config templates
├── contracts/
│   ├── roles/                   # role files, not runtime personas
│   ├── workflows/               # one governed operating workflow
│   └── policies/                # source, promotion, private boundary, tools
├── examples/
│   └── onboarding-mini/         # runnable synthetic example and expected receipts
├── fixtures/
│   ├── public/onboarding-mini/
│   └── adversarial/             # stale, contradiction, missing-owner, secret-like
├── tests/
│   ├── unit/
│   ├── contract/
│   ├── retrieval/
│   ├── integration/
│   ├── privacy/
│   ├── golden/
│   └── clone_smoke/
├── docs/
│   ├── index.md
│   ├── quickstart.md
│   ├── architecture/
│   ├── concepts/
│   ├── guides/
│   ├── reference/
│   ├── operations/
│   ├── security/
│   ├── testing.md
│   └── troubleshooting.md
├── assets/diagrams/
│   ├── source/                  # Mermaid/D2/Graphviz text source
│   ├── generated/               # deterministic SVG
│   └── alt/                     # text descriptions
├── scripts/                     # thin wrappers; no hidden authority
├── project/                     # existing contracts/evidence during migration
├── wiki/                        # reviewed public durable memory
└── .local/                      # ignored runtime/config/cache/fixture outputs
```

### Canonical workflow placement

One workflow should be visible in both `contracts/workflows/knowledge-agent.yaml` and `docs/architecture/operating-workflow.md`:

```text
admit request
  -> validate authority and source boundary
  -> assemble stable context
  -> retrieve semantic candidates and exact evidence
  -> requirements-and-market-research role
  -> role-specific candidate work
  -> deterministic requirement/decision validation
  -> independent evidence and privacy review
  -> approve, repair, block, or escalate
  -> public promotion candidate or private handoff
  -> receipt and measured next action
```

The `requirements-and-market-research` role is one bounded step, not a parallel architecture. It may discover and structure evidence; it may not promote a claim, authorize a tool, or approve its own output.

## Required public documentation

| Document | Reader question | Required content |
|---|---|---|
| `README.md` | What is this, what works now, and where do I start? | One-sentence promise, truth/status table, three reader paths, five-minute provider-disabled demo, architecture thumbnail, security boundary, docs index. |
| `docs/index.md` | Where is the authoritative page for my task? | Tutorial, concept, guide, reference, operation, security, and contribution navigation; status/supersession legend. |
| `docs/quickstart.md` | Can a clean clone prove the core without secrets? | Prerequisites, install, fixture demo, expected files/receipts, verification, uninstall, exact non-capabilities. |
| `docs/architecture/overview.md` | How do layers and boundaries fit? | Seven layers, public/private seam, controller/role separation, retrieval and durable-memory distinction, current versus planned. |
| `docs/architecture/operating-workflow.md` | What happens to one request? | State transitions, gates, repair cap, terminal states, receipt fields, sequence diagram. |
| `docs/concepts/knowledge-record.md` | What makes an answer source-grounded? | Evidence path, authority, owner, freshness, requirement/decision links, contradictions, approval state. |
| `docs/concepts/role-contract.md` | What may a role do? | Input/output, source/tool allowlist, forbidden actions, reviewer, stop rule, examples. |
| `docs/guides/onboarding-agent.md` | How do I adapt this to one employee role? | Bounded corpus, questions, first useful task, action validation, escalation, update lifecycle. |
| `docs/guides/obsidian-local-adapter.md` | How do I connect a vault safely? | Disposable test vault, read-only default, include/exclude paths, no secret persistence, rollback/uninstall, compatibility. |
| `docs/guides/adapt-a-project.md` | How do I replace the synthetic fixture? | Source inventory, authority matrix, config copy, validation queries, review gate, acceptance test. |
| `docs/reference/configuration.md` | What may I configure and where? | Public profiles, ignored local config, env names, defaults, fail-closed rules, config precedence. |
| `docs/reference/schemas.md` | What are the machine contracts? | Source, claim, requirement, role, run, review, approval, and promotion receipts. |
| `docs/security/data-boundaries.md` | What stays public, private, local, or externally gated? | Threat model, tool authority classes, model/context disclosure, logging/telemetry, incident reporting. |
| `docs/testing.md` | What proves a change? | Test pyramid, fixture rules, deterministic commands, privacy cases, expected receipts, CI matrix. |
| `docs/troubleshooting.md` | What failed and how do I recover? | Missing adapter, stale index, invalid source ID, blocked approval, corrupted local state, full uninstall. |
| `examples/README.md` | Which examples are safe to run? | Synthetic-only declaration, scenario index, expected output, known non-proof. |

**INTERPRETATION:** Every page should begin with a compact truth header: `status`, `authority`, `last_verified`, `applies_to`, and `supersedes`. Every command block should say whether it reads, writes locally, starts a service, invokes a provider, or writes externally.

## Architecture diagram set and visual grammar

### Required diagram set

1. **System context and public/private seam:** people, public repository, local private configuration, Obsidian adapter, optional provider/external gates.
2. **Seven-layer knowledge-agent tower:** Authority; Context; Retrieval; Requirements/Research; Bounded Roles; Review/Promotion; Measurement.
3. **One-request sequence:** operator, controller, retriever, role, independent reviewer, durable memory, external gate.
4. **Knowledge-record lifecycle:** discovered -> classified -> cited -> reconciled -> reviewed -> promoted -> stale/superseded.
5. **Role and authority map:** read-only retrieval, deterministic transform, candidate writer, reviewer, integrator, external-action role.
6. **Clean-clone proof path:** clone -> install -> synthetic fixture -> cited response -> validation -> blocked action -> receipts.
7. **Dashboard integration plan:** a dashed future adapter from reviewed receipts to a read-only status view; no implementation or live-runtime implication.

### Visual grammar

**FACT:** Current ArchFlow public visuals use a dark architectural field, ivory content, fine grid/hairlines, amber-gold illuminated arches and paths, layered/tower composition, restrained teal status marks, and numbered stages. Local primary references include `styles.css`, `project/dashboard/styles.css`, `project/content/assets/generated/growth-team-onboarding-knowledge-arch-20260728.png`, and `project/runs/20260717-tower-viewport-fit/desktop-stage-07.png`.

**INTERPRETATION:** Translate that style into a deterministic documentation system, not third-party artwork:

- charcoal/blue-black for the operating envelope;
- ivory for public-safe knowledge and readable text;
- amber/gold for flow, checkpoints, and human review;
- teal for verified/accepted state;
- muted blue for retrieval or configured infrastructure;
- rust/red only for blocked or unsafe state;
- nested arches or stacked bands only for stable architectural layers;
- rectangles for roles/artifacts, circles for states/receipts, double vertical lines for approval gates;
- solid lines for implemented/proved routes, dashed lines for planned routes, dotted lines for optional adapters;
- labels plus shape/stroke differences so meaning never depends on color alone.

Use a maximum of seven primary layers, one left-to-right reading direction, 16 px minimum diagram text, short labels, and an alternate narrow/mobile rendering. Store editable text source, generated SVG, and a plain-language alt description. Add a caption with `scope`, `status`, `version`, and `not proof of` wording. Avoid screenshots as the canonical diagram and avoid decorative 3D art in reference pages.

## Examples, fixtures, and test layout

### Golden onboarding fixture

`examples/onboarding-mini/` should contain only synthetic public-safe material:

- a short product brief;
- one approved requirement with ID and owner;
- one current decision with rationale and review date;
- one stale note that contradicts the decision;
- one role handbook;
- one proposed first-week action;
- a source manifest and expected review receipts.

The demo must answer one onboarding question, validate one proposed action against the requirement and decision, expose the contradiction, refuse one unapproved external action, and write deterministic JSON/Markdown receipts under `.local/demo/`.

### Adversarial fixtures

| Fixture | Expected behavior |
|---|---|
| Missing source path | Reject as evidence. |
| Stale authoritative-looking note | Mark stale; do not silently prefer it. |
| Contradictory current sources | Return GAP and require reconciliation. |
| Missing owner or review trigger | Produce candidate only; block promotion. |
| Secret-shaped value | Redact/stop; fail public-safety test. |
| Path outside allowlist | Refuse before read. |
| Provider enabled without approval | Refuse before invocation. |
| External write request | Produce approval packet only. |
| Maker self-approval | Fail review contract. |
| Interrupted run | Resume from declared state without repeating an irreversible step. |

### Test gates

1. **Unit:** schemas, state transitions, source filtering, contradiction logic, receipt serialization.
2. **Contract:** role/config/workflow schema validation and public/private promotion rules.
3. **Retrieval:** lexical baseline, semantic adapter parity when available, path/line provenance, no-private-source results.
4. **Integration:** provider-disabled end-to-end fixture, Obsidian disposable-vault read-only fixture, pause/resume, repair cap.
5. **Privacy/security:** secret patterns, path escape, tool authority, log redaction, ignored local state.
6. **Golden:** stable Markdown/JSON receipts for onboarding question, action validation, contradiction, and blocked action.
7. **Clone smoke:** new temporary checkout, documented install, demo, tests, uninstall; no pre-existing env, cache, model, or private vault.
8. **Docs/visual:** link check, code-block smoke, schema references, diagram source/build parity, alt-text presence.

**HYPOTHESIS:** The clone-smoke and adversarial fixtures will provide more trust than a larger example gallery. Add examples only when each demonstrates a distinct contract and has an expected receipt.

## Incremental adaptation path

### Phase 0 — Truth and navigation

- Add current/planned truth labels and one docs index.
- Declare canonical architecture, workflow, role, and source-policy files.
- Keep existing `project/` evidence in place.

### Phase 1 — Provider-disabled core

- Add typed source, claim, requirement, role, review, and receipt schemas.
- Implement lexical retrieval and exact source read over the synthetic fixture.
- Add the single admitted workflow and deterministic review gates.
- Ship the golden fixture, clone smoke, and privacy tests.

### Phase 2 — Thin private/local adapter

- Add the Obsidian adapter interface and disposable-vault tests.
- Keep real target/configuration outside the public repository.
- Default to read-only discovery and dry-run receipts; require a separate gate for mutation.

### Phase 3 — Optional retrieval/model adapters

- Add LlamaIndex behind the retrieval interface only after lexical baseline tests.
- Keep provider-disabled mode canonical.
- Benchmark semantic recall, provenance completeness, privacy, latency, and fallback before changing defaults.

### Phase 4 — Contributor and release hardening

- Publish contributor, security, compatibility, migration, upgrade, uninstall, and release guides.
- Add deterministic diagram generation and CI parity checks.
- Perform license/provenance review for every adopted dependency or copied snippet.

### Phase 5 — Dashboard plan gate

- Define a read-only projection over sanitized run/review receipts.
- Do not implement until the CLI/fixture truth states and receipt schemas are stable.
- Require the UI to distinguish configured, prepared, executed, reviewed, proved, gated, and stale.

## Contradictions and unresolved gaps

- **FACT:** Mature official quickstarts often optimize for fast provider-backed or Docker-backed success; ArchFlow requires a zero-secret provider-disabled first proof. This is an intentional divergence, not a missing feature ([LangGraph quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart), [CrewAI quickstart](https://docs.crewai.com/en/quickstart), [Dify repository](https://github.com/langgenius/dify)).
- **FACT:** LlamaIndex says its README may lag its docs. ArchFlow therefore needs explicit authority/supersession metadata rather than one undifferentiated docs folder ([LlamaIndex repository](https://github.com/run-llama/llama_index)).
- **FACT:** Obsidian's sample provides build/lint/release scaffolding but no test script. ArchFlow must supply its own disposable-vault test harness ([sample package](https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/package.json)).
- **FACT:** Self-hosted assistants may still have optional telemetry or cloud-provider routes. “Self-hosted” alone is insufficient evidence that no data leaves the machine ([Khoj privacy](https://docs.khoj.dev/privacy/), [AnythingLLM repository](https://github.com/Mintplex-Labs/anything-llm)).
- **GAP:** This review did not establish that any assistant natively models ArchFlow's complete evidence tuple: authority, owner, freshness, contradictions, requirement/decision references, approval state, and receipts.
- **GAP:** No repository was checked out at an immutable commit. Default-branch structure can change after the access date.
- **GAP:** No comparative license determination was made. The reviewed repositories use different licenses and terms; pattern adoption does not authorize code copying. Relevant first-party license files include [LangGraph](https://github.com/langchain-ai/langgraph/blob/main/LICENSE), [LlamaIndex](https://github.com/run-llama/llama_index/blob/main/LICENSE), [CrewAI](https://github.com/crewAIInc/crewAI/blob/main/LICENSE), [Obsidian sample](https://github.com/obsidianmd/obsidian-sample-plugin/blob/master/LICENSE), [Khoj](https://github.com/khoj-ai/khoj/blob/master/LICENSE), [Dify](https://github.com/langgenius/dify/blob/main/LICENSE), [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm/blob/master/LICENSE), and [Open WebUI](https://github.com/open-webui/open-webui/blob/main/LICENSE).
- **GAP:** No dependency, security, performance, accessibility, or production-readiness audit was performed.
- **GAP:** Orbit integration identity/configuration and real Obsidian behavior are outside this lane.
- **GAP:** Dashboard work remains plan-only by contract.

## Recommendation to the integrator

**INTERPRETATION:** Adopt the proposed repository/doc/diagram structure selectively, with the following non-negotiable spine:

1. one typed admitted workflow;
2. role contracts as data, never personas as authority;
3. semantic candidate plus exact source read;
4. authority/owner/freshness/contradiction/requirement/review fields on every promoted knowledge record;
5. provider-disabled golden fixture as the clean-clone default;
6. separate maker, reviewer, and promotion receipts;
7. disposable-vault Obsidian tests and ignored private configuration;
8. source-controlled deterministic diagrams with truth-state legends;
9. dashboard projection only after receipt schemas are stable.

This is the smallest architecture that preserves the strongest verified precedents without inheriting the breadth, cloud assumptions, or implicit authority of the mature platforms reviewed.
