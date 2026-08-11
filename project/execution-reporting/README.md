# Execution reporting contract

Every meaningful ArchFlow execution should leave one public-safe execution report in an ignored caller-controlled workspace such as `project/local/execution-reports/<run-id>/execution-report.md`. The report is the audit bridge between the task contract, role work, architecture layers, checks, deliverables, and reviewed memory. Reports are not committed automatically.

## Required evidence

Each report records:

- run ID, objective, execution type, risk, and terminal status;
- the integrator, each actor/reviewer lane, claimed file scope, and whether the lane actually executed;
- packaged skills and project methods used by each actor, with `used`, `configured_only`, or `not_recorded` status;
- deliverables, source references, check commands, measured results, and remaining gaps;
- LangGraph state/route/checkpoint evidence;
- CrewAI role/task evidence and whether the result is direct runtime proof or only a configured contract;
- LlamaIndex corpus/retrieval evidence, source-path compliance, fallback state, and benchmark result;
- parallel branch claims, overlap result, handoff, and integrator merge decision;
- interpretation of the evidence and the next conclusive gate;
- memory promotion destination, or an explicit `not_promoted` reason.

## Truth states

Use only these execution states: `configured`, `planned`, `locally_tested`, `executed`, `reviewed`, `promoted`, `blocked`, and `not_recorded`. A configuration file is not execution proof. A passing smoke test is not provider, deployment, uptime, or writeback proof.

## Conclusive metrics

The minimum evidence set is:

| Metric | Conclusive when | Interpretation |
|---|---|---|
| `artifact_completeness` | all required deliverables have paths, status, and checksum or parse result | The run produced the promised package, not just chat output. |
| `claim_traceability` | every material claim links to a repo-relative source or check | The report is source-grounded. |
| `agent_accountability` | every executed lane names actor, skills, scope, reviewer, and handoff | Work can be attributed and independently checked. |
| `parallel_conflict_free` | all branch claims are exclusive and merge review passes | Parallelism preserved ownership instead of creating hidden overwrite risk. |
| `langgraph_state_evidence` | run ID, node route, terminal state, and checkpoint/absence are recorded | The controller state is observable; it does not prove a live always-on service. |
| `crewai_role_evidence` | role/task mapping and runtime level are recorded | CrewAI contribution is distinguished from LangGraph control and direct runtime activation. |
| `llamaindex_source_evidence` | corpus boundary, retrieval mode, source paths, and fallback/benchmark are recorded | Retrieval is bounded and reproducible; similarity alone is insufficient. |
| `review_verdict` | independent review returns `accept`, `revise`, or `block` | Completion is a reviewed decision, not self-reporting. |
| `memory_promotion` | destination, reviewer, promotion status, or explicit `not_promoted` reason is recorded | Durable memory is intentional and auditable. |

Missing evidence is a metric value of `not_recorded`, never an inferred pass.

If an organization later evaluates a separately authorized provider adapter, its metrics are conclusive only when the report contains the exact run ID, timestamp, adapter, approved model identifier, approval, prompt/output tokens, actual cost, pricing source, latency, and ledger entry. The public release contains no provider run history. Browser-local or static dashboard events never enter a runtime execution ledger.

## Maintained-knowledge structure

Keep the full working report under the ignored local execution-report root. Promote only independently reviewed, reusable meaning into `project/database/solution-memory-record.schema.json` or an organization-specific private system that preserves source lineage, freshness, supersession, and access control. Never commit raw prompts, private inputs, browser state, or accumulated run archives as product data.
