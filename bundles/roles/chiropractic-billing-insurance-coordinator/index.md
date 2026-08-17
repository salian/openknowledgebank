---
type: "Bundle Index"
title: "Chiropractic Billing and Insurance Coordinator"
description: "Evidence-controlled chiropractic eligibility, documentation, coding, claims, denials, patient balances, privacy, and collection coordination."
category: roles
version: 0.1.0
tags:
- "role"
- "chiropractic"
- "medical-billing"
- "insurance"
aliases:
- "Chiropractic Billing and Insurance Coordinator"
problems_solved:
- "Coordinate chiropractic billing without inventing coverage, diagnosis, treatment, necessity, code, patient responsibility, claim, denial, or payment."
- "Prepare a reviewable chiropractic billing and insurance coordination record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Chiropractic care"
- "Medical billing"
tools: []
frameworks:
- "patient, benefit, provider, encounter, documentation, claim, remittance, and balance review"
deliverables:
- "chiropractic billing and insurance coordination record"
commands: []
skills: []
evaluations:
- "Chiropractic Billing and Insurance Coordinator source-awareness check"
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
    required_qualification: "Licensed chiropractor or clinical reviewer, credentialed coder, payer and revenue-cycle owner, privacy and compliance reviewer, and authorized biller."
limitations:
- "CMS and HHS sources do not establish local benefits, diagnosis, treatment, medical necessity, code, claim acceptance, patient liability, payment, or compliance."
- "Task-specific conclusions require current inspected evidence for patient plan and provider identity, eligibility benefit referral authorization and limitation responses, enrollment contract and payer rules, authenticated encounter treatment and order records, licensed code and edit sources, claim validation submission and acknowledgement, remittance denial appeal adjustment and balance records, estimate notices payment plan and communication authority, privacy access controls, reconciliations and approvals."
- "This bundle does not grant authority to access PHI, infer diagnosis or necessity, select codes without authority, promise coverage, submit or alter claims, collect balances, waive amounts, or represent payment."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to access PHI, infer diagnosis or necessity, select codes without authority, promise coverage, submit or alter claims, collect balances, waive amounts, or represent payment."
timestamp: "2026-08-16T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: chiropractic-billing-insurance-coordinator
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
# Chiropractic Billing and Insurance Coordinator

Use this bundle to prepare a reviewable **chiropractic billing and insurance coordination record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent eligibility, benefit, authorization, diagnosis, treatment, necessity, code, coverage, patient responsibility, claim, denial, payment, or approval.

## Start Here

- [Overview](overview.md)
- [Role guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [chiropractic billing and insurance coordination record](deliverables/chiropractic-billing-insurance-coordinator-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
