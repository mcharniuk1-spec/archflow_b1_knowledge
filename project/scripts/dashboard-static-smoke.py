#!/usr/bin/env python3
"""Render-smoke the static ArchFlow dashboard routes with headless Chrome.

This test proves the read-only dashboard can render the two required operating
surfaces without a live backend:

- (1) PRD/ICP Flow
- (2) Agent Orchestra

It intentionally does not test provider calls, durable writeback, microphone
permission, or deployment. Those remain gated runtime checks.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DASHBOARD_DATA = REPO_ROOT / "project" / "dashboard" / "data.json"

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"mstrl_[A-Za-z0-9_-]+"),
    re.compile(r"OPENROUTER_API_KEY\s*="),
    re.compile(r"MISTRAL_API_KEY\s*="),
    re.compile(r"OPENAI_API_KEY\s*="),
]

ROUTE_MARKERS = {
    "#jarvis": [
        "Jarvis Command Center",
        "Architecture 1",
        "Architecture 2",
        "Manual transcript fallback",
        "Operating Switchboard",
        "PRD/ICP service product",
        "Reliable agent orchestra",
        "Blocked Gates",
        "Proof And Backlog Drawer",
        "D-6 Proof and blocker visibility",
        "E2.0A dry run",
        "Public-Safe Sample Outputs",
        "Sanitized PRD excerpt",
        "Agent node config",
        "Jarvis Chat",
        "Voice input requires browser microphone permission",
    ],
    "#history": [
        "Chat History",
        "Full persistent browser-local conversation with Jarvis",
    ],
    "#service": [
        "(1) PRD/ICP Flow",
        "Architecture 1",
        "Architecture 2",
        "Client source intake",
        "PRD builder",
        "ICP evidence cards",
        "Client-output approval",
        "Service output packet",
        "Runtime gate: provider disabled",
        "Runtime gate: writeback approval required",
        "MODEL PROVIDER none",
        "No secrets, raw transcripts, provider calls, backend writes, or deployment actions run here.",
    ],
    "?panel=svc-intake#service": [
        "(1) PRD/ICP Flow",
        "Client source intake",
        "Inputs",
        "Outputs",
        "Overview",
        "Configuration",
        "Prompts",
        "Safety And Business Fit",
        "Provider calls require approval",
        "Provider calls, writeback, deployment, raw capture, and third-party tool installation require explicit approval and verification before execution.",
        "MODEL PROVIDER none",
        "No secrets, raw transcripts, provider calls, backend writes, or deployment actions run here.",
    ],
    "#schema": [
        "(2) Agent Orchestra",
        "Architecture 1",
        "Architecture 2",
        "Operator command intake",
        "Classify request",
        "Codex development response",
        "Architecture review",
        "Safety and source review",
        "Runtime gate: provider disabled",
        "Runtime gate: writeback approval required",
        "MODEL PROVIDER none",
        "No secrets, raw transcripts, provider calls, backend writes, or deployment actions run here.",
    ],
    "?panel=architecture-review#schema": [
        "(2) Agent Orchestra",
        "Architecture review",
        "Inputs",
        "Outputs",
        "Overview",
        "Configuration",
        "Prompts",
        "Safety And Business Fit",
        "Provider calls require approval",
        "Provider calls, writeback, deployment, raw capture, and third-party tool installation require explicit approval and verification before execution.",
        "MODEL PROVIDER none",
        "No secrets, raw transcripts, provider calls, backend writes, or deployment actions run here.",
    ],
    "#config": [
        "Chain Configuration And Subprompting",
        "Agent Chain Links",
        "Export config packet",
        "Export creates a review packet",
        "does not mutate GitHub, Notion, WikiLLM, or runtime services",
    ],
    "#plan": [
        "E1-E7 Project Plan",
        "Recent Source Links",
        "B2B SaaS product teams",
        "E2.0 dry run",
    ],
}


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        return


def find_chrome() -> str:
    candidates = [
        os.environ.get("CHROME_PATH"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise RuntimeError("Headless Chrome/Chromium was not found. Set CHROME_PATH to run this smoke test.")


def validate_dashboard_data() -> None:
    with DASHBOARD_DATA.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    required = [
        "project",
        "status_cards",
        "activity",
        "sources",
        "wiki",
        "langgraph",
        "crewai",
        "env",
        "packages",
        "gates",
    ]
    missing = [key for key in required if key not in data]
    if missing:
        raise AssertionError(f"dashboard data missing required keys: {', '.join(missing)}")


def render_route(chrome: str, base_url: str, route_hash: str, timeout_seconds: int, retries: int) -> str:
    url = f"{base_url}/project/dashboard/{route_hash}"
    command = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--disable-background-networking",
        "--disable-sync",
        "--no-first-run",
        "--no-default-browser-check",
        "--hide-scrollbars",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=2000",
        "--dump-dom",
        url,
    ]
    last_error = ""
    for attempt in range(retries + 1):
        try:
            completed = subprocess.run(command, check=False, text=True, capture_output=True, timeout=timeout_seconds)
        except subprocess.TimeoutExpired as error:
            last_error = f"timed out after {timeout_seconds} seconds"
        else:
            if completed.returncode == 0:
                return completed.stdout
            last_error = completed.stderr.strip() or f"exit code {completed.returncode}"
        if attempt < retries:
            time.sleep(1)
    raise RuntimeError(f"Chrome failed for {route_hash}: {last_error}")


def assert_markers(route_hash: str, html: str) -> None:
    missing = [marker for marker in ROUTE_MARKERS[route_hash] if marker not in html]
    if missing:
        raise AssertionError(f"{route_hash} missing markers: {', '.join(missing)}")
    leaked = [pattern.pattern for pattern in SECRET_PATTERNS if pattern.search(html)]
    if leaked:
        raise AssertionError(f"{route_hash} rendered forbidden secret pattern(s): {', '.join(leaked)}")


def run_smoke(timeout_seconds: int, retries: int) -> None:
    validate_dashboard_data()
    chrome = find_chrome()

    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(REPO_ROOT), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}"

    try:
        for route_hash in ROUTE_MARKERS:
            html = render_route(chrome, base_url, route_hash, timeout_seconds, retries)
            assert_markers(route_hash, html)
    finally:
        server.shutdown()
        server.server_close()

    print(f"dashboard_static_smoke=ok routes={len(ROUTE_MARKERS)} provider_calls=0 writeback=0")


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test the static ArchFlow dashboard routes.")
    parser.add_argument("--timeout", type=int, default=60, help="Per-route headless Chrome timeout in seconds.")
    parser.add_argument("--retries", type=int, default=2, help="Per-route retry count for local Chrome startup timing.")
    args = parser.parse_args()
    try:
        run_smoke(args.timeout, args.retries)
    except Exception as error:  # noqa: BLE001 - command-line verifier should print direct failure.
        print(f"dashboard_static_smoke=failed reason={error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
