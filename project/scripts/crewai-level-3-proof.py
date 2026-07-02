#!/usr/bin/env python3
"""Run a public-safe CrewAI Level 3 direct runtime proof.

This proof intentionally uses a deterministic local LLM adapter. It verifies
CrewAI direct task execution, output capture, model-call ledger writing, and
budget-guard behavior without calling OpenRouter or any external provider.
"""

from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from crewai import Agent, Crew, Process, Task
from crewai.llms.base_llm import BaseLLM


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "project"
RUN_ID = "2026-07-02-crewai-level-3-proof"
RUN_DIR = PROJECT / "runs" / RUN_ID
LEDGER = RUN_DIR / "model-call-ledger.jsonl"

DAILY_BUDGET_USD = 5.00
MAX_PER_RUN_USD = 1.99


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def append_ledger(record: dict[str, Any]) -> None:
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def count_text_tokens(text: str) -> int:
    return len([part for part in text.replace("\n", " ").split(" ") if part])


class BudgetGuard:
    def __init__(self) -> None:
        self.run_spend = 0.0

    def check(self, planned_cost: float) -> None:
        if self.run_spend + planned_cost > MAX_PER_RUN_USD:
            raise RuntimeError("run_budget_cap_exceeded")
        if self.run_spend + planned_cost > DAILY_BUDGET_USD:
            raise RuntimeError("daily_budget_cap_exceeded")

    def record(self, actual_cost: float) -> None:
        self.run_spend += actual_cost


BUDGET = BudgetGuard()


class DeterministicProofLLM(BaseLLM):
    """CrewAI-compatible local LLM that returns fixed public-safe outputs."""

    def __init__(self) -> None:
        super().__init__(
            model="archflow-deterministic-crewai-proof",
            provider="local",
            llm_type="custom",
        )

    def call(
        self,
        messages: str | list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        callbacks: list[Any] | None = None,
        available_functions: dict[str, Any] | None = None,
        from_task: Task | None = None,
        from_agent: Agent | None = None,
        response_model: type[Any] | None = None,
    ) -> str:
        prompt_text = json.dumps(messages, default=str) if not isinstance(messages, str) else messages
        agent_role = getattr(from_agent, "role", "unknown_agent")
        task_name = getattr(from_task, "name", None) or "unnamed_task"
        planned_cost = 0.0
        BUDGET.check(planned_cost)

        if "review" in task_name:
            output = (
                "FACT: AF Review checked the direct CrewAI proof output.\n"
                "INTERPRETATION: The proof demonstrates direct CrewAI task execution with a deterministic local LLM, not OpenRouter runtime activation.\n"
                "GAP: Production provider-backed CrewAI still requires an approved backend, server-side secrets, live provider ledger entries, and owner approval.\n"
                "VERDICT: approved_for_status_proof_passed_not_default_runtime."
            )
        else:
            output = (
                "FACT: Direct CrewAI runtime executed a PRD/ICP fixture task.\n"
                "PRD_PACKET: Intake is a public-safe B2B SaaS product-team brief; output is a source-bound PRD/ICP proof packet.\n"
                "ICP: B2B SaaS product teams with product leadership ownership.\n"
                "ACCEPTANCE_CRITERIA: source boundary stated; no external writeback; no provider call; review gate required.\n"
                "NEXT_QUESTION: Which approved source packet should feed the first non-proof run?"
            )

        BUDGET.record(planned_cost)
        append_ledger(
            {
                "timestamp_utc": utc_now(),
                "run_id": RUN_ID,
                "epic_or_task": "crewai_level_3_direct_runtime_proof",
                "provider": "local_deterministic",
                "model_id": self.model,
                "model_role": agent_role,
                "prompt_version": "crewai-level-3-proof-v1",
                "source_ids_used": ["fixture:tiny-public-safe-prd-icp"],
                "input_artifact": "project/runs/2026-07-02-crewai-level-3-proof/input-fixture.md",
                "output_artifact": "project/runs/2026-07-02-crewai-level-3-proof/crew-output.md",
                "context_window_tokens": 0,
                "prompt_tokens": count_text_tokens(prompt_text),
                "output_tokens": count_text_tokens(output),
                "actual_or_estimated_cost": planned_cost,
                "cost_currency": "USD",
                "pricing_source": "local deterministic proof; no provider pricing",
                "budget_cap": MAX_PER_RUN_USD,
                "budget_remaining": round(MAX_PER_RUN_USD - BUDGET.run_spend, 4),
                "daily_budget_cap": DAILY_BUDGET_USD,
                "decision": "allow_zero_cost_local_proof_call",
                "reviewer_model_id": "af_review_deterministic_local",
                "human_gate_required": True,
                "runtime_source": "local_crewai_direct_runtime",
                "status": "ok",
                "error_type": "",
                "task_name": task_name,
            }
        )
        return output


