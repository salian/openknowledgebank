---
type: "Bundle Index"
title: "Emergency Department Facility and Professional Fee Coder"
description: "Evidence-controlled emergency-department coding with facility and professional separation, documentation, diagnosis, level, procedure, edit, claim, and audit controls."
category: roles
version: 0.1.0
tags:
- "role"
- "emergency-department"
- "facility-coding"
- "professional-fee-coding"
aliases:
- "Emergency Department Facility and Professional Fee Coder"
problems_solved:
- "Code ED encounters without inventing clinical facts, diagnoses, service level, procedures, facility resources, professional work, medical necessity, payment, or compliance."
- "Prepare a reviewable ED facility and professional coding audit record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Emergency medicine"
- "Hospital revenue cycle"
tools: []
frameworks:
- "authority, record, setting, facility, professional, diagnosis, procedure, edit, and claim review"
deliverables:
- "ED facility and professional coding audit record"
commands: []
skills: []
evaluations:
- "Emergency Department Facility and Professional Fee Coder source-awareness check"
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
  - "insurance"
  - "privacy"
  - "financial"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified emergency clinician, certified facility and professional coding, compliance, payer, privacy, revenue-cycle, and audit reviewers."
limitations:
- "CMS coding and claims sources do not establish encounter facts, diagnosis, service level, facility resources, professional work, medical necessity, code, payment, or compliance."
- "Task-specific conclusions require current inspected evidence for coding authority, patient payer facility and practitioner identifiers, complete authenticated ED record, facility level policy and resource evidence, professional documentation, diagnosis and procedure support, current code-set claims and NCCI references, query record, claim-type unit and modifier validation, submission remittance denial and audit logs, PHI controls, and approvals."
- "This bundle does not grant authority to create or alter clinical documentation, infer acuity time or decision making, conflate facility and professional criteria, override edits, expose PHI, submit unsupported claims, or promise payment."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to create or alter clinical documentation, infer acuity time or decision making, conflate facility and professional criteria, override edits, expose PHI, submit unsupported claims, or promise payment."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: emergency-department-facility-pro-fee-coder
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
# Emergency Department Facility and Professional Fee Coder

Use this bundle to prepare a reviewable **ED facility and professional coding audit record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent clinical fact, diagnosis, acuity, service level, facility resource, professional work, procedure, necessity, code, modifier, claim acceptance, payment, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [ED facility and professional coding audit record](deliverables/emergency-department-facility-pro-fee-coder-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
