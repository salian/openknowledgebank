---
type: "Tool Guide"
title: "Procore"
description: "Source-aware guidance for Procore."
resource: "https://developers.procore.com/"
okb_bundle_id: procore
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Construction project, financial, quality, safety, workforce, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter project records, contracts, budgets, commitments, changes, invoices, inspections, incidents or timecards, share plans, authorize APIs, approve payments, or represent safety, schedule, cost, quality, contractual, or completion state"
---
# Procore Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developers.procore.com/
- https://support.procore.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Procore project, financial, and control review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter project records, contracts, budgets, commitments, changes, invoices, inspections, incidents or timecards, share plans, authorize APIs, approve payments, or represent safety, schedule, cost, quality, contractual, or completion state.

## Guardrails

- Do not invent project or company identity, drawing revision, RFI or submittal status, contract interpretation, budget, cost, change entitlement, invoice, payment, schedule, inspection, safety conclusion, completion, API result, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