def configure_runtime() -> None:
    local_home = PROJECT / "local" / "home"
    local_home.mkdir(parents=True, exist_ok=True)
    os.environ["HOME"] = str(local_home)
    os.environ["CREWAI_STORAGE_DIR"] = "archflow_level3_proof"
    os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
    os.environ["CREWAI_DISABLE_TRACKING"] = "true"
    os.environ["CREWAI_TRACING_ENABLED"] = "false"
    os.environ["OTEL_SDK_DISABLED"] = "true"


def write_fixture() -> None:
    write_text(
        RUN_DIR / "input-fixture.md",
        """# Tiny Public-Safe PRD/ICP Fixture

Status: public-safe proof fixture

## Source Boundary

This fixture contains invented non-client product-team context. It contains no private source text, credentials, private URLs, local paths, raw transcripts, account IDs, or customer data.

## Product-Team Brief

A B2B SaaS product leader wants to convert scattered meeting notes and backlog fragments into a reviewed PRD, acceptance criteria, task matrix, source-bound gaps, and an ICP evidence checklist.

## Expected Proof Output

- Context digest.
- PRD/ICP proof packet.
- Acceptance criteria.
- Review gate result.
- No provider call.
- No external writeback.
""",
    )


def run_crewai_proof() -> tuple[str, str]:
    llm = DeterministicProofLLM()
    manager = Agent(
        role="AF Manager Level 3 Proof Agent",
        goal="Run one direct CrewAI PRD/ICP proof task from a tiny public-safe fixture.",
        backstory="A bounded ArchFlow proof agent that produces public-safe PRD/ICP packets.",
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )
    reviewer = Agent(
        role="AF Review Level 3 Proof Agent",
        goal="Review the direct CrewAI proof output for public safety and runtime-boundary honesty.",
        backstory="A bounded ArchFlow reviewer that approves, revises, or blocks direct runtime proof outputs.",
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )

    prd_task = Task(
        name="prd_icp_proof_task",
        description=(
            "Read the tiny public-safe PRD/ICP fixture and produce a concise proof packet. "
            "Keep the output public-safe. State that no provider call and no external writeback are performed."
        ),
        expected_output="Public-safe PRD/ICP proof packet with acceptance criteria and next question.",
        agent=manager,
    )
    review_task = Task(
        name="review_proof_task",
        description=(
            "Review the proof packet. Confirm whether it proves direct CrewAI runtime mechanics and whether Level 3 can become "
            "proof_passed_not_default_runtime. Preserve all provider and writeback gates."
        ),
        expected_output="FACT/INTERPRETATION/GAP review verdict.",
        agent=reviewer,
        context=[prd_task],
    )
    crew = Crew(
        agents=[manager, reviewer],
        tasks=[prd_task, review_task],
        process=Process.sequential,
        memory=False,
        cache=False,
        planning=False,
        verbose=False,
        output_log_file=False,
    )
    result = crew.kickoff()
    task_outputs = getattr(result, "tasks_output", []) or []
    prd_output = str(task_outputs[0]) if task_outputs else str(result)
    review_output = str(task_outputs[-1]) if task_outputs else str(result)
    return prd_output, review_output


