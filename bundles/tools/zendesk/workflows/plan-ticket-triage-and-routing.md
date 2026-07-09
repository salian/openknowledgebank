---
type: Workflow
title: Plan Ticket Triage and Routing
description: "Plan Zendesk ticket triage, view, group, organization, SLA, and routing work with verified source and account evidence."
okb_bundle_id: zendesk
timestamp: "2026-07-09T00:00:00Z"
---

# Plan Ticket Triage and Routing

## Purpose

Create a reviewable plan for how Zendesk support work should be categorized, prioritized, assigned, routed, escalated, monitored, and reported.

## Evidence to Inspect First

- Current Zendesk Help or release documentation for the relevant ticketing, routing, SLA, view, macro, trigger, automation, and AI behavior.
- User-provided account evidence for products, plan/add-ons, brands, channels, ticket fields, ticket forms, statuses, tags, groups, organizations, users, roles, permissions, views, macros, triggers, automations, routing rules, SLAs, integrations, and AI agents.
- Report or dashboard definitions for backlog, first response, full resolution, reopen, escalation, SLA, CSAT, deflection, automated resolution, and workload metrics.
- Sandbox or test records when a change could affect live routing, reporting, automation, AI behavior, or customer communications.

## Output Shape

1. Source note.
2. Current-state map: channels, intake, classification, ownership, groups, organizations, views, routing, SLAs, automations, AI touchpoints, reporting, and integrations.
3. Gap list: missing evidence and unsupported assumptions.
4. Proposed triage/routing plan: source, criteria, destination, priority, SLA logic, exception handling, fallback owner, and monitoring.
5. Impact assessment: customer impact, agent impact, reporting impact, permission impact, data impact, AI impact, and integration impact.
6. Validation plan: sample tickets, sandbox or test account evidence, report reconciliation, queue/view monitoring, and acceptance criteria.
7. Confirmation and rollout plan: approvers, deployment window, rollback trigger, and rollback steps.

## Reconciliation Pattern

When two Zendesk reports, views, exports, APIs, or dashboards disagree, do not choose a winner until their definitions align. Compare dataset, source object, filters, ownership/sharing, time zone, date field, status values, requester/assignee/group logic, SLA logic, snapshots, deduplication, and data freshness. Separate expected differences from unresolved discrepancies.
