---
type: "Tool Guide"
title: "Microsoft Dynamics 365 Finance, Supply Chain Management, and Business Central"
description: "Source-aware guidance for Microsoft Dynamics 365 Finance, Supply Chain Management, and Business Central."
resource: "https://learn.microsoft.com/en-us/dynamics365/finance/"
okb_bundle_id: microsoft-dynamics-365
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Enterprise finance, supply-chain, and business-management ERP platforms"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "post or reverse transactions, change ledgers, tax, inventory, vendors, customers or master data, approve purchases or payments, deploy extensions, change access, migrate data, or represent financial, inventory, tax, operational, or compliance state"
---
# Microsoft Dynamics 365 Finance, Supply Chain Management, and Business Central Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://learn.microsoft.com/en-us/dynamics365/finance/
- https://learn.microsoft.com/en-us/dynamics365/supply-chain/
- https://learn.microsoft.com/en-us/dynamics365/business-central/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Dynamics 365 ERP scope, control, and implementation review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before post or reverse transactions, change ledgers, tax, inventory, vendors, customers or master data, approve purchases or payments, deploy extensions, change access, migrate data, or represent financial, inventory, tax, operational, or compliance state.

## Guardrails

- Do not invent product applicability, company or environment state, account mapping, posting, balance, tax treatment, inventory, costing, approval, segregation of duties, integration, migration, close, compliance, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
