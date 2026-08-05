#!/usr/bin/env python3
"""Static and render smoke test for the ArchFlow Crew Desk.

The test serves the repository locally, renders every primary route in
headless Chrome, checks route-specific content and public-safety markers, and
validates the contract/visual/compatibility surface. It does not activate a
provider, write externally, or claim a live agent runtime.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import threading
import time
import xml.etree.ElementTree as ET
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DASHBOARD = ROOT / "project" / "dashboard"
ASSETS = ROOT / "project" / "assets" / "architecture"
CONTRACTS = ROOT / "project" / "system" / "contracts"

ROUTE_MARKERS = {
    "#today": ["One responsive operating flow", "Ask Taras", "First 30 minutes", "Provider disabled"],
    "#work": ["Create one mission card", "Selected crew and handoff order", "Execution boundary", "Save browser-local mission"],
    "#knowledge": ["Seven connected layers", "LlamaIndex", "TurboVec", "Skill Spectre", "Architecture views"],
    "#team": ["Responsive role crew", "Adaptive workflow packs", "Communication protocol", "Oksana"],
    "#review": ["End-to-end trace", "Fail-closed review gates", "Browser-local receipt notebook", "Idempotent action"],
    "#setup": ["Portable installation boundary", "Retrieval and state configuration", "Obsidian", "Orbit", "Provider and writeback stay disabled"],
}

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?i)(?:api[_-]?key|token|password|secret)\s*[:=]\s*['\"][^<\s]{12,}"),
    re.compile("/" + "Users/"),
]


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        return


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise AssertionError(f"{path.relative_to(ROOT)} must contain an object")
    return value


def find_chrome() -> str:
    candidates = [
        os.environ.get("CHROME_PATH"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise RuntimeError("Headless Chrome/Chromium not found. Set CHROME_PATH.")


def validate_contracts() -> None:
    data = load_json(DASHBOARD / "data.json")
    crew = load_json(CONTRACTS / "knowledge-crew-config.json")
    roles = load_json(CONTRACTS / "role-catalog.json")
    workflows = load_json(CONTRACTS / "role-workflows.json")
    controller = load_json(CONTRACTS / "operating-model.json")
    if data.get("schema_version") != "2.0.0":
        raise AssertionError("dashboard data schema must be 2.0.0")
    if data["counts"] != {
        "layers": 7,
        "roles": 21,
        "workflow_packs": 10,
        "research_methods": 10,
        "context_token_ceiling": 12000,
    }:
        raise AssertionError(f"dashboard counts drifted: {data['counts']}")
    call_names = [role["call_name"] for role in roles["roles"]]
    if len(call_names) != 21 or len(set(call_names)) != 21:
        raise AssertionError("role call names must be 21 unique values")
    if any(re.fullmatch(r"[A-Za-z]+", name) is None for name in call_names):
        raise AssertionError("role call names must contain English letters only")
    if [layer["id"] for layer in crew["layers"]] != [f"L{i}" for i in range(1, 8)]:
        raise AssertionError("knowledge layers must be ordered L1-L7")
    if len(workflows["packs"]) != 10:
        raise AssertionError("expected ten adaptive workflow packs")
    role_ids = {role["id"] for role in roles["roles"]}
    required_defaults = {"inputs", "owned_output", "allowed_skills", "allowed_tools", "permission_mode", "reviewer_route", "handoff_to"}
    for role in roles["roles"]:
        if not required_defaults.issubset(role.get("task_defaults", {})):
            raise AssertionError(f"role task contract incomplete: {role['id']}")
    for pack in workflows["packs"]:
        if not set(pack["roles"]).issubset(role_ids):
            raise AssertionError(f"workflow pack uses a noncanonical role ID: {pack['id']}")
    if controller["provider_default"] != "disabled" or controller["writeback_default"] != "disabled":
        raise AssertionError("controller public defaults must stay disabled")


def validate_visuals() -> None:
    stems = [
        "knowledge-crew-tower",
        "context-input-flow",
        "output-receipt-flow",
        "onboarding-teamwork-flow",
    ]
    required_text = {
        "knowledge-crew-tower": ["CASE AUTHORITY", "LLAMAINDEX", "TURBOVEC", "LANGGRAPH", "ACCOUNTABLE OUTPUTS"],
        "context-input-flow": ["STABLE CAG", "LLAMAINDEX ROUTER", "EXACT-READ GATE", "ROLE-SAFE CAPSULE"],
        "output-receipt-flow": ["REQUIREMENT COVERAGE", "INDEPENDENT REVIEW", "RESULT RECEIPT", "MAINTAINED KNOWLEDGE"],
        "onboarding-teamwork-flow": ["FIRST MISSION", "TEAM WORK", "MANAGER / OWNER INTERRUPT", "EMPLOYEE OUTCOME"],
    }
    for stem in stems:
        svg = ASSETS / f"{stem}.svg"
        png = ASSETS / f"{stem}.png"
        if not svg.exists() or not png.exists() or png.stat().st_size < 100_000:
            raise AssertionError(f"missing or empty visual pair: {stem}")
        ET.parse(svg)
        text = svg.read_text(encoding="utf-8").upper()
        missing = [marker for marker in required_text[stem] if marker not in text]
        if missing:
            raise AssertionError(f"{stem} missing labels: {missing}")


def validate_compatibility() -> None:
    config = load_json(ROOT / "vercel.json")
    redirects = {item.get("source"): item.get("destination") for item in config.get("redirects", [])}
    for source in ("/dashboard", "/dashboard/"):
        if redirects.get(source) != "/project/dashboard/":
            raise AssertionError(f"{source} must redirect to the Crew Desk")
    for source in ("/jarvis", "/jarvis/"):
        if redirects.get(source) != "/project/dashboard/#today":
            raise AssertionError(f"{source} must redirect to embedded Crew Desk guidance")
    jarvis_html = (ROOT / "jarvis.html").read_text(encoding="utf-8")
    if "project/dashboard/#today" not in jarvis_html or "Guarded operator chat" in jarvis_html:
        raise AssertionError("legacy Jarvis page must be a compatibility redirect, not a second operator surface")


def validate_source_boundary() -> None:
    source = (DASHBOARD / "app.js").read_text(encoding="utf-8")
    required = [
        "provider_called: false",
        "writeback_performed: false",
        "external_action_performed: false",
        "validateBridge",
        "materializeRoleTaskBindings",
        "role_task_bindings",
        "intersection_only_no_authority_expansion",
        'Object.prototype.hasOwnProperty.call(source, "turbovec_candidate")',
        'parsed.hostname === "127.0.0.1"',
        'parsed.hostname === "localhost"',
        "archflow_local_review_packet",
    ]
    missing = [marker for marker in required if marker not in source]
    if missing:
        raise AssertionError(f"dashboard source boundary missing: {missing}")
    if re.search(r"fetch\(\s*(?!path\b)", source):
        raise AssertionError("dashboard may fetch only its fixed local contract path variable")


def render(chrome: str, url: str, timeout: int) -> str:
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
        "--hide-scrollbars",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=1800",
        "--dump-dom",
        url,
    ]
    completed = subprocess.run(command, text=True, capture_output=True, timeout=timeout, check=False)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or f"Chrome exited {completed.returncode}")
    return completed.stdout


def assert_route(route: str, html: str) -> None:
    missing = [marker for marker in ROUTE_MARKERS[route] if marker not in html]
    if missing:
        raise AssertionError(f"{route} missing markers: {missing}")
    if "Architecture 1" in html or "Architecture 2" in html:
        raise AssertionError(f"{route} exposed removed top-level architecture labels")
    leaks = [pattern.pattern for pattern in SECRET_PATTERNS if pattern.search(html)]
    if leaks:
        raise AssertionError(f"{route} exposed blocked patterns: {leaks}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=0)
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--skip-browser", action="store_true")
    args = parser.parse_args()

    validate_contracts()
    validate_visuals()
    validate_compatibility()
    validate_source_boundary()
    print("dashboard_static_contract=ok")

    if args.skip_browser:
        print("browser_render=skipped")
        return 0

    chrome = find_chrome()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), QuietHandler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    previous = Path.cwd()
    try:
        os.chdir(ROOT)
        thread.start()
        time.sleep(0.15)
        base = f"http://127.0.0.1:{port}/project/dashboard/"
        for route in ROUTE_MARKERS:
            assert_route(route, render(chrome, base + route, args.timeout))
            print(f"route={route}:ok")
    finally:
        server.shutdown()
        server.server_close()
        os.chdir(previous)
    print("dashboard_render_smoke=ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
