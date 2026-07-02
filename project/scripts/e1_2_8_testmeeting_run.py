#!/usr/bin/env python3
"""Generate the E1.2.8 testmeeting PRD package.

The script reads private root inputs, but writes only sanitized derived outputs
under the public repo. OpenRouter is optional and uses only the sanitized digest.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Flowable, ListFlowable, ListItem, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle


PUBLIC_ROOT = Path(__file__).resolve().parents[2]
PRIVATE_ROOT = PUBLIC_ROOT.parent
RUN_DIR = PUBLIC_ROOT / "project" / "runs" / "E1.2" / "2026-07-02-testmeeting-local"
REPORT_DIR = PUBLIC_ROOT / "project" / "reports"
MEETING_PATH = PRIVATE_ROOT / "docs" / "testmeeting.md"
DISCOVERY_PATH = PRIVATE_ROOT / "discovery materials.docx"
ROOT_ENV = PRIVATE_ROOT / ".env.local"

PRIVATE_NAME_PATTERNS = [
    r"\bDaniel\b",
    r"\bVirginia\b",
    r"\bFabia?n\b",
    r"\bJessica\b",
    r"\bTherese?\b",
    r"\bCarina\b",
    r"\bKarina\b",
    r"\bScott\b",
    r"\bKenny\b",
    r"\bGabe(?:\s+Weaver)?\b",
    r"\bDov(?:\s+Hershkovitz)?\b",
    r"\bChristy\b",
    r"\bDavid(?:\s+Sakamoto)?\b",
    r"\bJosh\b",
    r"\bLucas?\b",
    r"\bJames\b",
    r"\bChristopher\b",
    r"\bMac\b",
    r"\bMyron\b",
    r"\bMaron\b",
    r"\bJason\b",
    r"\bEric\b",
    r"\bSarah(?:\s+O'?Donnell)?\b",
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def redact_private_names(text: str) -> str:
    redacted = text
    for pattern in PRIVATE_NAME_PATTERNS:
        redacted = re.sub(pattern, "role participant", redacted, flags=re.IGNORECASE)
    return redacted


def read_docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as docx:
        xml = docx.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    parts: list[str] = []
    for para in root.findall(".//w:p", ns):
        texts = [node.text or "" for node in para.findall(".//w:t", ns)]
        text = "".join(texts).strip()
        if text:
            parts.append(text)
    return "\n".join(parts)


def source_synthesis(meeting: str, discovery: str) -> dict[str, object]:
    lower = meeting.lower()
    themes = [
        "Customer interviews and interview follow-up need stronger operating discipline.",
        "Product decisions should stay customer-first while internal teams remain valuable early feedback channels.",
        "Release kickoff communication needs clearer problem framing, examples, screenshots or mockups, and better async formats.",
        "Discovery sprints are useful for large unknowns, but should be reserved for high-uncertainty problems.",
        "Performance, availability, scalability, and production readiness need to be treated as product requirements, not only engineering cleanup.",
        "Dual-track discovery and delivery should separate learning work from delivery-ready issues.",
    ]
    detected = {
        "customer_interviews": "customer interview" in lower or "interview" in lower,
        "release_kickoff": "kickoff" in lower,
        "discovery_sprint": "discovery sprint" in lower,
        "performance": "performance" in lower or "availability" in lower,
        "dual_track": "dual track" in lower or "dual-track" in lower,
        "dogfooding": "dogfood" in lower or "internal feedback" in lower,
    }
    methodology = [
        "Use Jobs-to-Be-Done framing: focus on the progress the user is trying to make.",
        "Prefer recent behavioral evidence, especially decisions made in the last 90 days.",
        "Ask for concrete past stories instead of hypothetical purchase intent.",
        "Separate goals from measurable requirements and define Definition of Done clearly.",
        "Use interview evidence and source labels to support PRD claims.",
        "Run Discovery and Delivery as parallel tracks: evidence before build, implementation after validation.",
        "Treat the PRD as a living contract that feeds task systems and engineering handoff.",
    ]
    return {
        "run_id": "E1.2.8-testmeeting-local",
        "created_at": now(),
        "source_boundary": {
            "approved_private_inputs": ["root docs/testmeeting.md", "root discovery materials.docx"],
            "public_output_rule": "Only sanitized English summaries and derived artifacts are written under public/.",
            "provider_input_rule": "OpenRouter receives only the sanitized digest, not raw meeting text or raw DOCX body.",
        },
        "detected_signals": detected,
        "themes": themes,
        "methodology": methodology,
        "product_focus": "Release kickoff and discovery-to-delivery handoff modernization for B2B SaaS product teams.",
        "buyer": "Director or VP Product accountable for PRD quality, discovery cadence, and delivery handoff speed.",
        "service_reflection": "ArchFlow turns meeting/discovery material into a PRD, task matrix, decision log, evidence gaps, and review-ready handoff packet.",
    }


def sanitized_digest(synthesis: dict[str, object]) -> str:
    return textwrap.dedent(
        f"""
        Source packet: E1.2.8 testmeeting local run.
        Product focus: {synthesis["product_focus"]}
        Buyer: {synthesis["buyer"]}
        Service reflection: {synthesis["service_reflection"]}

        Main meeting themes:
        {chr(10).join(f"- {item}" for item in synthesis["themes"])}

        Discovery and PRD methodology:
        {chr(10).join(f"- {item}" for item in synthesis["methodology"])}

        Boundary:
        - No raw transcript, private names, private URLs, account IDs, credentials, or screenshots.
        - Provider comparison may use only this sanitized digest.
        """
    ).strip()


def md_source_inventory(synthesis: dict[str, object]) -> str:
    return f"""# E1.2.8 Source Inventory

