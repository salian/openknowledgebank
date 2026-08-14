---
type: "Tool Guide"
title: "MatrixCare"
description: "Source-aware guidance for MatrixCare."
resource: "https://www.matrixcare.com/"
okb_bundle_id: matrixcare
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Post-acute electronic health record and care operations platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or change patient records, document care, alter medication or orders, schedule services, exchange protected health information, submit claims, change billing, or make clinical, eligibility, payment, or compliance decisions"
---
# MatrixCare Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.matrixcare.com/
- https://www.matrixcare.com/solutions/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable MatrixCare clinical, operational, and revenue-cycle review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or change patient records, document care, alter medication or orders, schedule services, exchange protected health information, submit claims, change billing, or make clinical, eligibility, payment, or compliance decisions.

## Guardrails

- Do not invent patient identity, diagnosis, medication, order, care plan, clinical status, eligibility, authorization, claim, payment, staffing, quality measure, interoperability, privacy compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
