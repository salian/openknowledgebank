---
type: "Bundle Index"
title: "Data Quality and Validation Report"
description: "Evidence-grounded data-quality reporting with scope, lineage, profiling, rule, sample, reconciliation, severity, limitation, remediation, and audit controls."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "data-quality"
- "validation"
- "data-governance"
aliases:
- "Data Quality and Validation Report"
problems_solved:
- "Report data quality without inventing scope, lineage, rule validity, completeness, accuracy, issue severity, remediation, fitness, or approval."
- "Prepare a reviewable source-linked data quality and validation report with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Data management"
- "Analytics"
tools: []
frameworks:
- "purpose, scope, lineage, profile, rule, sample, reconciliation, issue, and remediation review"
deliverables:
- "source-linked data quality and validation report"
commands: []
skills: []
evaluations:
- "Data Quality and Validation Report source-awareness check"
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
  - "legal"
  - "financial"
  - "privacy"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified domain, legal, finance, privacy, data, and accountable decision reviewers for the artifact and jurisdictions."
limitations:
- "NIST sources do not establish local lineage, rule validity, data accuracy, completeness, issue severity, remediation success, fitness for use, or approval."
- "Task-specific conclusions require current inspected evidence for report sponsor and data authority, decision purpose scope population period and systems, source-to-target lineage and extraction logs, schema and metric definitions, profiling outputs and reproducible queries, approved validation rules and thresholds, sample frame and method, control totals and reconciliations, issue examples rates denominators severity rationale and owner, privacy controls, remediation retest limitations and approvals."
- "This bundle does not grant authority to access or expose data without authority, alter source records, fabricate lineage or test results, suppress issues, certify fitness, close remediation, publish, or trigger decisions without approval."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access or expose data without authority, alter source records, fabricate lineage or test results, suppress issues, certify fitness, close remediation, publish, or trigger decisions without approval."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: data-quality-report
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
# Data Quality and Validation Report

Use this bundle to prepare a reviewable **source-linked data quality and validation report** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent scope, lineage, population, rule validity, completeness, accuracy, consistency, timeliness, severity, remediation, fitness, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [source-linked data quality and validation report](deliverables/data-quality-report-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
