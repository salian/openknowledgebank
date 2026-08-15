---
type: "Bundle Index"
title: "Quality Assurance Scorecard"
description: "Evidence-grounded quality scorecard with defined criteria, sampling, scoring anchors, calibration, uncertainty, fairness, and use controls."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "quality-assurance"
- "scorecard"
aliases:
- "Quality Assurance Scorecard"
problems_solved:
- "Design or report QA scoring without inventing standards, samples, observations, weights, scores, reliability, performance, or employment consequences."
- "Prepare a reviewable quality assurance scorecard and calibration guide with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Quality assurance"
- "Customer operations"
tools: []
frameworks:
- "purpose, criterion, sample, scoring, calibration, uncertainty, and use review"
deliverables:
- "quality assurance scorecard and calibration guide"
commands: []
skills: []
evaluations:
- "Quality Assurance Scorecard source-awareness check"
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
  - "employment"
  - "privacy"
  - "legal"
  - "safety"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified quality, statistical, operational, privacy, employment, accessibility, safety, and legal reviewers as applicable."
limitations:
- "ISO 9001 and NIST statistical guidance provide general quality and measurement principles; they do not establish local standards, sampling validity, observations, scores, reviewer reliability, employee performance, compliance, or decision authority."
- "Task-specific conclusions require current inspected evidence for quality objectives and current standards, process and population, customer and safety requirements, criterion definitions and anchors, weighting rationale, sample frame and selection, reviewed records and provenance, reviewer training and calibration, agreement and uncertainty, privacy and fairness assessment, disputes, versioning, owners, and approvals."
- "This bundle does not grant authority to access or expose interactions, score people or records, alter weights, make employment decisions, declare compliance, publish rankings, or approve corrective action."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access or expose interactions, score people or records, alter weights, make employment decisions, declare compliance, publish rankings, or approve corrective action."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: qa-scorecard
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
# Quality Assurance Scorecard

Use this bundle to prepare a reviewable **quality assurance scorecard and calibration guide** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent criterion applicability, sample representativeness, observed fact, score, weight, reviewer agreement, quality level, employee performance, fairness, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [quality assurance scorecard and calibration guide](deliverables/qa-scorecard-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
