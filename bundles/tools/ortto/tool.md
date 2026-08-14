---
type: "Tool Guide"
title: "Ortto"
description: "Source-aware guidance for Ortto."
resource: "https://help.ortto.com/"
okb_bundle_id: ortto
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Customer data, journey orchestration, messaging, analytics, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "ingest or identify customer data, change consent or audiences, send messages, activate journeys, enable AI, connect systems, export data, spend funds, or represent delivery, attribution, conversion, or revenue"
---
# Ortto Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://help.ortto.com/
- https://ortto.com/product/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Ortto customer-data and journey review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before ingest or identify customer data, change consent or audiences, send messages, activate journeys, enable AI, connect systems, export data, spend funds, or represent delivery, attribution, conversion, or revenue.

## Guardrails

- Do not invent customer identity, consent, profile or activity accuracy, audience membership, message delivery, journey execution, AI output, attribution, conversion, revenue, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