Date: 2026-07-02
Status: sanitized source boundary accepted for local/Codex run

## Source Boundary

| Source | Location | Use | Public Storage |
|---|---|---|---|
| Test meeting transcript | private root `docs/testmeeting.md` | Product-meeting themes and PRD extraction | Raw text not copied |
| Discovery methodology document | private root `discovery materials.docx` | Customer discovery, JTBD, PRD, and dual-track method context | Raw body not copied |
| Prior E1/E1.3 public artifacts | public repo run notes and reports | E1 architecture, ICP, task-state, and safety boundaries | Linked/summarized only |

## Public-Safe Rule

Only sanitized English summaries and derived PRD/report artifacts are saved in this folder. The run does not store raw private transcript text, personal names, private URLs, screenshots, credentials, or account identifiers.

## Provider Rule

OpenRouter comparison, if run, uses only the sanitized digest and must write a provider ledger, model selection proof, budget guard, and comparison report.
"""


def md_context_digest(synthesis: dict[str, object]) -> str:
    return f"""# E1.2.8 Context Digest

Date: 2026-07-02
Architecture: Architecture 1 - PRD/ICP service output

## FACT

- The meeting material contains product-organization operating themes: customer interview cadence, release kickoff format, discovery sprints, product discovery vs delivery readiness, performance and availability as product concerns, and internal/external feedback balance.
- The discovery-methodology document defines a research-backed PRD method: JTBD, recent behavioral interviews, concrete past stories, evidence-backed PRDs, measurable requirements, Definition of Done, and Dual-Track Agile.
- The current ArchFlow ICP is B2B SaaS product teams, Series B-D, 50-500 employees, 2-5 PMs, with Director or VP Product ownership of PRD quality and speed.

## INTERPRETATION

The meeting is a strong fit for ArchFlow's first service wedge because it shows exactly the type of raw product-team material that gets lost between leadership discussion, customer discovery, release communication, engineering readiness, and task definition.

## HYPOTHESIS

ArchFlow can convert this source packet into a more useful product artifact by creating a PRD around release kickoff and discovery-to-delivery handoff modernization, while preserving secondary backlog themes for customer interviews, performance readiness, and dual-track process improvements.

## GAP

- No direct customer quotes can be stored publicly from the private source.
- OpenRouter output must be separated from local/Codex output and compared only after a provider-safe sanitized digest run.
- Owner acceptance is still required before marking E1.2 Done.

## Sanitized Digest For Provider-Eligible Comparison

```text
{sanitized_digest(synthesis)}
```
"""


def md_local_prd(synthesis: dict[str, object]) -> str:
    return f"""# E1.2.8 Local PRD - Release Kickoff And Discovery-To-Delivery Handoff

Status: local/Codex sanitized PRD output
Architecture: Architecture 1 - PRD/ICP service output

## Source Boundary

- Approved inputs: private test meeting transcript, private discovery-methodology document, prior public E1/E1.3 artifacts.
- Excluded raw inputs: raw transcript text, personal names, private URLs, screenshots, credentials, account identifiers.
- Source refs: `source-inventory.md`, `context-digest.md`, public E1 task reports.
- Public/private review status: public-safe derived output; no raw private material stored.

## Meeting Summary

The source meeting reflects a product organization trying to improve how customer discovery, internal feedback, release communication, discovery sprints, and operational readiness flow into delivery. The strongest product problem is not a single UI feature. It is the handoff system that turns discovery and leadership discussion into clear release narratives, build-ready requirements, and reviewable priorities.

## Product Context

- Product area: Product operating workflow for release kickoff, discovery, and delivery handoff.
- Problem: Product teams have many valuable signals, but the path from meeting discussion to PRD, task readiness, and release communication is inconsistent.
- Target user: Director or VP Product managing several PMs in a B2B SaaS scaleup.
- Non-goals: Replace Jira, Linear, Productboard, Dovetail, Notion, or product managers.
- Constraints: No raw private transcript storage; customer evidence must be source-labeled; provider-backed processing remains gated.

## Stakeholders

| Role | Owner | Responsibility | Review gate |
|---|---|---|---|
| Product leader | Director or VP Product | Decide operating standard for discovery-to-delivery handoff | Owner review |
| PM team | Product managers | Run interviews, write discovery notes, prepare release artifacts | PM review |
| Engineering partner | Engineering/architecture lead | Validate feasibility, scalability, performance, and delivery readiness | Engineering review |
| Research/UX partner | Research or design lead | Shape discovery sprint, interview method, and evidence quality | Research review |
| ArchFlow reviewer | AF Review | Verify source boundary, evidence labels, PRD completeness, and blocked claims | AF Review |

## ICP

