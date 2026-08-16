---
type: "Bundle Index"
title: "Radiology Coding and Billing Specialist"
description: "Evidence-controlled radiology coding and billing with order, report, supervision, professional and technical component, code, edit, privacy, claim, and payment boundaries."
category: roles
version: 0.1.0
tags:
- "role"
- "radiology"
- "medical-coding"
- "medical-billing"
aliases:
- "Radiology Coding and Billing Specialist"
problems_solved:
- "Code radiology services without inventing orders, interpretations, supervision, components, modifiers, necessity, claim status, or payment."
- "Prepare a reviewable radiology coding and billing review workpaper with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Radiology"
- "Medical billing"
tools: []
frameworks:
- "patient, order, service, report, component, code, edit, claim, and reconciliation review"
deliverables:
- "radiology coding and billing review workpaper"
commands: []
skills: []
evaluations:
- "Radiology Coding and Billing Specialist source-awareness check"
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
    required_qualification: "Qualified radiologist or clinical reviewer, credentialed radiology coder, payer and revenue-cycle owner, privacy, compliance, and authorized biller."
limitations:
- "CMS and HHS sources do not establish a local order, performed study, interpretation, supervision, component, code, modifier, medical necessity, claim acceptance, payment, or compliance."
- "Task-specific conclusions require current inspected evidence for patient payer provider facility and equipment identity, eligibility authorization and order, authenticated protocol performed-study contrast supply and interpretation records, supervision and credential evidence, professional technical and facility responsibility, current payer policy licensed code sets fee schedule and NCCI sources, claim field edit and modifier validation, submission acknowledgement remittance denial adjustment reconciliation, privacy controls and approvals."
- "This bundle does not grant authority to access images or PHI, infer findings or necessity, create orders or reports, select codes without authority, alter documentation, submit or adjust claims, or represent payment."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access images or PHI, infer findings or necessity, create orders or reports, select codes without authority, alter documentation, submit or adjust claims, or represent payment."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: radiology-coding-billing-specialist
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
# Radiology Coding and Billing Specialist

Use this bundle to prepare a reviewable **radiology coding and billing review workpaper** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent order, performed study, finding, interpretation, supervision, component, code, modifier, necessity, claim, denial, payment, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [radiology coding and billing review workpaper](deliverables/radiology-coding-billing-specialist-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
