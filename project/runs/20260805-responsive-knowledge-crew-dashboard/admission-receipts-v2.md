# Canonical Admission Receipts V2

Status: emitted by the local provider-disabled LangGraph admission launcher after the canonical role/state repair.

## Architecture

- Run: `20260805-responsive-knowledge-crew-dashboard-architecture`
- Profile: `architecture`
- Receipt: `sha256:fc2170338235ce646cd36e4d8a8409875738c7b8abc556911fa9cf7a303dc399`
- Admission sequence: `admission.validated → admission.cag_bound → admission.role_plan_composed → admission.retrieval_plan_bound → admission.accepted_planning_only`
- Current workflow state: `context_bound`
- Planned workflow: `work_planning → candidate_review → answered`
- Roles: Yaromyr / `goal_and_architecture_operator`; Bohdan / `admission_controller`; Halyna / `independent_reviewer`; Maksym / `integrator`

## Operator Surface

- Run: `20260805-responsive-knowledge-crew-dashboard-surface`
- Profile: `documentation`
- Receipt: `sha256:f0e54ffa48090ed3a0ed79edc23d7b046692227365dfa3a2eb559b3f47cac55a`
- Admission sequence: `admission.validated → admission.cag_bound → admission.role_plan_composed → admission.retrieval_plan_bound → admission.accepted_planning_only`
- Current workflow state: `context_bound`
- Planned workflow: `work_planning → candidate_review → answered`
- Roles: Marta / `surface_projection_operator`; Halyna / `independent_reviewer`; Maksym / `integrator`

Both receipts state `crew_kickoff: false`, `task_invoked: false`, `checkpoint_write: false`, `writes: false`, `external_actions: false`, and `provider_mode: disabled`. The receipt hashes supersede the earlier v1 hashes, which remain historical in immutable reviewer reports only.
