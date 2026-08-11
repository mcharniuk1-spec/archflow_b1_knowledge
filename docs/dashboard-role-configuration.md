# Dashboard Role Configuration

Status: current role projection contract
Canonical source: `project/system/contracts/role-catalog.json`

## Canonical fields

Every role defines a read-only public default contract:

- stable role ID, deterministic functional display label, role goal, lane, and responsibility;
- required Knowledge Case inputs;
- one owned output;
- reviewed public skills and abstract tool-capability ceilings;
- permission mode and forbidden actions;
- ordered reviewer route and deterministic handoff target.

Every exported mission materializes a `role_task_binding` with case/workflow IDs, source and requirement references, expected output, exact targets, deterministic checks, typed `GAP-*` references, a fixed handoff payload whose names all resolve to binding fields, and stop conditions.

The dashboard does not edit catalog authority. Users edit the case objective, evidence boundary, expected output, reviewer, and stop condition in **Project**; **Roles & Skills** projects canonical role fields and the onboarding/teamwork schema. Missing exact sources, approved requirements, or mutation targets remain visible readiness gaps. A binding does not grant permission, activate a model, or update the catalog.

Effective capability is `case authority ∩ role ceiling ∩ runtime capability ∩ exact targets − denials`. `allowed_actions` may exist only in the case authority object; it is never copied into a role default or synthesized by the dashboard.

## Functional display labels

| Functional label | Stable role ID | Primary responsibility |
|---|---|---|
| GoalAndArchitectureOperator | `goal_and_architecture_operator` | Goal, done, state, gates |
| AdmissionController | `admission_controller` | Risk, run profile, stop rules |
| SourceAndContextOperator | `source_and_context_operator` | Allowlist, context, retrieval, capsule |
| RequirementsAndMarketResearch | `requirements_and_market_research` | Evidence, market/pain, requirements, acceptance |
| OnboardingGuide | `onboarding_guide` | Role-safe onboarding and first mission |
| TaskAndHandoffPlanner | `task_and_handoff_planner` | Dependencies, task packet, checks |
| PositioningAndCopyMaker | `positioning_and_copy_maker` | Positioning, message, caption, claim table |
| QualificationAndChannelPlanner | `qualification_and_channel_planner` | Company/person fit, currentness, channel |
| Designer | `designer` | Brief, editable visual/interface, accessibility |
| ImplementationMaker | `implementation_maker` | Claimed change and focused checks |
| ActionValidator | `action_validator` | Requirements, authority, effects, rollback |
| Verifier | `verifier` | Deterministic verification and readback |
| IndependentReviewer | `independent_reviewer` | Approve, revise, or block |
| KnowledgeLibrarian | `knowledge_librarian` | Lineage, promotion, supersession, freshness |
| Integrator | `integrator` | Lanes, conflicts, merge, receipts, handoff |
| ExternalActionOperator | `external_action_operator` | One exact approved action |
| ReleaseOperator | `release_operator` | Release evidence and approved Git action |
| GrowthAndOutcomeAnalyst | `growth_and_outcome_analyst` | Denominators and observed/modeled outcomes |
| ObservabilityAndEfficiencyObserver | `observability_and_efficiency_observer` | Drift, usage evidence, reproducibility gaps |
| SurfaceProjectionOperator | `surface_projection_operator` | Truthful read-only UI and export |
| ProductPackagingEngineer | `product_packaging_engineer` | Clean clone and lifecycle proof |

Each compatibility `call_name` is the PascalCase projection of its stable role ID, contains English letters only, and is unique. JSON remains the canonical machine-readable source.

## Selection

Choose the smallest workflow pack, then add a role only when it owns a required output, check, approval review, or handoff. Keep maker and final reviewer different for consequential work.

Workflow packs store stable role IDs. Functional labels are resolved only for people-facing display and never carry authority. Reviewer-route closure is deterministic and terminates at `@case_owner`; unknown roles, self-review, cycles, and handoff mismatches fail validation.
