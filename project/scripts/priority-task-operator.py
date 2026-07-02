#!/usr/bin/env python3
"""ArchFlow Priority Task Operator.

Scans ``project/project-plan.md`` for task tables, ranks unfinished tasks by
urgency + importance, and writes a compact execution packet for the next
automated PitAgent handoff.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime
from pathlib import Path


ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")
HEADER_RE = re.compile(r"^\|\s*Task\s*\|\s*Status\s*\|\s*Type\s*\|\s*Due\s*\|\s*Public Output\s*\|")
SEPARATOR_RE = re.compile(r"^\|\s*[-:]+\s*(\|\s*[-:]+\s*)+\|$")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


STATUS_DONE = {"done", "completed", "closed", "archive", "archived"}


def parse_due_date(raw_due: str) -> date | None:
    match = DATE_RE.search(raw_due)
    if not match:
        return None
    return datetime.strptime(match.group(0), "%Y-%m-%d").date()


def importance_score(task_type: str) -> int:
    normalized = task_type.lower()
    if "sales" in normalized:
        return 95
    if "ops" in normalized:
        return 90
    if "website" in normalized:
        return 85
    if "research" in normalized:
        return 82
    if "content" in normalized:
        return 78
    if "doc" in normalized:
        return 55
    return 65


def urgency_score(due: date | None, today: date) -> int:
    if due is None:
        return 20

    days_left = (due - today).days
    if days_left < 0:
        return 120 + abs(days_left) * 6
    if days_left == 0:
        return 100
    if days_left == 1:
        return 95
    if days_left == 2:
        return 88
    if days_left <= 4:
        return 80 - (days_left - 3) * 4
    if days_left <= 7:
        return 68 - (days_left - 5) * 3
    if days_left <= 14:
        return 48 - (days_left - 8)
    return 38


def status_score(status: str) -> tuple[int, bool]:
    normalized = " ".join(status.lower().split())
    if normalized in STATUS_DONE:
        return (-1000, True)
    if "review" in normalized:
        return (28, False)
    if "in progress" in normalized:
        return (42, False)
    if "to do" in normalized or normalized == "todo":
        return (35, False)
    if "backlog" in normalized:
        return (25, False)
    if "blocked" in normalized:
        return (12, False)
    return (30, False)


def parse_tasks(plan_path: Path) -> list[dict[str, str]]:
    text = plan_path.read_text(encoding="utf-8").splitlines()
    tasks: list[dict[str, str]] = []
    epic = ""

    for line in text:
        header_match = re.match(r"^##\s+(E\d+[^|]*)", line)
        if header_match:
            epic = header_match.group(1).strip()
            continue

        if not line.startswith("|"):
            continue
        if HEADER_RE.match(line) or SEPARATOR_RE.match(line):
            continue

        match = ROW_RE.match(line)
        if not match:
            continue

        task, status, task_type, due, public_output = (
            x.strip() for x in match.groups()
        )
        if task.lower() in {"task", ""}:
            continue
        if task_type.lower() in {"type", ""}:
            continue

        tasks.append(
            {
                "epic": epic,
                "task": task,
                "status": status,
                "type": task_type,
                "due": due,
                "public_output": public_output,
                "due_date": parse_due_date(due),
            }
        )

    return tasks


def score_task(task: dict[str, str | None], today: date) -> tuple[int, int, int, bool]:
    score_by_status, is_completed = status_score(task["status"])
    score = score_by_status
    due_score = urgency_score(task["due_date"], today)
    importance = importance_score(task["type"])
    score += due_score + importance
    return score, due_score, importance, is_completed


def format_task_row(task: dict[str, str | None], rank: int, score: int, due_score: int, importance: int) -> str:
    due_date = task["due_date"] if task["due_date"] else "-"
    return (
        f"| {rank} | {score} | {due_score}/{importance} | {task['epic']} | "
        f"{task['task']} | {task['status']} | {task['type']} | {due_date} |"
    )


def write_markdown_artifacts(
    run_dir: Path,
    all_tasks: list[dict[str, str | None]],
    ranked: list[tuple[dict[str, str | None], int, int, int]],
    selected: tuple[dict[str, str | None], int, int, int] | None,
    max_recent_completed: int,
) -> tuple[Path, Path, Path]:
    run_dir.mkdir(parents=True, exist_ok=True)
    selected_task_path = run_dir / "selected-task.md"
    pitagent_prompt_path = run_dir / "pitagent-chat-prompt.md"
    packet_path = run_dir / "kb-notion-github-packet.md"
    json_path = run_dir / "selected-task.json"

    completed = [
        task for task in all_tasks if task["status"].lower() in STATUS_DONE
    ][-max(1, max_recent_completed) :]

    with selected_task_path.open("w", encoding="utf-8") as handle:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        handle.write(f"# ArchFlow Priority Task Operator Run\n\n")
        handle.write(f"Timestamp: {now}\n")
        handle.write("Status: implemented\n\n")

        handle.write("## Completed tasks reviewed\n\n")
        if completed:
            for task in completed[-8:]:
                handle.write(f"- {task['epic']} | {task['task']} ({task['status']})\n")
        else:
            handle.write("- No completed tasks matched current table format.\n")

        handle.write("\n## Ranked candidates\n\n")
        if ranked:
            handle.write(
                "| Rank | Score | Urgency/Importance | Epic | Task | Status | Type | Due |\n"
            )
            handle.write(
                "|---|---:|---:|---|---|---|---|---|\n"
            )
            for i, (task, score, due_score, importance) in enumerate(ranked[:12], start=1):
                handle.write(format_task_row(task, i, score, due_score, importance) + "\n")

        if selected is None:
            handle.write("\nNo selected task: all rows were completed.\n")
        else:
            handle.write("\n## Selected task\n\n")
            task, score, due_score, importance = selected
            handle.write(f"- Task: `{task['task']}`\n")
            handle.write(f"- Epic: `{task['epic']}`\n")
            handle.write(f"- Status: `{task['status']}`\n")
            handle.write(f"- Type: `{task['type']}`\n")
            handle.write(f"- Due: `{task['due']}`\n")
            handle.write(f"- Score: `{score}` (urgency `{due_score}`, importance `{importance}`)\n\n")
            handle.write("- Next action: create a PitAgent handoff chat and execute this task in the next operator slot.\n")

    payload = {
        "run_timestamp": datetime.now().isoformat(timespec="seconds"),
        "selected_task": selected[0] if selected is not None else None,
        "selected_task_score": selected[1] if selected is not None else None,
    }
    json_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")

    selected_task_title = selected[0]["task"] if selected is not None else "No active task"
    task_context = (
        selected[0]["epic"] if selected is not None and selected[0].get("epic") else "-"
    )
    due_value = selected[0]["due"] if selected is not None else "-"

    with pitagent_prompt_path.open("w", encoding="utf-8") as handle:
        handle.write("# New PitAgent Handoff\n\n")
        handle.write(
            "You are the next operator for the ArchFlow priority-task lane.\n"
            "Use this packet to review previous automation output, verify execution,\n"
            "and run reliability checks before closing the task.\n\n"
        )
        handle.write("## Context\n")
        handle.write(f"- Selected task: `{selected_task_title}`\n")
        handle.write(f"- Epic: `{task_context}`\n")
        handle.write(f"- Planned due: `{due_value}`\n\n")
        handle.write("## Required checks\n")
        handle.write("1. Confirm task scope is still valid in `project/project-plan.md`.\n")
        handle.write("2. Validate all prerequisites from this task row are available.\n")
        handle.write("3. Record KB update evidence in `wiki/log.md` and task-packet fields.\n")
        handle.write("4. Prepare Notion status payload and repository push packet.\n")
        handle.write("5. Mark this task complete only if execution output is observable in repository and checks are documented.\n\n")
        handle.write("## Notion packet\n")
        handle.write("- Task status target: `In Progress` before execution, `Done/Review` after execution.\n")
        handle.write("- Blocked fields: keep GAP notes in a separate bullet if task cannot be executed automatically.\n\n")
        handle.write("## Git packet\n")
        handle.write("- `git status --short`\n")
        handle.write("- `git add -A`\n")
        handle.write("- `git commit -m \"Run: priority task operator execution\"`\n")
        handle.write("- `git push`\n")

    selected_title = selected[0]["task"] if selected is not None else "No active task"
    selected_status = selected[0]["status"] if selected is not None else "-"

    with packet_path.open("w", encoding="utf-8") as handle:
        handle.write("# KB/Notion/GitHub packet\n\n")
        handle.write(f"Selected task: `{selected_title}`\n")
        handle.write(f"Current status: `{selected_status}`\n\n")
        handle.write("## Knowledge Base update\n")
        handle.write(
            "- Add selected task evidence, ranking rationale, and execution result to `wiki/log.md`.\n"
        )
        handle.write("- Keep a no-PII summary of execution status and checks.\n\n")
        handle.write("## Notion packet\n")
        handle.write("- Prepare a task update entry with: status, owner, blockers, expected output, next action.\n")
        handle.write("- Include `priority_score`, `urgency`, and `importance` values.\n\n")
        handle.write("## GitHub packet\n")
        handle.write("- Confirm branch contains updated packet files.\n")
        handle.write("- Run local checks and then push only after safety scan passes.\n")
        handle.write("- Push commands:\n")
        handle.write("  - `git status --short`\n")
        handle.write("  - `git add -A`\n")
        handle.write("  - `git commit -m \"Run: priority task operator packet\"`\n")
        handle.write("  - `git push`\n")

    return selected_task_path, pitagent_prompt_path, packet_path


def run() -> None:
    parser = argparse.ArgumentParser(description="Priority task operator")
    parser.add_argument(
        "--plan",
        default="project/project-plan.md",
        help="Path to project plan file.",
    )
    parser.add_argument("--run-id", required=True, help="Run folder name under project/runs/")
    parser.add_argument(
        "--max-recent-completed",
        type=int,
        default=8,
        help="How many completed tasks to include in the evidence context.",
    )
    args = parser.parse_args()

    plan_path = Path(args.plan)
    if not plan_path.exists():
        raise SystemExit(f"Plan file not found: {plan_path}")

    run_dir = Path("project/runs") / args.run_id
    all_tasks = parse_tasks(plan_path)
    if not all_tasks:
        raise SystemExit("No parseable tasks found in project-plan.md")

    today = date.today()
    ranked = []
    for task in all_tasks:
        score, due_score, importance, is_completed = score_task(task, today)
        if is_completed:
            continue
        ranked.append((task, score, due_score, importance))

    ranked.sort(key=lambda item: item[1], reverse=True)
    selected = ranked[0] if ranked else None

    selected_task_path, pitagent_prompt_path, packet_path = write_markdown_artifacts(
        run_dir, all_tasks, ranked, selected, args.max_recent_completed
    )

    if selected:
        title = selected[0]["task"]
        score = selected[1]
        print(f"Selected task: {title}")
        print(f"Score: {score}")
    else:
        print("No active tasks found.")
    print(f"Selected task packet: {selected_task_path}")
    print(f"PitAgent prompt: {pitagent_prompt_path}")
    print(f"KB/Notion/Git packet: {packet_path}")


if __name__ == "__main__":
    run()
