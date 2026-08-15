---
type: "Bundle Index"
title: "Value-at-Risk Analysis"
description: "Evidence-grounded VaR analysis documenting portfolio scope, market data, method, assumptions, validation, backtesting, stress context, and limits."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "value-at-risk"
- "market-risk"
aliases:
- "Value-at-Risk Analysis"
problems_solved:
- "Estimate VaR without inventing positions, prices, distributions, dependencies, model validity, loss bounds, capital effects, or trading authority."
- "Prepare a reviewable value-at-risk analysis and validation record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Financial risk"
- "Investment management"
tools: []
frameworks:
- "portfolio, market-data, method, assumption, validation, backtest, and limit review"
deliverables:
- "value-at-risk analysis and validation record"
commands: []
skills: []
evaluations:
- "Value-at-Risk Analysis source-awareness check"
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
[]
adjacent_bundles: []
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  []
  soc: []
  isco_08: []
  esco: []
content_risk:
  classification: "regulated"
  domains:
  - "financial"
  - "regulatory"
  - "accounting"
  - "legal"
  - "privacy"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified market-risk, quantitative, independent model-validation, finance, accounting, legal or regulatory, data, and governance reviewers."
limitations:
- "Basel market-risk standards and Federal Reserve model-risk guidance apply to particular regulated contexts; they do not establish local positions, prices, assumptions, model validity, VaR values, maximum loss, capital requirements, compliance, or authority."
- "Task-specific conclusions require current inspected evidence for portfolio and legal-entity scope, position and valuation reconciliations, approved market-data sources, model version and code, confidence level horizon and history, distribution and dependency assumptions, mappings and proxies, nonlinear treatment, missing-data controls, reproducible outputs, uncertainty and sensitivity, backtesting and exceptions, independent validation, stress comparisons, limits, governance, and approvals."
- "This bundle does not grant authority to access trading data, change positions or limits, select regulatory treatment, certify a model, represent maximum loss, set capital, execute trades, publish risk, or approve use."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access trading data, change positions or limits, select regulatory treatment, certify a model, represent maximum loss, set capital, execute trades, publish risk, or approve use."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: var-analysis
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: "No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available."
  evidence_note: "No measured score is claimed."
evaluation_detail:
  status: blocked
  next_action: "Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard."
---
# Value-at-Risk Analysis

Use this bundle to prepare a reviewable **value-at-risk analysis and validation record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent position, valuation, market input, distribution, dependence, model validity, VaR result, maximum loss, backtest outcome, exception, capital effect, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [value-at-risk analysis and validation record](deliverables/var-analysis-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
