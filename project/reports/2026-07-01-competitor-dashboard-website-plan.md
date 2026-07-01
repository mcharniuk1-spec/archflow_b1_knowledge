# Competitor-Backed Dashboard And Website Improvement Plan

Date: 2026-07-01
Status: planning brief for next execution

## Executive Answer

ArchFlow should move forward in two coordinated directions.

Direction 1 is the internal dashboard: make it feel like a real operating cockpit for two separate orchestras. The first orchestra is the buyer-facing PRD/ICP service flow. The second orchestra is the internal reliable agent-control system. The current dashboard already has the right structural split, but it needs clearer first-screen operation, stronger visual hierarchy, explicit state/proof panels, better mobile/modal proof, and a more legible relationship between Jarvis, nodes, approvals, and generated outputs.

Direction 2 is the public website: position ArchFlow as a service-led automation and agentic operating-architecture company for product teams. The public offer should be "source-backed operating architecture that turns messy chats, docs, meetings, product decisions, and agent work into PRDs, reports, tasks, responsibilities, evidence packets, and approval-gated execution." The site should sell a practical service path first, not a finished autonomous AI platform.

Ronaldo may start from this planning and design brief only. He must not touch Jesus's active dashboard smoke-test/setup files until Jesus appends `complete` or `handoff` in `project/live/communication/agent-communication-log.md`.

## Situation And Complication

ArchFlow has a strong internal control-system direction and a coherent first product/service hypothesis. The problem is that the dashboard and public story can still feel too internal. A buyer needs to understand the result: better PRDs, clearer tasks, fewer lost decisions, source-labeled evidence, and a safer path from product strategy to implementation. An operator needs to understand the control system: what agent is doing what, what inputs are allowed, what outputs are blocked, what state is live, what provider/backend gates are closed, and what evidence supports each claim.

Competitors in this category do not sell "AI" by itself. They sell product work outcomes:

- Zeda.io frames itself around Voice of Customer, product insights, impact-first roadmaps, integrations, and revenue-linked decisions.
- mySecond frames the category as a PM operating system with skills, workflows, persistent context, approvals, and adoption visibility.
- BuildBetter emphasizes customer signal capture, contextual structuring, company taxonomy, business impact, and closing loops.
- Productboard Spark emphasizes PM-specific agents, delivery-ready product specifications, traceable outputs, collaboration, and context from data, docs, and codebase.
- ChatPRD emphasizes PRDs, one-pagers, user stories, gap analysis, coaching, exports, and integrations.

The implication: ArchFlow should not compete as another generic PRD generator or AI chatbot. It should compete as a service-led implementation of governed product-work operating systems: PRD/report/task systems plus reliable agent-management architecture.

## Customer And Stakeholder Job

Primary ICP: product teams in B2B SaaS scaleups, especially Series B-D, roughly 50-500 employees, 2-5 PMs, and a Director or VP Product owner accountable for PRD quality, discovery-to-delivery speed, and cross-functional alignment.

Functional job: convert scattered product material into a reviewed PRD, reporting packet, task list, responsibilities, acceptance criteria, evidence cards, and an execution-ready agent workflow.

Social job: look organized and rigorous in front of engineering, leadership, sales, customer success, and stakeholders.

Emotional job: reduce the fear that important decisions, assumptions, customer evidence, risks, or implementation details were missed.

Current alternatives: manual PRD writing, generic ChatGPT/Claude prompts, meeting-note tools, Notion templates, Linear/Jira tickets, consultants, and ungoverned internal agent experiments.

Switching trigger: repeated PRD rework, slow discovery-to-delivery cycles, scattered product context, inconsistent PM output, weak evidence for roadmap choices, or pressure to adopt AI without creating a fragile agent stack.

Adoption barriers: privacy, source trust, integration with existing tools, fear of autonomous writeback, lack of proof, and uncertainty about who owns the system after delivery.

## Evidence And Assumptions

FACT: The current dashboard has separate Jarvis, PRD/ICP Flow, Agent Orchestra, config, and plan views.

FACT: The current project keeps provider activation, Railway backend, durable writeback, deployment, and owner-device voice proof gated.

FACT: Jesus says Ronaldo may start from a planning/design brief only and must avoid active smoke-test/setup files until Jesus posts `complete` or `handoff`.

FACT: The current primary ICP is one lane: B2B SaaS product teams.

ASSUMPTION: Product teams will value a service-led "operating system setup" if it produces tangible artifacts faster than internal teams can create them.

ASSUMPTION: A public website can safely sell the methodology before a live backend is implemented, provided it does not claim autonomous provider-backed execution.

GAP: E2 market evidence, E5 ROI proof, E6 outreach, and E7 payment verdict are not complete. Public claims must stay framed as hypothesis, service offer, or internal proof until those gates exist.

