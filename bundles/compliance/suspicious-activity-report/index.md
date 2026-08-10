---
type: Bundle Index
title: Suspicious Activity Report
description: Evidence-grounded assessment, documentation, filing, retention, and confidentiality review for suspicious activity reports.
category: compliance
version: 0.1.0
tags:
- sar
- fincen
- bsa-aml
aliases:
- SAR
- Suspicious activity reporting
problems_solved:
- Assess Suspicious Activity Report applicability and evidence.
- Prepare a reviewable compliance workpaper without inventing legal conclusions.
industries:
- Financial Services
- Legal and Compliance
- Cross-industry
tools:
[]
frameworks:
- source-applicability-control-evidence review
deliverables:
- suspicious activity report decision and evidence brief
commands: []
skills: []
evaluations:
- Suspicious Activity Report source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- bsa-aml-compliance-program
- bsa-e-filing
adjacent_bundles:
[]
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  []
  soc:
  []
  isco_08:
  []
  esco: []
content_risk:
  classification: regulated
  domains:
  - regulatory
  - legal
  - financial
  - security
  professional_review:
    status: not_reviewed
    required_qualification: A qualified legal, compliance, regulatory, and subject-matter reviewer appropriate to the entity, activity, and jurisdiction.
limitations:
- Official sources describe general regulatory requirements; they do not determine entity applicability, local facts, records, calculations, filings, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for institution type and governing SAR rule, transaction and customer records, alert and investigation evidence, detection date, threshold analysis, filing history, supporting documents, confidentiality controls, escalation, and approvals.
- This bundle does not grant authority to file, amend, disclose, or confirm a SAR; contact a subject; freeze or close an account; alter monitoring; or represent a legal conclusion.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before taking any action to file, amend, disclose, or confirm a SAR; contact a subject; freeze or close an account; alter monitoring; or represent a legal conclusion.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: suspicious-activity-report
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard.
---
# Suspicious Activity Report

Use this bundle to prepare a reviewable **suspicious activity report decision and evidence brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent applicability, legal conclusions, thresholds, deadlines, exemptions, filing status, control effectiveness, compliance, approval, or authority.

## Start Here

- [Overview](overview.md)
- [Official Reference Index](references/index.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [suspicious activity report decision and evidence brief](deliverables/suspicious-activity-report-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
