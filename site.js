(function () {
  "use strict";

  const layers = [
    {
      number: "Layer 07",
      short: "Measure",
      title: "Measure & evolve",
      pain: "You cannot improve what you cannot baseline.",
      outcome:
        "We pair baseline and candidate traces across quality, retrieval, cost, safety, recovery, and human effort before a change is promoted.",
      methods: ["Benchmark", "Trace ledger", "Promotion gate"]
    },
    {
      number: "Layer 06",
      short: "Remember",
      title: "Remember & act safely",
      pain: "Decisions disappear when nobody owns the memory after delivery.",
      outcome:
        "We promote reviewed deltas into durable memory, refresh navigation, and gate every external action with approval, rollback, and readback.",
      methods: ["WikiLLM", "Obsidian", "Graphify", "Readback"]
    },
    {
      number: "Layer 05",
      short: "Verify",
      title: "Verify & protect",
      pain: "Enterprise answers cannot rest on unchecked agent confidence.",
      outcome:
        "We run deterministic checks, independent review, provenance, and safety gates before a claim, memory update, or client handoff.",
      methods: ["Source proof", "Maker-checker", "Safety gate"]
    },
    {
      number: "Layer 04",
      short: "Execute",
      title: "Execute & repair",
      pain: "Agents drift when roles, skills, and limits are vague.",
      outcome:
        "We give each role the right skills and bounded repair loops with attempt, token, time, cost, and stop limits.",
      methods: ["Role packs", "Skills", "Repair caps"]
    },
    {
      number: "Layer 03",
      short: "Orchestrate",
      title: "Orchestrate & approve",
      pain: "Parallel work breaks when state, dependencies, and approval have no owner.",
      outcome:
        "LangGraph owns transitions and checkpoints; role teams execute inside the graph; humans approve irreversible edges.",
      methods: ["LangGraph", "Checkpoints", "Human gates"]
    },
    {
      number: "Layer 02",
      short: "Connect",
      title: "Connect the company brain",
      pain: "Truth scattered across tools and people cannot be reliably retrieved.",
      outcome:
        "We assemble stable context first, retrieve only from approved sources, and keep each answer linked to source IDs and freshness.",
      methods: ["CAG", "Bounded RAG", "Source IDs", "Freshness"]
    },
    {
      number: "Layer 01",
      short: "Govern",
      title: "Govern goals & sources",
      pain: "No safe automation starts without authority and a shared definition of done.",
      outcome:
        "We define allowed sources, permissions, one observable goal, budgets, stop conditions, and the verifier before an agent acts.",
      methods: ["Goal contract", "Permissions", "Budgets", "Stop rules"]
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