## Quality Review Of The Current Work

### What Is Strong

- The two paradigms are now explicit: `(1) PRD/ICP Flow` and `(2) Agent Orchestra`.
- The dashboard is honest about static/browser-local state and avoids direct browser-side provider calls.
- Node controls expose real operating fields: inputs, outputs, prompts, system prompts, comments, run history, configuration, connections, safety, and approvals.
- The project has public-safety scanning, workflow validation, runtime guard, dashboard JSON generation, and run notes.
- The public plan already has a practical ICP and E1-E7 spine.

### What Is Weak

- The dashboard still reads like an internal engineering surface before it reads like an operating cockpit.
- Jarvis should be the first-screen command area with a stronger visual "voice sphere/chat" presence; today it is present but not yet the emotional center.
- The relationship between buyer-facing service output and internal agent-control mechanics needs a clearer mental model.
- Modal click-through, mobile operation, and Chrome route smoke are still under active proof by Jesus.
- Public website positioning is not yet a high-conversion service page; the old real-estate/short-term-rental visual language is outdated as positioning.
- The brand assets are useful visually, but the category message must shift to product-team operating systems and agent governance.

### Current Risk

The biggest risk is overclaiming. ArchFlow can safely show a static dashboard, service process, and controlled architecture. It cannot yet claim live provider-backed Jarvis, live Railway backend, automatic writeback, or validated market demand.

## Direction 1: Improve The Internal Dashboard

### Dashboard Purpose

The dashboard should let the operator run a governed agentic system from one place:

1. Capture a command or source packet through Jarvis.
2. Choose the relevant orchestra: PRD/ICP service flow or internal Agent Orchestra.
3. Inspect each node's inputs, outputs, config, prompts, comments, and last-run evidence.
4. See what is static, local, live, gated, blocked, or approved.
5. Export packets for Codex review without pretending the browser can write durable state.

### Visual And Usage Improvements

1. First-screen Jarvis operating area
   - Make Jarvis the dominant first viewport, not just another panel.
   - Use a large voice sphere or command core with clear states: static, listening requested, transcript captured, packet queued, writeback blocked.
   - Keep voice claims factual: "browser requested", "recognition started", "manual fallback", or "not supported".

2. Two-orchestra navigation
   - Replace the long tab feeling with a compact operating switcher:
     - `Service Product: PRD/ICP`
     - `Control System: Agent Orchestra`
   - Show a short "what this lane does" strip under the switcher.
   - Add lane color/shape differences that do not rely on color alone.

3. Node map readability
   - Add a mini-map or stage rail so long horizontal graphs are easier to scan.
   - Keep draggable node blocks, but give nodes stronger stage labels: Intake, Draft, Evidence, Synthesis, Approval, Output.
   - Add a selected-node breadcrumb and incoming/outgoing count.

4. N8N-style control panel polish
   - Use tabs inside the large panel: Overview, Inputs, Outputs, Config, Prompt, Runs, Comments.
   - Put connection controls near ports, not buried under generic settings.
   - Add a "last run interpreted" block with FACT, INTERPRETATION, HYPOTHESIS, GAP.

5. State badges and proof badges
   - Every page should show explicit state:
     - static snapshot
     - browser-local
     - local bridge absent
     - provider disabled
     - writeback gated
     - smoke-test status
   - Add a "proof drawer" for latest check results and source run notes.

6. Motion and brand interaction
   - Reuse the legacy ArchFlow visual motif only as a stroke-only arch system, not as real-estate positioning.
   - Use subtle 3D/3GS-style button motion on hover: depth shift, shadow rotation, border glint, and small icon movement.
   - Avoid decorative blobs and generic AI gradients.
   - Use restrained transitions for node hover, lane switching, panel open, and packet queued states.

7. Mobile and accessibility
   - Nodes must be keyboard activatable.
   - Large modal must close by button, backdrop, and Escape.
   - Mobile should switch to stage cards plus expandable node drawers instead of forcing a wide graph first.

### Contextual And Logical Improvements

1. Define the two orchestras as operating contracts
   - PRD/ICP Flow: source packet -> PRD -> evidence fork -> ICP -> demo package -> approval -> output packet.
   - Agent Orchestra: owner command -> classification -> Codex/local execution -> monitor -> reviewer fork -> safety review -> integrator -> owner approval -> memory/run update.

2. Add input/output contracts per node
   - Required inputs.
   - Allowed inputs.
   - Forbidden inputs.
   - Expected outputs.
   - Possible output destinations.
   - Approval rule.

3. Add provider/config taxonomy
   - `MODEL_PROVIDER=none` default.
   - `local bridge absent`.
   - `OpenRouter planned`.
   - `Mistral planned`.
   - `Ollama local optional`.
   - `writeback blocked`.

