# Marketing Role Pack - ICP Evidence To Payment Verdict

Date: 2026-07-13
Status: active role architecture; all contact, publication, access, pricing, and payment actions remain owner-gated

## Operating sequence

```text
approved audience question
  -> ICP Evidence Agent
  -> Buyer Discovery Agent
  -> Positioning and Copy Agent
  -> ABM Channel Agent
  -> Claims and Safety Reviewer (claim, target, channel, action)
  -> owner approval pause
  -> owner/external action or explicit no-action receipt
  -> action readback
  -> Growth Evidence Agent
  -> Claims and Safety Reviewer (measurement and verdict)
  -> AF Knowledge promotion review
```

LangGraph owns the state transitions. A role may prepare one bounded packet but cannot promote its own high-risk output or skip an approval edge. Parallel research is allowed only when source ranges do not overlap; one integrator reconciles the evidence before messaging.

## Shared state contract

Every role reads and writes the same minimal fields:

- `account_or_cohort_id`
- `forcing_moment`
- `buyer_role_hypothesis`
- `evidence_refs`
- `evidence_freshness`
- `claim_state`
- `access_scope`
- `message_version`
- `approval_state`
- `next_commitment`
- `payment_stage`
- `stop_reason`
- `review_phase`
- `external_action_receipt`
- `readback_state`

No role stores secrets, raw private source material, personal contact exports, or a claim without source and state.

## Canonical role and skill bindings

| Marketing contract name | Canonical roster key | Executable operator skill packages | Project method checklists |
|---|---|---|---|
| ICP Evidence Agent | `af_research` | `company-research`, `deep-research`, `decision-mapping` | market structure, source triage, account evidence, job signals |
| Buyer Discovery Agent | `af_discovery` | `customer-journey-map`, `discovery-process` | JTBD, 90-day story, customer forces, five whys |
| Positioning And Copy Agent | `af_copy` | `content-strategy`, `content-research-writer`, `copywriting`, `copy-editing` | positioning, source-grounded copy, outreach drafting, claim status |
| Claims And Safety Reviewer | `af_review` | `agent-security-governance` | public safety, privacy/access, freshness, anti-ICP, secret/path scan |
| ABM Channel Agent | `af_abm_channel` | `acquisition-channel-advisor`, `company-research`, `customer-journey-map` | segmentation, sequence design, CRM hygiene |
| Growth Evidence Agent | `af_growth_evidence` | `data-analytics-insight`, `forecast-validation-and-backtesting`, `business-health-diagnostic` | funnel, experiment, modeled ROI, payment-stage classification |
| AF Knowledge promotion review | `af_knowledge` | project-local `task-handout` and `outquestions` | reviewed delta, supersession, readback, durable promotion |
| Product Packaging Engineer | `af_product_packaging` | `backend-api-architecture`, `codebase-design`, `code-clarity-and-docs`, `agent-security-governance`, `deployment-observability`, `debugging-checklist`, `browser-qa-performance-a11y` | install/MCP/admin/lifecycle/release gates |

Backticked package names above are discoverable executable skills in the current operator environment or cited project-local skill packages. Plain-language items are methods/checklists, not executable skill claims. Every runtime must still receive only the bounded skills named in its task contract.

## Roles and skills

### ICP Evidence Agent

Purpose: verify the cohort, company, current role, and forcing moment before an account becomes a messaging task.

Primary skills:

- `company-research`
- `deep-research`
- market-structure-analysis
- research-source-triage
- account-evidence-card-writing
- job-signal-analysis
- `decision-mapping`
- fact-interpretation-hypothesis-gap

Inputs: approved public sources, cohort rules, anti-ICP rules, source freshness limits.
Output: two-signal account card or accurate rejection.
Gate: current role and trigger are verified; unsupported fields remain GAP.
Forbidden: bulk personal-data acquisition, private-channel access, scraping outside approved terms, or a sales-ready label from one signal.

### Buyer Discovery Agent

Purpose: recover the buyer's 90-day forcing-moment story, current alternatives, decision ownership, access tolerance, and next commitment.

Primary skills:

- `customer-journey-map`
- discovery-process
- JTBD discovery
- ninety-day-story-extraction
- customer-forces-analysis
- five-whys
- source-boundary-control

Inputs: reviewed account card and owner-approved conversation material.
Output: discovery evidence packet with direct evidence separated from interpretation.
Gate: buyer, champion, urgency, alternatives, access/trust, and next commitment are explicit.
Forbidden: inventing quotes, recording without consent, or treating interest as demand.

### Positioning And Copy Agent

Purpose: turn one verified forcing moment into one claim, one proof object, one objection response, and one low-friction CTA.

Primary skills:

- `content-strategy`
- `content-research-writer`
- `copywriting`
- copy-editing
- positioning-synthesis
- source-grounded-copywriting
- outreach-message-drafting
- claim-status-check

Inputs: reviewed evidence and discovery packets.
Output: message matrix, website copy candidate, content brief, outreach draft, and evidence table.
Gate: every outward claim has a source/evidence state; PRD writing is not the lead hook.
Forbidden: guaranteed outcomes, fake social proof, unverified numerical ROI, or unsourced buyer language.

