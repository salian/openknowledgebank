---
type: "Tool Guide"
title: "Copper CRM"
description: "Source-aware guidance for Copper CRM."
resource: "https://www.copper.com/"
okb_bundle_id: copper
timestamp: "2026-08-13T00:00:00Z"
tool_category: "CRM and client relationship platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import or update contacts, connect Google Workspace, send automated email, move opportunities, create projects, change permissions, export personal data, or represent pipeline or revenue outcomes"
---
# Copper CRM Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.copper.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Copper CRM configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import or update contacts, connect Google Workspace, send automated email, move opportunities, create projects, change permissions, export personal data, or represent pipeline or revenue outcomes.

## Guardrails

- Do not invent person or company identity, consent, opportunity stage or value, email delivery, project state, forecast, attribution, revenue outcome, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
