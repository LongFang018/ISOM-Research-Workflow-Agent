#!/usr/bin/env python3
"""Create a blank Markdown workbook for the paper research workflow."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


SECTIONS = {
    "single": [
        "Source Inventory",
        "Paper Card",
        "Theory Map",
        "Variable Dictionary",
        "Methodology / Identification Audit",
        "Contribution Map",
        "Evidence Audit",
    ],
    "multi": [
        "Source Inventory",
        "Literature Matrix",
        "Stream Comparison",
        "Gap Map",
        "Research Direction Portfolio",
        "Next Papers To Read",
        "Evidence Audit",
    ],
    "review": [
        "Source Inventory",
        "Short Summary",
        "Merit of the Research Problem",
        "Quality of Articulation of the Problem",
        "Research Design",
        "Analysis and Interpretation of Results",
        "Overall Quality of the Research",
        "Major Issues",
        "Minor Issues",
        "Revision Path",
        "Editor Comments",
        "Lessons For My Work",
    ],
    "full": [
        "Source Inventory",
        "Paper Card",
        "Theory Map",
        "Variable Dictionary",
        "Methodology / Identification Audit",
        "Contribution Map",
        "Literature Matrix",
        "Gap Map",
        "Research Direction Portfolio",
        "Reviewer Memo",
        "Evidence Audit",
    ],
}


def build_workbook(title: str, mode: str) -> str:
    lines = [
        f"# {title}",
        "",
        f"- workflow_mode: {mode}",
        f"- created: {date.today().isoformat()}",
        "- status: blank",
        "",
    ]
    for section in SECTIONS[mode]:
        lines.extend([f"## {section}", "", "TBD", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=sorted(SECTIONS), default="full")
    parser.add_argument("--title", default="Paper Research Workbook")
    parser.add_argument("--out", required=True, help="Output Markdown path")
    args = parser.parse_args()

    output = Path(args.out).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_workbook(args.title, args.mode), encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
