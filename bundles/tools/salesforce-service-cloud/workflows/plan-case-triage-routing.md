---
type: Workflow
title: Plan Case Triage and Routing
description: "Plan Service Cloud case triage, queue, and routing work with verified source and org evidence."
okb_bundle_id: salesforce-service-cloud
timestamp: "2026-07-09T00:00:00Z"
---

# Plan Case Triage and Routing

## Purpose

Create a reviewable plan for how cases or service work should be categorized, prioritized, routed, owned, escalated, and monitored in Salesforce Service Cloud.

## Evidence to Inspect First

- Current Salesforce Help or release documentation for the relevant Service Cloud, queue, and Omni-Channel behavior.
- User-provided org evidence for objects, fields, record types, queues, skills, presence statuses, routing model, assignment/escalation rules, flows, entitlements, milestones, channels, and permissions.
- Report or dashboard definitions for backlog, first response, resolution, reopen, escalation, SLA, CSAT, and workload metrics.
- Sandbox or test records when a change could affect live routing.

## Output Shape

1. Source note.
2. Current-state map: channels, case intake, classification, ownership, queues, routing, escalation, entitlements, automation, and reporting.
3. Gap list: missing evidence and unsupported assumptions.
4. Proposed routing plan: source, criteria, destination, priority, capacity/skills if applicable, exception handling, and fallback owner.
5. Impact assessment: customer impact, agent impact, reporting impact, permission impact, data impact, and integration impact.
6. Validation plan: sample cases, sandbox test, report reconciliation, queue monitoring, and acceptance criteria.
7. Confirmation and rollout plan: approvers, deployment window, rollback trigger, and rollback steps.

## Reconciliation Pattern

When two reports or tools disagree, do not choose a winner until their definitions align. Compare report type, filters, ownership/sharing, time zone, date field, status values, queue ownership, entitlement logic, snapshots, deduplication, and data freshness. Separate expected differences from unresolved discrepancies.
