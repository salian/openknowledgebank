---
type: "Bundle Index"
title: "HCC Risk Adjustment Coder for Medicare Advantage Plans"
description: "Evidence-controlled risk-adjustment coding support with encounter, diagnosis, ICD-10-CM, CMS model, documentation, audit, and submission boundaries."
category: roles
version: 0.1.0
tags:
- "role"
- "hcc-coding"
- "risk-adjustment"
- "medicare-advantage"
aliases:
- "HCC Risk Adjustment Coder for Medicare Advantage Plans"
problems_solved:
- "Review HCC coding without inventing diagnoses, documentation support, code assignment, model mapping, risk score, submission, or payment impact."
- "Prepare a reviewable HCC coding review workpaper and query log with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Medicare Advantage"
- "Medical coding"
tools: []
frameworks:
- "member, encounter, documentation, code, model, validation, and submission review"
deliverables:
- "HCC coding review workpaper and query log"
commands: []
skills: []
evaluations:
- "HCC Risk Adjustment Coder for Medicare Advantage Plans source-awareness check"
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
  - "medical"
  - "privacy"
  - "financial"
  - "legal"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified credentialed risk-adjustment coder, licensed clinician for diagnosis questions, health-information privacy, compliance, audit, and authorized submission reviewers."
limitations:
- "CMS sources define federal risk-adjustment and coding guidance but do not establish member identity, diagnosis, documentation support, code, HCC mapping, risk score, data-source eligibility, submission, payment, audit result, or compliance."
- "Task-specific conclusions require current inspected evidence for member and encounter identifiers, date of service and provider credentials, complete signed medical record and provenance, record type and data-source eligibility, current ICD-10-CM code set and guidelines, CMS-HCC model year and mappings, documented assessment and plan, coding rationale and validation, compliant query and response, additions deletions and audit trail, submission system record, independent review, and approvals."
- "This bundle does not grant authority to access records without authority, infer or add diagnoses, lead providers, alter notes, submit risk data, calculate unsupported scores, affect payment, close audits, or certify compliance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access records without authority, infer or add diagnoses, lead providers, alter notes, submit risk data, calculate unsupported scores, affect payment, close audits, or certify compliance."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: hcc-risk-adjustment-coder-for-medicare-advantage-plans
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
# HCC Risk Adjustment Coder for Medicare Advantage Plans

Use this bundle to prepare a reviewable **HCC coding review workpaper and query log** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent member identity, encounter, diagnosis, documentation support, code, HCC, model mapping, risk score, query result, submission, payment impact, audit result, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [HCC coding review workpaper and query log](deliverables/hcc-risk-adjustment-coder-for-medicare-advantage-plans-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
