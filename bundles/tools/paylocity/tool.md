---
type: "Tool Guide"
title: "Paylocity"
description: "Source-aware guidance for Paylocity."
resource: "https://www.paylocity.com/products/"
okb_bundle_id: paylocity
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Payroll, HR, workforce, talent, engagement, and integration platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or change employee, candidate, pay, tax, time, benefit or performance data, run or approve payroll, schedule workers, reimburse expenses, call APIs, change access, or make employment, eligibility, payment, or compliance decisions"
---
# Paylocity Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.paylocity.com/products/
- https://developer.paylocity.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Paylocity payroll, HR, and integration review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or change employee, candidate, pay, tax, time, benefit or performance data, run or approve payroll, schedule workers, reimburse expenses, call APIs, change access, or make employment, eligibility, payment, or compliance decisions.

## Guardrails

- Do not invent person identity, employment or candidate status, compensation, hours, tax withholding, payroll calculation, benefit eligibility, performance, reimbursement, API result, payment, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
