---
name: archflow-e1-runtime-guard
description: Validate the ArchFlow E1 runtime before Git push. Use after setup or before publication to confirm the public safety boundary, workflow YAML, LangGraph smoke path, LlamaIndex readiness, CrewAI readiness, and saved project skills without installing packages during the hook.
---

# ArchFlow E1 Runtime Guard

## Purpose

Use this skill whenever E1 runtime work is changed or pushed. It keeps the Block 1 setup repeatable by checking that the public project can still run the knowledge-base spine:

`public safety scan -> workflow validation -> LangGraph smoke path -> LlamaIndex import -> CrewAI import -> Git push`

The skill is intentionally a guard, not an installer. Package installation happens as an explicit setup step before pushing.

## When To Use

- Before pushing E1.1, E1.2, or workflow changes.
- After changing `project/workflows/`, `project/agents/`, `project/scripts/`, or `skills/`.
- After installing or upgrading LangGraph, LlamaIndex, CrewAI, LangSmith, Pydantic, or PyYAML.
- After changing the approved corpus boundary.

## Required Checks

1. Run the public safety scan.
   - Blocks secrets, private links, local absolute paths, raw private source folders, and tracked env files.

2. Validate workflow YAML.
   - `project/workflows/langgraph-controller.yaml`
   - `project/workflows/llamaindex-rag.yaml`
   - `project/workflows/crewai-crew.yaml`
   - `project/workflows/knowledge-integration.yaml`
   - `project/config/model-routing.yaml`

3. Verify runtime imports in the project local environment.
   - LangSmith SDK.
   - LangGraph.
   - LangChain Core.
   - Pydantic.
   - PyYAML.
   - LlamaIndex core.
   - CrewAI.

4. Run the LangGraph smoke workflow.
   - Use sanitized state only.
   - Trace to LangSmith only if the ignored local env file is present.
   - Do not send raw transcripts, private links, credentials, or broad local file content.

5. Keep the hook side-effect light.
   - No package install.
   - No broad indexing.
   - No raw source ingestion.
   - No Notion writes.
   - No deploy.

6. Keep CrewAI storage local.
   - Set a project-local runtime home for CrewAI checks.
   - Disable CrewAI telemetry and tracking during guard runs.
   - Treat CrewAI as role/task configuration until an explicit model execution step is approved.

## Hook Connection

The public repository pre-push hook calls:

```bash
python3 scripts/public_safety_scan.py
python3 project/scripts/pre-push-runtime-guard.py
```

The guard script uses the project local Python environment and fails the push if the runtime spine is broken.

## Failure Handling

Use this order when the guard fails:

1. Fix public safety findings first.
2. Fix YAML parsing and schema errors second.
3. Fix missing package imports third, one package group at a time.
4. Re-run the LangGraph smoke script.
5. Regenerate dashboard data.
6. Re-run the pre-push hook before committing.

## Agent Responsibilities

- `AF Tools`: package, env, Git, and hook readiness.
- `AF Context`: approved source boundary and context digest readiness.
- `AF Manager`: workflow status, task sequence, and acceptance criteria.
- `AF Knowledge`: WikiLLM run notes and durable memory candidates.
- `AF Review`: safety gate and unsupported-claim check.
- `AF Publisher`: Git-ready state after all checks pass.

## Done Criteria

The skill is working when the hook runs both safety and runtime guards, the LangGraph smoke workflow completes, workflow YAML validates, LlamaIndex and CrewAI imports succeed, and no tracked public file contains private or secret material.
