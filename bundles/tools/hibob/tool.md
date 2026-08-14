---
type: "Tool Guide"
title: "Bob by HiBob"
description: "Source-aware guidance for Bob by HiBob."
resource: "https://www.hibob.com/platform/"
okb_bundle_id: hibob
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Human capital management, payroll, talent, and workforce planning platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter worker records, hire or terminate, change compensation, time, leave, benefits or payroll, issue documents, run reviews, export data, or represent employment or compliance state"
---
# Bob by HiBob Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.hibob.com/platform/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current HiBob product and help documentation for the subscribed modules and jurisdictions.
- Company, site, worker, employment, role, compensation, time, absence, payroll, benefit, review, document, workflow, integration, permission, and audit state.
- HR, payroll, employment-law, privacy, security, reconciliation, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Bob HR configuration and workforce process review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter worker records, hire or terminate, change compensation, time, leave, benefits or payroll, issue documents, run reviews, export data, or represent employment or compliance state.

## Guardrails

- Do not invent worker identity, employment status, compensation, time or leave, benefit eligibility, payroll, performance assessment, document signature, consent, legal compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
