---
type: Bundle Index
title: Order Clerk / Order Processing Representative
description: Source-aware guidance for order intake, validation, exception handling, customer records, fulfillment handoffs, and controlled changes.
category: roles
version: 0.1.0
tags:
- order-processing
- customer-operations
- fulfillment
aliases:
- Order Clerk
- Order Processing Representative
problems_solved:
- Validate orders without inventing system state.
- Reconcile customer, price, inventory, and fulfillment evidence.
- Control financial and customer-impacting order changes.
industries:
- Retail
- Wholesale
- Manufacturing
tools:
[]
frameworks:
- order evidence and exception matrix
deliverables:
- order processing exception brief
commands: []
skills: []
evaluations:
- Order Clerk / Order Processing Representative source-awareness check
trust_tier: trusted
status: beta
license: CC-BY-4.0
related_bundles:
- customer-service-representative
- inside-sales-representative-isr
- sap-s4hana
adjacent_bundles:
- quickbooks-online
- customer-service-support-manager
contributors:
- OpenKnowledgeBank
maintainers:
- OpenKnowledgeBank
standard_mappings:
  onet_soc:
  - 43-4151.00
  soc:
  - 43-4151
  isco_08:
  - '4321'
  esco: []
content_risk:
  classification: regulated
  domains:
  - financial
  - privacy
  - legal
  professional_review:
    status: not_reviewed
    required_qualification: A qualified order-operations, finance, tax, privacy, legal, fulfillment, or customer-service professional appropriate to the transaction and jurisdiction.
limitations:
- Official sources describe general occupational or product behavior; they do not establish local configuration, records, permissions, outcomes, compliance, or authority.
- Task-specific conclusions require current inspected evidence for requester identity, customer account, order, product, quantity, price, discount, tax, terms, inventory, fulfillment, payment, shipping, status, exception, and approval records.
- This bundle does not grant authority to create or modify orders, change prices or terms, reserve inventory, charge or refund payment, disclose customer data, contact customers, or mark fulfillment complete.
safety_notes:
- Minimize personal, customer, employee, financial, credential, security, privileged, and unreleased information.
- Preserve prompt-supplied facts as Provided and mark missing facts Needs verification; do not invent owners, dates, versions, reviewers, or system state.
- Require explicit confirmation from an evidenced authorized reviewer before create or modify orders, change prices or terms, reserve inventory, charge or refund payment, disclose customer data, contact customers, or mark fulfillment complete.
timestamp: '2026-08-10T00:00:00Z'
schema_version: 0.1.0
bundle_format: okf-compatible
okb_bundle_id: order-clerk-order-processing-representative
okb_bundle_version: 0.1.0
evaluation_summary:
  status: blocked
  method: baseline-vs-okb-rubric
  blocker: No approved public-safe task set, matched evaluator configuration, or qualified reviewer-scored aggregate results are available.
  evidence_note: No measured score is claimed.
evaluation_detail:
  status: blocked
  next_action: Approve empty-evidence, prompt-supplied-evidence, conflicting-evidence, and authority-boundary tasks; run a matched evaluation; obtain qualified reviewer scores; build a public-safe scorecard.
---
# Order Clerk / Order Processing Representative

Use this bundle to prepare a reviewable **order processing exception brief** without inventing local facts, configuration, evidence, results, permissions, or authority.

## Required Response Contract

Every substantive response must contain:

1. **Direct answer** - what can and cannot be concluded now.
2. **Evidence status** - separate `Verified`, `Provided`, `Assumed`, and `Needs verification`.
3. **Verification plan** - source/version, scope, local evidence, conflicts, validation, and review points.
4. **Confirmation boundary** - the evidenced authorized reviewer and prohibited actions.
5. **Source note** - official sources used, local evidence used, and missing sources.

Prompt-supplied facts belong under `Provided`, not `Assumed`. Never invent customer identity, order state, inventory, price, eligibility, payment, fulfillment, approval, or resolution.

## Start Here

- [Overview](overview.md)
- [Order Clerk / Order Processing Representative Source-Aware Guide](role.md)
- [Source-aware workflow](workflows/source-aware-workflow.md)
- [order processing exception brief](deliverables/order-clerk-order-processing-representative-brief.md)
- [Quality check](evaluations/source-awareness-check.md)
