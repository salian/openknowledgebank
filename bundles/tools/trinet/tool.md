---
type: "Tool Guide"
title: "TriNet"
description: "Source-aware guidance for TriNet."
resource: "https://www.trinet.com/products"
okb_bundle_id: trinet
timestamp: "2026-08-14T00:00:00Z"
tool_category: "PEO, HR, payroll, tax, benefits, time, expense, compliance-support, and employee platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or change employee, compensation, payroll, tax, benefit, time or expense data, hire or terminate workers, run payroll, initiate payments, change benefits, or make employment, classification, eligibility, tax, compliance, or legal decisions"
---
# TriNet Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.trinet.com/products
- https://www.trinet.com/products/hr-platform

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable TriNet payroll, benefits, and PEO control review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or change employee, compensation, payroll, tax, benefit, time or expense data, hire or terminate workers, run payroll, initiate payments, change benefits, or make employment, classification, eligibility, tax, compliance, or legal decisions.

## Guardrails

- Do not invent worker identity or classification, employment relationship, compensation, hours, payroll calculation, tax filing, benefit eligibility or coverage, payment, HR advice, compliance, legal conclusion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
