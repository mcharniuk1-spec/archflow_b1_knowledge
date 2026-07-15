# Operations Guide

## Two operating surfaces

The dashboard and Jarvis share a browser-local activity record. It contains only preview mode and local report/handoff references; it is not authentication, account memory, a database record, or a runtime event feed. In Guest preview, prepare Knowledge Service first and retain a public-safe boundary. In Admin preview, an operator may also reference an existing reviewed local report, but all real actions remain separately gated.

### Knowledge Service

Use this surface when approved product, research, or customer information needs to become a reviewed output: a PRD, ICP, decision brief, backlog, research packet, or knowledge update.

Inputs mean:

- **Request:** the outcome needed and its forcing moment.
- **Source boundary:** the approved summaries, paths, or references that may support the packet.
- **Output contract:** the artifact shape, reviewer, and decision it must support.
- **Approval gate:** the named operator who may advance a reviewed packet.

The result is a source-grounded packet that separates facts, interpretations, hypotheses, and gaps. It cannot ingest broad private storage or promote memory automatically.

### Agent Control

Use this surface to specify how bounded work should be governed.

Inputs mean:

- **Task contract:** objective, constraints, expected artifact, owner, and stop rule.
- **Role contract:** allowed tools, skills, sources, output, reviewer, and handoff target.
- **Route:** dependency, retry/stop condition, and merge policy.
- **Approval gate:** the action that must pause until an operator authorizes it.

Drafting an agent or node in the browser creates only a local role/task candidate. An approved operator performs actual subagent creation or file changes under the repository contract.

## Jarvis report-first sequence

Jarvis asks for goal, public repository reference or safe label, allowed evidence/exclusions, requested output, independent reviewer, and constraints/stop conditions. It prepares a local Knowledge Service report in chat and can download it as Markdown/JSON. Only then should the operator choose Agent Control, which prepares a proposed role/task/file handoff. The report never fetches or clones the reference, and the handoff never creates the proposed files.

Admin/Guest controls are browser-local preview labels. Guest hides API/token controls and never loads the public model catalog automatically. Admin may explicitly load a public catalog or submit a guarded API review, but a selected model, acknowledgement, or API response still does not prove provider execution, spending authority, or writeback.

## Stage sequence

The console can animate a quiet browser-local preparation sequence:

1. capture the request and authority boundary;
2. classify the risk, task type, and required sources;
3. assemble a task/role contract;
4. prepare a bounded candidate packet;
5. review source, safety, and claim boundaries;
6. stop for approval; and
7. export a review bundle.

An active stage in this local sequence means only that the browser is assembling a review bundle. A real runtime display requires a sanitized event containing `run_id`, `node_id`, `state`, `observed_at`, `evidence_ref`, `authority_scope`, and `writeback_state`.

## Review-bundle handoff

The download contains local workflow schema, role configuration, local packets, sequence state, and a truth boundary. It is not a Git patch, commit, changed repository file, provider invocation, or writeback receipt.

The safe handoff sequence is:

```text
browser-local draft -> review bundle -> approved operator review
-> scoped repository change -> validation -> separate Git/deploy/provider/writeback approval
```

## Data Lab

The Data Lab reads generated public JSON. Its small SQL-like preview supports simple `SELECT columns FROM table LIMIT n` queries for skills, roles, workflow nodes, sources, and run summaries. It does not support arbitrary SQL, server connections, private data, joins, mutations, or external calls. See [the public data model](../project/database/README.md).
