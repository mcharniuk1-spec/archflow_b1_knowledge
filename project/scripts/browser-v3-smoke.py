#!/usr/bin/env python3
"""Verify the ArchFlow Knowledge Operator and Jarvis V3 browser contract.

The smoke is dependency-free beyond Chrome. It uses the exact-viewport CDP
client from ``dashboard-screenshot-smoke.py`` and performs no provider call,
authentication attempt, download, or external write.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import tempfile
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
HELPER_PATH = Path(__file__).with_name("dashboard-screenshot-smoke.py")
BREAKPOINTS = {
    "desktop": (1440, 1200),
    "laptop": (1024, 1200),
    "tablet": (768, 1200),
    "mobile": (390, 1200),
    "compact": (320, 1200),
}
ROUTES = {
    "manual": "A practical operating system for human + agent work.",
    "operations": "Prepare a bounded case",
    "communication": "One communication surface, one visible state.",
    "agents": "A role exists to own an output, not to decorate an org chart.",
    "setup": "The core works without an API key.",
    "runs": "Evidence is useful only when the denominator is visible.",
    "architecture": "Four views, one operating model.",
    "knowledge": "Retrieval finds evidence; review decides what becomes knowledge.",
    "workflow": "State tracing connects every loop.",
    "configuration": "Portable defaults, private values, explicit activation.",
}


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        return


def load_browser_helper():
    spec = importlib.util.spec_from_file_location("archflow_dashboard_cdp", HELPER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load the exact-viewport Chrome helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def wait_for(browser, expression: str, label: str, timeout_seconds: int) -> object:
    deadline = time.monotonic() + timeout_seconds
    last = None
    while time.monotonic() < deadline:
        last = browser.evaluate(expression)
        if last:
            return last
        time.sleep(0.1)
    raise RuntimeError(f"timed out waiting for {label}; last={last!r}")


LAYOUT_EXPRESSION = r"""
(() => {
  const visible = (node) => {
    if (!(node instanceof Element)) return false;
    const style = getComputedStyle(node);
    const box = node.getBoundingClientRect();
    return style.display !== 'none' && style.visibility !== 'hidden' && box.width > 0 && box.height > 0;
  };
  const box = (node) => {
    const value = node.getBoundingClientRect();
    return {left:value.left,right:value.right,top:value.top,bottom:value.bottom,width:value.width,height:value.height};
  };
  const name = (node) => node.id || node.getAttribute('data-route') || node.className || node.tagName;
  const collision = (a, b) => {
    const left = box(a); const right = box(b);
    return Math.min(left.right, right.right) - Math.max(left.left, right.left) > 1 &&
      Math.min(left.bottom, right.bottom) - Math.max(left.top, right.top) > 1;
  };
  const controlViolations = [...document.querySelectorAll('a,button,input,textarea,select')]
    .filter(visible)
    .flatMap((node) => {
      const value = box(node);
      const outside = !node.closest('.nav') && (value.left < -1 || value.right > innerWidth + 1);
      const tooSmall = ['INPUT','TEXTAREA','SELECT','BUTTON'].includes(node.tagName) && node.type !== 'checkbox' && value.height < 36;
      return outside || tooSmall ? [{node:name(node), outside, tooSmall, box:value}] : [];
    });
  const grids = ['.topbar-actions','.docs-grid','.field-row','.metric-grid-v3','.skill-grid-v3','.workflow-grid-v3','.setup-grid','.case-actions-v3'];
  const collisions = grids.flatMap((selector) => [...document.querySelectorAll(selector)].flatMap((grid) => {
    const children = [...grid.children].filter(visible); const failures = [];
    for (let i=0; i<children.length; i+=1) for (let j=i+1; j<children.length; j+=1) {
      if (collision(children[i], children[j])) failures.push({selector,left:name(children[i]),right:name(children[j])});
    }
    return failures;
  }));
  const duplicateIds = [...document.querySelectorAll('[id]')].map((node) => node.id).filter((id, index, all) => all.indexOf(id) !== index);
  const unlabeled = [...document.querySelectorAll('input,textarea,select')].filter(visible).filter((node) => {
    const id = node.id; return !node.getAttribute('aria-label') && !(id && document.querySelector(`label[for="${CSS.escape(id)}"]`)) && !node.closest('label');
  }).map(name);
  const animated = matchMedia('(prefers-reduced-motion: reduce)').matches
    ? [...document.querySelectorAll('*')].filter(visible).filter((node) => {
        const style = getComputedStyle(node);
        return style.animationName !== 'none' && !['0s','0ms','0.01ms'].includes(style.animationDuration);
      }).map(name)
    : [];
  return {
    rootOverflow: document.documentElement.scrollWidth > innerWidth + 1 || document.body.scrollWidth > innerWidth + 1,
    rootWidth: document.documentElement.scrollWidth,
    viewportWidth: innerWidth,
    controlViolations,
    collisions,
    duplicateIds,
    unlabeled,
    animated,
    title: document.querySelector('#pageTitle')?.textContent || document.title,
    text: document.querySelector('#view')?.textContent || document.body.textContent,
  };
})()
"""


def assert_layout(result: object, marker: str, route: str, breakpoint: str) -> dict[str, object]:
    if not isinstance(result, dict):
        raise RuntimeError(f"no layout result for {route}/{breakpoint}")
    failures: list[str] = []
    if result.get("rootOverflow"):
        failures.append(f"root overflow {result.get('rootWidth')}>{result.get('viewportWidth')}")
    for key in ("controlViolations", "collisions", "duplicateIds", "unlabeled", "animated"):
        if result.get(key):
            failures.append(f"{key}={result[key]}")
    if marker not in str(result.get("text", "")):
        failures.append(f"missing marker {marker!r}")
    if failures:
        raise RuntimeError(f"browser contract failed for {route}/{breakpoint}: {'; '.join(failures)}")
    return {
        "route": route,
        "breakpoint": breakpoint,
        "width": result.get("viewportWidth"),
        "root_overflow": False,
        "control_violations": 0,
        "collisions": 0,
        "duplicate_ids": 0,
        "unlabeled_fields": 0,
        "reduced_motion_animations": 0,
    }


def jarvis_check(browser, url: str, size: tuple[int, int], breakpoint: str) -> dict[str, object]:
    browser.navigate(url, size, ready_selector="#packet-form")
    result = browser.evaluate(
        r"""
        (() => {
          const rootOverflow = document.documentElement.scrollWidth > innerWidth + 1 || document.body.scrollWidth > innerWidth + 1;
          const fields = [...document.querySelectorAll('#packet-form input,#packet-form textarea,#packet-form button')];
          const outside = fields.filter((node) => { const r=node.getBoundingClientRect(); return r.left < -1 || r.right > innerWidth + 1; }).map((node) => node.id || node.name || node.tagName);
          const labels = fields.filter((node) => node.tagName !== 'BUTTON' && node.type !== 'checkbox').filter((node) => !node.closest('label') && !(node.id && document.querySelector(`label[for="${CSS.escape(node.id)}"]`))).map((node) => node.id);
          const forbidden = ['owner token','api base','guest preview','model catalog'].filter((value) => document.body.textContent.toLowerCase().includes(value));
          const github = document.querySelector('a[aria-label*="GitHub"]')?.href || '';
          const admin = document.querySelector('[data-admin-action]')?.href || '';
          return {rootOverflow,outside,labels,forbidden,github,admin,text:document.body.textContent};
        })()
        """
    )
    if not isinstance(result, dict):
        raise RuntimeError(f"Jarvis returned no layout result at {breakpoint}")
    failures = []
    for key in ("outside", "labels", "forbidden"):
        if result.get(key):
            failures.append(f"{key}={result[key]}")
    if result.get("rootOverflow"):
        failures.append("root horizontal overflow")
    if result.get("github") != "https://github.com/mcharniuk1-spec/archflow_b1_knowledge":
        failures.append("GitHub link is not canonical HTTPS")
    if result.get("admin") != "https://www.arch-flow.dev/api/auth/google/start?return=jarvis":
        failures.append(f"local administrator route is not hosted server auth: {result.get('admin')}")
    if "Turn a loose issue into a bounded work packet." not in str(result.get("text", "")):
        failures.append("Jarvis product marker missing")
    if failures:
        raise RuntimeError(f"Jarvis contract failed at {breakpoint}: {'; '.join(failures)}")
    return {"breakpoint": breakpoint, "width": size[0], "root_overflow": False, "status": "ok"}


def handoff_check(browser, jarvis_url: str, dashboard_prefix: str, size: tuple[int, int], timeout_seconds: int) -> dict[str, object]:
    browser.navigate(jarvis_url, size, ready_selector="#packet-form")
    browser.evaluate(
        r"""
        (() => {
          const set = (id, value) => { const node=document.querySelector(id); node.value=value; node.dispatchEvent(new Event('input',{bubbles:true})); };
          set('#packet-objective','Prepare a public onboarding architecture brief.');
          set('#packet-output','A source-linked brief with gaps, decisions, and a reviewer handoff.');
          set('#packet-decision','Choose the smallest safe onboarding workflow.');
          document.querySelector('input[name="public_safe_confirmation"]').checked=true;
          document.querySelector('#packet-form').requestSubmit();
          return true;
        })()
        """
    )
    wait_for(
        browser,
        f"location.href.startsWith({json.dumps(dashboard_prefix)}) && location.hash === '#communication' && document.querySelector('#view')?.textContent.includes('Prepare a public onboarding architecture brief.')",
        "Jarvis handoff import",
        timeout_seconds,
    )
    result = browser.evaluate(
        r"""
        (() => ({
          transit: sessionStorage.getItem('archflow.public.v3.handoff'),
          url: location.href,
          content: document.querySelector('#view')?.textContent || '',
        }))()
        """
    )
    if not isinstance(result, dict) or result.get("transit") is not None:
        raise RuntimeError("dashboard did not consume and remove the Jarvis transit packet")
    if "review_required" in str(result.get("url", "")) or "Prepare%20a%20public" in str(result.get("url", "")):
        raise RuntimeError("Jarvis packet data leaked into the URL")
    if "Ready for review" not in str(result.get("content", "")):
        raise RuntimeError("Communication Center did not render the imported review state")
    return {"status": "ok", "transit_key_removed": True, "packet_in_url": False, "provider_calls": 0, "external_writes": 0}


def storage_migration_check(browser, dashboard_url: str, size: tuple[int, int]) -> dict[str, object]:
    browser.navigate(f"{dashboard_url}#manual", size)
    browser.evaluate(
        r"""
        (() => {
          localStorage.removeItem('archflow.public.v3.legacy-cleared');
          localStorage.setItem('archflow.jarvis.legacy','remove');
          localStorage.setItem('archflow.dashboard.legacy','remove');
          localStorage.setItem('archflow.crewDesk.legacy','remove');
          localStorage.setItem('archflow.sharedSession','remove');
          localStorage.setItem('unrelated.keep','yes');
          location.reload();
          return true;
        })()
        """
    )
    time.sleep(0.5)
    browser.navigate(f"{dashboard_url}#manual", size)
    result = browser.evaluate(
        r"""
        (() => ({
          jarvis: localStorage.getItem('archflow.jarvis.legacy'),
          dashboard: localStorage.getItem('archflow.dashboard.legacy'),
          crew: localStorage.getItem('archflow.crewDesk.legacy'),
          shared: localStorage.getItem('archflow.sharedSession'),
          unrelated: localStorage.getItem('unrelated.keep'),
          migration: localStorage.getItem('archflow.public.v3.legacy-cleared'),
        }))()
        """
    )
    if not isinstance(result, dict):
        raise RuntimeError("browser storage migration returned no result")
    if any(result.get(key) is not None for key in ("jarvis", "dashboard", "crew", "shared")):
        raise RuntimeError(f"legacy browser state survived migration: {result}")
    if result.get("unrelated") != "yes" or result.get("migration") != "complete":
        raise RuntimeError(f"storage migration removed unrelated data or lacked receipt: {result}")
    browser.evaluate("localStorage.removeItem('unrelated.keep')")
    return {"status": "ok", "legacy_keys_removed": 4, "unrelated_key_preserved": True}


def direct_file_check(browser, size: tuple[int, int]) -> dict[str, object]:
    dashboard = (REPO_ROOT / "project" / "dashboard" / "index.html").as_uri() + "#manual"
    jarvis = (REPO_ROOT / "jarvis.html").as_uri()
    browser.navigate(dashboard, size)
    dash = browser.evaluate("({text:document.querySelector('#view')?.textContent||'',jarvis:document.querySelector('#jarvisLink')?.href||'',github:document.querySelector('#githubLink')?.href||''})")
    browser.navigate(jarvis, size, ready_selector="#packet-form")
    intake = browser.evaluate("({dashboard:document.querySelector('[data-dashboard-link]')?.href||'',admin:document.querySelector('[data-admin-action]')?.href||'',text:document.body.textContent})")
    if not isinstance(dash, dict) or "A practical operating system" not in str(dash.get("text", "")):
        raise RuntimeError("direct-file dashboard did not render generated data fallback")
    if not str(dash.get("jarvis", "")).endswith("/jarvis.html") or dash.get("github") != "https://github.com/mcharniuk1-spec/archflow_b1_knowledge":
        raise RuntimeError(f"direct-file dashboard route contract failed: {dash}")
    if not isinstance(intake, dict) or not str(intake.get("dashboard", "")).endswith("/project/dashboard/index.html#communication"):
        raise RuntimeError(f"direct-file Jarvis dashboard route failed: {intake}")
    if intake.get("admin") != "https://www.arch-flow.dev/api/auth/google/start?return=jarvis":
        raise RuntimeError(f"direct-file Jarvis administrator route failed: {intake}")
    return {"status": "ok", "dashboard": True, "jarvis": True, "filesystem_root_link": False}


def run(report_path: Path, timeout_seconds: int) -> dict[str, object]:
    helper = load_browser_helper()
    chrome_path = helper.find_chrome()
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(REPO_ROOT), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    origin = f"http://127.0.0.1:{server.server_port}"
    dashboard_url = f"{origin}/project/dashboard/"
    jarvis_url = f"{origin}/jarvis.html"
    browser = helper.ExactViewportChrome(chrome_path, timeout_seconds)
    route_results: list[dict[str, object]] = []
    jarvis_results: list[dict[str, object]] = []
    screenshots: list[str] = []
    try:
        browser.client.command("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-reduced-motion", "value": "reduce"}]})
        for breakpoint, size in BREAKPOINTS.items():
            for route, marker in ROUTES.items():
                browser.navigate(f"{dashboard_url}#{route}", size)
                route_results.append(assert_layout(browser.evaluate(LAYOUT_EXPRESSION), marker, route, breakpoint))
            jarvis_results.append(jarvis_check(browser, jarvis_url, size, breakpoint))
        handoff = handoff_check(browser, jarvis_url, dashboard_url, BREAKPOINTS["mobile"], timeout_seconds)
        migration = storage_migration_check(browser, dashboard_url, BREAKPOINTS["mobile"])
        direct_file = direct_file_check(browser, BREAKPOINTS["compact"])
        with tempfile.TemporaryDirectory(prefix="archflow-v3-visual-") as directory:
            for name, url, size, selector in (
                ("dashboard-desktop.png", f"{dashboard_url}#manual", BREAKPOINTS["desktop"], "#view"),
                ("dashboard-mobile.png", f"{dashboard_url}#manual", BREAKPOINTS["mobile"], "#view"),
                ("jarvis-desktop.png", jarvis_url, BREAKPOINTS["desktop"], "#packet-form"),
                ("jarvis-mobile.png", jarvis_url, BREAKPOINTS["mobile"], "#packet-form"),
            ):
                target = Path(directory) / name
                browser.capture(url, target, size, ready_selector=selector)
                if target.stat().st_size < 10_000:
                    raise RuntimeError(f"visual evidence was unexpectedly small: {name}")
                screenshots.append(name)
    finally:
        browser.close()
        server.shutdown()
        server.server_close()
    report = {
        "schema_version": "1.0",
        "status": "pass",
        "tested_at": "2026-08-11",
        "routes": route_results,
        "jarvis": jarvis_results,
        "handoff": handoff,
        "storage_migration": migration,
        "direct_file": direct_file,
        "visual_inspection_set": screenshots,
        "breakpoints": {name: {"width": size[0], "height": size[1]} for name, size in BREAKPOINTS.items()},
        "provider_calls": 0,
        "external_writes": 0,
        "limitations": [
            "Headless local browser proof, not production availability.",
            "Google authorization needs deployed credentials and live callback readback.",
            "Visual screenshots are temporary QA evidence and contain no private input.",
        ],
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the ArchFlow dashboard and Jarvis V3 browser contract.")
    parser.add_argument("--report", type=Path, default=REPO_ROOT / "project" / "qa" / "dashboard-v3-browser.json")
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()
    try:
        report = run(args.report, args.timeout)
    except Exception as error:  # noqa: BLE001
        print(f"browser_v3_smoke=failed reason={error}")
        return 1
    print(
        "browser_v3_smoke=ok "
        f"route_viewports={len(report['routes'])} jarvis_viewports={len(report['jarvis'])} "
        "handoff=ok direct_file=ok provider_calls=0 external_writes=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
