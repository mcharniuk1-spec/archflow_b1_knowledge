# ArchFlow

ArchFlow is a local-first, public-safe knowledge crew for employee onboarding, reliable daily work, research, specialist delivery, action validation, and maintained organizational knowledge.

It runs one case from:

`goal → source boundary → context → requirements → role work → validation → review/approval → readback → maintained knowledge`

PRDs, market studies, outreach packets, copy, designs, implementations, and reports are adaptive role outputs inside this flow—not separate architectures.

[![ArchFlow seven-layer responsive knowledge crew](project/assets/architecture/knowledge-crew-tower.png)](project/assets/architecture/knowledge-crew-tower.svg)

*Seven exact layers connect the public/private-safe knowledge spine on the left to employee and business outputs on the right. Select the image for the editable, full-resolution labeled SVG.*

## What you can use now

- A typed, provider-disabled Knowledge Case controller.
- Twenty-one responsibility roles with Ukrainian call names written in English letters and schema-backed inputs, output ownership, skill/tool ceilings, permission mode, reviewer route, and handoff.
- Ten adaptive workflow packs for onboarding, research, tasks, outreach, content, design, implementation, reporting, knowledge maintenance, and release.
- Explicit LlamaIndex, TurboVec, CrewAI, LangGraph, WikiLLM, Obsidian, Orbit, and Graphify boundaries.
- A responsive non-technical Crew Desk for local mission drafts, role/workflow inspection, review trace, configuration proposals, and JSON exports.
- Four editable architecture views with exact captions.
- Deterministic eligible/blocked/adversarial fixtures and public-safety checks.

The public default calls no model, ingests no private vault, performs no writeback, and executes no external action.

## Three-minute local start

```bash
git clone <your-repository-url> archflow
cd archflow
python3 project/system/validate_system.py
python3 project/scripts/generate-dashboard-data.py
python3 -m http.server 4173
```

Open:

- `http://127.0.0.1:4173/project/dashboard/#today` — current mission and onboarding guidance.
- `http://127.0.0.1:4173/project/dashboard/#work` — create a browser-local mission.
- `http://127.0.0.1:4173/project/dashboard/#knowledge` — layers, framework jobs, diagrams, methods, and skill lifecycle.
- `http://127.0.0.1:4173/project/dashboard/#team` — all roles and workflow packs.
- `http://127.0.0.1:4173/project/dashboard/#review` — trace, gates, receipts, and promotion.
- `http://127.0.0.1:4173/project/dashboard/#setup` — local bounded configuration proposals.

`/jarvis` is a compatibility redirect to Today. Guidance is embedded in the case; Jarvis is not a second brain or source of truth.

## Architecture views

| View | What it explains |
|---|---|
| [Seven-layer tower](project/assets/architecture/knowledge-crew-tower.svg) | Knowledge/database inputs, all layers, role control, and accountable outputs |
| [Input and perception](project/assets/architecture/context-input-flow.svg) | Stable CAG, source admission, document/node identity, LlamaIndex, TurboVec, exact reads, and the context capsule |
| [Output and receipts](project/assets/architecture/output-receipt-flow.svg) | Specialist candidates, requirement/authority checks, independent review, exact action, readback, and promotion |
| [Onboarding and teamwork](project/assets/architecture/onboarding-teamwork-flow.svg) | Employee journey, specialist responsibilities, manager interrupts, repairs, and learning |

<p>
  <a href="project/assets/architecture/context-input-flow.svg"><img src="project/assets/architecture/context-input-flow.png" width="49%" alt="ArchFlow input and context perception flow"></a>
  <a href="project/assets/architecture/output-receipt-flow.svg"><img src="project/assets/architecture/output-receipt-flow.png" width="49%" alt="ArchFlow output, review, and receipt flow"></a>
</p>
<p>
  <a href="project/assets/architecture/onboarding-teamwork-flow.svg"><img src="project/assets/architecture/onboarding-teamwork-flow.png" width="99%" alt="ArchFlow employee onboarding and teamwork flow"></a>
</p>

Connection language is process-specific:

- In the tower, blue source lines bind a database or knowledge capability to the layer that may use it; amber output lines show the accountable artifact that leaves that layer.
- In the input view, blue paths carry admitted rules, responsibilities, requirements, task queries, receipts, and gaps; violet paths are ranked retrieval/structural candidates; the exact-read gate is the mandatory evidence transition before action.
- In the output view, blue paths are specialist candidates, coral paths are validation/review/repair, amber paths are approval-bound action or decision delivery, and green paths begin only after verification/readback.
- In onboarding/teamwork, blue is the employee mission/context path, violet is specialist role contribution, coral is manager interrupt or maker-reviewer repair, and amber is accepted learning with maintained-knowledge lineage.

Colors never mean generic “govern / understand / create” stages. Every line terminates at a named source, role-owned artifact, gate, receipt, or knowledge outcome.

## Seven accountable layers

1. **Case authority and employee scope** — goal, role, data class, permission, risk, reviewer, done, and stop.
2. **Reviewed knowledge and source spine** — authority, ownership, currentness, supersession, allowlist, and exclusions.
3. **Bounded context perception** — stable CAG, LlamaIndex retrieval, optional TurboVec candidates, structural pointers, and exact reads.
4. **Adaptive role crew** — smallest responsible team with role-safe tasks, tools, prohibitions, reviewers, and handoffs.
5. **Specialist research and delivery** — onboarding, requirements, tasks, outreach, copy, design, implementation, and reports.
6. **Graph control, validation, and review** — typed state, reducers, checkpoints, interrupts, repairs, deterministic checks, and independent review.
7. **Receipts, outcomes, and maintained knowledge** — exact result/readback, employee learning, promotion, lineage, and freshness.

Read the [complete strategic architecture](docs/responsive-knowledge-crew-architecture.md).

## Framework responsibilities

| System | Exact job | Authority boundary |
|---|---|---|
| WikiLLM | Portable reviewed indexes, memory, insights, runs, issues, decisions, and log | Durable only after review/promotion |
| Obsidian | Optional private human semantic workspace | No automatic public copy; plugins are privileged local code |
| LlamaIndex | Allowlisted documents/nodes, metadata, routing, filtering, ranking, source return | Candidate evidence only |
| TurboVec | Optional 4-bit vector candidate behind the LlamaIndex adapter | Not the default; never replaces citations or lexical fallback |
| Orbit + Graphify | Definitions, references, paths, relationships, and likely impact | Structural evidence followed by exact reads |
| CrewAI | Role, task, knowledge-input, output, delegation, reviewer, and handoff contracts | No separate memory/state/permission |
| LangGraph | Case state, routes, reducers, interrupts, bounded repair, checkpoints, and terminals | Transition control, not knowledge truth |
| Crew Desk | Human-readable local projection and review-packet export | Browser-local proposal only |

Public retrieval baseline:

- chunk size `800`, overlap `120`;
- lexical/vector/rerank top-k `5/5/5`;
- final sources `8`;
- source paths and exact read required;
- deterministic lexical fallback;
- TurboVec `4-bit`, current verdict `optional_trial_not_default`;
- promotion requires 20 fixed queries, no recall regression, full citation retention, filters, persistence parity, and independent review.

## Meet the crew

The call names make responsibility easier to discuss; machine authority remains in [role-catalog.json](project/system/contracts/role-catalog.json).

| Work | Named roles |
|---|---|
| Goal, admission, and context | Yaromyr, Bohdan, Solomiia |
| Requirements and onboarding | Oksana, Taras |
| Tasks, copy, outreach, design, implementation | Danylo, Olena, Andrii, Kateryna, Dmytro |
| Validation and independent proof | Iryna, Mykola, Halyna |
| Integration, knowledge, release, outcomes | Larysa, Maksym, Pavlo, Nazar, Zoriana, Ostap, Marta, Roman |

