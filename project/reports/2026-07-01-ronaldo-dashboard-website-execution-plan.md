# Ronaldo Dashboard And Website Execution Plan

Date: 2026-07-01
Status: planning/design package

## Scope

This plan is public-safe planning only. It does not edit dashboard implementation files, activate providers, deploy, push, write external systems, or claim backend/runtime behavior that has not been implemented and verified.

Coordination state: Jesus posted `Status: complete` for the dashboard smoke-test/setup lane in `project/live/communication/agent-communication-log.md`. Implementation work is now unblocked from that specific gate, but any agent touching implementation files must first append a fresh starting claim, check current `git status`, and verify no newer active lane has claimed the same files.

## Source Labels

- SOURCE: `project/reports/2026-07-01-competitor-dashboard-website-plan.md`
- SOURCE: `project/issues/2026-07-01-dashboard-website-improvement-issues.md`
- SOURCE: `project/runs/2026-07-01-competitor-dashboard-website-plan/agent-handout.md`
- SOURCE: `project/reports/2026-07-01-legacy-design-reference-and-prd-calculator-brief.md`
- SOURCE: `wiki/runs/2026-07-01-legacy-design-reference-and-prd-calculator.md`
- SOURCE: Live communication log entries through 2026-07-01 13:05
- SOURCE: Competitor references listed in the competitor plan: Zeda.io, mySecond, BuildBetter, Productboard Spark, and ChatPRD

Direct fetch note: the legacy site URL was not reachable from this execution environment, so this plan uses the inspected local addendum as the source of record for visual mechanics.

## 1. Dashboard UX Execution Plan

### UX Goal

Make the dashboard read as a controlled operating cockpit for ArchFlow's two orchestras:

- Service Product: PRD/ICP flow for buyer-facing outputs.
- Control System: agent orchestra for internal execution, review, safety, and memory/run updates.

The first screen must answer: what command starts work, which lane handles it, what is live or static, what is blocked, and what proof exists.

### Phase 0 - Coordination Gate

Before touching dashboard implementation, smoke-test/setup, or public website prototype files, the implementer must confirm current live coordination state.

Acceptance:

- Communication log contains the Jesus smoke-test/setup completion entry.
- Implementer appends a new starting entry before implementation edits.
- Implementer checks current `git status`.
- Claimed files do not overlap with another active agent.

### Phase 1 - First View And Operating Model

Design the first viewport around a Jarvis command core.

Required elements:

- Jarvis command input and chat/history area.
- Voice sphere or command-state visual with factual states only: static, browser requested, manual fallback, packet queued, or blocked.
- Persistent state badges: static snapshot, browser-local, provider disabled, local bridge absent, writeback gated.
- Two-orchestra switcher with lane definitions and expected outputs.
- A visible proof drawer entry point.

Acceptance:

- A first-time operator can identify where to start without reading documentation.
- No label implies provider-backed Jarvis, durable writeback, Railway runtime, or autonomous execution.
- The two lanes state inputs, outputs, and blocked actions in one read.

### Phase 2 - Node Map And Control Panel

Improve node-map scanability and make the selected-node panel task-oriented.

Required elements:

- Stage rail: Intake, Draft, Evidence, Synthesis, Approval, Output.
- Selected-node breadcrumb.
- Incoming and outgoing connection counts.
- Mini-map or compact overview for long graphs.
- Node panel tabs: Overview, Inputs, Outputs, Config, Prompt, Runs, Comments.
- A FACT / INTERPRETATION / HYPOTHESIS / GAP block for latest run interpretation.

Acceptance:

- Operator can locate prompts, config, run history, and comments in one click.
- Every node shows required inputs, allowed inputs, forbidden inputs, expected outputs, destinations, and approval rule.
- Mobile users get stage cards or drawers rather than a forced wide graph as the only entry point.

### Phase 3 - Proof, Issues, And Gating

Expose proof and blockers inside the dashboard.

Required elements:

- Latest check cards for public safety scan, workflow validation, runtime guard, JS syntax, JSON parse, and route smoke.
- Issue queue grouped by visual QA, runtime/provider gates, evidence/ICP gaps, public-safety issues, and deployment/merge blockers.
- Claim policy panel that distinguishes static demo, local browser behavior, planned backend, and implemented runtime.

Acceptance:

- Dashboard cannot be mistaken for a live provider-backed backend.
- Blockers are visible without opening run notes.
- A node or lane cannot display complete unless it has a linked artifact, check, or explicit approval.

### Phase 4 - Brand Interaction And Accessibility

Adapt the ArchFlow visual system without weakening operator density.

Required elements:

