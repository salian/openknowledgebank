---
type: Workflow
title: Review Zendesk Automation and AI
description: "Review Zendesk triggers, automations, macros, AI agents, Help Center knowledge sources, and integrations before customer-impacting changes."
okb_bundle_id: zendesk
timestamp: "2026-07-09T00:00:00Z"
---

# Review Zendesk Automation and AI

## Purpose

Create a source-aware review of Zendesk automation or AI behavior before it changes customer communications, ticket state, routing, permissions, reporting, integrations, or agent workload.

## Evidence to Inspect First

- Current Zendesk Help for trigger, automation, macro, routing, AI agent, Help Center, and channel behavior.
- Current Zendesk Developer docs for API, webhook, app, and integration behavior when technical actions are in scope.
- User-provided account evidence for the specific triggers, automations, macros, views, SLAs, routing rules, AI agents, knowledge sources, handoff/escalation paths, permissions, apps, webhooks, and integrations.
- Test tickets, sandbox results, sample customer journeys, fallback behavior, monitoring, and rollback evidence.

## Output Shape

1. Source note.
2. Automation or AI inventory: name, purpose, trigger condition, action, owner, channel, customer-facing effect, data touched, and dependency.
3. Verified behavior and gaps: what is source-confirmed, account-confirmed, assumed, and missing.
4. Conflict review: overlapping triggers, automation timing, macro use, routing/SLA effects, AI handoff, Help Center knowledge boundaries, app/webhook side effects, and report impacts.
5. Risk review: customer communications, privacy/security, regulated data, AI hallucination/escalation, support workload, reporting, permissions, and integrations.
6. Test plan: sample tickets or conversations, expected outcomes, negative cases, monitoring, and acceptance criteria.
7. Confirmation and rollback: explicit approval required, change window, rollback trigger, owner, and rollback steps.

## Confirmation Boundary

Require explicit confirmation before activating, disabling, reordering, or editing live triggers, automations, macros, routing, SLAs, AI agents, knowledge-source connections, apps, webhooks, integrations, exports, or customer-facing messages.
