# Legacy Design Reference And PRD/ICP Calculator Brief

Date: 2026-07-01
Status: design addendum for Ronaldo and future website execution

## Executive Answer

The owner-provided legacy ArchFlow public site should be treated as the visual interaction reference, not as the current positioning reference.

Keep the design mechanics:

- layered 3D arch assets;
- scroll-driven arch drift;
- cursor-driven hover-depth on buttons and cards;
- warm editorial palette;
- Playfair-style display typography;
- dark command panels with arch-line overlays;
- calculator-first proof interaction.

Replace the category message:

- old: short-term rental automation systems;
- new: source-backed PRD/ICP systems, analytical executable agents, and governed knowledgebase-driven agent orchestration.

## What The Legacy Site Actually Uses

FACT: The legacy site uses 3D-looking arch WebP assets in layered fields, not a visible full Three.js scene in the inspected public HTML/JS.

FACT: The motion model is still valuable and should be reused:

- `arc-field` containers with `perspective`;
- `arc-object` images with CSS variables for position, rotation, opacity, and z-depth;
- per-asset `data-speed`, `data-drift`, and `data-rotate` attributes;
- scroll listeners that update `--scroll-x`, `--scroll-y`, `--arc-z`, and `--arc-rotate`;
- ambient light variables on the body;
- hover-depth JS for links, buttons, tabs, toggle pills, cards, tool chips, and choice labels.

INTERPRETATION: For the new website, "match the 3js effects" means preserve the perceived 3D depth, parallax, cursor response, and arch-world identity. It does not require adding Three.js unless a later implementation needs true WebGL.

## Visual Requirements For The New Public Website

### Keep From Legacy

- Stroke/arch brand motif as the main spatial metaphor.
- Layered arch assets moving at different scroll speeds.
- Hero title with editorial scale and warm/dark contrast.
- Sticky glass header.
- Accent CTA buttons with subtle pulse.
- Hover-depth on every important interactive element.
- Dark command/control panel with arch-line overlays.
- Calculator as first proof interaction.
- Reduced-motion fallback.

### Change From Legacy

- Remove short-term-rental language.
- Remove property manager/listing/maintenance/turnover service framing.
- Replace rental service cards with product-team operating-system cards.
- Replace tool map with product work stack map: meetings, docs, feedback, PRD, Linear/Jira, Notion/Confluence, GitHub, Codex, and agent orchestration.
- Replace ROI from rental automation with PRD/ICP and agent-readiness calculator.

## New Hero Direction

Primary headline:

Source-backed PRDs. Governed agent workflows.

Supporting copy:

ArchFlow turns scattered product context from meetings, docs, chats, research, and decisions into PRDs, ICP evidence, executable tasks, and approval-gated agent runs.

Hero visual:

- Large 3D arch field on the right or behind the hero.
- A dark command panel showing four outputs:
  - PRD packet;
  - ICP evidence;
  - task matrix;
  - agent run queue.
- Below hero: four focus cards:
  - Source clarity;
  - Evidence quality;
  - Requirement readiness;
  - Agent execution control.

CTA:

- Primary: `Run PRD/ICP diagnostic`
- Secondary: `See the operating model`

## Simplified PRD/ICP Calculator

### Calculator Name

PRD/ICP Operating ROI Calculator

### Goal

Use the legacy calculator pattern but simplify the model for product-team PRD/ICP and analytical executable-agent scope.

### Modes

Use two tabs only:

1. `PRD/ICP ROI`
2. `Knowledgebase Readiness`

### Inputs For PRD/ICP ROI

Keep the first version to six controls:

| Input | Control | Purpose |
|---|---|---|
| Product people involved | stepper or range | PM/leadership/BA people affected by PRD work. |
| Weekly PRD/research/task hours | range | Time spent on product docs, synthesis, ticket shaping, evidence review, and stakeholder updates. |
| Blended hourly cost | range | Internal labor-cost estimate. |
| Rework/context-loss share | range | Share of work lost to missing context, unclear ownership, weak evidence, or repeated rewriting. |
| Recoverable share with ArchFlow | range | Conservative share of wasted effort the service can reduce. |
| Setup plus support cost | range | Planning estimate for diagnostic, PRD packet, dashboard setup, and support. |

### Outputs For PRD/ICP ROI

