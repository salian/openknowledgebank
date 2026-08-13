---
type: "Tool Guide"
title: "Optum APIs (formerly Change Healthcare)"
description: "Source-aware guidance for Optum APIs (formerly Change Healthcare)."
resource: "https://developer.optum.com/"
okb_bundle_id: change-healthcare
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Healthcare API and transaction platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access or transmit protected health information, query eligibility, submit or alter claims or payments, change trading-partner configuration, issue credentials, call production APIs, or represent clinical, coverage, payment, or compliance outcomes"
---
# Optum APIs (formerly Change Healthcare) Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://developer.optum.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Optum APIs (formerly Change Healthcare) configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access or transmit protected health information, query eligibility, submit or alter claims or payments, change trading-partner configuration, issue credentials, call production APIs, or represent clinical, coverage, payment, or compliance outcomes.

## Guardrails

- Do not invent current product applicability, patient or member identity, authorization, eligibility or coverage, code or claim accuracy, payer adjudication, payment status, API result, regulatory compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
