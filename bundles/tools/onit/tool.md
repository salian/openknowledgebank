---
type: "Tool Guide"
title: "Onit"
description: "Source-aware guidance for Onit."
resource: "https://www.onit.com/products/"
okb_bundle_id: onit
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise legal management, matter, spend, workflow, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter matters, budgets, invoices, billing rules, vendors or contracts, approve spend, enable AI agents, export privileged data, change access, or represent legal, invoice, savings, compliance, or payment conclusions"
---
# Onit Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.onit.com/products/
- https://www.onit.com/news/onit-changes-the-game/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Onit legal matter, spend, and AI review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter matters, budgets, invoices, billing rules, vendors or contracts, approve spend, enable AI agents, export privileged data, change access, or represent legal, invoice, savings, compliance, or payment conclusions.

## Guardrails

- Do not invent matter identity, privilege, invoice accuracy, billing-rule application, budget, savings, contract state, AI finding, legal conclusion, payment authorization, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
