(function () {
  "use strict";

  const layers = [
    {
      number: "Layer 07",
      short: "Outcomes",
      title: "Receipts, outcomes, and maintained knowledge",
      pain: "A successful command is not a verified result or reusable company knowledge.",
      outcome:
        "Record exact readback, employee outcomes, promotion decisions, lineage, supersession, and freshness.",
      methods: ["Readback", "WikiLLM", "Promotion"]
    },
    {
      number: "Layer 06",
      short: "Control",
      title: "Graph control, validation, and review",
      pain: "Work cannot advance safely when state, requirements, verification, and approval are implicit.",
      outcome:
        "LangGraph controls typed transitions, reducers, interrupts, repair bounds, checks, independent review, and terminal receipts.",
      methods: ["LangGraph", "Validation", "Review"]
    },
    {
      number: "Layer 05",
      short: "Delivery",
      title: "Specialist research and delivery",
      pain: "Generic agents lose the methods and quality bar of the work being performed.",
      outcome:
        "Role-owned research, outreach, copy, design, implementation, reporting, and onboarding produce bounded reviewable candidates.",
      methods: ["Research", "Design", "Delivery"]
    },
    {
      number: "Layer 04",
      short: "Crew",
      title: "Adaptive role crew",
      pain: "Responsibility disappears when role ownership, prohibitions, reviewers, and handoffs are vague.",
      outcome:
        "Select the smallest responsible crew with explicit tasks, tools, skills, forbidden actions, reviewer routes, and communication contracts.",
      methods: ["CrewAI", "Role packs", "Handoffs"]
    },
    {
      number: "Layer 03",
      short: "Perception",
      title: "Bounded context perception",
      pain: "Loading everything loses authority, freshness, provenance, and the current requirement.",
      outcome:
        "Combine stable CAG, bounded LlamaIndex retrieval, optional TurboVec candidates, structural pointers, exact reads, and role memory.",
      methods: ["LlamaIndex", "TurboVec", "Exact reads"]
    },
    {
      number: "Layer 02",
      short: "Knowledge",
      title: "Reviewed knowledge and source spine",
      pain: "Sources cannot guide work when authority, ownership, freshness, and supersession are unknown.",
      outcome:
        "Maintain public WikiLLM and optional private Obsidian knowledge with allowlists, lineage, currentness, exclusions, and structural maps.",
      methods: ["WikiLLM", "Obsidian", "Orbit", "Graphify"]
    },
    {
      number: "Layer 01",
      short: "Authority",
      title: "Case authority and employee scope",
      pain: "No reliable work begins without a bounded outcome, role, permission, reviewer, and stop rule.",
      outcome:
        "Bind the employee goal, data class, allowed sources, exact authority, risk, done conditions, reviewer, and stop conditions.",
      methods: ["Goal", "Authority", "Risk", "Stop rules"]
    }
  ];

  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);
  const captureMode = new URLSearchParams(window.location.search).has("figma");
  const roiPreviewMode = new URLSearchParams(window.location.search).has("roi-preview");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  if (captureMode) document.documentElement.dataset.capture = "true";
  if (roiPreviewMode) document.documentElement.dataset.roiPreview = "true";

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

  const roiForm = document.querySelector("[data-roi-form]");
  if (!roiForm) return;

  const currency = new Intl.NumberFormat("en-IE", {
    style: "currency",
    currency: "EUR",
    maximumFractionDigits: 0
  });
  const decimal = new Intl.NumberFormat("en", { maximumFractionDigits: 1 });

  function fieldValue(name, fallback) {
    const field = roiForm.elements.namedItem(name);
    const value = Number(field?.value);
    return Number.isFinite(value) ? value : fallback;
  }

  function setResult(name, value) {
    const node = roiForm.querySelector(`[data-roi="${name}"]`);
    if (node) node.textContent = value;
  }

  function setControlOutput(name, value) {
    const node = roiForm.querySelector(`[data-output="${name}"]`);
    if (node) node.textContent = value;
  }

  function syncRangeTrack(field) {
    const min = Number(field.min);
    const max = Number(field.max);
    const value = Number(field.value);
    if (!Number.isFinite(min) || !Number.isFinite(max) || max <= min || !Number.isFinite(value)) return;
    const progress = ((value - min) / (max - min)) * 100;
    field.style.setProperty("--range-progress", `${progress}%`);
  }

  function updateRoi() {
    const people = clamp(fieldValue("people", 1), 1, 250);
    const weeklyHours = clamp(fieldValue("hours", 0), 0, 20);
    const rate = clamp(fieldValue("rate", 0), 0, 350);
    const tools = clamp(fieldValue("tools", 1), 1, 30);
    const centralization = clamp(fieldValue("centralization", 1), 1, 10);
    const governance = clamp(fieldValue("governance", 1), 1, 10);
    const recovery = clamp(fieldValue("recovery", 0), 0, 100);
    const investment = clamp(fieldValue("investment", 0), 0, 150000);

    const monthlyContextHours = people * weeklyHours * 4.33;
    const recoveredHours = monthlyContextHours * (recovery / 100);
    const monthlyValue = recoveredHours * rate;
    const yearlyValue = monthlyValue * 12;
    const toolScore = clamp(10 - Math.max(0, tools - 3) * 0.55, 1, 10);
    const score = Math.round((centralization * 0.4 + governance * 0.4 + toolScore * 0.2) * 10);
    const payback = monthlyValue > 0 ? investment / monthlyValue : Infinity;

    setControlOutput("people", `${people} ${people === 1 ? "person" : "people"}`);
    setControlOutput("hours", `${decimal.format(weeklyHours)} h`);
    setControlOutput("rate", currency.format(rate));
    setControlOutput("tools", `${tools} ${tools === 1 ? "surface" : "surfaces"}`);
    setControlOutput("centralization", `${centralization} / 10`);
    setControlOutput("governance", `${governance} / 10`);
    setControlOutput("recovery", `${recovery}%`);
    setControlOutput("investment", currency.format(investment));

    roiForm.querySelectorAll('input[type="range"]').forEach(syncRangeTrack);

    const modeledQuality = clamp(Math.round(score * 0.35 + recovery * 0.65), 0, 100);
    roiForm.style.setProperty("--readiness-hue", `${8 + score * 1.16}`);
    roiForm.style.setProperty("--readiness-lightness", `${69 + score * 0.08}%`);
    roiForm.style.setProperty("--outcome-lightness", `${88 + modeledQuality * 0.1}%`);
    roiForm.style.setProperty("--outcome-saturation", `${24 + modeledQuality * 0.12}%`);

    setResult("score", String(score));
    setResult("hours", `${decimal.format(recoveredHours)} h`);
    setResult("monthly", currency.format(monthlyValue));
    setResult("yearly", currency.format(yearlyValue));
    setResult(
      "payback",
      !Number.isFinite(payback) ? "Set recovery" : payback < 0.5 ? "< 0.5 months" : payback > 36 ? "> 36 months" : `${decimal.format(payback)} months`
    );

    const scoreBar = roiForm.querySelector("[data-score-bar]");
    if (scoreBar) scoreBar.style.width = `${score}%`;

    const dimensions = [
      { value: centralization, text: "Source fragmentation is the strongest modeled drag. Start with a source map, owner map, and decision-memory spine." },
      { value: governance, text: "Review maturity is the strongest modeled drag. Start with done conditions, provenance, approval, and promotion gates." },
      { value: toolScore, text: "Tool-surface pressure is the strongest modeled drag. Start with routing, shared identifiers, and one retrieval contract." }
    ].sort((a, b) => a.value - b.value);

    setResult("diagnosis", `${dimensions[0].text} Validate this scenario against observed work before treating it as recovered value.`);
  }

  roiForm.addEventListener("input", updateRoi);
  roiForm.addEventListener("change", updateRoi);
  updateRoi();

  if (window.location.hash === "#roi") {
    const roiSection = document.querySelector("#roi");
    const jumpToRoi = () => {
      if (!roiSection) return;
      document.documentElement.style.scrollBehavior = "auto";
      window.scrollTo(0, roiSection.getBoundingClientRect().top + window.scrollY);
    };
    window.setTimeout(jumpToRoi, 60);
    window.setTimeout(jumpToRoi, 360);
  }
})();
