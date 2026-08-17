---
type: "Bundle Index"
title: "Insurance Eligibility and Benefits Verification Specialist"
description: "Evidence-controlled health-plan eligibility and benefit verification with identity, payer, provider, service, authorization, estimate, privacy, and no-guarantee boundaries."
category: roles
version: 0.1.0
tags:
- "role"
- "insurance-verification"
- "eligibility"
- "medical-billing"
aliases:
- "Insurance Eligibility and Benefits Verification Specialist"
problems_solved:
- "Verify benefits without inventing patient identity, active coverage, provider status, authorization, limits, accumulator, patient responsibility, payment, or guarantee."
- "Prepare a reviewable eligibility and benefits verification record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Healthcare"
- "Health insurance"
tools: []
frameworks:
- "patient, plan, provider, service, transaction, response, estimate, and handoff review"
deliverables:
- "eligibility and benefits verification record"
commands: []
skills: []
evaluations:
- "Insurance Eligibility and Benefits Verification Specialist source-awareness check"
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
    required_qualification: "Authorized eligibility and payer-operations reviewer plus clinical, revenue-cycle, privacy, compliance, and patient-financial reviewers."
limitations:
- "Transaction and privacy sources do not establish a patient's current coverage, provider network status, authorization, benefit applicability, accumulator accuracy, patient responsibility, claim payment, or guarantee."
- "Task-specific conclusions require current inspected evidence for request and access authority, patient and subscriber identifiers, payer plan group and effective dates, provider and facility identifiers, proposed service date place and description, inquiry and response payload or portal record, call reference and representative, network authorization referral limit exclusion and accumulator responses, estimate assumptions, discrepancy follow-up, privacy access and credential controls, timestamp and handoff approval."
- "This bundle does not grant authority to access PHI or portals without authority, alter patient or plan data, promise coverage or payment, infer authorization, quote final responsibility, schedule or cancel care, or represent guarantee."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access PHI or portals without authority, alter patient or plan data, promise coverage or payment, infer authorization, quote final responsibility, schedule or cancel care, or represent guarantee."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: insurance-eligibility-benefits-verification-specialist
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
# Insurance Eligibility and Benefits Verification Specialist

Use this bundle to prepare a reviewable **eligibility and benefits verification record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent patient identity, eligibility, active coverage, network status, authorization, benefit, limit, accumulator, patient responsibility, medical necessity, payment, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [eligibility and benefits verification record](deliverables/insurance-eligibility-benefits-verification-specialist-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
