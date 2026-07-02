(function () {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (reducedMotion.matches) return;

  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)");
  const selectors = [
    "a:not(.skip-link)",
    "button:not(:disabled)",
    ".system-grid article",
    ".output-card",
    ".lane-card",
    ".choice-field label"
  ].join(",");

  function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function pointMetrics(element, event) {
    const rect = element.getBoundingClientRect();
    if (!rect.width || !rect.height) return null;
    const x = clamp(((event.clientX - rect.left) / rect.width - 0.5) * 2, -1, 1);
    const y = clamp(((event.clientY - rect.top) / rect.height - 0.5) * 2, -1, 1);
    const distance = clamp(Math.hypot(x, y), 0, 1);
    return { x, y, distance };
  }

  function setDepthVars(element, metrics, force = 1) {
    if (!metrics) return;
    const isLargeSurface = element.matches(".system-grid article, .output-card, .lane-card");
    const tilt = isLargeSurface ? 7 : 5.4;
    const shift = isLargeSurface ? 3 : 2;
    const lift = isLargeSurface ? 10 : 7;
    element.style.setProperty("--depth-rot-x", `${(-metrics.y * tilt * force).toFixed(3)}deg`);
    element.style.setProperty("--depth-rot-y", `${(metrics.x * tilt * force).toFixed(3)}deg`);
    element.style.setProperty("--depth-shift-x", `${(metrics.x * shift * force).toFixed(3)}px`);
    element.style.setProperty("--depth-shift-y", `${(metrics.y * shift * force).toFixed(3)}px`);
    element.style.setProperty("--depth-z", `${(lift * (0.55 + metrics.distance * 0.45) * force).toFixed(3)}px`);
    element.style.setProperty("--depth-scale", (1 + 0.012 * force).toFixed(4));
    element.style.setProperty("--depth-light-x", `${(50 + metrics.x * 32).toFixed(2)}%`);
    element.style.setProperty("--depth-light-y", `${(50 + metrics.y * 32).toFixed(2)}%`);
    element.style.setProperty("--depth-light", (0.25 + metrics.distance * 0.28 * force).toFixed(3));
  }

  function setPressVars(element, metrics) {
    if (!metrics) return;
    element.style.setProperty("--press-rot-x", `${(-metrics.y * 8).toFixed(3)}deg`);
    element.style.setProperty("--press-rot-y", `${(metrics.x * 8).toFixed(3)}deg`);
    element.style.setProperty("--press-z", "8px");
    element.style.setProperty("--press-light-x", `${(50 + metrics.x * 36).toFixed(2)}%`);
    element.style.setProperty("--press-light-y", `${(50 + metrics.y * 36).toFixed(2)}%`);
    element.style.setProperty("--press-light", (0.48 + metrics.distance * 0.24).toFixed(3));
    element.classList.add("is-press-tilting");
  }

  function resetDepth(element) {
    element.style.setProperty("--depth-rot-x", "0deg");
    element.style.setProperty("--depth-rot-y", "0deg");
    element.style.setProperty("--depth-shift-x", "0px");
    element.style.setProperty("--depth-shift-y", "0px");
    element.style.setProperty("--depth-z", "0px");
    element.style.setProperty("--depth-scale", "1");
    element.style.setProperty("--depth-light", "0");
    element.classList.remove("is-depth-hovered");
  }

  function resetPress(element) {
    element.style.setProperty("--press-rot-x", "0deg");
    element.style.setProperty("--press-rot-y", "0deg");
    element.style.setProperty("--press-z", "0px");
    element.style.setProperty("--press-light", "0");
    element.classList.remove("is-press-tilting");
  }

  function attach(element) {
    if (element.dataset.depthHoverReady === "true") return;
    if (element.closest("[data-depth-hover-disabled]")) return;
    element.dataset.depthHoverReady = "true";
    element.classList.add("depth-hover");

    if (finePointer.matches) {
      element.addEventListener("pointerenter", (event) => {
        element.classList.add("is-depth-hovered");
        setDepthVars(element, pointMetrics(element, event), 0.65);
      });
      element.addEventListener("pointermove", (event) => {
        element.classList.add("is-depth-hovered");
        setDepthVars(element, pointMetrics(element, event), 1);
      });
      element.addEventListener("pointerleave", () => resetDepth(element));
      element.addEventListener("blur", () => resetDepth(element));
    }

    element.addEventListener("pointerdown", (event) => {
      if (event.pointerType === "mouse" && finePointer.matches) return;
      setPressVars(element, pointMetrics(element, event));
    });
    element.addEventListener("pointerup", () => setTimeout(() => resetPress(element), 130));
    element.addEventListener("pointercancel", () => resetPress(element));
    element.addEventListener("pointerleave", (event) => {
      if (event.pointerType !== "mouse" || !finePointer.matches) resetPress(element);
    });
  }

  function attachAll(root = document) {
    root.querySelectorAll(selectors).forEach(attach);
  }

  document.addEventListener("DOMContentLoaded", () => {
    attachAll();
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        mutation.addedNodes.forEach((node) => {
          if (!(node instanceof Element)) return;
          if (node.matches(selectors)) attach(node);
          attachAll(node);
        });
      });
    });
    observer.observe(document.body, { childList: true, subtree: true });
  });
})();
