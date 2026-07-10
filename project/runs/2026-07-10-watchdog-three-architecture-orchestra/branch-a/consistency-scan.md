# Role / Runtime Consistency Scan

Status: complete on 2026-07-10.

## Scope

- `AGENTS.md`
- `project/operating-rules.md`
- `project/agentic-stack.md`
- `project/context/cag-core.yaml`
- `project/agents/agent-roster.yaml`
- `project/agents/skills-by-agent.md`
- `project/workflows/langgraph-controller.yaml`
- `project/workflows/crewai-crew.yaml`

## FACT

- The governing contracts previously contained several current-runtime labels, including Codex, Hermes, and named dashboard roles.
- Existing contracts already prohibited watchdog execution, high-risk self-approval, unapproved provider activation, deployment, and external writeback.
- The scan added an explicit role/runtime policy where missing and relabeled current bindings so they cannot be read as permanent authority.

## INTERPRETATION

Named runtimes and agent keys remain useful implementation bindings. Their authority now derives from the assigned role contract, which preserves a separate verifier/safety gate and blocks self-review of high-risk work even if one runtime could technically fulfil multiple roles.

## GAP

This configuration consistency evidence does not prove a running LangGraph/CrewAI service, a provider route, or hosted freshness. Dependency-backed workflow validation remains unavailable in the current interpreter because its YAML dependency is absent; no installation was authorized.
