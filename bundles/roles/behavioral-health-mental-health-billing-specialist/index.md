---
type: "Bundle Index"
title: "Behavioral Health and Mental Health Billing Specialist"
description: "Evidence-controlled behavioral-health billing with benefit, provider, service, documentation, coding, privacy, claim, denial, and payment boundaries."
category: roles
version: 0.1.0
tags:
- "role"
- "behavioral-health"
- "medical-billing"
- "revenue-cycle"
aliases:
- "Behavioral Health and Mental Health Billing Specialist"
problems_solved:
- "Prepare behavioral-health claims without inventing coverage, diagnosis, service, documentation, code, authorization, submission, denial, or payment."
- "Prepare a reviewable behavioral-health claim preparation and exception brief with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Behavioral healthcare"
- "Medical billing"
tools: []
frameworks:
- "patient, payer, provider, service, documentation, code, claim, and reconciliation review"
deliverables:
- "behavioral-health claim preparation and exception brief"
commands: []
skills: []
evaluations:
- "Behavioral Health and Mental Health Billing Specialist source-awareness check"
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
  - "financial"
  - "privacy"
  - "legal"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified behavioral-health clinician, credentialed coder, payer and revenue-cycle owner, privacy and compliance reviewer, and authorized biller."
limitations:
- "CMS and HHS sources do not establish a patient's coverage, diagnosis, service, documentation sufficiency, code, authorization, claim acceptance, payment, or compliance."
- "Task-specific conclusions require current inspected evidence for patient payer and provider identifiers, eligibility benefits and authorization response, enrollment and contract, authenticated encounter and service record, date place duration and rendering provider, current payer policy and licensed code-set access, claim field and edit validation, privacy access and disclosure controls, submission acknowledgement remittance denial adjustment and reconciliation records, escalations and approvals."
- "This bundle does not grant authority to access records, infer diagnoses or medical necessity, select codes without authority, alter documentation, submit or adjust claims, contact patients or payers, post payment, or represent coverage or reimbursement."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access records, infer diagnoses or medical necessity, select codes without authority, alter documentation, submit or adjust claims, contact patients or payers, post payment, or represent coverage or reimbursement."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: behavioral-health-mental-health-billing-specialist
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
# Behavioral Health and Mental Health Billing Specialist

Use this bundle to prepare a reviewable **behavioral-health claim preparation and exception brief** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent patient identity, eligibility, benefit, authorization, diagnosis, service, documentation sufficiency, code, claim status, denial cause, payment, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [behavioral-health claim preparation and exception brief](deliverables/behavioral-health-mental-health-billing-specialist-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
