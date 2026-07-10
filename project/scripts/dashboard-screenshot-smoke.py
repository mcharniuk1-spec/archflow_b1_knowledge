#!/usr/bin/env python3
"""Capture public-safe dashboard route screenshots with headless Chrome."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = REPO_ROOT / "project" / "runs" / "2026-07-02-e1-2-testmeeting-dashboard-architecture"
ROUTES = {
    "service": "#service",
    "schema": "#schema",
}
BREAKPOINTS = {
    "desktop": (1440, 1200),
    "mobile": (390, 1200),
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
    raise RuntimeError("Headless Chrome/Chromium was not found. Set CHROME_PATH to run screenshot smoke.")


def capture(chrome: str, url: str, output_path: Path, size: tuple[int, int], timeout_seconds: int) -> dict[str, object]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    width, height = size
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
        "--force-device-scale-factor=1",
        f"--window-size={width},{height}",
        f"--screenshot={output_path}",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=2500",
        url,
    ]
    completed = subprocess.run(command, check=False, text=True, capture_output=True, timeout=timeout_seconds)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or f"chrome exited {completed.returncode}")
    size_bytes = output_path.stat().st_size
    if size_bytes < 10_000:
        raise RuntimeError(f"screenshot too small: {output_path} ({size_bytes} bytes)")
    try:
        report_path = output_path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        # Temporary QA output may intentionally live outside the public repo.
        # Keep the generated report portable and free of local absolute paths.
        report_path = output_path.name
    return {
        "path": report_path,
        "width": width,
        "height": height,
        "bytes": size_bytes,
    }


def run(output_dir: Path, timeout_seconds: int) -> list[dict[str, object]]:
    chrome = find_chrome()
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(REPO_ROOT), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}/project/dashboard/"
    results: list[dict[str, object]] = []
    try:
        for route_name, route_hash in ROUTES.items():
            for breakpoint_name, size in BREAKPOINTS.items():
                filename = f"dashboard-{route_name}-{breakpoint_name}.png"
                url = f"{base_url}{route_hash}"
                result = capture(chrome, url, output_dir / filename, size, timeout_seconds)
                result.update({"route": route_name, "breakpoint": breakpoint_name, "url_shape": f"/project/dashboard/{route_hash}"})
                results.append(result)
    finally:
        server.shutdown()
        server.server_close()

    report_path = output_dir / "dashboard-screenshot-smoke.json"
    report_path.write_text(json.dumps({"status": "ok", "screenshots": results}, indent=2) + "\n", encoding="utf-8")
    md_lines = [
        "# Dashboard Screenshot Smoke",
        "",
        "Status: ok",
        "",
        "| Route | Breakpoint | File | Bytes |",
        "|---|---|---|---:|",
    ]
    for item in results:
        md_lines.append(f"| {item['route']} | {item['breakpoint']} | `{item['path']}` | {item['bytes']} |")
    (output_dir / "dashboard-screenshot-smoke.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture dashboard route screenshots.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT), help="Directory for screenshot artifacts.")
    parser.add_argument("--timeout", type=int, default=60, help="Per-screenshot Chrome timeout.")
    args = parser.parse_args()
    try:
        results = run(Path(args.output_dir), args.timeout)
    except Exception as error:  # noqa: BLE001
        print(f"dashboard_screenshot_smoke=failed reason={error}", file=sys.stderr)
        return 1
    print(f"dashboard_screenshot_smoke=ok screenshots={len(results)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
