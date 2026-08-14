---
type: "Tool Guide"
title: "MoEngage"
description: "Source-aware guidance for MoEngage."
resource: "https://www.moengage.com/product/"
okb_bundle_id: moengage
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Cross-channel customer engagement, analytics, personalization, and AI platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "ingest or identify customer data, change consent or segments, send messages, activate journeys, run experiments, enable AI decisions, connect destinations, spend funds, or represent delivery, conversion, attribution, or revenue"
---
# MoEngage Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.moengage.com/product/
- https://developers.moengage.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable MoEngage journey, data, and AI governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before ingest or identify customer data, change consent or segments, send messages, activate journeys, run experiments, enable AI decisions, connect destinations, spend funds, or represent delivery, conversion, attribution, or revenue.

## Guardrails

- Do not invent customer identity, consent, profile or event accuracy, segment membership, send or delivery, experiment validity, AI decision, attribution, conversion, revenue, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
