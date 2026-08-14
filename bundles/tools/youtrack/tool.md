---
type: "Tool Guide"
title: "YouTrack"
description: "Source-aware guidance for YouTrack."
resource: "https://www.jetbrains.com/help/youtrack/"
okb_bundle_id: youtrack
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Issue tracking, agile planning, helpdesk, workflow, knowledge, reporting, integration, and API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter issues, tickets, workflows or permissions, send notifications, execute scripts, connect systems, expose tokens, call APIs, migrate data, or represent state, priority, estimate, SLA, dependency, delivery date, or completion"
---
# YouTrack Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.jetbrains.com/help/youtrack/
- https://www.jetbrains.com/youtrack/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable YouTrack issue, helpdesk, workflow, and API review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter issues, tickets, workflows or permissions, send notifications, execute scripts, connect systems, expose tokens, call APIs, migrate data, or represent state, priority, estimate, SLA, dependency, delivery date, or completion.

## Guardrails

- Do not invent deployment or version applicability, issue or ticket state, priority, estimate, SLA, dependency, workflow or API result, migration, delivery date, completion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
