---
type: "Tool Guide"
title: "Pipedrive"
description: "Source-aware guidance for Pipedrive."
resource: "https://support.pipedrive.com/"
okb_bundle_id: pipedrive
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Sales CRM, pipeline, automation, AI, API, webhook, and MCP platform"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "import or identify contacts, send or track email, create or change leads, deals, activities, projects, products or forecasts, activate automations, grant API or MCP access, enable AI notetaking, or represent pipeline, forecast, meeting, or revenue"
---
# Pipedrive Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://support.pipedrive.com/
- https://developers.pipedrive.com/docs/api/v1

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Pipedrive CRM, API, and AI integration review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before import or identify contacts, send or track email, create or change leads, deals, activities, projects, products or forecasts, activate automations, grant API or MCP access, enable AI notetaking, or represent pipeline, forecast, meeting, or revenue.

## Guardrails

- Do not invent plan or API-version availability, contact identity, consent, deal ownership, stage, amount, forecast, email or meeting state, AI transcript or summary, automation, MCP or API action, revenue, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
