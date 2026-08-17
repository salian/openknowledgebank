---
type: "Bundle Index"
title: "Ambulance and EMS Billing and Coding Specialist"
description: "Evidence-controlled ambulance billing with dispatch, transport, crew, origin, destination, mileage, level, necessity, signature, payer, claim, and appeal boundaries."
category: roles
version: 0.1.0
tags:
- "role"
- "ambulance"
- "ems"
- "medical-billing"
aliases:
- "Ambulance and EMS Billing and Coding Specialist"
problems_solved:
- "Prepare ambulance claims without inventing dispatch, transport, crew, origin, destination, mileage, service level, medical necessity, signature, payment, or compliance."
- "Prepare a reviewable ambulance claim evidence and exception record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Emergency medical services"
- "Healthcare revenue cycle"
tools: []
frameworks:
- "authority, dispatch, transport, crew, route, mileage, level, necessity, claim, and denial review"
deliverables:
- "ambulance claim evidence and exception record"
commands: []
skills: []
evaluations:
- "Ambulance and EMS Billing and Coding Specialist source-awareness check"
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
  - "safety"
  professional_review:
    status: not_reviewed
    required_qualification: "Qualified EMS clinical, certified ambulance coding and billing, payer policy, patient privacy, revenue-cycle, and authorized claim reviewers."
limitations:
- "CMS and HHS sources do not establish dispatch or transport facts, mileage, service level, medical necessity, signature validity, coverage, code, payment, or compliance."
- "Task-specific conclusions require current inspected evidence for billing authority, patient payer supplier vehicle and crew identifiers, dispatch and patient-care records, pickup destination and facility evidence, odometer route loaded-mileage and transport status, service level supplies and clinical support, signatures and exceptions, current payer code modifier fee and coverage sources, claim validation submission remittance denial and appeal logs, PHI and location controls, and approvals."
- "This bundle does not grant authority to create clinical or transport records, infer mileage or level, alter signatures, override coverage edits, expose PHI or location, submit or appeal without authority, post unsupported adjustments, or promise payment."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to create clinical or transport records, infer mileage or level, alter signatures, override coverage edits, expose PHI or location, submit or appeal without authority, post unsupported adjustments, or promise payment."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: ambulance-ems-billing-coding-specialist
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
# Ambulance and EMS Billing and Coding Specialist

Use this bundle to prepare a reviewable **ambulance claim evidence and exception record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent dispatch, transport, crew, origin, destination, mileage, service level, medical necessity, signature, coverage, code, claim acceptance, payment, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [ambulance claim evidence and exception record](deliverables/ambulance-ems-billing-coding-specialist-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
