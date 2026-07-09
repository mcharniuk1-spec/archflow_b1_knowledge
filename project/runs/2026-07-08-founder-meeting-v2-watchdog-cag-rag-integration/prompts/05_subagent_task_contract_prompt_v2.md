# Subagent Task Contract Prompt v2

Use this for every bounded subagent or actor.

## Template

```text
Task title:
Execution type:
Risk level:
Goal:
Context capsule summary:
Allowed files/areas:
Forbidden actions:
Inputs:
Expected outputs:
Acceptance criteria:
Evidence required:
Maximum attempts:
Stop condition:
Reviewer:
Output format:
```

## Rules

- Do not exceed file scope.
- Do not use paid or external tools unless explicitly approved.
- Do not modify production, secrets, environment variables, deployment settings, private data, or unrelated files.
- Do not claim completion without evidence.
- Stop when acceptance criteria are met.
- If blocked, report blocker and next safe action.
- Codex reviews and integrates outputs.