- Stroke-only arch motif as flow markers and connection accents.
- Warm/dark palette with accent CTAs.
- Editorial display type only for true hero/command moments.
- Hover-depth buttons with small shadow/position/icon movement.
- Legacy-style arch layers using `data-speed`, `data-drift`, `data-rotate`, CSS `perspective`, `translate3d`, ambient sheen variables, and pointer lighting.
- Keyboard activation for nodes, Escape/backdrop/button modal close, and mobile drawer proof.

Acceptance:

- Interface feels like ArchFlow while remaining dense and operational.
- Text does not overlap at mobile or desktop sizes.
- Motion clarifies state changes and does not become decorative noise.

## 2. Public Website Sitemap And First-Page Wireframe/Copy Outline

### Sitemap

1. Home
2. Services
3. PRD/ICP System
4. Agent Operating System
5. Method
6. Proof / Build Log
7. Diagnostic

### Home Page Wireframe

#### First View

Headline:

Source-backed PRDs and governed agent workflows for product teams.

Subcopy:

ArchFlow turns scattered product context into structured requirements, evidence packets, task definitions, responsibilities, and approval-gated agent execution.

Primary CTA:

Book a workflow diagnostic

Secondary CTA:

See the operating model

Visual:

Full-width process scene: source packet -> evidence cards -> PRD -> task matrix -> agent node -> approval gate. Use layered arch WebP-style assets, scroll drift, ambient sheen, dark command panels, and depth-hover interaction. Avoid old real-estate imagery.

Trust line:

Service-led architecture. Source labels. Explicit gaps. Human approval gates.

#### Problem Band

Copy blocks:

- Product context is scattered across meetings, docs, tickets, and stakeholder chats.
- PRDs get rewritten because assumptions and evidence are unclear.
- Generic AI prompts create drafts but do not preserve operating memory.
- Agent experiments become risky when permissions, providers, and writeback are not gated.

#### Outcome Band

Deliverables:

- Source packet
- PRD/reporting packet
- Evidence and gap cards
- Task and responsibility matrix
- Agent workflow map
- Approval and handoff log

#### Service Packages

Diagnostic:

Map source readiness, workflow gaps, privacy constraints, current tools, and ownership.

PRD/ICP Packet:

Convert source material into a reviewed PRD, evidence summary, ICP notes, task definitions, and acceptance criteria.

Agent Operating System Setup:

Design the controlled dashboard, node contracts, review gates, and handoff/memory process.

Backend/Provider Enablement:

Optional later phase only after approval and runtime proof.

#### Method

Intake -> structure -> evidence -> requirements -> tasks -> agents -> review -> handoff.

#### Proof / Transparency

Show public-safe examples and build-log links. Label static examples, gated items, and implemented checks. Do not use fake customers, fake ROI, or private screenshots.

#### Diagnostic CTA

Question focus:

- current PRD process
- current tools
- source material readiness
- privacy constraints
- budget owner
- urgency trigger
- desired output destination

#### Calculator-First Proof Interaction

Place a simplified calculator immediately after the hero or as the first proof section. Reuse the legacy calculator pattern, but change the model from rental automation to product-team PRD/ICP and knowledgebase readiness.

Calculator name:

PRD/ICP Operating ROI Calculator

Modes:

- PRD/ICP ROI
- Knowledgebase Readiness

PRD/ICP ROI inputs:

- Product people involved
- Weekly PRD/research/task hours
- Blended hourly cost
- Rework/context-loss share
- Recoverable share with ArchFlow
- Setup plus support cost

PRD/ICP ROI outputs:

- Monthly value of recovered work
- Yearly value of recovered work
- First-year ROI planning estimate
- Estimated payback
- Recommended first package

Knowledgebase Readiness inputs:

- Source centralization
- Evidence quality
- PRD consistency
- Tool integration readiness
- Approval maturity

Knowledgebase Readiness outputs:

- Knowledgebase readiness score out of 100
- Agent execution readiness score out of 100
- Recommended first action

Formula boundary:

All calculator results are planning estimates only. Do not claim guaranteed savings, financial advice, validated ROI, or demand proof until E5/E6/E7 evidence exists.

## 3. Brand-System Adaptation Brief

### Keep

- Stroke arch motif as the core identity device.
- Layered 3D-looking arch assets with scroll-driven drift and CSS depth.
- Editorial typography for major moments and page titles.
- Warm/dark palette with restrained light surfaces.
- Accent CTAs.
- Hover-depth and 3D button motion.
- Dark command panels with arch-line overlays.
- Calculator-first proof interaction.
- "Form Follows Flow" as a system-flow idea.

### Drop

- Real-estate and short-term-rental positioning.
- Generic AI gradient language.
- Decorative blobs or one-note purple/blue palettes.
- Any visual suggesting a finished autonomous AI platform.
- Any dashboard or website copy implying live providers, Railway runtime, or durable writeback before proof.

