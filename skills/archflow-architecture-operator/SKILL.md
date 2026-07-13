---
name: archflow-architecture-operator
description: Design, audit, or revise ArchFlow agentic architectures and role packs. Use when work concerns Goal Engineering, Loop Engineering, LangGraph sequencing, role and skill allocation, RAG or knowledge-layer boundaries, architecture generation, tool adoption, safety gates, architecture benchmarks, or conversion of a business workflow such as PRD, ICP, content, outreach, finance, engineering, or media into a bounded execution system.
---

# ArchFlow Architecture Operator

## Required order

1. Read the project operating rules, current architecture, goal contract, loop contract, role registry, skill governance, approved corpus policy, and `project/proof-ledger.md`.
2. Classify every statement as `proven`, `review`, `planned`, `blocked`, or `superseded`.
3. Define one goal with an observable done condition, independent verifier, budget, stop rules, and authority boundary.
4. Build a task graph before assigning agents. Keep dependent work sequential and parallelize only independent read-only or bounded extraction work.
5. Bind each task to a role contract and the minimum required skills. A runtime or model name never grants authority.
6. Put LangGraph in charge of state and routing. Use Loop Engineering inside task nodes for bounded maker/checker repair. Never create an unbounded nested loop.
7. Route retrieval through the approved corpus and require source paths, stable document/chunk IDs, and lexical fallback.
8. Require an independent correctness gate and a separate safety/claim gate before memory promotion or external action.
9. Promote only reviewed conclusions to WikiLLM. Treat Graphify as generated structure, Obsidian as human semantic navigation, and Nexus as a live bridge whose availability must be proven.
10. Write a run record, handout, unresolved issue, and decision when the architecture changes materially.

## Selection rules

- Read [architecture-layers.md](references/architecture-layers.md) when creating or reviewing the full system.
- Read [role-packs.md](references/role-packs.md) when assigning company roles, Terra/Luna work, or department-specific skills.
- Read [tool-adoption-gates.md](references/tool-adoption-gates.md) before adding a framework, MCP server, hook, vector store, model, or external skill.
- Read [metrics.md](references/metrics.md) when comparing the architecture with a baseline or deciding whether a trial can graduate.

## Non-negotiable boundaries

- Do not install or execute third-party code before provenance, license, security scan, pinned version, rollback, and bounded test evidence exist.
- Do not use background hooks that bypass permissions or silently mutate a vault.
- Do not let Cognee, a vector store, Notion, a dashboard, or an Obsidian plugin become a competing source of truth.
- Do not claim provider execution, live MCP readiness, retrieval improvement, token savings, or reliability improvement without current measurement.
- Do not change the website, dashboard, deploy, publish, send outreach, or mutate a client system unless the task explicitly authorizes that action and its specific gate passes.
- Interpret `provider-disabled` as zero network/cloud model calls. Local model calls require an explicit `local-model-enabled` contract. Interpret `model-disabled` as zero cloud and local model calls.

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
- durable run, issue, decision, and next safe action.
