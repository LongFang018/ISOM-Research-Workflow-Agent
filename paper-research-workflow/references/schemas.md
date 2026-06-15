# Output Schemas

Load this file when the user asks for paper cards, variable extraction, method audits, contribution maps, gap identification, research directions, literature synthesis, reviewer reports, or evidence audits.

## Paper Card

```yaml
paper_name:
year_month:
authors_citation:
venue:
research_area:
phenomenon:
research_question:
theory_base:
context:
data:
method:
main_findings:
claimed_contribution:
actual_contribution:
managerial_implications:
limitations:
most_reusable_elements:
evidence_map:
  - claim:
    page:
    section:
    quote:
    source_status: stated | table-derived | appendix-derived | inferred | missing
    confidence: high | medium | low
```

Use `actual_contribution` to state the defensible contribution after reading the design, evidence, and positioning. Do not merely repeat the authors' claim.

## Theory Map

```yaml
theory_base:
  - theory_name:
    role_in_paper:
    key_assumptions:
    constructs_used:
    mechanism:
    boundary_conditions:
    evidence:
mechanism_chain:
  - antecedent:
    mechanism:
    outcome:
    moderators:
    scope_conditions:
missing_theory_or_underdeveloped_link:
```

## Variables Extraction

```yaml
variables:
  - variable_name:
    construct_name:
    theoretical_role: independent | dependent | mediator | moderator | control | mechanism | outcome
    definition_in_paper:
    operationalization:
    data_source:
    unit_of_analysis:
    time_granularity:
    measurement_window:
    transformation:
    expected_sign:
    hypothesis_link:
    table_or_model_used:
    validity_concerns:
    alternative_measures:
    evidence:
      page:
      section:
      quote:
      source_status: stated | table-derived | appendix-derived | inferred | missing
    confidence: high | medium | low
```

Add these fields when useful:

```yaml
construct_level: individual | team | firm | platform | market | product | transaction | process | other
measurement_type: direct measure | proxy | scale | index | text-derived | model-estimated | experimental manipulation
possible_endogeneity:
missingness_or_sample_selection:
replication_notes:
```

## Methodology / Identification Audit

```yaml
methodology_identification_audit:
  design_type:
  method_family:
  estimand:
  identifying_variation:
  treatment_definition:
  control_group:
  timing:
  sample_construction:
  model_specification:
  fixed_effects:
  standard_errors:
  key_assumptions:
  assumption_tests:
  robustness_checks:
  placebo_tests:
  mechanism_tests:
  heterogeneity_tests:
  threats_to_identification:
  external_validity:
  data_limitations:
  reproducibility_assets:
  causal_claim_strength: descriptive | associational | suggestive causal | credible causal | experimental causal
  what_would_reviewer_attack:
  what_is_actually_strong:
  evidence:
    - claim:
      page:
      section:
      quote:
      confidence:
```

For non-causal analytical, optimization, simulation, or prediction papers, adapt the audit:

```yaml
model_or_algorithm_audit:
  objective_function_or_prediction_target:
  assumptions:
  decision_variables:
  constraints:
  benchmark_or_counterfactual:
  validation_strategy:
  sensitivity_analysis:
  calibration_or_training_data:
  evaluation_metrics:
  managerial_decision_link:
  failure_modes:
```

## Contribution Map

```yaml
contribution_map:
  paper_type: theory | empirical-causal | empirical-descriptive | predictive | analytical-model | design-science | review | mixed
  positioning:
    focal_conversation:
    compared_streams:
    closest_prior_work:
    claimed_gap:
  contribution_items:
    - contribution_type: theoretical | empirical | methodological | phenomenological | managerial | boundary-condition
      author_claim:
      actual_increment:
      evidence:
      novelty: high | medium | low
      durability: likely durable | context-bound | fragile
      weakness:
      reusable_for_my_work:
```

Contribution questions:

| Contribution type | Ask |
| --- | --- |
| Theoretical | Does it propose a new mechanism, boundary condition, construct, or construct relationship? |
| Empirical | Does it use new data, a new setting, or a sharper measurement strategy? |
| Methodological | Does it improve estimation, identification, optimization, experiment design, or validation? |
| Phenomenological | Does it explain an emerging practice, technology, or operational issue? |
| Managerial | Could it change firm, platform, or operations decisions? |
| Boundary condition | Where should the result hold, fail, or reverse? |

## Gap Identification

```yaml
gaps:
  - gap_type: theory | measurement | identification | context | method | data | practice
    gap_statement:
    why_it_matters:
    evidence_from_paper_or_literature:
    severity: high | medium | low
    tractability: high | medium | low
    related_papers:
```

Gap definitions:

| Gap type | Meaning |
| --- | --- |
| Theory gap | Existing theory cannot explain a mechanism, contradiction, or boundary. |
| Measurement gap | A key construct is proxied crudely or measured at the wrong level/time. |
| Identification gap | Existing studies have endogeneity, selection, or weak causal inference. |
| Context gap | New technologies, platforms, regulations, or operating contexts alter the mechanism. |
| Method gap | Existing methods cannot handle dynamics, networks, strategy interaction, or heterogeneity. |
| Data gap | New data can observe behavior or process states previously invisible. |
| Practice gap | A practically important decision is under-modeled or under-theorized. |

## Research Direction

```yaml
research_directions:
  - research_direction:
    core_research_question:
    why_now:
    theoretical_mechanism:
    possible_setting:
    candidate_data:
    key_variables:
    identification_strategy:
    expected_contribution_to_IS:
    expected_contribution_to_OM:
    main_risks:
    minimum_viable_study:
    related_papers_to_read_next:
    journal_fit:
```

Make each direction testable. Avoid directions that are only "study X in a new context" unless the context changes the mechanism, measurement, or decision problem.

## Literature Matrix

```yaml
literature_matrix:
  - paper:
    stream:
    theory:
    phenomenon:
    context:
    data:
    key_variables:
    method:
    identification_or_validation:
    main_finding:
    contribution:
    limitations:
    reusable_elements:
    gaps_opened:
```

## Reviewer Report

```yaml
reviewer_report:
  reviewer_mode: IS | OM | combined
  short_summary:
  merit_of_the_research_problem:
  quality_of_articulation_of_the_problem:
  research_design:
  analysis_and_interpretation_of_results:
  overall_quality_of_the_research:
  what_a_reviewer_would_praise:
  what_a_reviewer_would_attack:
  fatal_flaws_if_submitted_today:
  major_issues:
    - issue:
      why_it_matters:
      evidence:
      revision_path:
  minor_issues:
  revision_suggestions:
  what_makes_it_publishable:
  what_you_can_learn_for_your_own_work:
  editor_comments:
```

## Evidence Audit

```yaml
evidence_audit:
  unsupported_claims:
    - claim:
      problem:
      needed_evidence:
  weak_links:
    - link:
      why_weak:
      possible_fix:
  hallucination_risks:
    - output_claim:
      risk:
      correction:
  overclaiming:
    - author_or_agent_claim:
      bounded_claim:
  missing_information:
    - item:
      likely_location:
      action:
```
