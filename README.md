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

## ⚖️ Ethics & AI Policy Guidelines

> [!IMPORTANT]
> This framework is designed to serve as an intellectual sparring partner and a structural drafting aid for academic reviewers. Before pasting any text from an active, unpublished invitation to review, please ensure your usage aligns with journal-specific policies.

### 1. Compliance with Journal AI Policies
Different publishers and societies have distinct, strict regulations regarding the use of Generative AI in the peer-review process. **Always verify the specific journal's policy before processing any text.** For example:
*   **Elsevier:** Explicitly states that peer reviewers must *not* upload a submitted manuscript or any part of it into generative AI tools, as it violates confidentiality and proprietary rights.
*   **Springer Nature:** Requires that peer reviewers do *not* upload manuscripts into generative AI tools to protect the confidentiality of the authors' intellectual property.
*   **INFORMS (e.g., Service Science):** Emphasizes that all review conclusions remain the sole responsibility of the human reviewer, and warns that uploading manuscripts to public-domain AI servers may constitute a breach of confidentiality and copyright laws.

### 2. Best Practices for Safe Use
If you wish to utilize this framework while fully adhering to the strict confidentiality policies above, consider these safe alternatives:
*   **Abstract/Paraphrase Only:** Input only highly aggregated, anonymized summaries or self-authored notes rather than the original manuscript text.
*   **Methodology Inquiries:** Use the modes to query specific methodological setups (e.g., *"How would an OM reviewer critique a Double Machine Learning approach with X limitations?"*) rather than pasting raw paper content.
*   **Structural Refinement:** Use the workflow to structure and polish your *own* rough review notes into standard journal formats.

### 3. Human-in-the-Loop & Accountability
*   **Objective Tone:** The feedback generated should remain constructive, peer-focused, and intellectually rigorous. 
*   **Sole Accountability:** AI-generated suggestions are strictly supplementary. The final review report, its scholarly accuracy, and the editorial recommendation are entirely your responsibility as the invited expert.


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