4. Add an issue queue inside the dashboard
   - Visual QA issues.
   - Runtime/provider gates.
   - Evidence/ICP gaps.
   - Public-safety issues.
   - Deployment/merge blockers.

5. Add source-backed decision tracking
   - Every recommendation should link to a run note, source packet, evidence card, or issue.
   - No node should show "complete" unless it has a check, artifact, or explicit owner approval.

6. Add test visibility
   - Show last pass/fail for public safety scan, workflow validation, runtime guard, JS syntax, JSON parse, and route smoke.
   - If Chrome route smoke is blocked or pending, show it as blocked/pending, not failed system state.

### Dashboard Issue Backlog

- D-1: Make Jarvis first-screen command core with voice sphere and chat history.
- D-2: Add a two-orchestra operating switcher with short lane definitions.
- D-3: Improve node map scanability with stage rail, mini-map, selected breadcrumb, and edge counts.
- D-4: Refine the node control panel into task-focused tabs.
- D-5: Add explicit state/proof badges to every operating page.
- D-6: Add issue queue and blocker drawer inside the dashboard.
- D-7: Add contextual help for static/local/backend/provider/writeback states.
- D-8: Add keyboard and mobile proof checklist after Jesus completes smoke-test lane.
- D-9: Add visual polish based on the stroke-only arch motif and hover-depth buttons.
- D-10: Add public-safe example packets for PRD, ICP, task, and agent-run outputs.

## Direction 2: Build The Public ArchFlow Services Website

### Website Purpose

The public website should sell ArchFlow as an automation-services company that creates complex agent-management systems and PRD/reporting/task-definition systems from a project knowledge base.

The first visitor should understand three things within the first viewport:

1. What ArchFlow creates: PRDs, reports, tasks, responsibilities, evidence packets, and approval-gated agent workflows.
2. Who it is for: product teams that have scattered context and need reliable discovery-to-delivery execution.
3. Why it is different: source-backed architecture, not generic prompts; governed agents, not autonomous chaos.

### Public Positioning

Primary statement:

ArchFlow turns messy product context into source-backed requirements and governed agent execution.

Supporting statement:

We build the knowledge base, PRD/reporting system, task-definition layer, and agent-control dashboard that let product teams move from meetings and scattered docs to reviewed implementation plans.

Avoid:

- "Fully autonomous AI agents."
- "Instant perfect PRDs."
- "Validated market demand."
- "Provider-backed Jarvis is live."
- "Railway backend is deployed."

### Visual And UX Direction

1. Brand carryover
   - Keep the legacy dark editorial hero, Playfair-style display type, warm light/dark palette, accent CTAs, and stroke-only arch motif.
   - Drop the old real-estate and short-term-rental concept.
   - Reinterpret "Form Follows Flow" as product-system flow: source -> decision -> requirement -> task -> agent -> approval.

2. Hero layout
   - First viewport should show ArchFlow as the product/service, not only tiny nav text.
   - Use an immersive full-width hero with a real or generated dashboard/process scene, not a split card layout.
   - Show a hint of the next section below the fold.

3. Interactive motif
   - Use 3D/3GS-style hover buttons for CTA and tool cards.
   - Use animated stroke arches as path markers between input, PRD, task, and agent states.
   - Keep motion purposeful and fast; no decorative blobs.

4. Product proof section
   - Show public-safe artifact examples:
     - raw source packet
     - PRD excerpt
     - evidence card
     - task/responsibility matrix
     - agent node config
     - approval log
   - Do not use private screenshots.

5. Website information architecture
   - Home
   - Services
   - PRD/ICP System
   - Agent Operating System
   - Method
   - Proof / Build Log
   - Diagnostic

### Contextual And Logical Website Structure

1. Home page
   - Hero: "Source-backed PRDs and governed agent workflows."
   - Subcopy: messy chats/docs/meetings -> PRD/report/task/evidence packets -> approval-gated execution.
   - CTA: "Book a workflow diagnostic" and "See the operating model".
   - Visual: animated pipeline from source packet to PRD to task graph to approved agent run.

2. Problem section
   - Scattered product context.
   - Repeated PRD rework.
   - Weak evidence for decisions.
   - Generic AI prompts that do not preserve team context.
   - Agent experiments without review gates.

3. Service packages
   - Diagnostic and source inventory.
   - PRD/report/task-definition packet.
   - Evidence/ICP review.
   - Agent operating dashboard setup.
   - Optional backend/provider/writeback setup after approval.

4. Method section
   - Intake.
   - Structure.
   - Evidence.
   - Requirements.
   - Tasks.
   - Agents.
   - Review.
   - Handoff.

5. Differentiation
   - Source labels and traceability.
   - Two-orchestra architecture.
   - Approval-gated execution.
   - Public-safe/private-source boundaries.
   - Service-led setup instead of DIY prompt library.

