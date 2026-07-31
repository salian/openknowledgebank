---
type: Deliverable Guide
title: Monitoring and Performance Dashboard Source-Aware Guide
description: Defines source-aware operational monitoring and performance visualization, evidence handling, and action boundaries.
tags:
- monitoring-dashboard
- observability
- performance
- deliverable
resource: https://sre.google/sre-book/monitoring-distributed-systems/
okb_bundle_id: monitoring-dashboard
timestamp: '2026-07-31T00:00:00Z'
---

# Monitoring and Performance Dashboard Source-Aware Guide

Source-aware deliverable bundle for specifying a monitoring dashboard with evidenced users, decisions, signals, definitions, sources, thresholds, freshness, ownership, and response links.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- audience, decisions, services, models, or processes in scope
- metric, event, log, and trace definitions
- source systems, queries, filters, aggregation, and dimensions
- time range, timezone, latency, freshness, and missing-data behavior
- baseline, objective, threshold, alert, and uncertainty
- owner, access, privacy, runbook, escalation, and validation evidence

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer metric meaning, query correctness, data freshness, threshold validity, system health, and response ownership.
- Require accountable confirmation before changing alerts, production monitoring, access, retention, or incident status, or publishing performance claims without validated data.
