---
type: "Tool Guide"
title: "RealPage"
description: "Source-aware guidance for RealPage."
resource: "https://www.realpage.com/products/"
okb_bundle_id: realpage
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Property management, leasing, resident, finance, revenue, and analytics platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or change applicant, resident, lease, unit, rent, payment, screening, pricing, maintenance or accounting data, collect funds, change access, or make housing, eligibility, pricing, payment, or compliance decisions"
---
# RealPage Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.realpage.com/products/
- https://www.realpage.com/support/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable RealPage property, resident, and financial-control review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or change applicant, resident, lease, unit, rent, payment, screening, pricing, maintenance or accounting data, collect funds, change access, or make housing, eligibility, pricing, payment, or compliance decisions.

## Guardrails

- Do not invent applicant or resident identity, screening result, eligibility, lease interpretation, rent or pricing recommendation, occupancy, payment, ledger balance, maintenance completion, fair-housing compliance, accounting, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
