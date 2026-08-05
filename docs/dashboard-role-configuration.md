# Dashboard Role Configuration

Status: current role projection contract
Canonical source: `project/system/contracts/role-catalog.json`

## Canonical fields

Every role defines a read-only public default contract:

- stable role ID, Ukrainian call name, role goal, lane, and responsibility;
- required Knowledge Case inputs;
- one owned output;
- reviewed public skills and abstract tool-capability ceilings;
- permission mode and forbidden actions;
- ordered reviewer route and deterministic handoff target.

Every exported mission materializes a `role_task_binding` with case/workflow IDs, source and requirement references, expected output, exact targets, deterministic checks, typed `GAP-*` references, a fixed handoff payload whose names all resolve to binding fields, and stop conditions.

The dashboard does not edit catalog authority. Users edit the mission, evidence boundary, expected output, risk, reviewer, and stop condition; the Work and Team views project canonical role fields. Missing exact sources, approved requirements, or mutation targets remain visible readiness gaps. A binding does not grant permission, activate a model, or update the catalog.

Effective capability is `case authority ∩ role ceiling ∩ runtime capability ∩ exact targets − denials`. `allowed_actions` may exist only in the case authority object; it is never copied into a role default or synthesized by the dashboard.

## Current call names

| Call name | Stable role ID | Primary responsibility |
|---|---|---|
| Yaromyr | `goal_and_architecture_operator` | Goal, done, state, gates |
| Bohdan | `admission_controller` | Risk, run profile, stop rules |
| Solomiia | `source_and_context_operator` | Allowlist, context, retrieval, capsule |
| Oksana | `requirements_and_market_research` | Evidence, market/pain, requirements, acceptance |
| Taras | `onboarding_guide` | Role-safe onboarding and first mission |
| Danylo | `task_and_handoff_planner` | Dependencies, task packet, checks |
| Olena | `positioning_and_copy_maker` | Positioning, message, caption, claim table |
| Andrii | `qualification_and_channel_planner` | Company/person fit, currentness, channel |
| Kateryna | `designer` | Brief, editable visual/interface, accessibility |
| Dmytro | `implementation_maker` | Claimed change and focused checks |
| Iryna | `action_validator` | Requirements, authority, effects, rollback |
| Mykola | `verifier` | Deterministic verification and readback |
| Halyna | `independent_reviewer` | Approve, revise, or block |
| Larysa | `knowledge_librarian` | Lineage, promotion, supersession, freshness |
| Maksym | `integrator` | Lanes, conflicts, merge, receipts, handoff |
| Pavlo | `external_action_operator` | One exact approved action |
| Nazar | `release_operator` | Release evidence and approved Git action |
| Zoriana | `growth_and_outcome_analyst` | Denominators and observed/modeled outcomes |
| Ostap | `observability_and_efficiency_observer` | Drift, usage evidence, reproducibility gaps |
| Marta | `surface_projection_operator` | Truthful read-only UI and export |
| Roman | `product_packaging_engineer` | Clean clone and lifecycle proof |

All names contain English letters only. JSON remains the canonical machine-readable source.

## Selection

Choose the smallest workflow pack, then add a role only when it owns a required output, check, approval review, or handoff. Keep maker and final reviewer different for consequential work.

Workflow packs store stable role IDs. Call names are resolved only for people-facing display. Reviewer-route closure is deterministic and terminates at `@case_owner`; unknown roles, self-review, cycles, and handoff mismatches fail validation.
