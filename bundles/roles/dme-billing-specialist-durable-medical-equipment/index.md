---
type: "Bundle Index"
title: "DME Billing Specialist for Durable Medical Equipment"
description: "Evidence-controlled DMEPOS billing with supplier, order, item, proof of delivery, coverage, code, modifier, authorization, claim, recertification, and appeal controls."
category: roles
version: 0.1.0
tags:
- "role"
- "dmepos"
- "durable-medical-equipment"
- "medical-billing"
aliases:
- "DME Billing Specialist for Durable Medical Equipment"
problems_solved:
- "Bill DMEPOS without inventing orders, item identity, delivery, continued need, coverage, coding, modifiers, authorization, payment, or compliance."
- "Prepare a reviewable DMEPOS claim and proof-of-delivery evidence record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Durable medical equipment"
- "Healthcare revenue cycle"
tools: []
frameworks:
- "supplier, beneficiary, order, item, delivery, coverage, code, claim, and continuation review"
deliverables:
- "DMEPOS claim and proof-of-delivery evidence record"
commands: []
skills: []
evaluations:
- "DME Billing Specialist for Durable Medical Equipment source-awareness check"
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
    required_qualification: "Qualified DMEPOS supplier compliance, certified coding and billing, payer and jurisdiction policy, clinical documentation, privacy, and authorized claim reviewers."
limitations:
- "CMS and HHS sources do not establish supplier status, valid order, item identity, delivery, continued need, coverage, code, authorization, payment, or compliance."
- "Task-specific conclusions require current inspected evidence for supplier enrollment accreditation location and billing authority, beneficiary payer and jurisdiction, treating-practitioner order and medical-record support, item HCPCS make model serial quantity and modifier, rental purchase repair and supply status, proof of delivery and pickup, prior authorization and coverage references, current fee and claim rules, recertification and continued-need records, claim validation remittance denial and appeal logs, PHI controls, and approvals."
- "This bundle does not grant authority to create orders or delivery records, substitute items or codes, infer continued need, alter signatures, override authorization or coverage edits, expose PHI, submit claims, or promise payment."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to create orders or delivery records, substitute items or codes, infer continued need, alter signatures, override authorization or coverage edits, expose PHI, submit claims, or promise payment."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: dme-billing-specialist-durable-medical-equipment
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
# DME Billing Specialist for Durable Medical Equipment

Use this bundle to prepare a reviewable **DMEPOS claim and proof-of-delivery evidence record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent supplier status, order, item identity, quantity, delivery, continued need, coverage, code, modifier, authorization, claim acceptance, payment, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [DMEPOS claim and proof-of-delivery evidence record](deliverables/dme-billing-specialist-durable-medical-equipment-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