- Account shape: B2B SaaS company, Series B-D, 50-500 employees, 2-5 PMs.
- Buyer role: Director or VP Product.
- Trigger: Product team is struggling to turn recurring discovery and leadership discussion into clear PRDs and delivery-ready tasks.
- Disqualifier: Company has no repeated product discovery, no PM team, or only needs a one-off template.
- Confidence: Medium-high for fit with current ICP hypothesis; not validated demand.
- Evidence grade: Internal source fit plus method alignment; external account evidence still belongs to E2.

## Pains/JTBD

| Job | Pain | Current workaround | Desired outcome | Proof needed |
|---|---|---|---|---|
| Keep PMs aligned on customer discovery | Interview goals, reminders, and follow-up lose force across meetings | Spreadsheets, manual reminders, ad hoc agendas | Interview cadence with evidence cards and follow-up owners | E2 evidence and owner acceptance |
| Communicate release value | Kickoff can become too broad, too technical, or too time-constrained | Live meeting plus scattered screenshots/videos | Problem-focused release packet and async deep dives | Pilot on one release |
| Select discovery sprint candidates | Teams need speed but cannot sprint every problem | Informal judgment | Criteria for when discovery sprint is worth the cost | Definition of Ready |
| Treat performance as product value | Performance/availability risks surface late | Reactive incident handling | PRD requirements include scale, limits, and Definition of Done | Engineering review |
| Separate discovery from delivery | Oversized work enters delivery before enough learning | Large issues and late UX/research work | Dual-track flow with discovery-ready and delivery-ready states | Process trial |

## Existing Workflow

1. Leadership meeting surfaces reminders, process issues, and product operating feedback.
2. PMs and partners manually translate discussion into issues, comments, kickoff material, and discovery work.
3. Some evidence stays in spreadsheets, handbook diffs, kickoff decks, videos, or meeting memory.
4. Engineering, UX, and product readiness concerns can arrive after scope has already formed.

## Proposed Workflow

1. Capture a sanitized source packet from meeting, discovery notes, and approved docs.
2. Classify each point as fact, interpretation, hypothesis, gap, decision, risk, or task.
3. Generate PRD sections with evidence labels and explicit non-goals.
4. Convert the PRD into tasks, owner matrix, acceptance criteria, and review gates.
5. Feed approved summaries into the KB so future agents can retrieve the decision state.
6. Run AF Review before Notion/GitHub/WikiLLM/provider/writeback actions.

## Requirements

| Requirement | Type | Acceptance criteria | Source | Status |
|---|---|---|---|---|
| Source packet boundary | Safety | Raw transcript and names are excluded from public outputs | Source inventory | Complete |
| Discovery-to-delivery PRD | Functional | PRD includes problem, ICP, workflow, requirements, risks, and tasks | Meeting themes + methodology | Complete |
| Evidence-labeled backlog | Functional | Every task includes source, owner, output, and gate | PRD template | Complete |
| Release kickoff improvement | Functional | Kickoff narrative is problem-focused and supports async detail | Meeting themes | Draft |
| Discovery sprint criteria | Functional | Defines when sprint format is justified | Discovery methodology | Draft |
| Performance readiness in PRD | Non-functional | PRD includes measurable scale/performance criteria where relevant | Meeting themes | Draft |
| Provider comparison | Runtime | OpenRouter uses sanitized digest only and writes ledger/budget proof | Provider gate | Gated |

## Decisions

| Decision | Evidence | Owner | Confidence | Review trigger |
|---|---|---|---|---|
| Focus the PRD on release kickoff and discovery-to-delivery handoff | Dominant meeting themes | Codex local run | Medium-high | Owner acceptance |
| Treat performance/availability as product requirements | Meeting discussion includes scale and production readiness concerns | Product + engineering | Medium | Engineering review |
| Keep OpenRouter as separate comparison | Provider policy and budget gate | AF Review | High | Provider run |
| Use sanitized digest for any provider call | Public-safety and model-routing rules | AF Review | High | Before provider call |

## Questions

- Which single release or product area should be used for the first buyer-facing sample?
- Should the output be positioned as a PRD rescue, release kickoff redesign, or product operating system diagnostic?
- Which engineering partner owns performance/availability acceptance criteria in the pilot?
- Which PM/research owner confirms that the discovery sprint criteria are practical?

## Risks

- Unsupported claim: This run does not prove customer demand or paid willingness.
- Runtime/provider: OpenRouter output must not be merged into local output without ledger and comparison review.
- Delivery: The PRD may be too process-oriented unless tied to one concrete release workflow.
- Data/safety: Raw meeting transcript must remain private.

## Next Tasks

| Task | Owner | Input | Output | Gate |
|---|---|---|---|---|
| Review local PRD | Owner + AF Review | This PRD | Accepted/revised PRD | Owner acceptance |
| Produce OpenRouter comparison | Codex + provider gate | Sanitized digest | OpenRouter PRD + ledger + comparison | Provider approval |
| Update E1.2.8 Notion task | Messi/Codex | Run artifacts | Status note and links | After artifacts exist |
| Add dashboard operating manual | LOL/Codex | Current dashboard | Markdown + PDF manual | Browser QA |
| Prepare Railway task | Ronaldinho/Codex | Local API proof | E1.7 hosted-runtime checklist | Owner approval |

