---
name: archflow-architecture-operator
description: Design, audit, or revise ArchFlow agentic architectures and role packs. Use when work concerns Goal Engineering, Loop Engineering, LangGraph sequencing, role and skill allocation, RAG or knowledge-layer boundaries, architecture generation, tool adoption, safety gates, architecture benchmarks, or conversion of a business workflow such as PRD, ICP, content, outreach, finance, engineering, or media into a bounded execution system.
---

# ArchFlow Architecture Operator

## Required order

1. Read the operating rules, goal and loop contracts, role and skill registries, approved corpus policy, `project/config/provider-registry.json`, and the retained database schemas.
2. Classify every statement as `proven`, `review`, `planned`, `blocked`, or `superseded`.
3. Define one goal with an observable done condition, independent verifier, budget, stop rules, and authority boundary.
4. Build a task graph before assigning agents. Keep dependent work sequential and parallelize only independent read-only or bounded extraction work.
5. Bind each task to a role contract and the minimum required skills. A runtime or model name never grants authority.
6. Put LangGraph in charge of state and routing. Use Loop Engineering inside task nodes for bounded maker/checker repair. Never create an unbounded nested loop.
7. Route retrieval through the approved corpus and require source paths, stable document/chunk IDs, and lexical fallback.
8. Require an independent correctness gate and a separate safety/claim gate before memory promotion or external action.
9. Shape reusable reviewed meaning as `project/database/solution-memory-record.schema.json`. A candidate is not promoted merely because it validates.
10. Write planning evidence inline or to a caller-supplied Git-ignored output directory. Use retained review and receipt schemas for verified results; never depend on tracked run history.

## Selection rules

- Read [architecture-layers.md](references/architecture-layers.md) when creating or reviewing the full system.
- Read [role-packs.md](references/role-packs.md) when assigning team roles, lead-integrator / bounded-worker coordination, or function-specific skills.
- Read [tool-adoption-gates.md](references/tool-adoption-gates.md) before adding a framework, MCP server, hook, vector store, model, or external skill.
- Read [metrics.md](references/metrics.md) when comparing the architecture with a baseline or deciding whether a trial can graduate.

## Non-negotiable boundaries

- Do not install or execute third-party code before provenance, license, security scan, pinned version, rollback, and bounded test evidence exist.
- Do not use background hooks that bypass permissions or silently mutate storage.
- Do not let a connector, vector store, dashboard, or plugin become a competing source of truth.
- Do not claim provider execution, live MCP readiness, retrieval improvement, token savings, or reliability improvement without current measurement.
- Do not change a website or dashboard, deploy, publish, send outreach, or mutate another system unless the task explicitly authorizes that action and its specific gate passes.
- Interpret `provider-disabled` as zero network/cloud model calls. Local model calls require an explicit `local-model-enabled` contract. Interpret `model-disabled` as zero cloud and local model calls.
- Treat `project/config/provider-registry.json` as the canonical provider truth surface. A documented adapter, environment-variable name, or browser display state does not prove availability or authorization.
- Do not fabricate an action receipt. Create `project/database/action-receipt.schema.json` evidence only after the action and checks occurred; keep an unexecuted proposal clearly distinct.
- Treat `project/database/review-bundle.schema.json` as a browser-local review shape, never an authorization signal. A maker still cannot approve its own high-risk output.

## Output contract

Return or write:

- goal contract and evidence state;
- architecture diagram or ordered layer map;
- task graph with dependencies;
- role/skill matrix and maker/checker separation;
- allowed corpus and retrieval mode;
- budgets, stop conditions, approval boundaries, and rollback;
- verification and safety checks;
- measured results or explicitly labeled hypotheses;
- independent-review verdict and next safe action;
- action receipt only when execution evidence exists;
- optional solution-memory candidate after reviewer approval.

Save auxiliary planning artifacts only to an explicitly supplied ignored local directory, or return them inline. Repository edits, provider calls, deployment, Git actions, and external writeback remain separately scoped actions.
