# Skill Packages by Functional Role

This page maps the ten portable public packages to the canonical roles that may use them. The role catalog, not this prose page, controls the machine-readable assignment.

## Package registry

| Package | Reusable job | Canonical roles |
|---|---|---|
| [`arcagcom`](../../skills/arcagcom/SKILL.md) | Coordinate file claims, bounded lanes, conflict stops, and handoffs | Implementation Maker; Integrator |
| [`archflow-agent-control`](../../skills/archflow-agent-control/SKILL.md) | Convert an approved report into role, task, permission, review, and stop contracts | Admission Controller; Action Validator; Integrator |
| [`archflow-architecture-operator`](../../skills/archflow-architecture-operator/SKILL.md) | Define or audit goals, loops, role architecture, retrieval, gates, and benchmarks | Goal and Architecture Operator; Product Packaging Engineer |
| [`archflow-e1-runtime-guard`](../../skills/archflow-e1-runtime-guard/SKILL.md) | Run provider-disabled configuration, schema, safety, and runtime checks | Verifier; Release Operator; Observability and Efficiency Observer; Product Packaging Engineer |
| [`archflow-knowledge-service`](../../skills/archflow-knowledge-service/SKILL.md) | Build a source-bounded evidence packet and a reviewed knowledge candidate | Source and Context Operator; Requirements and Market Research; Onboarding Guide; Positioning and Copy Maker; Qualification and Channel Planner; Knowledge Librarian; Surface Projection Operator |
| [`archflow-task-breakdown`](../../skills/archflow-task-breakdown/SKILL.md) | Turn an approved objective into ordered tasks, dependencies, checks, and gates | Task and Handoff Planner |
| [`humanize-writing`](../../skills/humanize-writing/SKILL.md) | Polish supplied prose without changing protected facts or claims | Positioning and Copy Maker |
| [`outquestions`](../../skills/outquestions/SKILL.md) | Expose blocking decisions, evidence gaps, and the next safe gate | Action Validator; Independent Reviewer; External Action Operator; Growth and Outcome Analyst; Observability and Efficiency Observer |
| [`priority-task-operator`](../../skills/priority-task-operator/SKILL.md) | Select the highest-priority eligible task from a caller-supplied plan | Task and Handoff Planner |
| [`task-handout`](../../skills/task-handout/SKILL.md) | Prepare a durable, public-safe handoff for the next operator | Task and Handoff Planner; Knowledge Librarian; Integrator; Release Operator |

## Method capabilities are not packages

The 21 roles also use capabilities such as source-boundary control, dependency mapping, factual classification, accessibility review, idempotency planning, exact-target readback, or claim calibration. These are methods applied inside a task contract. They do not create an eleventh skill package, activate a provider, or prove a tool is available.

The Designer intentionally has no default package. Its exact design capability must be supplied by the case and remain within the tools and target permissions allowed by the canonical catalog. Roles outside the four reusable packs remain available for custom cases, but every custom selection still needs admission, an output owner, an independent review route, and integration.

## Role-pack distribution

| Stage | Pack | Makers | Review and integration |
|---|---|---|---|
| Research | `research_to_decision` | Requirements and Market Research; Source and Context Operator | Admission Controller; Independent Reviewer; Integrator |
| Define | `definition_to_task_graph` | Goal and Architecture Operator; Task and Handoff Planner | Admission Controller; Action Validator; Independent Reviewer; Integrator |
| Act | `responsive_product_change` | Product Packaging Engineer; Implementation Maker | Admission Controller; Verifier; Independent Reviewer; Integrator |
| Remember | `reviewed_memory_update` | Knowledge Librarian | Admission Controller; Independent Reviewer; Integrator |

The source of truth for these memberships is [`actionable-role-packs.json`](actionable-role-packs.json). A pack is configuration until a caller supplies an approved case and binds each role to a bounded task.
