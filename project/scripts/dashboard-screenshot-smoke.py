#!/usr/bin/env python3
"""Capture public-safe dashboard route screenshots with headless Chrome."""

from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = REPO_ROOT / "project" / "local" / "qa" / "dashboard-screenshots"
ROUTES = {
    "documentation": "#manual",
    "project": "#operations",
    "roles_skills": "#agents",
    "setup": "#setup",
    "evidence": "#runs",
}
TECHNICAL_CONTRAST_ROUTES = {
    "schemas": "#architecture",
    "knowledge": "#knowledge",
    "workflow": "#workflow",
    "configuration": "#configuration",
}
BREAKPOINTS = {
    "desktop": (1440, 1200),
    "laptop": (1024, 1200),
    "tablet": (768, 1200),
    "mobile": (390, 1200),
    "compact": (320, 1200),
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


class CDPClient:
    """Small dependency-free Chrome DevTools Protocol client for exact viewports."""

    def __init__(self, websocket_url: str, timeout_seconds: int) -> None:
        parsed = urlparse(websocket_url)
        self.socket = socket.create_connection((parsed.hostname, parsed.port), timeout=timeout_seconds)
        self.socket.settimeout(timeout_seconds)
        self.next_id = 1
        key = base64.b64encode(os.urandom(16)).decode("ascii")
        path = parsed.path + (f"?{parsed.query}" if parsed.query else "")
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {parsed.hostname}:{parsed.port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        )
        self.socket.sendall(request.encode("ascii"))
        response = self._read_until(b"\r\n\r\n")
        if b" 101 " not in response.split(b"\r\n", 1)[0]:
            raise RuntimeError("Chrome DevTools WebSocket handshake failed")

    def _read_until(self, marker: bytes) -> bytes:
        data = bytearray()
        while marker not in data:
            chunk = self.socket.recv(4096)
            if not chunk:
                raise RuntimeError("Chrome DevTools socket closed during handshake")
            data.extend(chunk)
        return bytes(data)

    def _read_exact(self, size: int) -> bytes:
        data = bytearray()
        while len(data) < size:
            chunk = self.socket.recv(size - len(data))
            if not chunk:
                raise RuntimeError("Chrome DevTools socket closed")
            data.extend(chunk)
        return bytes(data)

    def _send_frame(self, payload: bytes, opcode: int = 0x1) -> None:
        first = 0x80 | opcode
        size = len(payload)
        if size < 126:
            header = bytes((first, 0x80 | size))
        elif size < 65536:
            header = bytes((first, 0x80 | 126)) + struct.pack("!H", size)
        else:
            header = bytes((first, 0x80 | 127)) + struct.pack("!Q", size)
        mask = os.urandom(4)
        masked = bytes(value ^ mask[index % 4] for index, value in enumerate(payload))
        self.socket.sendall(header + mask + masked)

    def _read_message(self) -> str:
        fragments = bytearray()
        while True:
            first, second = self._read_exact(2)
            final = bool(first & 0x80)
            opcode = first & 0x0F
            masked = bool(second & 0x80)
            size = second & 0x7F
            if size == 126:
                size = struct.unpack("!H", self._read_exact(2))[0]
            elif size == 127:
                size = struct.unpack("!Q", self._read_exact(8))[0]
            mask = self._read_exact(4) if masked else b""
            payload = self._read_exact(size)
            if masked:
                payload = bytes(value ^ mask[index % 4] for index, value in enumerate(payload))
            if opcode == 0x8:
                raise RuntimeError("Chrome DevTools closed the WebSocket")
            if opcode == 0x9:
                self._send_frame(payload, opcode=0xA)
                continue
            if opcode in (0x0, 0x1):
                fragments.extend(payload)
                if final:
                    return fragments.decode("utf-8")

    def command(self, method: str, params: dict[str, object] | None = None) -> dict[str, object]:
        command_id = self.next_id
        self.next_id += 1
        payload = json.dumps({"id": command_id, "method": method, "params": params or {}}).encode("utf-8")
        self._send_frame(payload)
        while True:
            message = json.loads(self._read_message())
            if message.get("id") != command_id:
                continue
            if "error" in message:
                raise RuntimeError(f"Chrome DevTools command failed: {message['error']}")
            result = message.get("result", {})
            return result if isinstance(result, dict) else {}

    def close(self) -> None:
        try:
            self._send_frame(b"", opcode=0x8)
        finally:
            self.socket.close()


class ExactViewportChrome:
    """Launch one isolated browser and capture routes via CDP device metrics."""

    def __init__(self, chrome: str, timeout_seconds: int) -> None:
        self.timeout_seconds = timeout_seconds
        self.profile = tempfile.TemporaryDirectory(prefix="archflow-dashboard-chrome-")
        probe = socket.socket()
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
        probe.close()
        self.process = subprocess.Popen(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-extensions",
                "--disable-background-networking",
                "--disable-sync",
                "--no-first-run",
                "--no-default-browser-check",
                f"--remote-debugging-port={port}",
                f"--user-data-dir={self.profile.name}",
                "about:blank",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        deadline = time.monotonic() + timeout_seconds
        targets: list[dict[str, object]] = []
        while time.monotonic() < deadline:
            if self.process.poll() is not None:
                raise RuntimeError(f"Chrome exited before DevTools was ready ({self.process.returncode})")
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=1) as response:
                    parsed = json.loads(response.read())
                    if isinstance(parsed, list):
                        targets = parsed
            except (OSError, ValueError):
                time.sleep(0.1)
                continue
            page_target = next((item for item in targets if item.get("type") == "page"), None)
            if page_target and isinstance(page_target.get("webSocketDebuggerUrl"), str):
                self.client = CDPClient(page_target["webSocketDebuggerUrl"], timeout_seconds)
                self.client.command("Page.enable")
                self.client.command("Runtime.enable")
                return
            time.sleep(0.1)
        raise RuntimeError("Chrome DevTools did not become ready before the timeout")

    def evaluate(self, expression: str) -> object:
        result = self.client.command(
            "Runtime.evaluate",
            {"expression": expression, "returnByValue": True, "awaitPromise": True},
        )
        if result.get("exceptionDetails"):
            raise RuntimeError(f"dashboard JavaScript evaluation failed: {result['exceptionDetails']}")
        payload = result.get("result", {})
        return payload.get("value") if isinstance(payload, dict) else None

    def navigate(
        self,
        url: str,
        size: tuple[int, int],
        require_overflow_free: bool = True,
        ready_selector: str = "#view",
    ) -> None:
        width, height = size
        self.client.command(
            "Emulation.setDeviceMetricsOverride",
            {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": False},
        )
        self.client.command("Emulation.setScrollbarsHidden", {"hidden": True})
        self.client.command("Page.navigate", {"url": url})
        expected_hash = f"#{urlparse(url).fragment}" if urlparse(url).fragment else ""
        deadline = time.monotonic() + self.timeout_seconds
        ready = False
        while time.monotonic() < deadline:
            overflow_clause = "document.documentElement.scrollWidth <= window.innerWidth && " if require_overflow_free else ""
            ready = bool(
                self.evaluate(
                    "document.readyState === 'complete' && "
                    f"location.hash === {json.dumps(expected_hash)} && "
                    f"{overflow_clause}"
                    f"document.querySelector({json.dumps(ready_selector)})?.textContent.trim().length > 200"
                )
            )
            if ready:
                break
            time.sleep(0.1)
        if not ready:
            raise RuntimeError(f"dashboard did not become ready or overflow-free at {width}x{height}")

    def capture(
        self,
        url: str,
        output_path: Path,
        size: tuple[int, int],
        ready_selector: str = "#view",
        scroll_selector: str | None = None,
    ) -> None:
        self.navigate(url, size, ready_selector=ready_selector)
        scroll_expression = (
            f"document.querySelector({json.dumps(scroll_selector)})?.scrollIntoView({{block: 'start'}}); "
            "window.scrollBy(0, -74);"
            if scroll_selector
            else "window.scrollTo(0, 0);"
        )
        self.client.command(
            "Runtime.evaluate",
            {
                "expression": (
                    f"{scroll_expression} "
                    "document.querySelector('.workspace')?.scrollTo(0, 0); "
                    "document.querySelector('.sidebar')?.scrollTo(0, 0);"
                )
            },
        )
        result = self.client.command(
            "Page.captureScreenshot",
            {"format": "png", "fromSurface": True, "captureBeyondViewport": False},
        )
        encoded = result.get("data")
        if not isinstance(encoded, str):
            raise RuntimeError("Chrome DevTools returned no screenshot data")
        output_path.write_bytes(base64.b64decode(encoded))

    def close(self) -> None:
        if hasattr(self, "client"):
            self.client.close()
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=5)
        self.profile.cleanup()


def capture(
    browser: ExactViewportChrome,
    url: str,
    output_path: Path,
    size: tuple[int, int],
    ready_selector: str = "#view",
    scroll_selector: str | None = None,
) -> dict[str, object]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    width, height = size
    browser.capture(
        url,
        output_path,
        size,
        ready_selector=ready_selector,
        scroll_selector=scroll_selector,
    )
    size_bytes = output_path.stat().st_size
    if size_bytes < 10_000:
        raise RuntimeError(f"screenshot too small: {output_path} ({size_bytes} bytes)")
    png = output_path.read_bytes()
    if png[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError(f"screenshot is not a PNG: {output_path}")
    actual_width, actual_height = struct.unpack("!II", png[16:24])
    if (actual_width, actual_height) != (width, height):
        raise RuntimeError(
            f"screenshot viewport mismatch: expected {width}x{height}, got {actual_width}x{actual_height}"
        )
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


def jarvis_layout_check(
    browser: ExactViewportChrome,
    jarvis_url: str,
    breakpoint_name: str,
    size: tuple[int, int],
) -> dict[str, object]:
    browser.client.command(
        "Emulation.setEmulatedMedia",
        {"media": "", "features": [{"name": "prefers-reduced-motion", "value": "reduce"}]},
    )
    browser.navigate(jarvis_url, size, ready_selector="#packet-form")
    result = browser.evaluate(
        """
        (() => {
          const visible = (element) => {
            const style = getComputedStyle(element);
            const rect = element.getBoundingClientRect();
            return style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && rect.height > 0;
          };
          const label = (element) => element.id || element.getAttribute('data-action') || element.className || element.tagName;
          const rect = (element) => {
            const value = element.getBoundingClientRect();
            return { left: value.left, right: value.right, top: value.top, bottom: value.bottom, width: value.width, height: value.height };
          };
          const overlap = (left, right) => {
            const a = rect(left);
            const b = rect(right);
            return Math.min(a.right, b.right) - Math.max(a.left, b.left) > 1 &&
              Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > 1;
          };
          const containerSelectors = [
            '.site-header', '.hero', '.hero-copy', '.route-map', '.workspace',
            '.packet-panel', '.context-rail', '.rail-card', '.field', '.field-row',
            '.submit-row', '.site-footer'
          ];
          const containerOverflow = containerSelectors.flatMap((selector) =>
            [...document.querySelectorAll(selector)].filter(visible).filter((element) => {
              const overflowX = getComputedStyle(element).overflowX;
              if (overflowX === 'hidden' || overflowX === 'clip') {
                const boundary = rect(element);
                return [...element.children].filter(visible).some((child) => {
                  const value = rect(child);
                  return value.left < boundary.left - 1 || value.right > boundary.right + 1;
                });
              }
              return element.scrollWidth > element.clientWidth + 1;
            }).map((element) => ({
              selector,
              overflowX: getComputedStyle(element).overflowX,
              scrollWidth: element.scrollWidth,
              clientWidth: element.clientWidth,
            }))
          );
          const controlViolations = [...document.querySelectorAll('a, button, input, select, textarea')]
            .filter(visible)
            .flatMap((element) => {
              const value = rect(element);
              const boundaryElement = element.closest('.field, .safety-confirmation, .submit-row, .header-actions, .site-footer') || document.documentElement;
              const boundary = rect(boundaryElement);
              const outsideViewport = value.left < -1 || value.right > innerWidth + 1;
              const formControl = element.matches('#packet-form input, #packet-form select, #packet-form textarea, #packet-form button');
              const outsideContainer = formControl && (value.left < boundary.left - 1 || value.right > boundary.right + 1);
              const undersized = formControl && element.type !== 'checkbox' && value.height < 40;
              return outsideViewport || outsideContainer || undersized
                ? [{ control: label(element), outsideViewport, outsideContainer, undersized, bounds: value }]
                : [];
            });
          const collisions = ['.header-actions', '.truth-row', '.hero', '.workspace', '.field-row', '.submit-row', '.context-rail', '.site-footer']
            .flatMap((selector) => [...document.querySelectorAll(selector)].flatMap((grid) => {
              const children = [...grid.children].filter(visible);
              const found = [];
              for (let index = 0; index < children.length; index += 1) {
                for (let other = index + 1; other < children.length; other += 1) {
                  if (overlap(children[index], children[other])) {
                    found.push({ selector, left: label(children[index]), right: label(children[other]) });
                  }
                }
              }
              return found;
            }));
          const workspace = document.querySelector('.workspace');
          const packet = document.querySelector('.packet-panel');
          const contextRail = document.querySelector('.context-rail');
          const workspaceBounds = rect(workspace);
          const packetBounds = rect(packet);
          const contextBounds = rect(contextRail);
          const stackedWithoutOverlap = innerWidth > 900 || contextBounds.top >= packetBounds.bottom - 1;
          const sideBySideWithoutOverlap = innerWidth <= 900 || contextBounds.left >= packetBounds.right - 1;
          const workspaceContained = [packetBounds, contextBounds].every((value) =>
            value.left >= workspaceBounds.left - 1 && value.right <= workspaceBounds.right + 1
          );
          const durationMs = (value) => {
            const trimmed = String(value).trim();
            if (trimmed.endsWith('ms')) return Number.parseFloat(trimmed);
            if (trimmed.endsWith('s')) return Number.parseFloat(trimmed) * 1000;
            return 0;
          };
          const motionViolations = [...document.querySelectorAll('*')].filter(visible).flatMap((element) => {
            const states = ['', '::before', '::after'];
            return states.flatMap((pseudo) => {
              const style = getComputedStyle(element, pseudo || null);
              const names = style.animationName.split(',').map((value) => value.trim());
              const animationActive = names.some((name) => name !== 'none') &&
                style.animationDuration.split(',').some((duration) => durationMs(duration) > 1);
              const transitionActive = style.transitionDuration.split(',').some((duration) => durationMs(duration) > 1);
              return animationActive || transitionActive ? [`${label(element)}${pseudo}`] : [];
            });
          });
          return {
            viewportOverflow: document.documentElement.scrollWidth > innerWidth + 1 || document.body.scrollWidth > innerWidth + 1,
            containerOverflow,
            controlViolations,
            collisions,
            stackedWithoutOverlap,
            sideBySideWithoutOverlap,
            workspaceContained,
            reducedMotionActive: matchMedia('(prefers-reduced-motion: reduce)').matches,
            motionViolations,
            viewport: { width: innerWidth, height: innerHeight },
          };
        })()
        """
    )
    if not isinstance(result, dict):
        raise RuntimeError(f"Jarvis layout returned no result at {breakpoint_name}")
    failures = []
    if result.get("viewportOverflow"):
        failures.append("root horizontal overflow")
    for key in ("containerOverflow", "controlViolations", "collisions", "motionViolations"):
        if result.get(key):
            failures.append(f"{key}={result[key]}")
    if not result.get("stackedWithoutOverlap"):
        failures.append("packet and guidance columns overlap instead of stacking")
    if not result.get("sideBySideWithoutOverlap"):
        failures.append("packet and guidance columns overlap at a wide viewport")
    if not result.get("workspaceContained"):
        failures.append("packet or guidance column escapes the workspace")
    if not result.get("reducedMotionActive"):
        failures.append("reduced-motion emulation is not active")
    if failures:
        raise RuntimeError(f"Jarvis responsive contract failed at {breakpoint_name}: {'; '.join(failures)}")
    return {
        "status": "ok",
        "breakpoint": breakpoint_name,
        "width": size[0],
        "height": size[1],
        "container_overflow_count": 0,
        "control_violation_count": 0,
        "collision_count": 0,
        "reduced_motion_animation_count": 0,
        "reduced_motion_transition_count": 0,
        "stacked_without_overlap": bool(result.get("stackedWithoutOverlap")),
        "side_by_side_without_overlap": bool(result.get("sideBySideWithoutOverlap")),
        "workspace_contained": bool(result.get("workspaceContained")),
    }


def contrast_check(
    browser: ExactViewportChrome,
    base_url: str,
    route_name: str,
    route_hash: str,
    breakpoint_name: str,
    size: tuple[int, int],
) -> dict[str, object]:
    browser.navigate(f"{base_url}{route_hash}", size, require_overflow_free=False)
    result = browser.evaluate(
        """
        (() => {
          const parse = (value) => {
            const match = String(value).match(/[\\d.]+/g);
            if (!match || match.length < 3) return null;
            return { rgb: match.slice(0, 3).map(Number), alpha: match.length > 3 ? Number(match[3]) : 1 };
          };
          const channel = (value) => {
            const scaled = value / 255;
            return scaled <= 0.04045 ? scaled / 12.92 : ((scaled + 0.055) / 1.055) ** 2.4;
          };
          const luminance = (rgb) => 0.2126 * channel(rgb[0]) + 0.7152 * channel(rgb[1]) + 0.0722 * channel(rgb[2]);
          const background = (element) => {
            let node = element;
            while (node) {
              const parsed = parse(getComputedStyle(node).backgroundColor);
              if (parsed && parsed.alpha > 0.99) return parsed.rgb;
              node = node.parentElement;
            }
            return [255, 255, 255];
          };
          const labels = [...document.querySelectorAll('#view .eyebrow, #view .workflow-grid-v3 > article > span, #view .table th')]
            .filter((element) => {
              const style = getComputedStyle(element);
              const value = element.getBoundingClientRect();
              return style.display !== 'none' && style.visibility !== 'hidden' && value.width > 0 && value.height > 0;
            });
          const measurements = labels.map((element) => {
            const foreground = parse(getComputedStyle(element).color)?.rgb;
            const backdrop = background(element);
            if (!foreground) return null;
            const lighter = Math.max(luminance(foreground), luminance(backdrop));
            const darker = Math.min(luminance(foreground), luminance(backdrop));
            return Number(((lighter + 0.05) / (darker + 0.05)).toFixed(3));
          }).filter((value) => value !== null);
          return {
            count: measurements.length,
            minimum_ratio: measurements.length ? Math.min(...measurements) : null,
            foreground: labels.length ? getComputedStyle(labels[0]).color : null,
          };
        })()
        """
    )
    if not isinstance(result, dict) or not result.get("count"):
        raise RuntimeError(f"no technical-view labels found for contrast check on {route_name}/{breakpoint_name}")
    minimum = float(result.get("minimum_ratio", 0))
    if minimum < 4.5:
        raise RuntimeError(
            f"technical-view label contrast failed on {route_name}/{breakpoint_name}: {minimum:.3f}:1"
        )
    return {
        "route": route_name,
        "breakpoint": breakpoint_name,
        "width": size[0],
        "height": size[1],
        "elements": int(result["count"]),
        "minimum_ratio": minimum,
        "foreground": result.get("foreground"),
        "threshold": 4.5,
        "status": "ok",
    }


def browser_storage_reset_check(browser: ExactViewportChrome, base_url: str) -> dict[str, object]:
    browser.navigate(f"{base_url}#operations", BREAKPOINTS["mobile"])
    browser.evaluate(
        """
        (() => {
          localStorage.setItem('archflow.public.v3.case-draft', JSON.stringify({
            schema_version: '3.0',
            kind: 'archflow_public_case',
            objective: 'QA seeded objective',
            decision: 'QA seeded decision',
            public_reference: 'public-safe-qa-reference',
            allowed_evidence: 'Public QA fixtures only.',
            exclusions: 'Private material.',
            requested_output: 'QA review packet',
            reviewer: 'Independent reviewer',
            constraints: 'No external action.',
            state: 'review_required',
            updated_at: '2026-01-01T00:00:00.000Z',
          }));
          localStorage.setItem('archflow.public.v3.events', JSON.stringify([{
            title: 'Existing browser-local activity',
            detail: 'Public QA fixture.',
            tone: 'ok',
            at: '2026-01-01T00:00:00.000Z',
          }]));
          sessionStorage.setItem('archflow.public.v3.handoff', 'qa-transit-keep');
          localStorage.setItem('qa.unrelated.persistent', 'keep');
          sessionStorage.setItem('qa.unrelated.session', 'keep');
          return true;
        })()
        """
    )
    browser.client.command("Page.reload", {"ignoreCache": True})
    deadline = time.monotonic() + browser.timeout_seconds
    seeded_draft_loaded = False
    while time.monotonic() < deadline:
        try:
            seeded_draft_loaded = bool(
                browser.evaluate(
                    "document.readyState === 'complete' && "
                    "document.querySelector('#objective')?.value === 'QA seeded objective' && "
                    "Boolean(document.querySelector('#resetCase'))"
                )
            )
        except RuntimeError:
            seeded_draft_loaded = False
        if seeded_draft_loaded:
            break
        time.sleep(0.1)
    if not seeded_draft_loaded:
        diagnostic = browser.evaluate(
            "({hash: location.hash, ready: document.readyState, "
            "objective: document.querySelector('#objective')?.value ?? null, "
            "resetControl: Boolean(document.querySelector('#resetCase')), "
            "storedDraft: localStorage.getItem('archflow.public.v3.case-draft')})"
        )
        raise RuntimeError(f"dashboard scoped reset fixture did not load: {diagnostic}")

    browser.evaluate("document.querySelector('#resetCase').click()")
    deadline = time.monotonic() + browser.timeout_seconds
    reset_applied = False
    while time.monotonic() < deadline:
        reset_applied = bool(
            browser.evaluate(
                "document.querySelector('#objective')?.value === '' && "
                "JSON.parse(localStorage.getItem('archflow.public.v3.case-draft') || 'null')?.state === 'draft' && "
                "JSON.parse(localStorage.getItem('archflow.public.v3.case-draft') || 'null')?.updated_at === null"
            )
        )
        if reset_applied:
            break
        time.sleep(0.1)
    if not reset_applied:
        raise RuntimeError("dashboard Reset draft control did not restore the V3 draft defaults")

    browser.client.command("Page.reload", {"ignoreCache": True})
    deadline = time.monotonic() + browser.timeout_seconds
    reloaded = False
    while time.monotonic() < deadline:
        try:
            reloaded = bool(
                browser.evaluate(
                    "document.readyState === 'complete' && "
                    "document.querySelector('#objective')?.value === '' && "
                    "Boolean(document.querySelector('#resetCase'))"
                )
            )
        except RuntimeError:
            reloaded = False
        if reloaded:
            break
        time.sleep(0.1)
    if not reloaded:
        raise RuntimeError("dashboard scoped reset did not persist across reload")

    result = browser.evaluate(
        """
        (() => {
          const draft = JSON.parse(localStorage.getItem('archflow.public.v3.case-draft') || 'null');
          const events = JSON.parse(localStorage.getItem('archflow.public.v3.events') || '[]');
          const handoff = sessionStorage.getItem('archflow.public.v3.handoff');
          const unrelated = {
            persistent: localStorage.getItem('qa.unrelated.persistent'),
            session: sessionStorage.getItem('qa.unrelated.session'),
          };
          localStorage.removeItem('archflow.public.v3.case-draft');
          localStorage.removeItem('archflow.public.v3.events');
          sessionStorage.removeItem('archflow.public.v3.handoff');
          localStorage.removeItem('qa.unrelated.persistent');
          sessionStorage.removeItem('qa.unrelated.session');
          return { draft, eventTitles: events.map((event) => event.title), handoff, unrelated };
        })()
        """
    )
    if not isinstance(result, dict):
        raise RuntimeError("dashboard storage reset returned no result")
    draft = result.get("draft", {})
    expected_defaults = {
        "objective": "",
        "decision": "",
        "public_reference": "",
        "requested_output": "",
        "state": "draft",
        "updated_at": None,
    }
    if not isinstance(draft, dict) or any(draft.get(key) != value for key, value in expected_defaults.items()):
        raise RuntimeError(f"dashboard scoped reset left a non-default case draft: {draft}")
    event_titles = result.get("eventTitles", [])
    if not isinstance(event_titles, list) or "Existing browser-local activity" not in event_titles or "Case draft cleared" not in event_titles:
        raise RuntimeError("dashboard scoped reset did not preserve existing activity and record the reset")
    if result.get("handoff") != "qa-transit-keep":
        raise RuntimeError("dashboard scoped reset removed the Jarvis handoff transit key")
    unrelated = result.get("unrelated", {})
    if unrelated != {"persistent": "keep", "session": "keep"}:
        raise RuntimeError("dashboard storage reset removed unrelated browser data")
    return {
        "status": "ok",
        "case_draft_default_after_reload": True,
        "existing_activity_preserved": True,
        "handoff_transit_preserved": True,
        "unrelated_local_storage_preserved": True,
        "unrelated_session_storage_preserved": True,
    }


def run(output_dir: Path, timeout_seconds: int) -> list[dict[str, object]]:
    chrome = find_chrome()
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(REPO_ROOT), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}/project/dashboard/"
    jarvis_url = f"http://127.0.0.1:{server.server_port}/jarvis.html"
    results: list[dict[str, object]] = []
    contrast_results: list[dict[str, object]] = []
    jarvis_layout_results: list[dict[str, object]] = []
    reset_result: dict[str, object] = {}
    browser: ExactViewportChrome | None = None
    try:
        browser = ExactViewportChrome(chrome, timeout_seconds)
        for route_name, route_hash in ROUTES.items():
            for breakpoint_name, size in BREAKPOINTS.items():
                filename = f"dashboard-{route_name}-{breakpoint_name}.png"
                url = f"{base_url}{route_hash}"
                result = capture(browser, url, output_dir / filename, size)
                result.update({"route": route_name, "breakpoint": breakpoint_name, "url_shape": f"/project/dashboard/{route_hash}"})
                results.append(result)
        for breakpoint_name, size in BREAKPOINTS.items():
            filename = f"jarvis-{breakpoint_name}.png"
            result = capture(browser, jarvis_url, output_dir / filename, size, ready_selector="#packet-form")
            result.update({"route": "jarvis", "breakpoint": breakpoint_name, "url_shape": "/jarvis.html"})
            results.append(result)
            jarvis_layout_results.append(jarvis_layout_check(browser, jarvis_url, breakpoint_name, size))
            form_filename = f"jarvis-form-{breakpoint_name}.png"
            form_result = capture(
                browser,
                jarvis_url,
                output_dir / form_filename,
                size,
                ready_selector="#packet-form",
                scroll_selector="#packet-form",
            )
            form_result.update({"route": "jarvis-form", "breakpoint": breakpoint_name, "url_shape": "/jarvis.html#request-form"})
            results.append(form_result)
        for route_name, route_hash in TECHNICAL_CONTRAST_ROUTES.items():
            for breakpoint_name, size in BREAKPOINTS.items():
                contrast_results.append(
                    contrast_check(browser, base_url, route_name, route_hash, breakpoint_name, size)
                )
        reset_result = browser_storage_reset_check(browser, base_url)
    finally:
        if browser is not None:
            browser.close()
        server.shutdown()
        server.server_close()

    report_path = output_dir / "dashboard-screenshot-smoke.json"
    report_path.write_text(
        json.dumps(
            {
                "status": "ok",
                "screenshots": results,
                "computed_contrast": contrast_results,
                "jarvis_responsive_contract": jarvis_layout_results,
                "browser_storage_reset": reset_result,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
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
    md_lines.extend(
        [
            "",
            "## Computed contrast",
            "",
            "| Technical route | Breakpoint | Labels | Minimum ratio | Threshold |",
            "|---|---|---:|---:|---:|",
        ]
    )
    for item in contrast_results:
        md_lines.append(
            f"| {item['route']} | {item['breakpoint']} | {item['elements']} | "
            f"{item['minimum_ratio']:.3f}:1 | {item['threshold']:.1f}:1 |"
        )
    md_lines.extend(
        [
            "",
            "## Jarvis responsive contract",
            "",
            "| Breakpoint | Viewport | Root/container overflow | Control violations | Collisions | Reduced-motion animations | Reduced-motion transitions |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for item in jarvis_layout_results:
        md_lines.append(
            f"| {item['breakpoint']} | {item['width']}×{item['height']} | "
            f"{item['container_overflow_count']} | {item['control_violation_count']} | "
            f"{item['collision_count']} | {item['reduced_motion_animation_count']} | "
            f"{item['reduced_motion_transition_count']} |"
        )
    md_lines.extend(
        [
            "",
            "## Browser data reset",
            "",
            "The real `Reset draft` control restored only the V3 case draft, preserved existing activity and Jarvis handoff transit, preserved unrelated local and session storage, and remained reset after reload. Status: ok.",
        ]
    )
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
