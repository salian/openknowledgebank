---
type: "Tool Guide"
title: "Melio"
description: "Source-aware guidance for Melio."
resource: "https://meliopayments.com/"
okb_bundle_id: melio
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Business accounts-payable, receivable, and payment platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect bank or card accounts, create vendors, schedule, approve, cancel or dispute payments, request funds, change accounting data, grant access, or represent payment, settlement, fee, tax, or compliance state"
---
# Melio Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://meliopayments.com/
- https://help.melio.com/hc/en-us

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Melio payment authorization and reconciliation review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect bank or card accounts, create vendors, schedule, approve, cancel or dispute payments, request funds, change accounting data, grant access, or represent payment, settlement, fee, tax, or compliance state.

## Guardrails

- Do not invent business or vendor identity, bank ownership, account balance, invoice validity, payment authorization, delivery, settlement, fee, exchange rate, accounting classification, tax treatment, fraud status, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
