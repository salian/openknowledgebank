---
type: "Bundle Index"
title: "Suspicious Activity Reporting"
description: "Current-source guidance for suspicious activity identification, escalation, SAR filing, confidentiality, retention, governance, and qualified review."
category: compliance
version: 0.1.0
tags:
- "compliance"
- "source-aware"
aliases:
- "SAR Filing"
- "Suspicious Activity Report"
- "BSA SAR"
problems_solved:
- "Determine what current sources say without inventing coverage, effective dates, facts, exceptions, records, filings, or compliance."
- "Prepare a reviewable applicability and evidence brief for qualified legal and compliance review."
industries:
- "Regulated services"
- "United States"
tools: []
frameworks:
- "risk-based suspicious activity reporting analysis"
deliverables:
- "privileged suspicious-activity escalation and filing-decision brief"
commands: []
skills: []
evaluations:
- "Suspicious Activity Reporting source-awareness check"
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
  - "financial"
  - "legal"
  - "privacy"
  - "regulatory"
  - "security"
  professional_review:
    status: not_reviewed
    required_qualification: "A qualified United States attorney or compliance professional with subject-matter and jurisdictional competence, plus the evidenced accountable owner."
limitations:
- "Controlling and agency sources state general requirements and interpretations; they do not establish local coverage, facts, exceptions, compliance, privilege, filing status, legal advice, or approval."
- "Task-specific conclusions require current inspected evidence for current controlling and interpretive sources, effective dates, jurisdiction, covered entity and activity, transaction or communication facts, consumer and consent evidence, disclosures, records, controls, exceptions, retention, filings, remediation, and approval evidence."
- "This bundle does not grant authority to label a person suspicious, investigate covertly, disclose SAR existence, access protected records, file or amend a SAR, contact subjects, close alerts, or represent a filing duty or compliance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to label a person suspicious, investigate covertly, disclose SAR existence, access protected records, file or amend a SAR, contact subjects, close alerts, or represent a filing duty or compliance."
timestamp: "2026-08-14T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: suspicious-activity-reporting
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
# Suspicious Activity Reporting

Use this bundle to prepare a reviewable **privileged suspicious-activity escalation and filing-decision brief** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent institution-specific applicability, suspicious intent, person culpability, reportability, amount, timing, SAR existence or content, filing status, safe harbor, violation, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Compliance guide](compliance.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [privileged suspicious-activity escalation and filing-decision brief](deliverables/suspicious-activity-reporting-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
