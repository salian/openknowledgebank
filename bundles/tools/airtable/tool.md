---
type: Tool Guide
title: Airtable
description: Defines source-aware Airtable schema, records, views, automation, integration, and permission review, evidence handling, and action boundaries.
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a Airtable base change brief with explicit evidence states.
confirmation_required:
- create or modify records or schema, share a base, invite users, enable automations, create webhooks, expose tokens, or overwrite synchronized data
okb_bundle_id: airtable
timestamp: '2026-07-31T00:00:00Z'
---
# Airtable

Source-aware tool bundle for Airtable schema, records, views, automation, integration, and permission review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative Sources

- https://airtable.com/developers/web/api/introduction
- https://support.airtable.com/getting-started-with-airtables-web-api

Name the applicable source URL in every substantive Source Note. Verify its current version, effective date, product surface, jurisdiction, and applicability; a generic label is insufficient when a specific source is listed.

## Evidence Required

- workspace, base, table, field, view, interface, form, and record IDs
- schema, field types, formulas, linked records, filters, sorting, permissions, collaborators, personal or OAuth token scopes, API pagination and limits, automations, integrations, webhooks, source-of-record rules, snapshots, tests, and approvals

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer schema, record count, formula result, permission, automation state, synchronization, API completeness, or source-of-record status.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that create or modify records or schema, share a base, invite users, enable automations, create webhooks, expose tokens, or overwrite synchronized data.
