---
type: "Tool Guide"
title: "DingTalk"
description: "Source-aware guidance for DingTalk."
resource: "https://www.alibabacloud.com/en/product/dingtalk-enterprise"
okb_bundle_id: dingtalk
timestamp: "2026-08-13T00:00:00Z"
tool_category: "Enterprise communication and collaboration platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or change users, groups, messages, meetings, attendance or approvals, install apps or bots, access contacts or files, change permissions, export data, or represent delivery or attendance"
---
# DingTalk Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://www.alibabacloud.com/en/product/dingtalk-enterprise

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation.
- Account edition, region, configuration, permissions, data model, integrations, and logs.
- Change owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable DingTalk configuration and use review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or change users, groups, messages, meetings, attendance or approvals, install apps or bots, access contacts or files, change permissions, export data, or represent delivery or attendance.

## Guardrails

- Do not invent user identity or employment status, message delivery, attendance, document ownership, approval state, bot action, permission, workflow result, or authorization.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
