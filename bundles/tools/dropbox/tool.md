---
type: Tool Guide
title: Dropbox
description: Defines source-aware file, folder, sharing, team, app permission, API, sync, retention, privacy, and audit review, evidence handling, and action boundaries.
resource: https://developers.dropbox.com/
okb_bundle_id: dropbox
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a dropbox review brief with explicit evidence states.
confirmation_required:
- upload, download, move, rename, share, unshare, restore, or delete files; change membership or permissions; export data; expose tokens; or send sensitive content
---
# Dropbox Source-Aware Tool Guide

Source-aware tool bundle for file, folder, sharing, team, app permission, API, sync, retention, privacy, and audit review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://developers.dropbox.com/
- https://www.dropbox.com/developers/documentation/http/documentation

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- account or team context, app and API version, OAuth scopes, file or folder IDs and revisions, sharing settings, membership, sync state, retention and legal-hold policy, event or audit logs, data classification, approvals, and rollback

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory evidence and label it as verified, provided, assumed, or needing verification.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, identifiers, versions, periods, scope, permissions, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source behavior and local evidence before naming state or result.
- Preserve prompt facts under `Provided`; distinguish them from verified facts, assumptions, and missing evidence.
- Do not infer file contents, revision, sync state, sharing audience, permission, retention, deletion status, or transfer result.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that upload, download, move, rename, share, unshare, restore, or delete files; change membership or permissions; export data; expose tokens; or send sensitive content.
