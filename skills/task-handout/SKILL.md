---
name: task-handout
description: Create a public-safe execution handout after substantial project work, multi-agent routing, or subtask execution. Use when a prompt hook asks for it, when a run uses one or more agent roles, when one or more subtasks are solved or changed, or when another operator needs a readable human summary plus an agent-ready continuation prompt.
---

# Task Handout

## Purpose

Use this skill at the start and end of any substantial execution, review, planning run, dialogue-to-output cycle, multi-agent operation, or subtask-solving pass. The handout is the bridge between logs and future execution: it explains what happened in human language, then gives another agent a concrete continuation prompt grounded in files, decisions, validation evidence, and open gaps.

The handout does not replace run logs, decisions, or WikiLLM memory. It makes them usable by the next operator.

## When To Use

- When the prompt hook emits `TASK_HANDOUT_HOOK_TRIGGER=required`.
- After a large Codex execution or multi-agent pass.
- When a prompt invokes one or more AF agents, LangGraph/CrewAI routing, parallel agents, reviewer/helper agents, or role-based execution.
- When the work solves, updates, creates, reviews, or starts one or more subtasks.
- When the user asks for a handout, continuation prompt, agent cooperation summary, or readable execution summary.
- Before handing work to another agent or a future thread.
- After converting dialogue, meeting notes, or strategic context into PRDs, tasks, and knowledge-base updates.

## Hook Trigger Contract

This project has a prompt hook at `.codex/hooks.json` that calls:

```bash
python3 project/scripts/task-handout-hook.py --event UserPromptSubmit
```

The hook is a reminder and routing guard. It does not write a handout by itself, because a prompt-level hook does not know which files and checks will exist after execution. It only marks that this prompt requires the skill. The executing agent must then read this skill and maintain the handout during or before finalization.

Trigger the skill when any of these are true:

- The prompt directly mentions task handout, handoff, continuation prompt, or hook trigger.
- The prompt invokes AF agent hooks, multi-agent work, parallel agents, reviewer/helper agents, LangGraph plus CrewAI, or one or more agents.
- The prompt asks to solve, update, create, review, or start one or more subtasks.
- The execution actually uses one or more agent roles or changes one or more subtask outputs, even if the initial prompt did not say so.

For execution-time use, run this helper manually when needed:

```bash
python3 project/scripts/task-handout-hook.py --event execution --force
```

Then create or update the run handout before the final response.

## Required Inputs

Collect only public-safe inputs:

1. User goal and current task stage.
2. Files created or changed.
3. Current status of the task, subtasks, and blockers.
4. Decisions made and why.
5. Checks run and their outcomes.
6. Known gaps, deferred items, and next actions.
7. The exact continuation boundary for the next agent.

Do not copy raw private transcripts, credentials, private URLs, local absolute paths, account IDs, or unapproved source material into a public handout.

## Output Location

For project runs, save the handout beside the run artifacts:

```text
project/runs/<run-id>/agent-handout.md
```

If the handout summarizes a separate execution that has no existing run folder, create:

```text
project/runs/<YYYY-MM-DD-short-run-name>/agent-handout.md
```

For durable memory, add a short run note under `wiki/runs/` only when the handout changes how future agents should operate.

## Required Structure

Use this structure unless the project has a stronger local template:

1. **Title and Purpose**
   - State what the handout covers and who should use it.

2. **Human Summary**
   - Write two to five readable paragraphs.
   - Explain the work in plain language, not just bullets.
   - Include what changed, why it matters, and what remains.

3. **Current State**
   - Task status.
   - Main artifacts.
   - Runtime or process readiness.
   - Any external board or publication state if verified.

4. **Agent Continuation Prompt**
   - Provide a copy-ready prompt for another agent.
   - Include goal, context files, constraints, first steps, expected outputs, and stop conditions.

5. **Execution Trace**
   - Summarize the run sequence.
   - Separate facts from interpretations when there are meaningful conclusions.

6. **Decisions**
   - Record decisions made and their rationale.
   - Mark deferred decisions explicitly.

7. **Artifacts**
   - Link to relative project files.
   - Describe what each file is for.

8. **Validation**
   - List checks run and pass/fail status.
   - If a check was skipped, explain why.

9. **Next Actions**
   - Give ordered next steps.
   - Include agent ownership when relevant.

10. **Safety Boundary**
   - State what must not be ingested, copied, published, or logged.

## Writing Rules

- Keep the handout in English.
- Make it readable for a human first, then actionable for an agent.
- Use relative paths inside public repositories.
- Link to files instead of duplicating large content.
- Prefer concrete status claims backed by artifacts or checks.
- Mark speaker ownership, market assumptions, and strategic interpretations as inferred unless verified.
- Keep public-safe summaries separate from private raw sources.

## Done Criteria

The handout is complete when a new agent can:

- Identify the current goal and stage.
- Find the relevant files without chat history.
- Understand what was executed and verified.
- Continue with the next task without redoing discovery.
- Avoid private-source and secret-handling mistakes.
