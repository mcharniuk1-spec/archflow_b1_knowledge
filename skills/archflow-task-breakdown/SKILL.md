---
name: archflow-task-breakdown
description: Break ArchFlow epics, tasks, and Notion initiatives into staged subtasks with execution order, gates, acceptance criteria, and public-safe reporting. Use for Block 1 knowledge-base work, LangGraph/CrewAI/LlamaIndex runtime planning, Notion task updates, agent-system architecture, and any ArchFlow task that must be decomposed without installing or changing everything at once.
---

# ArchFlow Task Breakdown

## Purpose

Use this skill to turn an ArchFlow epic or task into a reliable execution structure that a human, Codex, Claude, Cursor, LangGraph, or CrewAI team can follow. The output should be Notion-ready and should preserve the current ArchFlow global goal:

`dialogue/chat/meeting material -> structured context -> PRD -> responsibility plan -> agent-ready knowledge base -> review gate -> ICP/research/outreach/payment test`

## Required Context

Before decomposing work, read the active ArchFlow routing files when available:

- `AGENTS.md`
- `public/project/project-plan.md`
- `public/project/agentic-stack.md`
- `workflow/13_resetup/README.md`
- `workflow/13_resetup/agents/agent5_final_resetup_prompt.md`
- `workflow/13_resetup/agents/agent6_block1_execution_pod.md`

Treat older STR and AutoFin material as history unless the user explicitly reactivates it.

## Decomposition Workflow

1. Identify the active epic and stop condition.
   - Write the main objective in one sentence.
   - Define what "done" means in files, Notion, verification, and memory.
   - Separate current execution from later research, content, website, and outreach work.

2. Apply the staged order.
   - Git safety.
   - Env/config.
   - Ollama.
   - LangSmith.
   - LangGraph.
   - Pydantic/YAML validation.
   - LlamaIndex.
   - CrewAI.
   - Observability/provenance papers and run reports.

3. Split each parent task into 4 to 8 subtasks.
   - Use IDs such as `E1.1.1`, `E1.1.2`, and so on.
   - Put dependencies before dependent work.
   - Keep each subtask small enough to verify in one focused run.
   - Do not combine package installation, configuration, runtime proof, and documentation in one subtask.

4. Add gates to every risky stage.
   - Network, credentials, GUI, live Notion, Git push, public website, production deploy, and broad ingestion all need explicit approval or a clear user request.
   - Never store secrets, raw credentials, private Notion links, or raw private transcripts in public files.
   - Use sanitized source packets before any public-safe proof run.

5. Assign execution agents.
   - `AF Tools`: source inventory, config, tool readiness, missing runtime checks.
   - `AF Context`: source summary, decision log, facts/assumptions/gaps.
   - `AF Manager`: PRD, backlog, responsibilities, success metrics.
   - `AF Knowledge`: KB update packet, source registry, memory candidates.
   - `AF Review`: evidence, safety, public-readiness, and final approval.

6. Define acceptance criteria and verification.
   - Each subtask needs a concrete output, check, and blocker rule.
   - Use small checks first: `git status`, env example parse, YAML parse, model smoke test, schema validation, retrieval smoke test, review checklist.
   - A task is not done if the result only exists in chat.

7. Prepare Notion-ready content.
   - Parent task page: executive summary, method, staged execution plan, questions to answer, acceptance criteria, risks, next actions.
   - Subtask records: task ID, title, status, type, dates, parent reference in notes, and one clear expected output.
   - Do not create duplicate parent tasks if an existing parent page exists.

8. Record durable results.
   - Save public-safe reports in `public/project/reports/` when requested.
   - Save run notes in `public/project/runs/` or the approved WikiLLM run layer.
   - Update memory only for reusable rules, corrected assumptions, or future-run implications.

## Output Shape

For each epic or parent task, produce:

- Summary paragraph.
- Key bullet points.
- Stage table with dependency, owner agent, output, check, and gate.
- Explicit todo list.
- Questions to answer before execution.
- Risks and mitigations.
- Acceptance criteria.
- Next execution step.

For each subtask, produce:

- ID and title.
- Why it exists.
- Inputs.
- Actions.
- Output.
- Verification.
- Blocker/approval rule.

## Decision Labels

Use these labels for meaningful planning conclusions:

```text
FACT:
INTERPRETATION:
HYPOTHESIS:
GAP:
```

Keep trivial mechanical steps concise, but never hide uncertainty in confident sequencing.

## Failure Modes

- Do not install every framework at once.
- Do not use CrewAI before the LangGraph control path and validation schema are defined.
- Do not index broad folders before the approved corpus is declared.
- Do not make LangSmith traces from raw private material.
- Do not publish public claims before the payment or firm-intent test validates demand.
