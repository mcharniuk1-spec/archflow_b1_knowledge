# Responsibility Matrix

## Agent Segments

| Segment | Agent | Purpose | Output |
|---|---|---|---|
| Source boundary | AF Tools | Verify inputs, env, runtime, and allowed corpus. | Source inventory and readiness report. |
| Context analysis | AF Context | Convert approved input into facts, interpretations, hypotheses, and gaps. | Context digest. |
| Product planning | AF Manager | Convert context into PRD, requirements, stages, and acceptance criteria. | PRD and milestone plan. |
| Research framing | AF Research | Define market, web, ICP, competitor, and content questions for later work. | Research backlog. |
| Knowledge maintenance | AF Knowledge | Convert approved outputs into durable memory and run notes. | KB update packet. |
| Review | AF Review | Check safety, evidence, claims, and boundary compliance. | Review report and status. |
| Publication | AF Publisher | Prepare public-safe Git-ready output after approval. | Release/run note. |
| Retrospective | AF Review plus helper | Identify process failures, missing evidence, and next improvements. | Retrospective notes. |

## Execution Tasks

| Task | Owner | Helper | Status | Acceptance Criteria |
|---|---|---|---|---|
| E1.2.1 Create sanitized source packet | AF Tools | AF Review | ready | Raw source omitted; boundary documented. |
| E1.2.2 Retrieve public context | AF Context | AF Tools | ready | LlamaIndex returns source-path results. |
| E1.2.3 Run parallel topic analysis | AF Context | AF Research | planned | Strategy, product, market, content, and operations sections exist. |
| E1.2.4 Merge summary | AF Manager | AF Context | planned | One sole summary document exists. |
| E1.2.5 Draft PRD | AF Manager | AF Review | planned | PRD includes scope, requirements, nodes, and acceptance criteria. |
| E1.2.6 Segment tasks by agents | AF Manager | AF Knowledge | planned | Responsibility matrix and backlog are explicit. |
| E1.2.7 Write KB update | AF Knowledge | AF Context | planned | Memory, insight, issue, and decision candidates are separated. |
| E1.2.8 Review gate | AF Review | Helper reviewer | planned | Approve, revise, or block with reasons. |
| E1.2.9 Prepare next research layer | AF Research | AF Manager | planned | Web research tasks are defined but not mixed into E1.2 setup. |

## Reviewer And Helper Pattern

The main agent keeps the full project context and execution state. The reviewer agent evaluates output quality, boundary safety, evidence, and sequencing. The helper agent goes deeper into narrow issues identified by the reviewer, then returns findings to the main agent. The main agent decides how to integrate those findings.

## Parallel Analysis Topics

- Strategy and company direction.
- Product requirement extraction.
- Market and ICP questions.
- Content and website implications.
- Runtime and dashboard implications.
- Knowledge-base and memory implications.