### Reinterpret

The arch becomes a route through product work:

source -> decision -> requirement -> task -> agent -> approval.

The dark editorial system becomes a serious operating architecture brand, not a landing-page decoration.

The warm accent CTA becomes a controlled action marker: diagnose, review, approve, export.

Hover-depth motion should communicate usable controls: command, inspect, approve, open proof, or export packet.

### Legacy Interaction Recipe

Match the perceived 3D/Three.js-like feel through the actual legacy pattern before inventing a new visual system:

- `arc-field` containers with CSS perspective.
- Layered `arc-object` image assets with CSS variables for position, opacity, rotation, and z-depth.
- Per-layer `data-speed`, `data-drift`, and `data-rotate` attributes for scroll transforms.
- Scroll updates for `--scroll-x`, `--scroll-y`, `--arc-z`, and `--arc-rotate`.
- Ambient sheen variables on the page shell or body.
- `depth-hover` pointer lighting using `--depth-light-x`, `--depth-light-y`, and `--depth-light`.
- Hover-depth on CTA buttons, service cards, calculator tabs, toggle pills, tool chips, and diagnostic choices.
- Reduced-motion fallback and smaller mobile arc movement.
- Sticky result panel on desktop, stacked result panel on mobile.

### Design Constraints

- No card-in-card layouts.
- Cards only for repeated artifacts, issue items, proof items, or tool panels.
- First viewport must signal ArchFlow clearly.
- Text must fit in all buttons and compact panels.
- Use source/proof labels when a claim depends on a run note or implementation state.

## 4. Issue Priority And Acceptance Criteria

### P0

D-1 Jarvis command core:

Acceptance: first viewport clearly starts with Jarvis, shows command state, and exposes packet queue or blocked state without provider overclaim.

D-2 Two-orchestra mode switch:

Acceptance: PRD/ICP Flow and Agent Orchestra are visibly separate, with inputs, outputs, and blocked actions.

D-3 State/proof badges:

Acceptance: every operating page distinguishes static, browser-local, provider disabled, local bridge absent, and writeback gated states.

W-1 Website repositioning:

Acceptance: homepage does not use real-estate or short-term-rental positioning as the active current offer.

W-2 Packaged buyer offer:

Acceptance: visitor can understand the diagnostic, PRD/ICP packet, agent operating setup, and optional backend/provider phase.

W-3 Product-team ICP:

Acceptance: homepage and first solution page are written for B2B SaaS product leaders first.

### P1

D-4 Node panel tabs:

Acceptance: Overview, Inputs, Outputs, Config, Prompt, Runs, and Comments are available for selected node inspection.

D-5 Graph/mobile navigation:

Acceptance: mobile can use stage cards/drawers, and desktop has a stage rail or mini-map.

D-6 Proof and blocker drawer:

Acceptance: current checks and blockers are visible without leaving the dashboard.

W-4 Diagnostic flow:

Acceptance: diagnostic captures qualification signals, source readiness, privacy constraint, urgency trigger, and budget-owner path.

W-4A Calculator-first proof interaction:

Acceptance: home page includes a two-mode calculator with PRD/ICP ROI and Knowledgebase Readiness, live-updating results, a formula explanation inside `details`, and copy that labels all values as planning estimates.

W-5 Public-safe artifact proof:

Acceptance: proof section uses sanitized examples only and labels static/gated/verified states.

W-6 Differentiation:

Acceptance: website explains source-backed operating architecture, two orchestras, and approval gates.

### P2

D-7 Brand polish:

Acceptance: stroke arches, warm/dark palette, accent CTAs, and hover-depth buttons are applied without reducing operator clarity.

D-8 Sample packets:

Acceptance: public-safe PRD, evidence, task matrix, and agent-run examples exist and contain no private source material.

W-7 Visual modernization:

Acceptance: site feels premium and current while dropping old vertical semantics.

W-8 Claim policy:

Acceptance: copy review catches fake ROI, fake customers, live-backend claims, provider claims, demand validation claims, and autonomous execution claims.

## Claim Guardrails

Allowed:

- Planning/design language.
- Service-led offer language.
- Static dashboard and public-safe artifact examples.
- Explicitly labeled gaps, gates, and assumptions.

Blocked until proof:

- Provider-backed Jarvis.
- Railway backend.
- Browser-side provider calls.
- Durable writeback.
- Autonomous execution.
- Market demand or ROI claims.
- External writes, deploys, or pushes.

## Confidence

Confidence: 0.78.

Reason: the source plan, issue backlog, and communication state are clear enough for execution planning. Confidence stays below 0.8 because Jesus's dashboard lane is still active and E2/E5/E6/E7 proof remains incomplete.
