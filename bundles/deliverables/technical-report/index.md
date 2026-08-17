---
type: "Bundle Index"
title: "Technical Report"
description: "Evidence-grounded technical report documenting purpose, methods, inputs, results, uncertainty, limitations, review, and reproducibility."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "technical-writing"
- "reporting"
aliases:
- "Technical Report"
problems_solved:
- "Report technical work without inventing methods, data, results, authorship, reproducibility, safety, or approval."
- "Prepare a reviewable technical report and evidence index with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Engineering"
- "Research"
tools: []
frameworks:
- "purpose, method, evidence, result, uncertainty, and reproducibility review"
deliverables:
- "technical report and evidence index"
commands: []
skills: []
evaluations:
- "Technical Report source-awareness check"
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
  - "safety"
  - "security"
  - "privacy"
  - "legal"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified technical, methods, data, safety, security, legal or rights, and publication reviewers for the subject."
limitations:
- "NASA and NISO guidance describes report preparation and presentation; it does not establish local methods, data quality, results, reproducibility, technical validity, safety, classification, authorship, or approval."
- "Task-specific conclusions require current inspected evidence for approved purpose and scope, author and contributor records, requirements and prior work, methods and protocols, data provenance and units, code and environment versions, equipment and calibration, calculations and outputs, uncertainty and sensitivity, contradictory evidence, limitations, safety and security review, rights, reproducibility checks, review comments, and approvals."
- "This bundle does not grant authority to alter source records, run unapproved experiments, expose restricted information, represent validation or reproducibility, make safety or performance claims, publish, or approve conclusions."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to alter source records, run unapproved experiments, expose restricted information, represent validation or reproducibility, make safety or performance claims, publish, or approve conclusions."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: technical-report
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
# Technical Report

Use this bundle to prepare a reviewable **technical report and evidence index** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent authorship, method, input, unit, data quality, calculation, result, causal explanation, uncertainty, reproducibility, technical validity, safety, classification, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [technical report and evidence index](deliverables/technical-report-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
