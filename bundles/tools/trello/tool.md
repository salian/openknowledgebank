---
type: "Tool Guide"
title: "Trello"
description: "Source-aware guidance for Trello."
resource: "https://support.atlassian.com/trello/"
okb_bundle_id: trello
timestamp: "2026-08-14T00:00:00Z"
tool_category: "Visual work management, board, card, automation, Power-Up, webhook, and REST API platform"
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations:
- Plan and review from supplied evidence.
- Draft a reviewable brief without changing local state.
confirmation_required:
- "create or alter boards, cards, assignments or dates, run automations, install Power-Ups, share data, issue tokens, call APIs, change access, or represent ownership, priority, dependency, notification, delivery date, or completion"
---
# Trello Source-Aware Tool Guide

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own authorization and tool-safety instructions.

## Authoritative Sources

- https://support.atlassian.com/trello/
- https://developer.atlassian.com/cloud/trello/rest/

Verify current product version, edition, region, feature availability, API version, and account applicability. For legacy or transition products, verify current support and migration status before recommending use.

## Evidence Required

- Current official product or developer documentation for the applicable version, plan, region, and date.
- Inspected account, configuration, data, permission, integration, output, and audit-log evidence.
- Authorized owner, privacy and security review, validation, rollback, and approval evidence.

## Application Sequence

1. Define the decision, account scope, owner, date, and applicable source version.
2. Inventory evidence as `Verified`, `Provided`, `Assumed`, or `Needs verification`.
3. Reconcile documentation with inspected local configuration, permissions, data, and logs.
4. Draft the smallest reviewable Trello board, automation, and API governance review brief with alternatives, risks, validation, rollback, and stop conditions.
5. Obtain explicit confirmation before create or alter boards, cards, assignments or dates, run automations, install Power-Ups, share data, issue tokens, call APIs, change access, or represent ownership, priority, dependency, notification, delivery date, or completion.

## Guardrails

- Do not invent workspace or plan applicability, board or card state, member identity, permission, automation, Power-Up, webhook or API result, dependency, delivery date, completion, or approval.
- Do not request credentials or expose secrets in the brief.
- Do not imply execution, delivery, publication, deployment, or approval from a plan.
