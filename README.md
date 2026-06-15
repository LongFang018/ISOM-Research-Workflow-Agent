# Paper Research Workflow Skill

A lightweight ChatGPT/Codex Skill for deep academic paper reading, variable extraction, methodology and identification auditing, contribution mapping, gap identification, research direction generation, and IS/OM reviewer-style critique.

This is designed for slow, evidence-grounded paper learning rather than quick summarization.

## What It Produces

- Paper Card
- Variable Dictionary
- Methodology / Identification Audit
- Contribution Map
- Gap Map
- Research Direction Portfolio
- IS / OM Reviewer Report
- Evidence Audit

## Repository Structure

```text
.
├── README.md
├── paper-research-workflow/
│   ├── SKILL.md
│   ├── agents/
│   │   └── openai.yaml
│   ├── references/
│   │   ├── schemas.md
│   │   ├── method-checklists.md
│   │   ├── reviewer-rubrics.md
│   │   └── agent-roles.md
│   ├── scripts/
│   │   └── new_workbook.py
│   └── assets/
│       └── lightweight-workbook-template.md
```

## Install

### Option 1: Copy Into Local Codex Skills

```bash
rsync -a paper-research-workflow/ ~/.codex/skills/paper-research-workflow/
```

Then invoke it in a new conversation:

```text
Use $paper-research-workflow to read this paper deeply.
```

Chinese prompt:

```text
使用 $paper-research-workflow 帮我读这篇 paper，提取 variable、methodology、contribution、gap，并生成 IS/OM reviewer notes。
```

### Option 2: Build a Zip

If your environment supports uploading a Skill zip, build one from the repository root:

```bash
zip -qr paper-research-workflow.zip paper-research-workflow
```

Then upload `paper-research-workflow.zip`. Confirm the uploaded archive exposes:

```text
paper-research-workflow/SKILL.md
```

## Usage

### Single Paper Deep Reading

```text
Use $paper-research-workflow.
Read the attached paper and produce:
1. Paper Card
2. Variable Dictionary
3. Methodology / Identification Audit
4. Contribution Map
5. Gap Map
6. Research Direction Portfolio
7. Evidence Audit
```

Chinese version:

```text
使用 $paper-research-workflow 阅读这篇论文。
请输出 Paper Card、变量表、methodology / identification audit、contribution map、gap map、research directions 和 evidence audit。
重点关注变量定义、operationalization、识别策略、可复用研究设计，以及我未来可以发展的研究方向。
```

### Multi-Paper Synthesis

```text
Use $paper-research-workflow to synthesize these papers.
Build a literature matrix, compare theoretical streams, identify gaps, and turn the gaps into research directions.
```

### IS Reviewer Mode

```text
Use $paper-research-workflow in IS Reviewer Mode.
Review this manuscript as if for a top IS journal.
Include short summary, merit of the problem, articulation, research design, analysis, overall quality, major/minor issues, editor comments, and revision path.
```

### OM Reviewer Mode

```text
Use $paper-research-workflow in OM Reviewer Mode.
Review this manuscript as if for an OM journal.
Focus on operational decision relevance, process mechanism, model/data fit, identification or validation, managerial implications, and publishability.
```

### Combined IS/OM Reviewer Mode

```text
Use $paper-research-workflow in combined IS/OM reviewer mode.
Separate what an IS reviewer would attack from what an OM reviewer would attack.
```

## Generate a Blank Workbook

The Skill includes a small script for creating Markdown workbooks.

Single paper:

```bash
python paper-research-workflow/scripts/new_workbook.py \
  --mode single \
  --title "Paper Title" \
  --out paper-workbook.md
```

Multi-paper synthesis:

```bash
python paper-research-workflow/scripts/new_workbook.py \
  --mode multi \
  --title "Literature Review Topic" \
  --out literature-workbook.md
```

Reviewer report:

```bash
python paper-research-workflow/scripts/new_workbook.py \
  --mode review \
  --title "Reviewer Report" \
  --out review-workbook.md
```

Full workflow:

```bash
python paper-research-workflow/scripts/new_workbook.py \
  --mode full \
  --title "Full Paper Research Workbook" \
  --out full-workbook.md
```

Available modes:

- `single`: single-paper workflow
- `multi`: multi-paper synthesis
- `review`: reviewer report
- `full`: full workflow

## Recommended Workflow

1. Provide source materials: PDF, copied sections, BibTeX, Zotero notes, tables, appendix, or reviewer rubric.
2. Start with the single-paper outputs: Paper Card, Variable Dictionary, Methodology / Identification Audit, and Contribution Map.
3. Ask for gap identification and research directions after the paper-level audit is complete.
4. Switch to Reviewer Mode to learn how IS or OM reviewers would evaluate the work.
5. Run Evidence Audit before reusing any output in your own research notes.

## Evidence Discipline

Recommended instruction:

```text
Do not hallucinate. Every important claim should have page, section, quote, source_status, and confidence.
Separate what the authors claim from what is actually supported.
Label reviewer inferences clearly.
```

Useful evidence fields:

- `evidence.page`
- `evidence.section`
- `evidence.quote`
- `source_status`
- `confidence`

## Method Coverage

The methodology audit includes checklists for:

- Panel fixed effects / observational regression
- Difference-in-differences / event studies
- Instrumental variables
- Regression discontinuity
- Experiments / RCT / A/B tests
- Matching / synthetic control
- Structural and economic models
- Analytical and OM models
- Simulation / optimization
- ML / prediction / text or image models
- Qualitative / case / design science

## Future Extensions

- Zotero / BibTeX ingestion script
- PDF table extraction script
- Paper Card to CSV / Excel exporter
- Reviewer report DOCX template
- Personal writing-style examples
- Journal-specific IS / OM rubrics
- Paper-to-research-agenda pipeline
