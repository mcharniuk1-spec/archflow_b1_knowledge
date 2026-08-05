# API and Packet Contract

Status: browser packet current; network execution adapters gated

The public Crew Desk uses fixed static JSON contracts and exports local review packets. It does not require an API.

## Local review packet

```json
{
  "schema_version": "2.0.0",
  "kind": "archflow_local_review_packet",
  "generated_at": "<timestamp>",
  "boundary": {
    "provider_called": false,
    "writeback_performed": false,
    "external_action_performed": false,
    "authority": "browser-local proposal only"
  },
  "case": {},
  "selected_workflow": {},
  "role_task_bindings": [
    {
      "binding_id": "binding-example-taras",
      "case_id": "case-example",
      "workflow_pack_id": "employee_onboarding",
      "base_or_closure": "base",
      "role_id": "onboarding_guide",
      "call_name": "Taras",
      "role_goal": "Give an employee role-safe context, explain why the work matters, and propose a validated first action.",
      "inputs": ["case.goal", "case.authority.requester_role", "case.requirements", "case.evidence", "case.gaps"],
      "source_refs": ["fixtures/synthetic-role-handbook.md#action-policy"],
      "requirement_refs": ["REQ-ONBOARD-001@1"],
      "owned_output": "employee_mission_card",
      "expected_output": "A source-visible first mission with an explicit escalation path.",
      "allowed_skills": ["archflow-knowledge-service"],
      "allowed_tools": ["read_contracts", "read_allowlisted_sources", "query_bounded_retrieval", "draft_local_artifact"],
      "known_gaps": [],
      "permission_boundary": {
        "authority_ref": "case.authority",
        "mode": "read_draft_only",
        "exact_targets_ref": "binding.exact_targets",
        "forbidden_actions_ref": "role_catalog.roles.onboarding_guide.forbidden",
        "rule": "intersection_only_no_authority_expansion"
      },
      "forbidden_actions": ["invented_company_truth", "permission_inheritance", "employee_monitoring", "unvalidated_instruction"],
      "exact_targets": [],
      "deterministic_checks": ["requirement reference present", "reviewer route terminates"],
      "reviewer_route": ["action_validator", "independent_reviewer", "@case_owner"],
      "handoff": {
        "to": "action_validator",
        "payload": ["case_id", "binding_id", "role_id", "owned_output", "source_refs", "requirement_refs", "exact_targets", "deterministic_checks", "known_gaps", "stop_conditions"]
      },
      "stop_conditions": ["current requirement missing", "source boundary invalid", "authority unresolved"]
    }
  ],
  "settings": {},
  "receipt_count": 0,
  "configuration_refs": {}
}
```

An approved runtime must revalidate the packet. Browser state is not authority or a checkpoint.

The example binding contains all 22 required fields from [role-task-binding.schema.json](../project/system/schemas/role-task-binding.schema.json); the complete eight-binding [onboarding fixture](../project/system/fixtures/onboarding-case.json) is the normative executable example. Role bindings are generated from the canonical catalog and selected workflow pack. `known_gaps` contains typed `GAP-*` references from the case; every handoff payload name must resolve to a binding field. Empty source, requirement, gap, or exact-target arrays are explicit states, not permission to infer missing values. The binding schema forbids an `allowed_actions` field.

Configuration import accepts `turbovec_candidate` only as the literal JSON booleans `true` or `false`. Strings, numbers, `null`, arrays, and objects are rejected transactionally without changing saved settings.

## Static reads

The dashboard fetches only:

- `project/system/contracts/knowledge-crew-config.json`
- `project/system/contracts/role-catalog.json`
- `project/system/contracts/role-workflows.json`
- `project/system/contracts/operating-model.json`
- `project/dashboard/data.json`

## Optional local bridge

Configuration accepts only:

- the current page origin;
- `http://127.0.0.1:<port>`;
- `http://localhost:<port>`.

The public UI does not automatically call the configured bridge. A future bridge must authenticate, bind case/actor/target authority, validate schema versions, enforce idempotency, store server-side secrets, and return exact receipts/readback.

## Compatibility endpoints

Older PRD/ICP and agent-orchestra endpoints, when present in historical services, are compatibility packet adapters only. They must normalize to the same Knowledge Case; they are not separate architectures. They remain provider/writeback disabled unless their current runtime proves all gates.

## Required action request

Any network action request must include:

- case and action IDs;
- actor role and accountable owner;
- exact operation, target class, and target;
- current requirement/decision versions;
- permission scope;
- side effects, reversibility, rollback;
- deterministic preflight and postcondition;
- readback;
- independent reviewer;
- target-specific approval when required.

Missing or stale fields fail closed.