def write_review_and_state(prd_output: str, review_output: str) -> None:
    write_text(RUN_DIR / "crew-output.md", "# CrewAI Level 3 Direct Runtime Output\n\n" + prd_output)
    write_text(RUN_DIR / "review-report.md", "# AF Review Report\n\n" + review_output)
    write_text(
        RUN_DIR / "budget-guard.json",
        json.dumps(
            {
                "run_id": RUN_ID,
                "daily_budget_usd": DAILY_BUDGET_USD,
                "max_per_run_usd": MAX_PER_RUN_USD,
                "actual_spend_usd": round(BUDGET.run_spend, 4),
                "provider_calls": 0,
                "openrouter_calls": 0,
                "status": "pass",
                "rule": "5 USD per day and always under 2 USD per run",
            },
            indent=2,
            sort_keys=True,
        ),
    )
    write_text(
        RUN_DIR / "runtime-proof.json",
        json.dumps(
            {
                "run_id": RUN_ID,
                "status": "proof_passed_not_default_runtime",
                "direct_crewai_task_run_pass": True,
                "public_safe_fixture": True,
                "deterministic_output_path": "project/runs/2026-07-02-crewai-level-3-proof/crew-output.md",
                "model_call_ledger": "project/runs/2026-07-02-crewai-level-3-proof/model-call-ledger.jsonl",
                "budget_guard": "project/runs/2026-07-02-crewai-level-3-proof/budget-guard.json",
                "review_report": "project/runs/2026-07-02-crewai-level-3-proof/review-report.md",
                "provider_runtime": "not_activated",
                "writeback_runtime": "not_activated",
                "recommended_level_3_status": "proof_passed_not_default_runtime",
                "default_runtime": False,
            },
            indent=2,
            sort_keys=True,
        ),
    )
    write_text(
        RUN_DIR / "dashboard-state.md",
        """# Dashboard State Packet

Screen (1) PRD/ICP Flow:
- Add or display `CrewAI Level 3 proof packet` after PRD Draft and before Review.
- Status: `proof_passed_not_default_runtime`.
- Runtime: deterministic local CrewAI proof, zero provider calls, zero writeback.

Screen (2) Agent Orchestra:
- Add or display `CrewAI Level 3 direct runtime proof` as a bounded worker/review lane feeding QA Gate.
- Status: `proof_passed_not_default_runtime`.
- Gates retained: OpenRouter provider activation, backend/local bridge, live writeback, Telegram, production promotion.
""",
    )


def write_handout() -> None:
    write_text(
        RUN_DIR / "agent-handout.md",
        """# CrewAI Level 3 Proof Handout

## Title And Purpose

This handout records the direct CrewAI Level 3 proof run. Use it before enabling any future provider-backed or default CrewAI runtime.

## Human Summary

The proof executed one direct CrewAI runtime flow using a tiny public-safe PRD/ICP fixture and a deterministic local LLM adapter. It did not call OpenRouter, did not spend provider budget, did not write external systems, and did not promote public claims.

The result proves CrewAI direct runtime mechanics for a bounded local fixture. It does not prove provider-backed CrewAI, backend deployment, live writeback, or production readiness.

## Current State

Status: `proof_passed_not_default_runtime`.

Main artifacts:
- `input-fixture.md`
- `crew-output.md`
- `review-report.md`
- `model-call-ledger.jsonl`
- `budget-guard.json`
- `runtime-proof.json`
- `dashboard-state.md`

## Agent Continuation Prompt

Continue only from the proof artifacts in this run folder. Preserve the Level 3 status as `proof_passed_not_default_runtime` unless the owner explicitly approves default runtime. Do not activate OpenRouter or external writeback from this proof alone.

## Execution Trace

FACT:
- Direct CrewAI executed a two-task sequential crew.
- The fixture was public-safe and invented.
- Ledger entries were written for each deterministic local LLM call.
- Budget guard passed with zero provider spend.

INTERPRETATION:
- Level 3 is now proven for local deterministic direct CrewAI mechanics.
- Provider-backed Level 3 remains a separate approval and backend/ledger task.

GAP:
- No OpenRouter call was made.
- No backend/local bridge was implemented.
- No external writeback was performed.

## Validation

Run-level validation is recorded in `runtime-proof.json`; repository-level validation is recorded in the live communication log.

## Safety Boundary

Do not store secrets, private source text, local absolute paths, private URLs, account IDs, raw transcripts, or credential values in this run folder.
""",
    )


def main() -> int:
    configure_runtime()
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    if LEDGER.exists():
        LEDGER.unlink()
    write_fixture()
    prd_output, review_output = run_crewai_proof()
    write_review_and_state(prd_output, review_output)
    write_handout()
    print("crewai_level_3_proof=ok")
    print("status=proof_passed_not_default_runtime")
    print("provider_calls=0")
    print("writeback=0")
    print("actual_spend_usd=0.00")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
