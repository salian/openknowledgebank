---
type: Slash Command
command: /plan-zendesk-support-work
title: Plan Zendesk Support Work
description: "Create a source-scoped Zendesk ticketing, routing, automation, AI, reporting, or API plan without inventing account configuration."
okb_bundle_id: zendesk
inputs:
  - support operations question or desired Zendesk change
  - Zendesk account evidence
  - ticket lifecycle, channel, routing, report, automation, Help Center, AI, permission, or API context
  - risk and approval constraints
outputs:
  - Zendesk readiness answer
  - required account evidence
  - proposed plan or change
  - validation and rollback checklist
  - source note
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-zendesk-support-work

Purpose: produce a Zendesk plan that is ready for human, support-operations, and administrator review, not an unsafely executed production change.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Inputs

- Business question, support workflow, reporting issue, API question, or desired Zendesk change.
- Zendesk account evidence, if available: Admin Center screenshots, exports, ticket fields/forms/statuses, views, macros, trigger and automation definitions, routing configuration, SLA policies, Help Center setup, AI agent setup, report/dashboard definitions, app/integration settings, permissions, or sandbox/test evidence.
- Ticket lifecycle, channel, brand, group, organization, requester, Help Center, AI, routing, escalation, reporting, API, privacy, or compliance context.
- Approval, privacy, security, AI governance, compliance, deployment, rollback, and monitoring constraints.

## Output Contract

Return:

1. Direct answer: whether enough evidence exists to plan the work now.
2. Source note: official Zendesk source categories, user-provided account evidence, and missing verification.
3. Verified facts: what is confirmed by Zendesk sources or user-provided account evidence.
4. Missing evidence: account setup, product, plan/add-on, schema, business-rule, report, permission, API, AI, or policy inputs needed.
5. Plan: proposed ticketing/routing/reporting/automation/AI/API work, with assumptions labeled.
6. Risk and confirmation boundary: customer impact, data impact, automation impact, AI/customer-facing impact, permission impact, and actions requiring explicit approval.
7. Validation and rollback: sandbox/test plan, sample records, report reconciliation, monitoring, owner, rollback trigger, and rollback action.

## Confirmation Boundary

Do not send customer communications, publish Help Center content, export data, modify records, deploy or activate triggers/automations/macros/routing/AI agents, change permissions, run API calls, or alter integrations without explicit user confirmation and authorized access.