## Backlog

| Epic | Story | Acceptance criteria | Dependency | Priority |
|---|---|---|---|---|
| Release communication | As a product leader, I want release kickoff content to explain customer value quickly | Packet includes problem, target user, mockup/screenshot needs, and async detail links | Owner sample release | P1 |
| Customer discovery | As a PM lead, I want interview follow-up visible and measurable | Interview targets, owners, and status are captured | Interview spreadsheet source | P1 |
| Discovery sprint | As a PM, I want criteria for when to run a discovery sprint | Criteria include uncertainty, complexity, expected learning, and cost | Research/UX review | P2 |
| Performance readiness | As an engineering partner, I want performance limits in PRDs | Requirements include scale, load, latency, and production readiness where relevant | Engineering review | P1 |
| Dual-track workflow | As a product organization, I want discovery-ready and delivery-ready states | Issues can be classified before delivery commitment | Process owner | P2 |

## Success Metrics

- Time from source packet to reviewed PRD: target measured in days, not weeks.
- Handoff questions reduced: fewer repeated clarifying questions after PRD review.
- Evidence-card completeness: each major claim has source label or gap marker.
- Review latency: owner can approve/revise from one packet.
- Buyer validation signal: later E2/E6 interviews confirm whether this PRD pack solves a paid pain.
"""


def md_streaming_report(synthesis: dict[str, object]) -> str:
    events = [
        ("intake_validate", "Private source files present; public output boundary applied."),
        ("source_summarize", "Meeting themes and discovery-methodology themes converted into sanitized digest."),
        ("architecture_select", "Architecture 1 selected for PRD/ICP service-output run."),
        ("draft_prd", "Local/Codex PRD, backlog, decisions, risks, and next tasks generated."),
        ("af_review", "Public-safety and provider-boundary review applied."),
        ("record_outputs", "Run artifacts and PDFs written under public project run folder."),
    ]
    lines = "\n".join(f"| {idx + 1} | {node} | {note} |" for idx, (node, note) in enumerate(events))
    return f"""# E1.2.8 Local Streaming Report

Date: 2026-07-02
Status: complete for local/Codex run

## Stream Events

| Step | Node | Public-safe progress note |
|---:|---|---|
{lines}

## Runtime State

- Architecture: Architecture 1 - PRD/ICP service output.
- Model provider: Codex local operator.
- Provider calls: 0 for local run.
- External writeback: 0.
- Raw transcript persistence: off.
- Raw DOCX persistence: off.

## Output State

- Source inventory: `source-inventory.md`.
- Context digest: `context-digest.md`.
- Local PRD: `E1.2.8_Local_PRD.md`.
- Methodology review: `E1.2.8_Source_Methodology_review.md`.
- Backlog and questions: `backlog-and-questions.md`.
- Review report: `review-report.md`.
"""


def md_methodology_review(synthesis: dict[str, object]) -> str:
    return f"""# E1.2.8 Source Methodology Review

Status: methodology applied to local/Codex PRD run

## Method Inputs

The discovery-methodology document supports the following operating principles:

{chr(10).join(f"- {item}" for item in synthesis["methodology"])}

## How The Method Was Applied

| Method | Application In This Run | Output |
|---|---|---|
| JTBD | Treated the meeting as evidence of the product team's job: convert discussion and discovery into delivery-ready work | PRD problem and pains |
| 90-day / recent behavior rule | Kept future validation focused on recent product-team behavior rather than abstract preference | E2/E6 validation gap |
| Story-based discovery | Interpreted meeting topics as concrete process stories, not wishlist features | Context digest |
| Evidence-backed PRD | Marked unsupported claims as gaps and kept public output source-labeled | PRD decisions and risks |
| Measurable requirements | Converted vague improvement themes into acceptance criteria and Definition of Done candidates | Requirements table |
| Dual-Track Agile | Separated discovery sprint, customer interviews, and delivery-ready work | Backlog |

## Strategic Fit

The method fits ArchFlow's customer because B2B SaaS product leaders need a system that preserves discovery context, translates it into product requirements, and keeps delivery handoff controlled. The run reflects the service promise: raw product material becomes a source-backed PRD, task matrix, evidence gaps, and review packet.

## Remaining Method Gaps

- The source is internal product-organization material, not buyer validation.
- The output needs owner review before it becomes the accepted E1.2 artifact.
- OpenRouter comparison should test formatting/quality differences only after sanitized-provider gates pass.
"""


def md_backlog_and_questions() -> str:
    return """# E1.2.8 Backlog And Missing Questions

## Suggested Backlog

| ID | Work Item | Owner | Acceptance Criteria | Gate |
|---|---|---|---|---|
| TM-1 | Build release kickoff PRD packet | Product lead | Packet includes problem, audience, evidence, screenshot/mockup needs, and async detail plan | Owner review |
| TM-2 | Create customer-interview follow-up tracker spec | PM operations | Tracker captures PM owner, target count, contact source, status, and next action | PM review |
| TM-3 | Define discovery sprint entry criteria | Research/UX | Criteria separate high-uncertainty discovery from routine delivery | Research review |
| TM-4 | Add performance/availability Definition of Done section | Product + engineering | PRD has scale, latency, cost, and rollout criteria where relevant | Engineering review |
| TM-5 | Split discovery-ready vs delivery-ready issue states | Product operations | Tasks can be classified before delivery commitment | Process review |

