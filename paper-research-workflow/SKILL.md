---
name: paper-research-workflow
description: Deep academic paper reading and research synthesis workflow. Use when Codex or ChatGPT needs to read PDFs, papers, working papers, literature sets, Zotero/BibTeX notes, reviewer requests, or journal rubrics to extract paper cards, variable definitions, methodology and identification audits, contribution maps, gap maps, research directions, and IS/OM reviewer reports aligned to the user's research workflow and writing style.
---

# Paper Research Workflow

## Overview

Use this skill for slow, evidence-grounded reading of academic papers, not for quick summaries. Convert papers into reusable research assets: paper cards, variable dictionaries, method and identification audits, contribution maps, gap maps, research directions, and reviewer reports for IS and OM outlets.

Match the user's language. Keep technical terms such as construct, operationalization, identification, endogeneity, robustness, and boundary condition in English when precision matters.

## Quick Start

1. Identify the task mode:
   - **Single paper**: produce a paper card, variable dictionary, method audit, contribution map, and evidence audit.
   - **Multiple papers**: add a literature matrix, stream comparison, gap map, and research direction portfolio.
   - **Reviewer mode**: produce an IS, OM, or combined reviewer report with major/minor issues and revision path.
2. Load only the needed references:
   - For exact output fields, read `references/schemas.md`.
   - For method-specific checks, read `references/method-checklists.md`.
   - For IS/OM review logic, read `references/reviewer-rubrics.md`.
   - For the ten-agent handoff model, read `references/agent-roles.md`.
3. Extract claims with page evidence. If page evidence is unavailable, label it `page: unknown` and lower confidence.
4. Separate the paper's **claimed contribution** from the **actual contribution** you infer after auditing evidence, methods, and positioning.

## Workflow

Run these steps in order unless the user asks for a narrower output.

1. **Ingest and structure**: capture citation metadata, abstract, section map, tables, figures, references, appendices, and page evidence.
2. **Close read**: summarize the phenomenon, research question, theory base, context, data, method, findings, limitations, and reusable elements.
3. **Extract theory and variables**: identify constructs, variable names, theoretical roles, operationalization, data source, unit, time granularity, measurement window, expected sign, hypotheses, and validity concerns.
4. **Audit methodology and identification**: classify the design family, estimand, variation, treatment/control, assumptions, diagnostics, robustness, mechanism tests, heterogeneity, and external validity.
5. **Map contributions**: evaluate theoretical, empirical, methodological, phenomenological, managerial, and boundary-condition contributions.
6. **Identify gaps**: distinguish theory, measurement, identification, context, method, data, and practice gaps.
7. **Convert gaps into directions**: propose research questions, mechanisms, setting/data, variables, identification strategy, IS/OM contribution, risks, minimum viable study, next papers, and journal fit.
8. **Reviewer pass**: write what reviewers would praise and attack, fatal flaws, revision suggestions, publishability conditions, and lessons for the user's own work.
9. **Audit pass**: flag unsupported claims, weak evidence, logic jumps, overclaiming, missing page citations, and places where the model inferred beyond the text.

## Evidence Rules

- Use short quotes only when they anchor a claim. Prefer paraphrase plus page/section evidence.
- Preserve uncertainty. Use `confidence: high | medium | low` on extracted variables, method claims, and gap claims.
- Mark source status as `stated`, `table-derived`, `appendix-derived`, `inferred`, or `missing`.
- Do not invent variables, hypotheses, robustness checks, or reviewer criticisms. If a criticism is plausible but not directly shown by the text, label it as reviewer inference.
- Treat tables, figures, and appendices as primary evidence for variables and methods.
- Keep negative findings and null results visible; they often define boundary conditions.

## Method Routing

Select one or more method families before auditing:

- Causal observational: panel FE, DiD, event study, IV, RDD, matching, synthetic control, natural experiment.
- Experimental: lab experiment, field experiment, RCT, A/B test, survey experiment.
- Predictive/ML: supervised learning, causal ML, text/image models, recommender or platform algorithms.
- Structural/economic model: demand, supply, two-sided markets, dynamic choice, equilibrium.
- Analytical/OM model: optimization, queueing, inventory, game theory, simulation, mechanism design.
- Qualitative/design science: case study, interviews, ethnography, design artifact, process tracing.

Read `references/method-checklists.md` for the selected family. If the paper mixes methods, audit the causal claim and the descriptive or predictive claim separately.

## Reviewer Mode

If the user names a journal or field, use that lens. If unclear, produce a combined IS/OM memo with separate attack surfaces.

- IS lens: theory, digital/IT phenomenon, construct clarity, identification, boundary conditions, and contribution to IS conversations.
- OM lens: operational decision relevance, process mechanism, model/data fit, performance implications, implementation feasibility, and contribution to OM conversations.

Reviewer reports must include: Short Summary, Merit of the Research Problem, Quality of Articulation of the Problem, Research Design, Analysis and Interpretation of Results, Overall Quality of the Research, major issues, minor issues, editor-facing comments, and revision path.

## Style Adapter

When writing for the user:

- Prioritize variable definitions, methodology/identification, contribution realism, and research direction usefulness.
- Write in a research-notebook style: precise, structured, and reusable for future papers.
- Make critique actionable. Convert each criticism into a revision, robustness check, alternative measurement, or future study path.
- Avoid generic praise. State why an element is reusable for the user's own work.
- Keep IS and OM implications distinct when both are relevant.

## Script

Use `scripts/new_workbook.py` to create a blank Markdown workbook:

```bash
python scripts/new_workbook.py --mode full --title "Paper Title" --out paper-workbook.md
```

Modes are `single`, `multi`, `review`, and `full`.
