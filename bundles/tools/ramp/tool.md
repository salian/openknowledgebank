---
type: "Tool Guide"
title: "Ramp"
description: "Source-aware guidance for Ramp."
resource: "https://support.ramp.com/"
okb_bundle_id: ramp
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Corporate card, spend, travel, accounts-payable, and finance automation platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "issue or change cards, limits or spend policies, submit or approve expenses, connect banks or accounting systems, pay bills, move funds, create vendors, expose API credentials, or represent transaction, balance, savings, accounting, tax, payment, or compliance state"
---
# Ramp Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://support.ramp.com/
- https://docs.ramp.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Ramp spend, payment, and accounting-control review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before issue or change cards, limits or spend policies, submit or approve expenses, connect banks or accounting systems, pay bills, move funds, create vendors, expose API credentials, or represent transaction, balance, savings, accounting, tax, payment, or compliance state.

## Guardrails

- Do not invent business or user identity, card or bank ownership, transaction legitimacy, receipt, expense classification, approval, account balance, savings, accounting treatment, tax treatment, payment, fraud status, compliance, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