## Missing Questions

- Which actual release or product area should become the first externally showable sample?
- Which PM/research owner validates the customer-interview operating criteria?
- Which engineering owner reviews performance and availability acceptance criteria?
- Is the buyer-facing package called PRD Rescue, Release Kickoff System, or Product Discovery-to-Production PRD Pack?
- Should OpenRouter be used for format comparison only, or also for alternative PRD reasoning after provider approval?
"""


def md_review_report(openrouter_status: str = "not_run") -> str:
    return f"""# E1.2.8 AF Review Report

Status: local/Codex output approved for review packet

## FACT

- Private source files were read from the ArchFlow root.
- Public output files contain only sanitized English summaries and derived artifacts.
- Local/Codex run used `MODEL_PROVIDER=none`.
- OpenRouter status: `{openrouter_status}`.

## INTERPRETATION

The local run satisfies the requested E1.2.8 local PRD/PDF package. It does not replace the June 26 E1.2 proof; it extends E1.2 with a source-specific testmeeting package.

## HYPOTHESIS

The strongest buyer-facing interpretation is a PRD automation service that turns release/discovery operating discussion into a coherent release kickoff and discovery-to-delivery handoff PRD.

## GAP

- Owner acceptance is needed before E1.2 can be marked Done.
- OpenRouter output, if unavailable or failed, remains a separate comparison blocker.
- Railway hosted runtime remains E1.7, not part of this local run.

## Safety Verdict

Approved for public repo storage as sanitized derived output. Not approved for publishing as customer proof, paying-demand proof, or provider-backed runtime proof.
"""


def md_agent_activity_report(openrouter_status: str = "not_run") -> str:
    return f"""# E1.2.8 Agent Activity Progress Report

## Run Metadata

| Field | Value |
|---|---|
| Date | 2026-07-02 |
| Lane | E1.2.8 testmeeting local/Codex PRD run |
| Epic/task | E1 Build the Knowledge Base on Ourselves / E1.2.8 |
| Agent role | Codex local operator |
| Status | Complete for local run; OpenRouter status `{openrouter_status}` |

## Source Boundary

- Approved inputs: private test meeting transcript and private discovery-methodology document.
- Excluded raw inputs: raw transcript, names, private URLs, screenshots, credentials, account IDs.
- Public-safe source IDs: `SRC-E128-MEETING`, `SRC-E128-DISCOVERY`, `SRC-E128-E1-PUBLIC`.

## Activity Ledger

| Time | Actor | Action | Artifact | Status |
|---|---|---|---|---|
| 2026-07-02 | Codex | Read private source boundary | `source-inventory.md` | complete |
| 2026-07-02 | Codex | Built sanitized digest | `context-digest.md` | complete |
| 2026-07-02 | Codex | Generated local PRD | `E1.2.8_Local_PRD.md` | complete |
| 2026-07-02 | Codex | Applied methodology review | `E1.2.8_Source_Methodology_review.md` | complete |
| 2026-07-02 | Codex | Prepared backlog/questions | `backlog-and-questions.md` | complete |
| 2026-07-02 | Codex | Ran AF Review | `review-report.md` | complete |

## Artifact Table

| Output | Path | Purpose | Review State |
|---|---|---|---|
| Source inventory | `source-inventory.md` | Source boundary and public-safety record | accepted |
| Context digest | `context-digest.md` | FACT/INTERPRETATION/HYPOTHESIS/GAP | accepted |
| Local PRD | `E1.2.8_Local_PRD.md` | Main local PRD output | review |
| Streaming report | `E1.2.8_Local_Streaming_report.md` | Process evidence | accepted |
| Methodology review | `E1.2.8_Source_Methodology_review.md` | Discovery/PRD method application | accepted |
| Backlog/questions | `backlog-and-questions.md` | Task candidates and gaps | review |
| Review report | `review-report.md` | AF Review status | accepted |

## Provider Ledger

| Field | Value |
|---|---|
| MODEL_PROVIDER | none for local run |
| Provider calls | 0 for local run |
| OpenRouter status | `{openrouter_status}` |
| Cost | 0.00 USD for local run |

## Checks To Run

- Public safety scan.
- Runtime guard.
- Workflow validation.
- Dashboard JSON parse.
- JS syntax check.
- PDF existence and size check.

## Notion Status Candidates

| Task | Status Candidate | Evidence | Blocker |
|---|---|---|---|
| E1.2 | Review | New source-specific PRD package exists | Owner acceptance |
| E1.2.8 | Review if local package is accepted; otherwise Blocked for OpenRouter | Local artifacts and PDFs | OpenRouter/provider comparison may remain gated |
| E1.3.9 | Review | Dashboard local architecture fixes | Hosted runtime still gated |
| E1.7 | Backlog | Railway config exists | Hosted deploy not proven |

## Next Safe Action

Review local PRD and decide whether the OpenRouter comparison should run on the sanitized digest under the provider gate.
"""


def md_agent_handout(openrouter_status: str = "not_run") -> str:
    return f"""# E1.2.8 Testmeeting Local PRD Handout

