#!/usr/bin/env python3
"""Controlled post-execution skill update reviewer.

This script is deliberately conservative. It reviews a completed run folder and
decides whether the evidence supports a reusable skill update. It never creates
new skills, never rewrites a SKILL.md, and only appends to existing support
files when --apply is passed.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNS = ROOT / "project" / "runs"
SKILLS = ROOT / "skills"
DEFAULT_SKILL = "evening-skill-registry-update"
MAX_TEXT_CHARS = 120_000

VALID_MODES = {"NO_UPDATE", "APPEND_PATTERN", "PATCH_EXISTING_SKILL"}
EVIDENCE_MARKERS = (
    "Pass:",
    "Fail:",
    "passed",
    "failed",
    "Checks",
    "Validation",
    "Files Changed",
    "Commands",
    "git diff --check",
    "Public safety scan",
    "workflow_validation=ok",
    "concrete improvement belongs",
    "No new skill is justified",
    "already-packetized",
    "owner-gated",
)

SKILL_KEYWORDS = {
    "archflow1": ("jarvis", "dashboard", "railway", "voice", "api contract"),
    "priority-task-operator": ("priority", "operator", "packetized", "owner-gated", "selected-task"),
    "evening-skill-registry-update": ("registry", "hook", "skill membership", "automation id"),
    "daily-public-project-review": ("retrospective", "rag", "inefficiency", "daily review"),
    "task-handout": ("handout", "handoff", "continuation prompt"),
    "arcagcom": ("live communication", "file claim", "agent communication", "handoff log"),
    "outquestions": ("owner decision", "approval gate", "blocked gate", "next safe action"),
    "archflow-task-breakdown": ("task breakdown", "subtask", "acceptance criteria"),
    "archflow-e1-runtime-guard": ("runtime guard", "pre-push", "workflow validation"),
}


@dataclass
class ReviewDecision:
    mode: str
    target_skill: str | None
    destination: str | None
    reason: str
    evidence: list[str]
    applied: bool = False
    skipped_apply_reason: str | None = None


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def latest_run_dir() -> Path | None:
    if not RUNS.exists():
        return None
    dirs = [path for path in RUNS.iterdir() if path.is_dir()]
    if not dirs:
        return None
    return max(dirs, key=lambda path: path.stat().st_mtime)


def read_run_text(run_path: Path) -> str:
    if run_path.is_file():
        return f"\n\n# FILE: {run_path.name}\n" + run_path.read_text(
            encoding="utf-8", errors="ignore"
        )[:MAX_TEXT_CHARS]

    candidates = [
        "summary.md",
        "run-summary.md",
        "agent-handout.md",
        "review-report.md",
        "selected-task.md",
    ]
    parts: list[str] = []
    for name in candidates:
        path = run_path / name
        if path.exists() and path.is_file():
            parts.append(f"\n\n# FILE: {name}\n")
            parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    if not parts:
        for path in sorted(run_path.glob("*.md"))[:8]:
            parts.append(f"\n\n# FILE: {path.name}\n")
            parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts)[:MAX_TEXT_CHARS]


def evidence_lines(text: str) -> list[str]:
    lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if any(marker.lower() in stripped.lower() for marker in EVIDENCE_MARKERS):
            lines.append(stripped)
        if len(lines) >= 8:
            break
    return lines


def explicit_field(text: str, name: str) -> str | None:
    match = re.search(rf"(?im)^\s*{re.escape(name)}\s*:\s*(.+?)\s*$", text)
    if not match:
        return None
    return match.group(1).strip().strip("`")


def explicit_mode(text: str) -> str | None:
    value = explicit_field(text, "SKILL_UPDATE_MODE")
    if value and value in VALID_MODES:
        return value
    return None


def infer_target_skill(text: str) -> str | None:
    direct = explicit_field(text, "SKILL_UPDATE_TARGET")
    if direct:
        return direct

    improvement = re.search(r"concrete improvement belongs in\s+`([^`]+)`", text, re.I)
    if improvement:
        return improvement.group(1)

    lowered = text.lower()
    scores: list[tuple[int, str]] = []
    for skill, keywords in SKILL_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in lowered)
        if score:
            scores.append((score, skill))
    if not scores:
        return None
    scores.sort(reverse=True)
    return scores[0][1]


def skill_exists(skill: str | None) -> bool:
    return bool(skill) and (SKILLS / skill / "SKILL.md").exists()


def destination_for(mode: str, skill: str | None) -> Path | None:
    if mode == "NO_UPDATE":
        return None
    folder = SKILLS / (skill if skill_exists(skill) else DEFAULT_SKILL)
    if mode == "APPEND_PATTERN":
        destination = folder / "successful-patterns.md"
    else:
        destination = folder / "candidate-patterns.md"
    if destination.exists():
        return destination
    return SKILLS / DEFAULT_SKILL / "candidate-patterns.md"


def automatic_mode(text: str, evidence: list[str]) -> tuple[str, str]:
    if not evidence:
        return "NO_UPDATE", "insufficient execution evidence"

    lowered = text.lower()
    if "same error appears twice" in lowered or "looped" in lowered:
        return "APPEND_PATTERN", "failure or loop evidence detected"
    if re.search(r"status:\s*(blocked|failed)", text, re.I):
        return "APPEND_PATTERN", "blocked or failed run evidence detected"
    if "concrete improvement belongs in" in lowered:
        return "PATCH_EXISTING_SKILL", "run identified a concrete improvement for an existing skill"
    if "SKILL_UPDATE_CANDIDATE" in text:
        return "APPEND_PATTERN", "explicit skill update candidate marker found"
    return "NO_UPDATE", "ordinary execution or weak reusable-skill evidence"


def build_entry(mode: str, run_path: Path, target_skill: str | None, reason: str, evidence: list[str]) -> str:
    text = read_run_text(run_path)
    title = explicit_field(text, "SKILL_UPDATE_TITLE") or run_path.stem
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    evidence_block = "\n".join(f"- {line}" for line in evidence[:5]) or "- GAP: no evidence line captured"
    target = target_skill or DEFAULT_SKILL
    if mode == "APPEND_PATTERN":
        return (
            f"\n## {title}\n\n"
            f"- Date recorded: {now}\n"
            f"- Related skill: `{target}`\n"
            f"- When to use: after a similar execution produces the same evidence pattern.\n"
            f"- When not to use: one-off runs, missing validation, missing changed-file evidence, or private-source-dependent work.\n"
            f"- Efficient sequence: read run evidence, verify checks, append only the reusable part, then stop when acceptance criteria are met.\n"
            f"- Evidence from execution:\n{evidence_block}\n"
            f"- Expected benefit: preserves reusable execution learning without creating a new skill or rewriting the controlling prompt.\n"
            f"- Update reason: {reason}\n"
        )
    return (
        f"\n## {title}\n\n"
        f"- Date recorded: {now}\n"
        f"- Candidate target: `{target}`\n"
        f"- Proposed mode: `PATCH_EXISTING_SKILL`\n"
        f"- Required human review: confirm this belongs in an existing support file or `SKILL.md` before promotion.\n"
        f"- Evidence from execution:\n{evidence_block}\n"
        f"- Stop rule: do not patch a controlling prompt unless this pattern repeats or the evidence proves a fundamental rule change.\n"
        f"- Update reason: {reason}\n"
    )


def review(run_path: Path) -> ReviewDecision:
    text = read_run_text(run_path)
    evidence = evidence_lines(text)

    mode = explicit_mode(text)
    if mode is None:
        mode, reason = automatic_mode(text, evidence)
    else:
        reason = "explicit SKILL_UPDATE_MODE marker found"

    target = infer_target_skill(text)
    if mode != "NO_UPDATE" and not skill_exists(target):
        reason = f"{reason}; no matching existing skill, falling back to candidate storage"
        target = DEFAULT_SKILL

    destination = destination_for(mode, target)
    return ReviewDecision(
        mode=mode,
        target_skill=target,
        destination=rel(destination) if destination else None,
        reason=reason,
        evidence=evidence,
    )


def apply_decision(decision: ReviewDecision, run_path: Path) -> ReviewDecision:
    if decision.mode == "NO_UPDATE":
        decision.skipped_apply_reason = "NO_UPDATE decisions do not write files"
        return decision
    if not decision.destination:
        decision.skipped_apply_reason = "no destination resolved"
        return decision

    destination = ROOT / decision.destination
    if not destination.exists():
        decision.skipped_apply_reason = "destination support file is missing; create it through a reviewed patch first"
        return decision

    entry = build_entry(decision.mode, run_path, decision.target_skill, decision.reason, decision.evidence)
    current = destination.read_text(encoding="utf-8")
    if run_path.stem in current:
        decision.skipped_apply_reason = "run already recorded in destination"
        return decision
    destination.write_text(current.rstrip() + "\n" + entry + "\n", encoding="utf-8")
    decision.applied = True
    return decision


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path)
    parser.add_argument("--latest", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    run_path = args.run_dir
    if args.latest or run_path is None:
        run_path = latest_run_dir()
    if run_path is None:
        raise SystemExit("post_execution_skill_update=fail:no_run_path")
    requested_path = run_path.as_posix()
    if not run_path.is_absolute():
        run_path = ROOT / run_path
    if not run_path.exists() or not (run_path.is_dir() or run_path.is_file()):
        raise SystemExit(f"post_execution_skill_update=fail:missing_run_path:{requested_path}")

    decision = review(run_path)
    if args.apply:
        decision = apply_decision(decision, run_path)

    if args.json:
        print(json.dumps(asdict(decision), indent=2))
    else:
        print(f"post_execution_skill_update={decision.mode}")
        print(f"target_skill={decision.target_skill or 'none'}")
        print(f"destination={decision.destination or 'none'}")
        print(f"applied={str(decision.applied).lower()}")
        print(f"reason={decision.reason}")
        for line in decision.evidence[:5]:
            print(f"evidence={line}")
        if decision.skipped_apply_reason:
            print(f"skipped_apply_reason={decision.skipped_apply_reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
