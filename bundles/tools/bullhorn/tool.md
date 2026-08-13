---
type: "Tool Guide"
title: "Bullhorn"
description: "Source-aware guidance for Bullhorn."
resource: "https://www.bullhorn.com/products/applicant-tracking-crm/"
okb_bundle_id: bullhorn
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Staffing applicant tracking and CRM platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or change candidate, client, job, submission or placement records, contact candidates, submit profiles, change status, export personal data, automate decisions, or represent hiring outcomes"
---
# Bullhorn Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.bullhorn.com/products/applicant-tracking-crm/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Bullhorn configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or change candidate, client, job, submission or placement records, contact candidates, submit profiles, change status, export personal data, automate decisions, or represent hiring outcomes.

## Guardrails

- Do not invent candidate identity, consent, qualification, employment status, client authority, submission or placement state, compensation, hiring decision, delivery, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
