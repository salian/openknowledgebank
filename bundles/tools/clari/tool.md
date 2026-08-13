---
type: "Tool Guide"
title: "Clari"
description: "Source-aware guidance for Clari."
resource: "https://www.clari.com/"
okb_bundle_id: clari
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Revenue orchestration platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "connect CRM or communication systems, ingest or export customer data, change forecasts or opportunities, activate AI or automation, send communications, or represent pipeline, forecast, deal, or revenue outcomes"
---
# Clari Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.clari.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Clari configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before connect CRM or communication systems, ingest or export customer data, change forecasts or opportunities, activate AI or automation, send communications, or represent pipeline, forecast, deal, or revenue outcomes.

## Guardrails

- Do not invent account or contact identity, opportunity stage or amount, activity completeness, model output, forecast accuracy, deal outcome, attribution, revenue result, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