6. Diagnostic page
   - Segment.
   - Current tools.
   - Current PRD process.
   - Source material readiness.
   - Privacy concerns.
   - Budget owner.
   - Desired output destination.
   - Urgency trigger.

7. Proof and transparency
   - Use public-safe run notes and sanitized examples.
   - Show what is working, what is gated, and what is not claimed.
   - Avoid fake logos, fake customer claims, or invented ROI.

### Public Website Issue Backlog

- W-1: Replace outdated real-estate/short-term-rental positioning with product-team operating-system positioning.
- W-2: Create a new homepage narrative around source-backed PRDs and governed agent workflows.
- W-3: Create a services page with service-led packages and clear deliverables.
- W-4: Create a PRD/ICP solution page with artifact examples and evidence gates.
- W-5: Create an Agent Operating System page explaining the internal orchestra and boundaries.
- W-6: Create a diagnostic page with analytics-ready lead questions.
- W-7: Create a public-safe proof/build-log page that links to sanitized run artifacts.
- W-8: Define a visual system that keeps the arch motif, editorial typography, accent CTAs, and hover-depth buttons without real-estate claims.
- W-9: Define website copy rules: no autonomous claims, no demand claims, no provider/live backend claims until implemented.
- W-10: Add conversion metrics: diagnostic starts, source-packet willingness, budget-owner path, privacy blocker, and paid diagnostic interest.

## Two-Orchestra Operating Model

### Orchestra 1: PRD/ICP Service Product

Purpose: create the buyer-facing output.

Flow:

1. Source intake.
2. PRD draft.
3. Evidence fork.
4. ICP synthesis.
5. Demo/landing output.
6. Approval.
7. Service packet.

Outputs:

- context digest
- PRD
- task matrix
- responsibility map
- evidence cards
- ICP profile
- demo/landing outline
- confidence level

### Orchestra 2: Reliable Agent Control System

Purpose: make execution inspectable and safe.

Flow:

1. Owner command.
2. Request classification.
3. Codex/local execution.
4. Monitor state.
5. Parallel reviewer fork.
6. Safety/source review.
7. Integrator merge.
8. Owner approval.
9. Run note and memory update.

Outputs:

- branch diff
- validation results
- run note
- issue
- decision
- dashboard data
- handoff packet

## Ronaldo Execution Brief

Ronaldo should begin in a separate Codex chat with this scope:

1. Read this report first.
2. Read `project/live/communication/README.md`, `current-agent-notice.md`, and the latest communication log.
3. Do not edit Jesus's active files until Jesus posts `complete` or `handoff`.
4. Create a design execution plan for dashboard and website.
5. Prepare public-safe wireframes/copy outlines as Markdown or a standalone prototype only if it does not touch active dashboard files.
6. Keep all claims source-labeled and bounded.
7. Do not deploy, push, activate providers, write Notion/GitHub/WikiLLM, or create backend/provider calls.

Allowed first outputs:

- dashboard UX improvement brief
- website sitemap and page copy outline
- brand-system adaptation brief
- public-safe wireframe description
- issue prioritization
- acceptance criteria

Blocked until Jesus handoff:

- `project/scripts/dashboard-static-smoke.py`
- `project/dashboard/README.md`
- `project/runs/2026-07-01-june30-transfer-provider-dashboard/run-summary.md`
- `wiki/runs/2026-07-01-june30-transfer-provider-dashboard.md`
- any dashboard implementation edit that conflicts with active smoke-test/setup work

## Acceptance Criteria For The Next Pass

Dashboard:

- The first screen clearly shows Jarvis as the operating center.
- The two orchestras are visually and logically separate.
- Node control panel tabs map to real operator tasks.
- Static/local/backend/provider/writeback state is impossible to misunderstand.
- Mobile/modal/keyboard operation has proof after Jesus completes the smoke-test lane.

Website:

- First viewport explains the service outcome in one read.
- ICP is product-team-first, not generic AI automation.
- Page structure shows service packages and concrete outputs.
- Visual design adapts ArchFlow brand without outdated real-estate positioning.
- CTA routes to a diagnostic, not vague "contact us".
- Claims avoid fake proof, fake customers, and unimplemented runtime promises.

## Sources Reviewed

- Zeda.io: https://zeda.io/
- mySecond: https://mysecond.ai/
- BuildBetter: https://www.buildbetter.ai/
- Productboard Spark: https://www.productboard.com/product/spark/
- ChatPRD: https://www.chatprd.ai/

## Confidence Level

Confidence: 0.76.

Reason: competitor positioning and current local state are clear enough for a planning/design brief. Confidence stays below 0.8 because E2 market research, E5 ROI proof, E6 outreach, E7 payment verdict, Jesus smoke-test completion, and public website implementation are not complete.
