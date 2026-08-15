---
type: "Bundle Index"
title: "Exploratory Data Analysis Report"
description: "Evidence-grounded exploratory analysis report documenting data provenance, quality, distributions, relationships, uncertainty, limitations, and next tests."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "data-analysis"
- "eda"
aliases:
- "Exploratory Data Analysis Report"
problems_solved:
- "Explore a dataset transparently without inventing provenance, representativeness, causal explanations, significance, or decision readiness."
- "Prepare a reviewable exploratory data analysis report with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Analytics"
- "Data science"
tools: []
frameworks:
- "data provenance, quality, exploratory pattern, uncertainty, and validation review"
deliverables:
- "exploratory data analysis report"
commands: []
skills: []
evaluations:
- "Exploratory Data Analysis Report source-awareness check"
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
  classification: "ymyl"
  domains:
  - "privacy"
  professional_review:
    status: not_reviewed
    required_qualification: "A qualified data analyst or statistician, data owner, privacy reviewer, and domain expert for the intended use."
limitations:
- "NIST guidance describes exploratory techniques and goals; it does not establish local data provenance, quality, representativeness, pattern validity, causal explanation, statistical significance, model suitability, or decision authority."
- "Task-specific conclusions require current inspected evidence for analysis question and prohibited uses, dataset version and provenance, collection and sampling process, population and period, schema and units, missingness and quality, transformations and code, descriptive outputs and graphics, subgroup and temporal checks, uncertainty and sensitivity, privacy controls, reproducible environment, review, and approvals."
- "This bundle does not grant authority to access or expose restricted data, alter source records, infer identity or sensitive traits, declare causality or significance, train or deploy a model, automate decisions, or publish findings."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access or expose restricted data, alter source records, infer identity or sensitive traits, declare causality or significance, train or deploy a model, automate decisions, or publish findings."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: exploratory-data-analysis-report
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
# Exploratory Data Analysis Report

Use this bundle to prepare a reviewable **exploratory data analysis report** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent data provenance, population, unit, quality, missingness mechanism, outlier meaning, relationship, causal explanation, significance, representativeness, model suitability, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [exploratory data analysis report](deliverables/exploratory-data-analysis-report-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