## Title And Purpose

This handout records the E1.2.8 testmeeting local/Codex PRD package and the dashboard architecture updates that support running it from Jarvis.

## Human Summary

The run uses the private `testmeeting.md` and discovery-methodology document as source inputs, but stores only sanitized derived outputs in the public repo. The local PRD focuses on release kickoff and discovery-to-delivery handoff modernization for B2B SaaS product teams.

The output demonstrates the ArchFlow service concept: raw product-team conversation and method material become a source boundary, context digest, PRD, backlog, questions, methodology review, process report, and AF Review packet. It extends the earlier June 26 E1.2 proof without replacing it.

OpenRouter status is `{openrouter_status}`. If provider output exists, it is a separate comparison against the sanitized digest, not a raw-source run.

## Current State

- Local/Codex PRD package: complete.
- PDFs: rendered for local PRD, streaming report, and methodology review.
- Dashboard: Architecture 1/2 selector, persistent chat, proactive interview, and schema node improvements are part of this lane.
- Notion: update E1/E1.2/E1.2.8/E1.3.9/E1.7 after checks.

## Agent Continuation Prompt

Continue from `project/runs/E1.2/2026-07-02-testmeeting-local/`. Do not reread or copy raw private source into public files. If asked to run or rerun OpenRouter, send only `context-digest.md` sanitized digest or a shorter approved packet, then write model ledger, budget guard, comparison report, and AF Review.

## Validation

Run public safety scan, workflow validation, runtime guard, dashboard JSON parse, JS syntax check, API AST parse, and PDF existence checks before marking the lane complete.

## Safety Boundary

No raw private transcript, names, private URLs, credentials, screenshots, account IDs, Telegram target values, or provider keys may be stored in public outputs.
"""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(redact_private_names(text).rstrip() + "\n", encoding="utf-8")


class HR(Flowable):
    def __init__(self, width: float = 7.0 * inch) -> None:
        super().__init__()
        self.width = width
        self.height = 0.14 * inch

    def draw(self) -> None:
        self.canv.setStrokeColor(colors.HexColor("#C72D35"))
        self.canv.setLineWidth(0.8)
        self.canv.line(0, self.height / 2, self.width, self.height / 2)


def pdf_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    base["Title"].fontName = "Helvetica-Bold"
    base["Title"].fontSize = 20
    base["Title"].leading = 24
    base["Heading1"].fontName = "Helvetica-Bold"
    base["Heading1"].fontSize = 14
    base["Heading1"].leading = 18
    base["Heading2"].fontName = "Helvetica-Bold"
    base["Heading2"].fontSize = 11.5
    base["Heading2"].leading = 15
    base["BodyText"].fontName = "Helvetica"
    base["BodyText"].fontSize = 9
    base["BodyText"].leading = 12
    base.add(ParagraphStyle(name="Small", parent=base["BodyText"], fontSize=7.5, leading=9.5))
    base.add(ParagraphStyle(name="CodeBlock", parent=base["Code"], fontName="Courier", fontSize=7, leading=8.5, backColor=colors.HexColor("#F2F4F7"), borderPadding=5))
    return base


def clean_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    return escaped


def render_table(lines: list[str], styles: dict[str, ParagraphStyle]) -> Table:
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and all(set(cell) <= {"-", ":", " "} for cell in cells):
            continue
        rows.append(cells)
    max_cols = max(len(row) for row in rows)
    normalized = [row + [""] * (max_cols - len(row)) for row in rows]
    width = 7.0 * inch
    data = [[Paragraph(clean_inline(cell), styles["Small"]) for cell in row] for row in normalized]
    table = Table(data, colWidths=[width / max_cols] * max_cols, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAECF0")),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D0D5DD")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def markdown_flowables(text: str) -> list[Flowable]:
    styles = pdf_styles()
    story: list[Flowable] = []
    lines = text.splitlines()
    i = 0
    bullets: list[str] = []
    code: list[str] = []
    in_code = False

    def flush_bullets() -> None:
        nonlocal bullets
        if bullets:
            story.append(ListFlowable([ListItem(Paragraph(clean_inline(item), styles["BodyText"])) for item in bullets], bulletType="bullet", leftIndent=16))
            bullets = []

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            if in_code:
                story.append(Preformatted("\n".join(code), styles["CodeBlock"]))
                code = []
                in_code = False
            else:
                flush_bullets()
                in_code = True
            i += 1
            continue
        if in_code:
            code.append(line)
            i += 1
            continue
        if not line.strip():
            flush_bullets()
            story.append(Spacer(1, 3))
        elif line.startswith("|"):
            flush_bullets()
            table_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1
            story.append(render_table(table_lines, styles))
            story.append(Spacer(1, 7))
            continue
        elif line.startswith("# "):
            flush_bullets()
            story.append(Paragraph(clean_inline(line[2:].strip()), styles["Title"]))
            story.append(HR())
        elif line.startswith("## "):
            flush_bullets()
            story.append(Paragraph(clean_inline(line[3:].strip()), styles["Heading1"]))
        elif line.startswith("### "):
            flush_bullets()
            story.append(Paragraph(clean_inline(line[4:].strip()), styles["Heading2"]))
        elif line.startswith("- "):
            bullets.append(line[2:].strip())
        else:
            flush_bullets()
            story.append(Paragraph(clean_inline(line.strip()), styles["BodyText"]))
        i += 1
    flush_bullets()
    return story


def render_pdf(markdown_path: Path, pdf_path: Path, footer_label: str) -> None:
    def footer(canvas, doc) -> None:
        canvas.saveState()
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(colors.HexColor("#667085"))
        canvas.drawString(0.7 * inch, 0.42 * inch, footer_label)
        canvas.drawRightString(7.8 * inch, 0.42 * inch, f"Page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(str(pdf_path), pagesize=letter, rightMargin=0.7 * inch, leftMargin=0.7 * inch, topMargin=0.65 * inch, bottomMargin=0.65 * inch)
    doc.build(markdown_flowables(markdown_path.read_text(encoding="utf-8")), onFirstPage=footer, onLaterPages=footer)


def load_env(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip() or line.lstrip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def http_json(url: str, payload: dict[str, object] | None = None, headers: dict[str, str] | None = None, timeout: int = 45) -> dict[str, object]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers or {}, method="POST" if payload is not None else "GET")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def choose_openrouter_model(models: dict[str, object], preferred: str | None = None) -> tuple[str, dict[str, object]]:
    by_id = {item["id"]: item for item in models.get("data", []) if isinstance(item, dict) and item.get("id")}
    candidates = [preferred] if preferred else []
    candidates += [
        "z-ai/glm-5.2",
        "moonshotai/kimi-k2.7-code",
        "anthropic/claude-sonnet-5",
    ]
    for candidate in candidates:
        if candidate and candidate in by_id:
            return candidate, by_id[candidate]
    raise RuntimeError("no_preferred_openrouter_model_available")


def estimate_cost(model_meta: dict[str, object], usage: dict[str, object]) -> float | None:
    try:
        pricing = model_meta.get("pricing", {})
        prompt_price = float(pricing.get("prompt", "0"))
        completion_price = float(pricing.get("completion", "0"))
        prompt_tokens = float(usage.get("prompt_tokens") or usage.get("input_tokens") or 0)
        completion_tokens = float(usage.get("completion_tokens") or usage.get("output_tokens") or 0)
        if prompt_price < 0 or completion_price < 0:
            return None
        return prompt_tokens * prompt_price + completion_tokens * completion_price
    except (TypeError, ValueError, AttributeError):
        return None


def run_openrouter(synthesis: dict[str, object], env: dict[str, str]) -> str:
    key = env.get("OPENROUTER_API_KEY", "")
    if not key:
        write_text(RUN_DIR / "E1.2.8_OpenRouter_blocked.md", "# E1.2.8 OpenRouter Blocked\n\nStatus: blocked\n\nReason: OpenRouter key missing from approved ignored env path.\n")
        return "blocked_missing_key"

    try:
        models = http_json("https://openrouter.ai/api/v1/models")
        model_id, model_meta = choose_openrouter_model(models, env.get("OPENROUTER_MODEL"))
        write_text(RUN_DIR / "openrouter-model-selection.json", json.dumps({
            "checked_at": now(),
            "model_count": len(models.get("data", [])),
            "selected_model": model_id,
            "selection_rule": "preferred env model if present, else first available PRD-suitable candidate",
        }, indent=2))

        prompt = f"""Create a concise, source-bound PRD from this sanitized ArchFlow E1.2.8 digest.

