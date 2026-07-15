#!/usr/bin/env python3
"""Render-smoke the static ArchFlow dashboard routes with headless Chrome.

This test proves the documentation-first operator console can render its
current product and reference routes without a live backend:

- operating manual, overview, architecture, knowledge, agents, runs,
  reference, and workflow.

It intentionally does not test provider calls, durable writeback, audio
capture/playback, or deployment. Those remain gated runtime checks.
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
VERCEL_CONFIG = REPO_ROOT / "vercel.json"
JARVIS_HTML = REPO_ROOT / "jarvis.html"
JARVIS_JS = REPO_ROOT / "jarvis.js"

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"mstrl_[A-Za-z0-9_-]+"),
    re.compile(r"OPENROUTER_API_KEY\s*="),
    re.compile(r"MISTRAL_API_KEY\s*="),
    re.compile(r"OPENAI_API_KEY\s*="),
]

ROUTE_MARKERS = {
    "#manual": [
        "Dashboard Operating Manual",
        "Knowledge Service",
        "Agent Control",
        "Packaged skills",
        "browser-local",
    ],
    "#overview": [
        "Documentation-first architecture console",
        "Build a maintained company brain",
        "Seven public groups",
        "What the architecture can support today",
    ],
    "#architecture": [
        "One operating system, seven grouped layers",
        "Layer index",
        "End-to-end contract",
        "Source-of-truth rule",
    ],
    "#knowledge": [
        "Retrieve narrowly, preserve provenance",
        "Retrieval cascade",
        "RAG parameters",
        "Corpus boundary",
    ],
    "#agents": [
        "Roles are contracts, not personas",
        "Configured specialist roles",
        "Skill governance",
        "Reviewed public skill catalog",
    ],
    "#operations": [
        "Two clear products, one governed handoff",
        "Knowledge Service",
        "Agent Control",
        "Prepare a review bundle",
    ],
    "#data": [
        "Inspect the public catalog without inventing a production database",
        "Read-only fixture query lab",
        "Run public preview",
        "Gated database roadmap",
    ],
    "#runs": [
        "Separate configuration, execution, review, and promotion",
        "Evidence-state vocabulary",
        "Recent public-safe activity",
        "Check registry",
    ],
    "#reference": [
        "Configure the architecture",
        "Build · Scale · Govern · Optimize",
        "Parameter families",
        "Status semantics",
        "Canonical architecture sources",
    ],
    "#schema": [
        "Full-screen workflow",
        "Canvas",
        "Stage list",
        "Export review packet",
        "MODEL PROVIDER none",
        "writeback approval required",
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
        "role_catalog",
        "skill_catalog",
        "knowledge_catalog",
        "configuration_catalog",
    ]
    missing = [key for key in required if key not in data]
    if missing:
        raise AssertionError(f"dashboard data missing required keys: {', '.join(missing)}")


def validate_vercel_route_contract() -> None:
    with VERCEL_CONFIG.open("r", encoding="utf-8") as handle:
        config = json.load(handle)
    redirects = {
        item.get("source"): item.get("destination")
        for item in config.get("redirects", [])
        if isinstance(item, dict)
    }
    for source in ("/dashboard", "/dashboard/"):
        if redirects.get(source) != "/project/dashboard/":
            raise AssertionError(
                f"{source} must redirect to canonical /project/dashboard/ so relative assets and data stay valid"
            )


def render_url(chrome: str, url: str, timeout_seconds: int, retries: int) -> str:
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
    raise RuntimeError(f"Chrome failed for {url}: {last_error}")


def render_route(chrome: str, base_url: str, route_hash: str, timeout_seconds: int, retries: int) -> str:
    return render_url(chrome, f"{base_url}/project/dashboard/{route_hash}", timeout_seconds, retries)


def assert_markers(route_hash: str, html: str) -> None:
    missing = [marker for marker in ROUTE_MARKERS[route_hash] if marker not in html]
    if missing:
        raise AssertionError(f"{route_hash} missing markers: {', '.join(missing)}")
    leaked = [pattern.pattern for pattern in SECRET_PATTERNS if pattern.search(html)]
    if leaked:
        raise AssertionError(f"{route_hash} rendered forbidden secret pattern(s): {', '.join(leaked)}")
    if "Strategic plan" in html or "#plan" in html:
        raise AssertionError(f"{route_hash} exposed a removed strategic-plan dashboard surface")


def validate_jarvis_static_contract(html: str) -> None:
    required_html = [
        "Prepare the report first",
        "Knowledge Service — prepare report first",
        "Guest preview",
        "Download report",
        "Download handoff",
        "Load public model catalog",
        "Local report first",
    ]
    missing_html = [marker for marker in required_html if marker not in html]
    if missing_html:
        raise AssertionError(f"Jarvis page missing markers: {', '.join(missing_html)}")
    source = JARVIS_JS.read_text(encoding="utf-8")
    required_source = [
        "data-load-model-catalog",
        "data-download-report",
        "data-download-package",
        'if (state.viewerMode === "guest") return;',
        "The browser did not send the report body, project reference, source boundary, or chat history",
    ]
    missing_source = [marker for marker in required_source if marker not in source]
    if missing_source:
        raise AssertionError(f"Jarvis source contract missing: {', '.join(missing_source)}")
    if "loadModels();" in source:
        raise AssertionError("Jarvis must not auto-load the public model catalog")
    leaked = [pattern.pattern for pattern in SECRET_PATTERNS if pattern.search(html)]
    if leaked:
        raise AssertionError(f"Jarvis rendered forbidden secret pattern(s): {', '.join(leaked)}")


def run_smoke(timeout_seconds: int, retries: int) -> None:
    validate_dashboard_data()
    validate_vercel_route_contract()
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
        jarvis_html = render_url(chrome, f"{base_url}/jarvis.html", timeout_seconds, retries)
        validate_jarvis_static_contract(jarvis_html)
    finally:
        server.shutdown()
        server.server_close()

    print(f"dashboard_static_smoke=ok routes={len(ROUTE_MARKERS)} jarvis_static=ok provider_calls=0 writeback=0")


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
