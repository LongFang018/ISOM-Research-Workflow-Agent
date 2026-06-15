# Agent Roles

Use this file when coordinating a full workflow. In lightweight mode, one assistant can simulate these agents sequentially; no separate runtime is required.

| Agent | Responsibility | Output |
| --- | --- | --- |
| Ingestion Agent | Read PDF/text, metadata, references, Zotero tags, and journal prompts. | Clean text, citation metadata, source inventory. |
| Structure Agent | Identify paper structure, sections, tables, figures, appendices, and reference cues. | Section map, table/figure map, evidence index. |
| Close Reading Agent | Build a faithful, non-hallucinated paper understanding. | Paper card, findings summary, reusable elements. |
| Theory Agent | Extract theory, constructs, mechanisms, assumptions, and boundary conditions. | Theory map, mechanism chain, construct list. |
| Variable Agent | Extract variable definitions, operationalization, data sources, units, windows, and validity concerns. | Variable dictionary. |
| Method Agent | Audit methodology, identification, assumptions, robustness, mechanisms, and external validity. | Methodology / identification audit. |
| Contribution Agent | Compare claimed and actual contribution across theory, data, method, phenomenon, management, and boundaries. | Contribution map. |
| Gap Agent | Identify gaps and convert them into research directions. | Gap map, research direction portfolio. |
| Reviewer Agent | Produce IS/OM reviewer reports, editor comments, major/minor issues, and revision path. | Review memo. |
| Audit Agent | Check evidence, hallucination risk, unsupported claims, and logic jumps. | Evidence audit and correction list. |

## Handoff Order

1. Ingestion Agent passes metadata and clean text to Structure Agent.
2. Structure Agent creates evidence anchors for all later agents.
3. Close Reading Agent writes the paper card using section-level evidence.
4. Theory Agent and Variable Agent work from the paper card plus methods/tables.
5. Method Agent audits the strongest empirical, model, experimental, or qualitative claim.
6. Contribution Agent compares author positioning against the audited evidence.
7. Gap Agent uses limitations, weak links, and neighboring literature to generate research directions.
8. Reviewer Agent writes field-specific critique using the full prior outputs.
9. Audit Agent checks every final claim for support and uncertainty labels.

## Minimum Viable Run

If time or source quality is limited, produce:

- Paper card
- Variable dictionary
- Methodology / identification audit
- Contribution map
- Three research directions
- Evidence audit

## Failure Handling

- If the PDF text is poor, ask for OCR, a better PDF, or copied text.
- If tables are unreadable, mark variable extraction as low confidence and request table images or appendix files.
- If no page numbers exist, cite section names and quote snippets.
- If the paper is conceptual, replace identification audit with theory/model logic audit.
- If the paper is an analytical OM model, audit assumptions, comparative statics, sensitivity, and managerial decision link.
