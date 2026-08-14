---
type: "Tool Guide"
title: "GoTo Meeting"
description: "Source-aware guidance for GoTo Meeting."
resource: "https://www.goto.com/meeting"
okb_bundle_id: goto-meeting
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Video meeting, collaboration, recording, and transcription platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "schedule or start meetings, invite participants, grant remote control, record or transcribe, share recordings, change retention, connect apps, or represent attendance or consent"
---
# GoTo Meeting Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.goto.com/meeting
- https://developer.goto.com/GoToMeetingV1/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current GoTo Meeting product, support, and API documentation for the plan and region.
- Account, organizer, meeting, participant, access, recording, transcript, integration, retention, and audit state.
- Consent, privacy and security review, accessibility, test, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable GoTo Meeting configuration and meeting-control review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before schedule or start meetings, invite participants, grant remote control, record or transcribe, share recordings, change retention, connect apps, or represent attendance or consent.

## Guardrails

- Do not invent participant identity, invitation or attendance, consent, recording or transcript accuracy, access, delivery, retention, meeting outcome, accessibility, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
