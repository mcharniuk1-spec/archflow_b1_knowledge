#!/usr/bin/env python3
"""Prompt and execution trigger for the task-handout skill.

The script is intentionally side-effect light. It never stores raw prompt text;
it only emits a reminder and writes a safe trigger marker into ignored local
runtime storage when the current prompt or execution implies multi-agent work,
agent role routing, or subtask handling.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
STATE_DIR = ROOT / "project" / "local" / "task-handout-hook"
STATE_FILE = STATE_DIR / "last-trigger.json"

DIRECT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("direct_task_handout", re.compile(r"\btask[- ]handout\b", re.I)),
    ("direct_handoff", re.compile(r"\b(handout|handoff|hand[- ]off|continuation prompt)\b", re.I)),
    ("direct_hook_trigger", re.compile(r"\bhook trigger\b|\btrigger hook\b", re.I)),
]

AGENT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("af_hook", re.compile(r"\bAF (Graph|Crew|Tools|Context|Manager|Knowledge|Review|Publisher)\b", re.I)),
    ("multi_agent", re.compile(r"\b(multi[- ]agent|multilevel agent|parallel agent|agent role|agent roles)\b", re.I)),
    ("agent_requested", re.compile(r"\bagents?\b", re.I)),
    ("langgraph_crewai_combo", re.compile(r"\bLangGraph\b.*\bCrewAI\b|\bCrewAI\b.*\bLangGraph\b", re.I | re.S)),
]

SUBTASK_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("subtask_requested", re.compile(r"\bsub[- ]?tasks?\b|\b1\+ ?subtasks?\b|\bone or more subtasks?\b", re.I)),
    ("task_id", re.compile(r"\bE\d+(?:\.\d+){1,}\b", re.I)),
    ("execution_stage", re.compile(r"\b(solve|execute|start|continue|finish|review)\b.{0,80}\b(tasks?|subtasks?)\b", re.I | re.S)),
]


def read_payload() -> str:
    try:
        return sys.stdin.read()
    except Exception:
        return ""


def strings_from_json(value: Any) -> list[str]:
    if isinstance(value, dict):
        parts: list[str] = []
        for key, item in value.items():
            if str(key).lower() in {
                "prompt",
                "message",
                "text",
                "input",
                "user_prompt",
                "userprompt",
                "instruction",
                "goal",
                "objective",
            }:
                if isinstance(item, str):
                    parts.append(item)
                else:
                    parts.extend(strings_from_json(item))
        return parts
    if isinstance(value, list):
        parts = []
        for item in value:
            parts.extend(strings_from_json(item))
        return parts
    if isinstance(value, str):
        return [value]
    return []


def extract_prompt_text(payload: str, override_text: str | None) -> str:
    if override_text:
        return override_text
    if not payload.strip():
        return ""
    try:
        decoded = json.loads(payload)
    except Exception:
        return payload
    parts = strings_from_json(decoded)
    return "\n".join(parts)


def detect_reasons(text: str, force: bool) -> list[str]:
    if force:
        return ["forced_execution_trigger"]
    reasons: list[str] = []
    for group in (DIRECT_PATTERNS, AGENT_PATTERNS, SUBTASK_PATTERNS):
        for name, pattern in group:
            if pattern.search(text):
                reasons.append(name)
    return sorted(set(reasons))


def write_marker(event: str, reasons: list[str]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "event": event,
        "triggered_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "reasons": reasons,
        "skill": "skills/task-handout/SKILL.md",
        "required_action": (
            "Read the task-handout skill now. If this prompt uses one or more "
            "agent roles or solves one or more subtasks, create or update the "
            "run agent-handout.md before final response."
        ),
    }
    STATE_FILE.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def emit_notice(event: str, reasons: list[str]) -> None:
    reason_text = ", ".join(reasons)
    print(
        "\n".join(
            [
                "TASK_HANDOUT_HOOK_TRIGGER=required",
                f"event={event}",
                f"reasons={reason_text}",
                "required_skill=skills/task-handout/SKILL.md",
                "required_action=Read the skill at the start of this prompt. "
                "If the execution uses one or more agent roles, multi-agent routing, "
                "or solves one or more subtasks, maintain an agent-handout.md beside "
                "the run artifacts before final response.",
            ]
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", default="manual")
    parser.add_argument("--text", default=None)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--print-no-trigger", action="store_true")
    args = parser.parse_args()

    prompt_text = extract_prompt_text(read_payload(), args.text)
    reasons = detect_reasons(prompt_text, args.force)
    if not reasons:
        if args.print_no_trigger:
            print("TASK_HANDOUT_HOOK_TRIGGER=not_required")
        return 0

    write_marker(args.event, reasons)
    emit_notice(args.event, reasons)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
