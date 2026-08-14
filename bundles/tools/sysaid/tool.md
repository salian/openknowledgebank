---
type: "Tool Guide"
title: "SysAid"
description: "Source-aware guidance for SysAid."
resource: "https://documentation.sysaid.com/"
okb_bundle_id: sysaid
timestamp: "2026-08-14T00:00:00Z"
tool_category: "IT service management, asset, workflow, self-service, AI, integration, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "access user or asset data, create or alter tickets, changes or approvals, run discovery or automation, enable AI agents, connect systems, expose credentials, or represent identity, priority, SLA, resolution, change success, security, or compliance"
---
# SysAid Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://documentation.sysaid.com/
- https://developers.sysaid.com/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable SysAid ITSM, automation, and AI governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before access user or asset data, create or alter tickets, changes or approvals, run discovery or automation, enable AI agents, connect systems, expose credentials, or represent identity, priority, SLA, resolution, change success, security, or compliance.

## Guardrails

- Do not invent record or asset identity, urgency or priority, SLA state, AI output, automation or API result, change approval, resolution, security finding, compliance, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
