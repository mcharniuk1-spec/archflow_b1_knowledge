(function () {
  "use strict";

  const layers = [
    {
      number: "Layer 07",
      short: "Outcomes",
      title: "Receipts, outcomes, and maintained knowledge",
      pain: "A successful command is not a verified result or reusable shared knowledge.",
      outcome:
        "Record exact readback, reviewed outcomes, promotion decisions, lineage, supersession, and freshness.",
      methods: ["Readback", "Review", "Promotion"]
    },
    {
      number: "Layer 06",
      short: "Control",
      title: "State control, validation, and review",
      pain: "Work cannot advance safely when state, requirements, verification, and approval are implicit.",
      outcome:
        "A typed controller governs transitions, interrupts, repair bounds, checks, independent review, and terminal receipts.",
      methods: ["Typed state", "Validation", "Review"]
    },
    {
      number: "Layer 05",
      short: "Delivery",
      title: "Specialist research and delivery",
      pain: "Generic agents lose the methods and quality bar of the work being performed.",
      outcome:
        "Role-owned research, definition, design, implementation, reporting, and onboarding produce bounded reviewable candidates.",
      methods: ["Research", "Design", "Delivery"]
    },
    {
      number: "Layer 04",
      short: "Crew",
      title: "Adaptive role crew",
      pain: "Responsibility disappears when role ownership, prohibitions, reviewers, and handoffs are vague.",
      outcome:
        "Select the smallest responsible crew with explicit tasks, tools, skills, forbidden actions, reviewer routes, and communication contracts.",
      methods: ["Role contracts", "Role packs", "Handoffs"]
    },
    {
      number: "Layer 03",
      short: "Perception",
      title: "Bounded context perception",
      pain: "Loading everything loses authority, freshness, provenance, and the current requirement.",
      outcome:
        "Combine stable rules, bounded allowlisted retrieval, structural pointers, exact reads, gaps, and role-safe context.",
      methods: ["Exact manifest", "Lexical retrieval", "Exact reads"]
    },
    {
      number: "Layer 02",
      short: "Knowledge",
      title: "Reviewed knowledge and source spine",
      pain: "Sources cannot guide work when authority, ownership, freshness, and supersession are unknown.",
      outcome:
        "Maintain reviewed solution and action memory with allowlists, lineage, currentness, exclusions, and supersession.",
      methods: ["Memory schemas", "Source maps", "Lineage"]
    },
    {
      number: "Layer 01",
      short: "Authority",
      title: "Case authority and responsibility scope",
      pain: "No reliable work begins without a bounded outcome, role, permission, reviewer, and stop rule.",
      outcome:
        "Bind the case objective, data class, allowed sources, exact authority, risk, done conditions, reviewer, and stop conditions.",
      methods: ["Goal", "Authority", "Risk", "Stop rules"]
    }
  ];

  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);
  const captureMode = new URLSearchParams(window.location.search).has("figma");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  if (captureMode) document.documentElement.dataset.capture = "true";

  const header = document.querySelector("[data-site-header]");
  const updateHeader = () => header?.classList.toggle("is-scrolled", window.scrollY > 20);
  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });

  const story = document.querySelector("[data-tower-story]");
  const towerElements = Array.from(document.querySelectorAll("[data-tower-layer]"));
  const towerStack = document.querySelector("[data-tower-stack]");
  const stepButtons = Array.from(document.querySelectorAll("[data-tower-step]"));
  const layerCard = document.querySelector(".layer-card");
  const layerNumber = document.querySelector("[data-layer-number]");
  const layerProgress = document.querySelector("[data-layer-progress]");
  const layerTitle = document.querySelector("[data-layer-title]");
  const layerPain = document.querySelector("[data-layer-pain]");
  const layerOutcome = document.querySelector("[data-layer-outcome]");
  const layerMethods = document.querySelector("[data-layer-methods]");
  const towerStatus = document.querySelector("[data-tower-status]");
  let activeLayer = -1;
  let towerFrame = null;

  function setLayerCopy(index, animate = true) {
    const layer = layers[index];
    if (!layer || index === activeLayer) return;
    activeLayer = index;

    if (animate && layerCard && !reducedMotion.matches) {
      layerCard.classList.remove("is-changing");
      void layerCard.offsetWidth;
      layerCard.classList.add("is-changing");
    }

    if (layerNumber) layerNumber.textContent = layer.number;
    if (layerProgress) layerProgress.textContent = `${index + 1} / ${layers.length}`;
    if (layerTitle) layerTitle.textContent = layer.title;
    if (layerPain) layerPain.textContent = layer.pain;
    if (layerOutcome) layerOutcome.textContent = layer.outcome;
    if (towerStatus) towerStatus.textContent = `${layer.number} in focus`;
    if (story) story.dataset.currentLayer = layer.number.replace("Layer ", "");
    if (towerStack) towerStack.dataset.activeLayer = layer.number.replace("Layer ", "");

    if (layerMethods) {
      layerMethods.replaceChildren(
        ...layer.methods.map((method) => {
          const chip = document.createElement("span");
          chip.textContent = method;
          return chip;
        })
      );
    }

    stepButtons.forEach((button, buttonIndex) => {
      if (buttonIndex === index) button.setAttribute("aria-current", "step");
      else button.removeAttribute("aria-current");
    });
  }

  function towerProgress() {
    if (!story) return 0;
    const rect = story.getBoundingClientRect();
    const travel = Math.max(story.offsetHeight - window.innerHeight, 1);
    return clamp(-rect.top / travel, 0, 1);
  }

  function renderTower() {
    towerFrame = null;
    if (!story || !towerElements.length) return;

    if (captureMode || reducedMotion.matches) {
      towerElements.forEach((element) => {
        element.style.transform = "translate3d(0, 0, 0)";
        element.style.opacity = "1";
        element.style.filter = "none";
      });
      if (captureMode || activeLayer < 0) setLayerCopy(0, false);
      return;
    }

    const progress = towerProgress();
    const stage = progress * layers.length;
    const index = Math.min(Math.floor(stage), layers.length - 1);
    setLayerCopy(index);

    towerElements.forEach((element, elementIndex) => {
      const local = clamp(stage - elementIndex, 0, 1);
      const fade = 1 - clamp((local - 0.58) / 0.42, 0, 1);
      const direction = elementIndex % 2 === 0 ? 1 : -1;
      const lift = local * (window.innerHeight * 0.68 + elementIndex * 12);
      const drift = direction * local * 20;
      const scale = 1 + local * 0.025;
      const rotation = direction * local * 1.6;
      const isFocus = elementIndex === index && local < 0.66;

      element.style.transform = `translate3d(${drift}px, ${-lift}px, ${local * 24}px) rotateZ(${rotation}deg) scale(${scale})`;
      element.style.opacity = String(fade);
      element.style.filter = isFocus
        ? "brightness(1.22) saturate(1.08) drop-shadow(0 0 18px rgba(239, 200, 140, 0.28))"
        : "brightness(0.94)";
    });
  }

  function requestTowerFrame() {
    if (towerFrame !== null) return;
    towerFrame = window.requestAnimationFrame(renderTower);
  }

  stepButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
      if (!story) return;
      if (reducedMotion.matches) {
        setLayerCopy(index, false);
        return;
      }
      const travel = Math.max(story.offsetHeight - window.innerHeight, 1);
      const target = story.offsetTop + (index / layers.length) * travel + 2;
      window.scrollTo({ top: target, behavior: reducedMotion.matches ? "auto" : "smooth" });
    });
  });

  window.addEventListener("scroll", requestTowerFrame, { passive: true });
  window.addEventListener("resize", requestTowerFrame, { passive: true });
  reducedMotion.addEventListener?.("change", requestTowerFrame);
  requestTowerFrame();

})();