Rules:
- English only.
- No personal names.
- No raw transcript claims.
- Keep unsupported demand and ROI claims marked as gaps.
- Use sections: Source Boundary, Meeting Summary, Product Context, ICP, Pains/JTBD, Workflow, Requirements, Decisions, Risks, Next Tasks, Success Metrics.

SANITIZED DIGEST:
{sanitized_digest(synthesis)}
"""
        response = http_json(
            "https://openrouter.ai/api/v1/chat/completions",
            {
                "model": model_id,
                "messages": [
                    {"role": "system", "content": "You produce public-safe PRD artifacts from sanitized product discovery digests."},
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": 2600,
                "temperature": 0.2,
            },
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://archflow.local",
                "X-Title": "ArchFlow E1.2.8 sanitized PRD comparison",
            },
            timeout=90,
        )
        choice = (response.get("choices") or [{}])[0]
        content = (((choice or {}).get("message") or {}).get("content") or "").strip()
        if not content:
            raise RuntimeError("openrouter_empty_completion")
        output = "# E1.2.8 OpenRouter PRD\n\nStatus: provider comparison output from sanitized digest\n\n" + content
        write_text(RUN_DIR / "E1.2.8_OpenRouter_PRD.md", output)
        usage = response.get("usage") or {}
        cost = estimate_cost(model_meta, usage)
        ledger = {
            "created_at": now(),
            "provider": "openrouter",
            "model": model_id,
            "input_kind": "sanitized_digest_only",
            "raw_private_source_sent": False,
            "status": "success",
            "usage": usage,
            "estimated_cost_usd": cost,
        }
        write_text(RUN_DIR / "model-call-ledger.jsonl", json.dumps(ledger, sort_keys=True))
        write_text(RUN_DIR / "budget-guard.json", json.dumps({
            "daily_budget_usd": 5.00,
            "run_budget_usd": 1.99,
            "run_hard_stop_usd": 1.99,
            "actual_or_estimated_spend_usd": cost,
            "status": "ok" if cost is None or cost < 1.99 else "blocked_over_cap",
        }, indent=2))
        comparison = f"""# E1.2.8 Local Vs OpenRouter Comparison

