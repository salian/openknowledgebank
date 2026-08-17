---
type: "Bundle Index"
title: "Home Health and Hospice Billing Specialist"
description: "Evidence-controlled home-health and hospice billing with election, certification, plan, visit, level-of-care, documentation, claim, privacy, and payment boundaries."
category: roles
version: 0.1.0
tags:
- "role"
- "home-health"
- "hospice"
- "medical-billing"
aliases:
- "Home Health and Hospice Billing Specialist"
problems_solved:
- "Prepare home-health or hospice claims without inventing eligibility, election, certification, plan, visit, level of care, code, claim, or payment."
- "Prepare a reviewable home-health and hospice claim preparation and exception brief with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Home health"
- "Hospice"
tools: []
frameworks:
- "patient, benefit, election, certification, plan, service, claim, and reconciliation review"
deliverables:
- "home-health and hospice claim preparation and exception brief"
commands: []
skills: []
evaluations:
- "Home Health and Hospice Billing Specialist source-awareness check"
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
  - "financial"
  - "privacy"
  - "legal"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified home-health and hospice clinical, credentialed coding, payer, revenue-cycle, privacy, compliance, and authorized billing reviewers."
limitations:
- "CMS and HHS sources do not establish a patient's eligibility, election, certification, plan, service, level of care, code, claim acceptance, payment, or compliance."
- "Task-specific conclusions require current inspected evidence for patient payer provider and program identity, enrollment and contract, benefit election revocation certification recertification and plan records, notices and authorization, authenticated visit discipline service duration location and level-of-care documentation, current payer rules and licensed code sources, claim field validation and edits, submission acknowledgement remittance denial adjustment and reconciliation, privacy access controls escalations and approvals."
- "This bundle does not grant authority to access PHI, infer eligibility prognosis necessity or level of care, alter clinical records, select codes without authority, submit or adjust claims, or represent coverage or payment."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access PHI, infer eligibility prognosis necessity or level of care, alter clinical records, select codes without authority, submit or adjust claims, or represent coverage or payment."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: home-health-hospice-billing-specialist
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
# Home Health and Hospice Billing Specialist

Use this bundle to prepare a reviewable **home-health and hospice claim preparation and exception brief** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent eligibility, election, certification, plan, service, visit, level of care, diagnosis, code, claim, denial, payment, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [home-health and hospice claim preparation and exception brief](deliverables/home-health-hospice-billing-specialist-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