The full roster, owned outputs, and prohibitions are in the [strategic architecture](docs/responsive-knowledge-crew-architecture.md#4-named-role-catalog).

## Research and work quality

All specialist work uses:

- source-authority triage;
- `FACT / INTERPRETATION / HYPOTHESIS / GAP`;
- triangulation and disconfirmation;
- claim tables with currentness and allowed use;
- maker → independent reviewer → maker repair → reviewer readback.

Requirements research adds JTBD, forcing moments, Five Whys, pain chains, ninety-day stories, market/account evidence, and requirements-to-acceptance. Outreach separates company fit, person currentness, channel, message, and exact send approval. Design preserves editable sources, wrapping, responsiveness, accessibility, and rollback.

## Skill cleaning and updates

Skills move through:

`discovered → quarantined → inspected → deduplicated → normalized → fixture-tested → reviewed → allowlisted → assigned → observed → updated → deprecated → removed`

Skill Spectre is a static package-inspection job; its public evidence is limited to two low-risk static scans and does not prove semantic scanning. “Video Spectre” is currently an inspection pattern only—inventory, isolate, scan, normalize, fixture-test, compare, approve, roll back—not a claimed public tool execution.

## Public/private boundary

| Keep in Git | Keep local/private | Keep only in secret storage |
|---|---|---|
| Contracts, schemas, synthetic fixtures, docs, editable diagrams | Internal sources, private vaults, indexes, embeddings, checkpoints, raw receipts | API keys, tokens, cookies, passwords, credentials |

The public project is independently operable. Optional Obsidian and Orbit adapters may use private local data, but private text, absolute paths, credentials, and raw traces never enter public Git.

## Verification

```bash
python3 project/system/validate_system.py
python3 project/scripts/generate-dashboard-data.py
node --check project/dashboard/app.js
python3 project/scripts/dashboard-static-smoke.py --skip-browser
python3 project/scripts/pre-push-runtime-guard.py
python3 scripts/public_safety_scan.py
```

With Chrome/Chromium installed:

```bash
python3 project/scripts/dashboard-static-smoke.py
```

The validator must keep one synthetic local documentation proposal eligible while blocking stale requirements, authority spoofing, target escape, reviewer spoofing, and malformed packets. Every evaluated proposal reports `executed: false`.

The mandatory push guard verifies the standard-library public core. Dependency-backed LangGraph, LlamaIndex, and CrewAI probes are a separate, explicit environment check: set `ARCHFLOW_VERIFY_OPTIONAL_RUNTIME=1` only after creating `project/local/venv` with those optional frameworks. A configured package or old local environment is not runtime proof unless that check completes.

## Repository map

| Path | Purpose |
|---|---|
| `project/system/contracts/` | Canonical controller, crew, roles, and workflow packs |
| `project/system/schemas/` | Typed case, role-task binding, and action-proposal packets |
| `project/system/fixtures/` | Synthetic and adversarial proof |
| `project/workflows/` | Framework-specific runtime contracts |
| `project/dashboard/` | Non-technical Crew Desk |
| `project/assets/architecture/` | Base artwork, editable SVGs, and README PNGs |
| `docs/` | Strategic, operational, adaptation, security, and API guidance |
| `wiki/` | Public WikiLLM durable memory pattern |
| `history/` | Sanitized historical summaries only |

## Documentation

- [Responsive knowledge crew architecture](docs/responsive-knowledge-crew-architecture.md)
- [Dashboard operating manual](docs/dashboard-operating-manual.md)
- [Onboarding knowledge agent](docs/onboarding-knowledge-agent.md)
- [Adapt ArchFlow](docs/adapting-archflow.md)
- [Quickstart](docs/quickstart.md)
- [Security and data boundaries](docs/security-and-data-boundaries.md)
- [Orbit Local integration](docs/orbit-local-integration.md)
- [Documentation index](docs/index.md)

## Calibrated limits

- The public dashboard has no model provider, durable team identity, checkpointer, or writeback.
- TurboVec evidence is a small synthetic isolated trial and cannot support a default-backend claim.
- SQLite/PostgreSQL persistence needs environment-specific migration and recovery proof.
- Orbit and Obsidian are optional local integrations; a clone cannot infer their live state.
- Graphify output must be regenerated when its source commit is stale.
- The repository has no software license grant yet. Public visibility is not permission to copy, modify, or redistribute it until the owner selects a license.
- No production, demand, ROI, availability, or autonomous-action claim exists without current receipts.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