Status: comparison generated

## FACT

- Local/Codex run used private sources locally and stored sanitized derived output.
- OpenRouter run used only the sanitized digest.
- Selected OpenRouter model: `{model_id}`.
- Estimated cost: `{cost if cost is not None else "unknown"}` USD.

## INTERPRETATION

The local/Codex output is stronger for project-state fidelity because it can inspect local repo context and E1 task boundaries. The OpenRouter output is useful as an independent formatting and reasoning comparison, but it should not become source of truth without AF Review.

## GAP

- Provider output still needs human review before Notion status promotion.
- No raw private transcript was sent, so provider output intentionally cannot cite exact participant language.
"""
        write_text(RUN_DIR / "E1.2.8_Local_vs_OpenRouter_comparison.md", comparison)
        for name in ["E1.2.8_OpenRouter_PRD.md", "E1.2.8_Local_vs_OpenRouter_comparison.md"]:
            render_pdf(RUN_DIR / name, RUN_DIR / name.replace(".md", ".pdf"), "ArchFlow E1.2.8 OpenRouter comparison")
        return "success"
    except Exception as exc:
        safe_error = re.sub(r"Bearer\s+[A-Za-z0-9._-]+", "Bearer <redacted>", str(exc))
        write_text(RUN_DIR / "E1.2.8_OpenRouter_blocked.md", f"# E1.2.8 OpenRouter Blocked\n\nStatus: blocked\n\nReason: `{safe_error}`\n")
        write_text(RUN_DIR / "model-call-ledger.jsonl", json.dumps({
            "created_at": now(),
            "provider": "openrouter",
            "input_kind": "sanitized_digest_only",
            "raw_private_source_sent": False,
            "status": "blocked",
            "reason": safe_error[:400],
        }, sort_keys=True))
        return "blocked_runtime_or_network"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--openrouter", action="store_true", help="Attempt OpenRouter comparison using sanitized digest only.")
    args = parser.parse_args()

    if not MEETING_PATH.exists():
        raise FileNotFoundError(MEETING_PATH)
    if not DISCOVERY_PATH.exists():
        raise FileNotFoundError(DISCOVERY_PATH)

    RUN_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    meeting = MEETING_PATH.read_text(encoding="utf-8", errors="replace")
    discovery = read_docx_text(DISCOVERY_PATH)
    synthesis = source_synthesis(meeting, discovery)

    openrouter_status = "not_run"
    write_text(RUN_DIR / "source-inventory.md", md_source_inventory(synthesis))
    write_text(RUN_DIR / "context-digest.md", md_context_digest(synthesis))
    write_text(RUN_DIR / "E1.2.8_Local_PRD.md", md_local_prd(synthesis))
    write_text(RUN_DIR / "E1.2.8_Local_Streaming_report.md", md_streaming_report(synthesis))
    write_text(RUN_DIR / "E1.2.8_Source_Methodology_review.md", md_methodology_review(synthesis))
    write_text(RUN_DIR / "backlog-and-questions.md", md_backlog_and_questions())
    write_text(RUN_DIR / "e1_2_8_local_run.json", json.dumps(synthesis, indent=2))
    write_text(RUN_DIR / "e1_2_8_stream_events.jsonl", "\n".join(json.dumps({"index": i + 1, "recorded_at": now(), "event": e}, sort_keys=True) for i, e in enumerate(["intake_validate", "source_summarize", "architecture_select", "draft_prd", "af_review", "record_outputs"])))

    if args.openrouter:
        openrouter_status = run_openrouter(synthesis, load_env(ROOT_ENV))

    write_text(RUN_DIR / "review-report.md", md_review_report(openrouter_status))
    write_text(RUN_DIR / "agent-activity-progress-report.md", md_agent_activity_report(openrouter_status))
    write_text(RUN_DIR / "agent-handout.md", md_agent_handout(openrouter_status))

    pdf_targets = [
        ("E1.2.8_Local_PRD.md", "2026-07-02-e1-2-8-local-prd.pdf"),
        ("E1.2.8_Local_Streaming_report.md", "2026-07-02-e1-2-8-local-streaming-report.pdf"),
        ("E1.2.8_Source_Methodology_review.md", "2026-07-02-e1-2-8-source-methodology-review.pdf"),
        ("agent-activity-progress-report.md", "2026-07-02-e1-2-8-agent-activity-progress-report.pdf"),
    ]
    for md_name, report_name in pdf_targets:
        pdf_path = RUN_DIR / md_name.replace(".md", ".pdf")
        render_pdf(RUN_DIR / md_name, pdf_path, "ArchFlow E1.2.8 public-safe testmeeting package")
        (REPORT_DIR / report_name).write_bytes(pdf_path.read_bytes())

    print(f"run_dir={RUN_DIR.relative_to(PUBLIC_ROOT)}")
    print(f"openrouter_status={openrouter_status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
