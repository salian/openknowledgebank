---
type: "Bundle Index"
title: "Purchase Order"
description: "Evidence-controlled purchase order draft with parties, authority, line items, terms, taxes, approvals, and commitment boundaries."
category: deliverables
version: 0.1.0
tags:
- "deliverable"
- "procurement"
- "purchase-order"
aliases:
- "Purchase Order"
problems_solved:
- "Prepare a purchase order without inventing supplier identity, authority, scope, price, tax, terms, funding, acceptance, or commitment."
- "Prepare a reviewable purchase order draft and approval record with explicit evidence, limitations, validation, and approval boundaries."
industries:
- "Procurement"
- "Finance"
tools: []
frameworks:
- "party, authority, item, price, term, approval, and issuance review"
deliverables:
- "purchase order draft and approval record"
commands: []
skills: []
evaluations:
- "Purchase Order source-awareness check"
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
  - "financial"
  - "legal"
  - "accounting"
  - "privacy"
  professional_review:
    status: not_reviewed
    required_qualification: "Authorized procurement, budget, accounting, tax, legal, privacy, security, and contract reviewers for the transaction and jurisdiction."
limitations:
- "The FAR provisions govern United States federal simplified acquisitions and do not establish another buyer's authority, supplier identity, commercial terms, tax treatment, funding, approval, contract formation, or local legal effect."
- "Task-specific conclusions require current inspected evidence for buyer and supplier legal records, delegated purchasing authority, approved requisition and budget, quote and sourcing record, governing agreement and terms, item specifications and quantities, delivery and acceptance rules, prices and currency, tax and freight basis, accounting codes, privacy and security review, calculations, approvals, and issuance record."
- "This bundle does not grant authority to create a binding order, select a supplier, commit funds, alter terms or prices, calculate unsupported tax, sign, transmit, approve, receive, or represent acceptance."
safety_notes:
- "Minimize personal, customer, employee, financial, credential, security, privileged, medical, and unreleased information."
- "Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state."
- "Require explicit confirmation from an evidenced authorized reviewer before taking any action to create a binding order, select a supplier, commit funds, alter terms or prices, calculate unsupported tax, sign, transmit, approve, receive, or represent acceptance."
timestamp: "2026-08-15T00:00:00Z"
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: purchase-order
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
# Purchase Order

Use this bundle to prepare a reviewable **purchase order draft and approval record** without inventing local facts, qualifications, records, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent party identity, purchasing authority, supplier selection, item or quantity, price, tax, funding, term, delivery, acceptance, signature, contract formation, or approval.

## Start Here

- [Overview](overview.md)
- [Deliverable guide](deliverable.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [purchase order draft and approval record](deliverables/purchase-order-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
