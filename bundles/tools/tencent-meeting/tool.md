---
type: "Tool Guide"
title: "Tencent Meeting"
description: "Source-aware guidance for Tencent Meeting."
resource: "https://meeting.tencent.com/"
okb_bundle_id: tencent-meeting
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Meeting, webinar, room, recording, transcription, administration, integration, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "schedule or host meetings, invite or identify participants, record or transcribe communications, share screens or files, grant host controls, call APIs, or represent attendance, consent, identity, recording, delivery, confidentiality, or compliance"
---
# Tencent Meeting Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://meeting.tencent.com/
- https://cloud.tencent.com/document/product/1095

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Tencent Meeting conferencing and recording-governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before schedule or host meetings, invite or identify participants, record or transcribe communications, share screens or files, grant host controls, call APIs, or represent attendance, consent, identity, recording, delivery, confidentiality, or compliance.

## Guardrails

- Do not invent service or regional applicability, participant identity, invitation or attendance, recording or transcription consent, transcript accuracy, confidentiality, API result, retention, compliance, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
