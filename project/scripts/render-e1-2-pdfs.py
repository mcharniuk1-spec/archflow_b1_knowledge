#!/usr/bin/env python3
"""Render E1.2 Markdown reports to PDF."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Flowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
RUN_DIR = ROOT / "project" / "runs" / "E1.2" / "2026-06-26-full-test"
REPORT_DIR = ROOT / "project" / "reports"
PDFS = [
    ("E1.2_PRD.md", "E1.2_PRD.pdf", "2026-06-26-e1-2-prd.pdf"),
    ("E1.2_Streaming_report.md", "E1.2_Streaming_report.pdf", "2026-06-26-e1-2-streaming-report.pdf"),
    ("E1.2_System_report.md", "E1.2_System_report.pdf", "2026-06-26-e1-2-system-report.pdf"),
]


class HR(Flowable):
    def __init__(self, width: float = 6.8 * inch, color=colors.HexColor("#667085")) -> None:
        super().__init__()
        self.width = width
        self.height = 0.15 * inch
        self.color = color

    def draw(self) -> None:
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(0.7)
        self.canv.line(0, self.height / 2, self.width, self.height / 2)


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    base["Title"].fontName = "Helvetica-Bold"
    base["Title"].fontSize = 21
    base["Title"].leading = 25
    base["Title"].spaceAfter = 12
    base["Heading1"].fontName = "Helvetica-Bold"
    base["Heading1"].fontSize = 15
    base["Heading1"].leading = 19
    base["Heading1"].spaceBefore = 14
    base["Heading1"].spaceAfter = 8
    base["Heading2"].fontName = "Helvetica-Bold"
    base["Heading2"].fontSize = 12
    base["Heading2"].leading = 15
    base["Heading2"].spaceBefore = 10
    base["Heading2"].spaceAfter = 6
    base["BodyText"].fontName = "Helvetica"
    base["BodyText"].fontSize = 9.4
    base["BodyText"].leading = 12.4
    base["BodyText"].spaceAfter = 5
    base.add(ParagraphStyle(name="Small", parent=base["BodyText"], fontSize=8, leading=10))
    base.add(
        ParagraphStyle(
            name="BlockCode",
            parent=base["Code"],
            fontName="Courier",
            fontSize=7.5,
            leading=9.2,
            backColor=colors.HexColor("#F2F4F7"),
            borderColor=colors.HexColor("#D0D5DD"),
            borderWidth=0.5,
            borderPadding=5,
            spaceBefore=4,
            spaceAfter=7,
        )
    )
    return base


def clean_inline(text: str) -> str:
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    escaped = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", escaped)
    return escaped


def parse_table(lines: list[str], style_map: dict[str, ParagraphStyle]) -> Table:
    rows: list[list[str]] = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if cells and all(set(cell) <= {"-", ":", " "} for cell in cells):
            continue
        rows.append(cells)
    width = 7.0 * inch
    max_cols = max(len(row) for row in rows)
    normalized = [row + [""] * (max_cols - len(row)) for row in rows]
    data = [
        [Paragraph(clean_inline(cell), style_map["Small"]) for cell in row]
        for row in normalized
    ]
    table = Table(data, colWidths=[width / max_cols] * max_cols, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAECF0")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#101828")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D0D5DD")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FCFCFD")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def markdown_to_flowables(text: str) -> list[Flowable]:
    style_map = styles()
    story: list[Flowable] = []
    lines = text.splitlines()
    i = 0
    in_code = False
    code_buffer: list[str] = []
    pending_bullets: list[str] = []

    def flush_bullets() -> None:
        nonlocal pending_bullets
        if pending_bullets:
            story.append(
                ListFlowable(
                    [
                        ListItem(Paragraph(clean_inline(item), style_map["BodyText"]), bulletColor=colors.HexColor("#344054"))
                        for item in pending_bullets
                    ],
                    bulletType="bullet",
                    start="circle",
                    leftIndent=16,
                )
            )
            pending_bullets = []

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            if in_code:
                story.append(Preformatted("\n".join(code_buffer), style_map["BlockCode"]))
                code_buffer = []
                in_code = False
            else:
                flush_bullets()
                in_code = True
            i += 1
            continue
        if in_code:
            code_buffer.append(line)
            i += 1
            continue
        if not line.strip():
            flush_bullets()
            story.append(Spacer(1, 3))
            i += 1
            continue
        if line.startswith("|"):
            flush_bullets()
            table_lines = []
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1
            story.append(parse_table(table_lines, style_map))
            story.append(Spacer(1, 7))
            continue
        if line.startswith("# "):
            flush_bullets()
            story.append(Paragraph(clean_inline(line[2:].strip()), style_map["Title"]))
            story.append(HR())
        elif line.startswith("## "):
            flush_bullets()
            story.append(Paragraph(clean_inline(line[3:].strip()), style_map["Heading1"]))
        elif line.startswith("### "):
            flush_bullets()
            story.append(Paragraph(clean_inline(line[4:].strip()), style_map["Heading2"]))
        elif line.startswith("- "):
            pending_bullets.append(line[2:].strip())
        elif line == "\\pagebreak":
            flush_bullets()
            story.append(PageBreak())
        else:
            flush_bullets()
            story.append(Paragraph(clean_inline(line.strip()), style_map["BodyText"]))
        i += 1
    flush_bullets()
    if code_buffer:
        story.append(Preformatted("\n".join(code_buffer), style_map["BlockCode"]))
    return story


def footer(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#667085"))
    canvas.drawString(0.7 * inch, 0.42 * inch, "ArchFlow E1.2 public-safe internal proof package")
    canvas.drawRightString(7.8 * inch, 0.42 * inch, f"Page {doc.page}")
    canvas.restoreState()


def render(md_name: str, pdf_name: str) -> None:
    source = RUN_DIR / md_name
    target = RUN_DIR / pdf_name
    doc = SimpleDocTemplate(
        str(target),
        pagesize=letter,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
    )
    story = markdown_to_flowables(source.read_text(encoding="utf-8"))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    for md_name, pdf_name, report_name in PDFS:
        render(md_name, pdf_name)
        shutil.copy2(RUN_DIR / pdf_name, REPORT_DIR / report_name)
        print(f"rendered={Path('project/runs/E1.2/2026-06-26-full-test') / pdf_name}")
        print(f"copied={Path('project/reports') / report_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
