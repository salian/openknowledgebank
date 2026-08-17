---
type: "Bundle Index"
title: "Dental Insurance Billing and Verification Coordinator"
description: "Evidence-controlled dental benefits and billing coordination with patient, payer, plan, eligibility, benefit estimate, documentation, code set, claim, remittance, and no-payment-guarantee boundaries."
category: roles
version: 0.1.0
tags:
- "role"
- "dental-billing"
- "insurance-verification"
- "revenue-cycle"
aliases:
- "Dental Insurance Billing and Verification Coordinator"
problems_solved:
- "Verify dental benefits and bill claims without inventing eligibility, benefits, clinical services, codes, documentation, patient cost, payment, or compliance."
- "Prepare a reviewable dental benefit verification and claim evidence record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Dental care"
- "Healthcare revenue cycle"
tools: []
frameworks:
- "authority, patient, plan, eligibility, benefit, service, code, claim, and remittance review"
deliverables:
- "dental benefit verification and claim evidence record"
commands: []
skills: []
evaluations:
- "Dental Insurance Billing and Verification Coordinator source-awareness check"
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
    required_qualification: "Licensed dental and qualified dental coding and billing, payer benefits, patient privacy, financial, revenue-cycle, and authorized claim reviewers."
limitations:
- "HHS transaction, code-set and security guidance does not establish eligibility, benefit availability, clinical service, documentation sufficiency, code, patient cost, claim acceptance, payment, or compliance."
- "Task-specific conclusions require current inspected evidence for practice coordinator and billing authority, patient payer plan group and provider identifiers, date-stamped eligibility and benefit response with limitations frequency deductible maximum waiting and coordination data, approved patient estimate disclaimer, authenticated treatment and service record, tooth surface image narrative and authorization support, current licensed dental code-set and payer rules, claim attachments submission remittance denial and appeal logs, PHI and financial controls, and approvals."
- "This bundle does not grant authority to diagnose or alter treatment records, guarantee benefits or patient cost, copy protected code descriptors improperly, invent tooth or surface facts, expose PHI, submit claims, post unsupported adjustments, or promise payment."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to diagnose or alter treatment records, guarantee benefits or patient cost, copy protected code descriptors improperly, invent tooth or surface facts, expose PHI, submit claims, post unsupported adjustments, or promise payment."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: dental-insurance-billing-verification-coordinator
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
# Dental Insurance Billing and Verification Coordinator

Use this bundle to prepare a reviewable **dental benefit verification and claim evidence record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent eligibility, benefit, limitation, clinical service, tooth or surface, documentation sufficiency, code, patient cost, claim acceptance, payment, compliance, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [dental benefit verification and claim evidence record](deliverables/dental-insurance-billing-verification-coordinator-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