### Claims And Safety Reviewer

Purpose: downgrade, block, or approve claims and action packets independently.

Primary skills:

- `agent-security-governance`
- public-safety-review
- secret-and-path-scan
- claim-status-check
- privacy and access-scope review
- source freshness review
- anti-ICP enforcement

Inputs: evidence and message packet on the first pass; target, channel, access, and action packet on the pre-action pass; event ledger and verdict packet on the final pass.
Output: approve, repair, or block verdict with exact reason.
Gate: provenance, recency, privacy, consent, permission, target, and rollback are explicit.
Forbidden: reviewing its own first draft as final, authorizing an external action, or silently deleting contrary evidence.

### ABM Channel Agent

Purpose: choose and prepare the narrowest evidence-backed path to a verified buyer without sending autonomously.

Primary skills:

- `acquisition-channel-advisor`
- company-research
- customer-journey-map
- outreach-sequence-design
- cohort segmentation
- CRM hygiene
- channel-experiment design

Inputs: approved message, target card, channel rules, and owner-defined contact boundary.
Output: warm-intro request, reviewed LinkedIn/email draft, sequence candidate, and send checklist.
Gate: target, channel, message version, source signal, CTA, owner approval, and stop conditions are named.
Forbidden: autonomous sending, connection requests, bulk enrichment, evasion of platform controls, or contact-state inflation.

### Growth Evidence Agent

Purpose: measure stage progression by cohort and forcing moment and prepare the payment verdict.

Primary skills:

- `data-analytics-insight`
- forecast-validation-and-backtesting
- business-health-diagnostic
- funnel instrumentation
- experiment design
- ROI scenario modeling
- payment-stage classification

Inputs: reviewed event ledger and explicit cohort definitions.
Output: stage funnel, objections, cohort comparison, modeled-versus-observed ROI, and pursue/pivot/stop recommendation.
Gate: attention, conversation, proposal, paid intent, and payment remain separate; denominators and missing events are visible.
Forbidden: invented events, cherry-picked cohorts, causal claims from descriptive results, or presenting the browser ROI scenario as observed savings.

### Product Packaging Engineer

Purpose: turn validated service contracts into an installable repository, least-privilege MCP, admin surface, and operator documentation after the E8.0 gate.

Primary skills:

- `backend-api-architecture`
- codebase-design
- code-clarity-and-docs
- `agent-security-governance`
- deployment-observability
- debugging-checklist
- browser-qa-performance-a11y

Inputs: E5 buyer/access/payment evidence, E7 safety benchmark, and approved productization contract.
Output: versioned package, schemas, install/upgrade/uninstall/rollback docs, sandbox proof, and release candidate.
Gate: E8.0, E7.4, least privilege, no stored secrets, source citations, approval before writeback, tenant isolation, rollback, and benchmark pass.
Forbidden: building the product because desk research alone looks promising or enabling write tools by default.

## Forcing-moment routing

| Trigger | Lead research route | Discovery emphasis | Proof object | Primary reviewer |
|---|---|---|---|---|
| Enterprise RFP/questionnaire | Product plus Security/Sales Engineering/RevOps role verification | Deadline, answer ownership, source trust, access | Evidence-linked answer pack | Claims/Safety Reviewer |
| Onboarding/hiring | Product leader plus PM champion | Senior-team interruption, decision recovery, freshness | Onboarding knowledge map | AF Review |
| Key-person departure | Product leader or founder | Handoff urgency, undocumented decisions, owner map | Continuity transfer pack | AF Knowledge plus AF Review |
| AI-agent rework | CTO/engineering plus Product | Context gaps versus model/tool limitations | Context and verification contract | Architecture Operator plus AF Review |
| Chronic search | Product leader; Product Ops may be user/champion, not assumed economic buyer | Repeated questions, contradiction, tolerated alternatives | Source and retrieval diagnostic | Growth Evidence Agent |

## Model and execution policy

- Deterministic extraction, validation, formatting, and scoring should be code-first when possible.
- Luna-class workers may perform bounded public-source extraction or draft variants.
- Terra-class integration is reserved for cross-source reconciliation, shared artifact mutation, or external-board writeback.
- Frontier models are reserved for ambiguous synthesis, sensitive contradiction resolution, and final high-impact language review.
- One role cannot approve its own high-risk output, regardless of model tier.
- Every model call must record model ID, role, input class, outcome, usage if returned, and reviewer state before performance claims are made.

## Promotion and stop rules

Promote a conclusion to audience knowledge only after the evidence and independent review are stored. Stop or downgrade when:

- the company or role is stale;
- there are fewer than two independent account signals;
- the forcing moment is inferred but not confirmed;
- access or consent is ambiguous;
- a message lacks source support;
- the buyer is anti-ICP;
- the action requires an unapproved send, publication, price, payment, or writeback;
- evidence contradicts the current ICP.

Contradiction is a research result and should update the hypothesis rather than trigger another unbounded loop.
