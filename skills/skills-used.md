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
| [`outquestions`](outquestions/SKILL.md) | Report what changed after each substantial execution and list the decision questions required before the next stage. |
| ArchFlow resetup contract | Preserve the June 24 company reset and Block 1 direction. |
| Loop Engineering operating contract | Keep agent workflows bounded with state, attempt caps, budget, maker/checker separation, and stop conditions. |
| Market evidence engine | Turn E2 into account universe, public-signal extraction, scoring, role verification, and reviewed ICP/output handoff. |
| Public-safety review | Keep public files free of secrets, personal data, local paths, and private IDs. |
| Ollama local check | Start local Ollama, list models, and run public-safe smoke tests. |
| Git publication flow | Initialize and publish only the public project folder. |

## Planned For Execution

| Skill or Method | Use |
|---|---|
| AF Graph | Run controlled Block 1 workflows. |
| AF RAG | Query approved project knowledge. |
| AF Crew | Split work across named agent roles. |
| AF Research | Build evidence cards, pain maps, ICP scorecards, and target shortlists. |
| AF Copy | Draft positioning, content, and outreach only from approved evidence. |
| AF Review | Approve or block output before handoff. |
| E1 runtime guard | Pre-push runtime validation for workflow YAML, LangGraph, LlamaIndex, CrewAI, and saved skills. |
| Outquestions | End each substantial run with next-stage decision questions, gates, risks, and a clear nontechnical report. |

## Agent Roles

| Role | Output |
|---|---|
| Tools Analyzer | Source inventory, extraction plan, tool gaps. |
| Context Analyzer | Context digest, facts, interpretations, hypotheses, gaps. |
| Manager / PRD Agent | PRD, backlog, owner matrix, metrics. |
| Research Agent | Account evidence cards, competitor gaps, pain maps, ICP scoring. |
| Knowledge Agent | KB update packet and memory candidates. |
| Copy Agent | Website positioning, content angles, outreach drafts, proposal copy. |
| Reviewer | Final approval or blocked status. |
| Evening registry automation | Skill registry refresh, validation, and run-note upkeep. |
| Task handout | Agent-readable handoff prompt and human execution summary after large runs. |
| Outquestions reporter | Decision questions and stage gates after each substantial execution. |

## Per-Agent Skill Registry

See `project/agents/skills-by-agent.md`.

This project intentionally publishes only the skills used or set up for ArchFlow agents. It does not publish the operator's full private skill inventory.
