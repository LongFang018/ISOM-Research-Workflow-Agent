# Method Checklists

Load this file after identifying the method family. Use only the relevant checklist sections.

## Universal Method Audit

For every paper, answer:

- What is the unit of analysis, treatment or decision, outcome, time window, and comparison?
- What exact estimand or performance object is being claimed?
- What variation or model assumption makes the claim informative?
- What is descriptive, correlational, causal, predictive, prescriptive, or theoretical?
- What would change the interpretation if omitted, mismeasured, or timed incorrectly?
- What robustness checks address the strongest alternative explanation?
- Which tests are reassuring but not decisive?

## Panel FE / Observational Regression

Check:

- Outcome, treatment, controls, fixed effects, sample restrictions, clustering, and time trends.
- Whether treatment timing precedes the outcome and avoids post-treatment controls.
- Whether controls are confounders, mediators, colliders, or bad controls.
- Whether within-unit variation is sufficient after fixed effects.
- Whether standard errors match treatment assignment and serial correlation.
- Whether alternative mechanisms or reverse causality remain.

Reviewer attacks:

- "The design absorbs too much or too little variation."
- "Controls are endogenous or measured after treatment."
- "The result is driven by time-varying confounding, functional form, or sample selection."

## Difference-in-Differences / Event Study

Check:

- Treatment timing, treated/control comparability, anticipation, staggered adoption, and contamination.
- Parallel trends evidence before treatment.
- Dynamic treatment effects and whether event-time coefficients are interpretable.
- Whether the estimator handles heterogeneous treatment effects under staggered adoption.
- Placebo timing, never-treated or not-yet-treated controls, and alternative windows.

Reviewer attacks:

- "Pre-trends or anticipation invalidate the comparison."
- "Controls are exposed indirectly."
- "Staggered timing creates weighting or heterogeneity problems."

## Instrumental Variables

Check:

- Relevance, exclusion restriction, monotonicity, first-stage strength, and interpretation of LATE.
- Whether the instrument affects the outcome through any channel besides treatment.
- Whether the instrument changes sample composition.
- Balance and falsification tests on pre-treatment variables.

Reviewer attacks:

- "The exclusion restriction is not credible."
- "The instrument changes multiple margins."
- "The LATE population is not the population discussed in the contribution."

## Regression Discontinuity

Check:

- Running variable, cutoff rule, bandwidth, manipulation, sorting, and continuity.
- Local randomization logic and whether units can precisely manipulate the cutoff.
- Balance around cutoff and density tests.
- Functional form, bandwidth sensitivity, and donut RD if needed.
- Whether the local estimand matches the paper's general claim.

Reviewer attacks:

- "Units manipulate the threshold."
- "The estimate is too local for the claimed contribution."
- "Bandwidth or polynomial choices drive the result."

## Experiments / RCT / A/B Tests

Check:

- Randomization unit, treatment arms, compliance, attrition, spillovers, and preregistration.
- Whether manipulation matches the theoretical construct.
- Whether outcomes are behavioral, self-reported, short-run, or durable.
- Power, multiple testing, balance, manipulation checks, and heterogeneous effects.
- External validity across subjects, tasks, markets, and incentives.

Reviewer attacks:

- "The manipulation is not the construct."
- "The setting lacks stakes or external validity."
- "Attrition, spillovers, or multiple comparisons weaken inference."

## Matching / Synthetic Control

Check:

- Assignment mechanism, covariate set, balance, common support, and donor pool.
- Whether matching uses only pre-treatment variables.
- Sensitivity to unobserved confounding.
- For synthetic control, pre-treatment fit, donor weights, placebo units, and post-treatment shocks.

Reviewer attacks:

- "Selection on unobservables remains."
- "The donor pool or covariates encode the answer."
- "Pre-period fit is weak or post-treatment shocks confound results."

## Structural / Economic Model

Check:

- Agents, utility/profit/objective functions, state variables, equilibrium concept, and identification.
- Which parameters are estimated versus calibrated.
- What data moments identify each parameter.
- Counterfactual validity and whether policy simulations extrapolate beyond support.
- Sensitivity to functional forms, distributions, and equilibrium selection.

Reviewer attacks:

- "The assumptions do the work."
- "Identification of parameters is unclear."
- "Counterfactuals exceed what the data can support."

## Analytical / OM Model

Check:

- Decision maker, objective, constraints, information structure, timing, and equilibrium or optimality concept.
- Whether assumptions map to a real operational process.
- Comparative statics, boundary cases, sensitivity, and managerial interpretation.
- Whether results are robust to alternative demand, cost, queueing, inventory, or behavioral assumptions.
- Whether the model yields new insight beyond algebraic restatement.

Reviewer attacks:

- "The operational setting is too stylized."
- "The insight depends on a narrow assumption."
- "Managerial implications do not follow from the model."

## Simulation / Optimization

Check:

- Objective function, constraints, data generation process, baseline, benchmark, and evaluation metric.
- Calibration, validation, sensitivity, and uncertainty.
- Feasibility under real information, compute, and operational constraints.
- Whether the benchmark is strong enough.

Reviewer attacks:

- "The benchmark is weak."
- "Simulation assumptions drive the result."
- "The proposed policy is impractical under real constraints."

## ML / Prediction / Text or Image Models

Check:

- Prediction target, feature timing, leakage, train/test split, validation, and deployment setting.
- Whether labels are valid and whether proxy labels encode bias.
- Whether model performance connects to theory, decision quality, or causal mechanism.
- Out-of-sample, cross-context, fairness, interpretability, and ablation checks.
- Whether the paper confuses prediction with explanation or causality.

Reviewer attacks:

- "The model leaks future information."
- "Predictive performance does not answer the research question."
- "The construct is reduced to an opaque or biased proxy."

## Qualitative / Case / Design Science

Check:

- Case selection, sampling, data sources, coding, triangulation, chain of evidence, and negative cases.
- Whether theory building is grounded in evidence rather than narrative.
- Whether constructs and mechanisms are transferable beyond the case.
- For design science, artifact requirements, design principles, evaluation, and contribution beyond implementation.

Reviewer attacks:

- "Case selection is convenience-based."
- "Evidence does not support the proposed mechanism."
- "The artifact is useful but not a research contribution."
