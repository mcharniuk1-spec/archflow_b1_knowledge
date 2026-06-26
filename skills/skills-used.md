# Skills And Methods Used

This project uses the following skills and methods.

## Used In This Setup

| Skill or Method | Use |
|---|---|
| Notion spec-to-implementation | Read the private project board and convert it into an implementation plan. |
| Notion knowledge capture | Extract reusable project knowledge without copying private raw content. |
| [`archflow-task-breakdown`](archflow-task-breakdown/SKILL.md) | Break ArchFlow epics and parent tasks into staged subtasks, gates, and public-safe execution outputs. |
| [`archflow-e1-runtime-guard`](archflow-e1-runtime-guard/SKILL.md) | Validate the E1 runtime spine and connect the saved skill workflow to the Git pre-push hook. |
| [`task-handout`](task-handout/SKILL.md) | Produce readable human summaries and copy-ready continuation prompts after substantial executions. |
| ArchFlow resetup contract | Preserve the June 24 company reset and Block 1 direction. |
| Public-safety review | Keep public files free of secrets, personal data, local paths, and private IDs. |
| Ollama local check | Start local Ollama, list models, and run public-safe smoke tests. |
| Git publication flow | Initialize and publish only the public project folder. |

## Planned For Execution

| Skill or Method | Use |
|---|---|
| AF Graph | Run controlled Block 1 workflows. |
| AF RAG | Query approved project knowledge. |
| AF Crew | Split work across named agent roles. |
| AF Review | Approve or block output before handoff. |
| E1 runtime guard | Pre-push runtime validation for workflow YAML, LangGraph, LlamaIndex, CrewAI, and saved skills. |

## Agent Roles

| Role | Output |
|---|---|
| Tools Analyzer | Source inventory, extraction plan, tool gaps. |
| Context Analyzer | Context digest, facts, interpretations, hypotheses, gaps. |
| Manager / PRD Agent | PRD, backlog, owner matrix, metrics. |
| Knowledge Agent | KB update packet and memory candidates. |
| Reviewer | Final approval or blocked status. |
| Evening registry automation | Skill registry refresh, validation, and run-note upkeep. |
| Task handout | Agent-readable handoff prompt and human execution summary after large runs. |

## Per-Agent Skill Registry

See `project/agents/skills-by-agent.md`.

This project intentionally publishes only the skills used or set up for ArchFlow agents. It does not publish the operator's full private skill inventory.
