---
type: "Bundle Index"
title: "Prior Authorization Specialist for Specialty Infusion and Oncology"
description: "Evidence-controlled specialty authorization with patient, payer, plan, drug and service, diagnosis support, policy, site, urgency, submission, decision, appeal, and clinical boundaries."
category: roles
version: 0.1.0
tags:
- "role"
- "prior-authorization"
- "infusion"
- "oncology"
aliases:
- "Prior Authorization Specialist for Specialty Infusion and Oncology"
problems_solved:
- "Coordinate authorization without inventing diagnosis, treatment, urgency, coverage, criteria, documentation, approval, scheduling readiness, payment, or outcome."
- "Prepare a reviewable specialty prior-authorization evidence and status record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Oncology"
- "Specialty infusion"
tools: []
frameworks:
- "authority, patient, plan, service, policy, clinical support, urgency, submission, and decision review"
deliverables:
- "specialty prior-authorization evidence and status record"
commands: []
skills: []
evaluations:
- "Prior Authorization Specialist for Specialty Infusion and Oncology source-awareness check"
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
  - "safety"
  - "regulatory"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified oncology or infusion clinician, payer authorization and benefits, pharmacy where applicable, patient privacy, scheduling safety, revenue-cycle, and appeal reviewers."
limitations:
- "CMS and HHS sources do not establish a patient's diagnosis, treatment, urgency, coverage criteria, documentation sufficiency, authorization, scheduling readiness, payment, or outcome."
- "Task-specific conclusions require current inspected evidence for organization and specialist authority, patient payer plan and benefit identifiers, provider enrollment and site, authenticated order with drug dose route frequency and dates, diagnosis and clinical-record support, current payer policy criteria and channel, prior treatment and test records as documented, clinician urgency and appeal decisions, consent and PHI controls, submission attachments timestamps requests decision reason and validity period, scheduling and billing handoffs, and approvals."
- "This bundle does not grant authority to diagnose, select or change treatment, invent urgency or clinical support, expose PHI, submit or appeal without authority, represent authorization as coverage or payment, schedule unsafe care, or promise outcomes."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to diagnose, select or change treatment, invent urgency or clinical support, expose PHI, submit or appeal without authority, represent authorization as coverage or payment, schedule unsafe care, or promise outcomes."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: prior-authorization-specialist-for-specialty-infusion-oncology
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
# Prior Authorization Specialist for Specialty Infusion and Oncology

Use this bundle to prepare a reviewable **specialty prior-authorization evidence and status record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent diagnosis, treatment, dose, urgency, criterion, documentation sufficiency, authorization, coverage, scheduling readiness, payment, clinical outcome, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [specialty prior-authorization evidence and status record](deliverables/prior-authorization-specialist-for-specialty-infusion-oncology-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
