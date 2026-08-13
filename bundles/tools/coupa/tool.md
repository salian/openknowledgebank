---
type: "Tool Guide"
title: "Coupa"
description: "Source-aware guidance for Coupa."
resource: "https://www.coupa.com/"
okb_bundle_id: coupa
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Business spend management platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "onboard suppliers, change bank details, create or approve requisitions, purchase orders, invoices or expenses, initiate payments, alter controls, export financial data, or represent settlement or compliance"
---
# Coupa Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.coupa.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Coupa configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before onboard suppliers, change bank details, create or approve requisitions, purchase orders, invoices or expenses, initiate payments, alter controls, export financial data, or represent settlement or compliance.

## Guardrails

- Do not invent supplier identity, bank details, contract terms, account coding, invoice validity, approval authority, payment status, savings, compliance, reconciliation, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