- Monthly value of recovered work.
- Yearly value of recovered work.
- First-year ROI planning estimate.
- Estimated payback.
- Recommended first package:
  - source inventory;
  - PRD/ICP packet;
  - agent operating dashboard;
  - backend/provider gate later.

### Inputs For Knowledgebase Readiness

Keep readiness to five sliders:

| Input | Meaning |
|---|---|
| Source centralization | Are meetings, docs, chats, and decisions findable? |
| Evidence quality | Are claims linked to feedback, market signals, or source notes? |
| PRD consistency | Are requirements written in a repeatable structure? |
| Tool integration readiness | Can outputs move to Notion, Linear/Jira, GitHub, or docs without manual recreation? |
| Approval maturity | Are risks, owner approvals, and writeback gates explicit? |

### Outputs For Knowledgebase Readiness

- Knowledgebase readiness score out of 100.
- Agent execution readiness score out of 100.
- Recommended first action:
  - clean source inventory;
  - build PRD packet;
  - add evidence cards;
  - define task matrix;
  - configure Agent Orchestra.

### Formula Boundary

All values are planning estimates, not guaranteed savings or financial advice. Do not claim validated ROI until E5/E6/E7 proof exists.

## Calculator Copy Draft

Eyebrow:

PRD/ICP operating calculator

Heading:

Estimate the cost of scattered product context before building the agent system.

Body:

Model the hours lost to PRD rewrites, repeated context sharing, unclear requirements, and weak evidence. The calculator recommends whether to start with a source inventory, PRD/ICP packet, knowledgebase cleanup, or Agent Orchestra setup.

Result summary template:

Based on these inputs, the first ArchFlow wedge should be `{recommended_package}`. The estimate suggests `{monthly_value}` of recoverable monthly product-work value and a readiness score of `{readiness}/100`.

## Interaction Requirements

Ronaldo should preserve these implementation patterns from the legacy site:

- `depth-hover` class for CTA buttons, cards, tabs, and calculator toggles;
- pointer-position light using `--depth-light-x`, `--depth-light-y`, and `--depth-light`;
- scroll-driven arch layer transforms using `data-speed`, `data-drift`, and `data-rotate`;
- mobile reduced motion and smaller arc movement;
- calculator tab switch with clear mode copy;
- range input outputs updating live;
- formula explanation inside a `details` block;
- sticky result panel on desktop, stacked result panel on mobile.

## Website Section Mapping From Legacy To New

| Legacy section | New section |
|---|---|
| Short-term rental hero | PRD/ICP and governed agent workflow hero |
| ROI calculator | PRD/ICP Operating ROI Calculator |
| Four rental service models | Four product-system service packages |
| Tool map | Product work and agent stack map |
| Diagnostic quiz | PRD/ICP workflow diagnostic |

## Four New Service Cards

1. Source-to-PRD Packet
   - Intake messy docs, meetings, chats, decisions, and constraints.
   - Output: PRD, acceptance criteria, questions, risks, and task matrix.

2. ICP Evidence Review
   - Structure market, customer, competitor, and account evidence.
   - Output: ICP card, evidence cards, source grades, gaps, and disqualifiers.

3. Agent Orchestra Setup
   - Configure node graph, prompts, approvals, run logs, and handoffs.
   - Output: dashboard schema, agent node configs, prompt library, and review packets.

4. Knowledgebase And Execution Loop
   - Define memory rules, source registry, update protocol, and validation gates.
   - Output: WikiLLM/Obsidian-style memory contract, run notes, issues, decisions, and dashboard data path.

## Ronaldo Instruction

Ronaldo should add this legacy-design constraint to his planning/design output. If he creates a prototype after Jesus handoff, it should reuse the legacy interaction recipe before inventing a new style.

Blocked until Jesus handoff remains unchanged:

- do not edit `project/scripts/dashboard-static-smoke.py`;
- do not edit `project/dashboard/README.md`;
- do not edit Jesus's run/wiki setup files;
- do not edit dashboard implementation files unless the active lane is complete or handed off.

## Confidence Level

Confidence: 0.82 for the visual interaction requirements because they come from the inspected live HTML, CSS, and JavaScript. Confidence: 0.68 for the calculator formula until E5 ROI proof and E6/E7 demand evidence exist.
