const header = document.querySelector("[data-elevates]");
const navToggle = document.querySelector(".nav-toggle");
const mobileNav = document.querySelector("#mobileNav");
const heroImage = document.querySelector(".hero-image");
const miniCalc = document.querySelector("#miniCalc");
const calcOutput = document.querySelector("#calcOutput");

const packages = [
  "Recommended first package: PRD rescue and evidence map.",
  "Recommended first package: ICP evidence review and positioning brief.",
  "Recommended first package: knowledgebase readiness and task matrix.",
  "Recommended first package: governed agent-orchestra setup plan."
];

function updateHeader() {
  if (!header) return;
  header.classList.toggle("is-elevated", window.scrollY > 16);
}

function toggleNav() {
  if (!navToggle || !mobileNav) return;
  const open = navToggle.getAttribute("aria-expanded") === "true";
  navToggle.setAttribute("aria-expanded", String(!open));
  mobileNav.classList.toggle("is-open", !open);
}

function updateHeroMotion(event) {
  if (!heroImage || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const rect = heroImage.getBoundingClientRect();
  const x = (event.clientX - rect.left) / Math.max(rect.width, 1) - 0.5;
  const y = (event.clientY - rect.top) / Math.max(rect.height, 1) - 0.5;
  heroImage.style.setProperty("--mx", `${x * 14}px`);
  heroImage.style.setProperty("--my", `${y * 10}px`);
}

function updateCalc() {
  if (!miniCalc || !calcOutput) return;
  const form = new FormData(miniCalc);
  const sources = Number(form.get("sources") || 3);
  const decisions = Number(form.get("decisions") || 2);
  const pressure = Number(form.get("pressure") || 4);
  const knowledgeGap = 6 - Math.round((sources + decisions) / 2);
  const index = Math.max(0, Math.min(packages.length - 1, Math.round((knowledgeGap + pressure - 2) / 2)));
  calcOutput.value = packages[index];
}

window.addEventListener("scroll", updateHeader, { passive: true });
window.addEventListener("pointermove", updateHeroMotion, { passive: true });
navToggle?.addEventListener("click", toggleNav);
miniCalc?.addEventListener("input", updateCalc);

document.querySelectorAll(".mobile-nav a").forEach((link) => {
  link.addEventListener("click", () => {
    navToggle?.setAttribute("aria-expanded", "false");
    mobileNav?.classList.remove("is-open");
  });
});

updateHeader();
updateCalc();
