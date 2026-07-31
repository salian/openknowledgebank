---
type: Tool Guide
title: Google Meet
description: Defines source-aware meeting space, conference record, participant session, recording, transcript, event, authorization, privacy, and artifact review, evidence handling, and action boundaries.
resource: https://developers.google.com/workspace/meet/api/guides/overview
okb_bundle_id: google-meet
timestamp: '2026-07-31T00:00:00Z'
tool_category: Workflow and operational software
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a google meet review brief with explicit evidence states.
confirmation_required:
- create or alter meeting spaces, invite participants, start recording or transcription, subscribe to events, access or share artifacts, change permissions, export data, or expose OAuth tokens
---
# Google Meet Source-Aware Tool Guide

Source-aware tool bundle for meeting space, conference record, participant session, recording, transcript, event, authorization, privacy, and artifact review, evidence reconciliation, reviewable decisions, and controlled consequential actions.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Authoritative and Identified Sources

- https://developers.google.com/workspace/meet/api/guides/overview
- https://developers.google.com/workspace/meet/api/guides/artifacts

Name the applicable source URL in every substantive Source Note. Verify its current version, date, product or method scope, and applicability. Where a source is secondary or proprietary material is unavailable, state that limitation rather than presenting the summary as canonical.

## Evidence Required

- Workspace edition and admin policy, meeting-space ID, conference record, participant authorization, recording and transcription settings, artifact IDs and Drive permissions, OAuth scopes, retention policy, event subscription, dates, notices, approvals, and audit evidence

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
- Do not infer attendance, participant identity, consent, recording or transcript existence, artifact contents, permission, retention, or meeting outcome.
- Do not invent artifact provenance, access, execution, approval, or an accountable reviewer.
- Require accountable confirmation before actions that create or alter meeting spaces, invite participants, start recording or transcription, subscribe to events, access or share artifacts, change permissions, export data, or expose OAuth tokens.
