---
type: Workflow
title: Monitoring and Performance Dashboard source-aware triage
---

# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: audience, decisions, services, models, or processes in scope, metric, event, log, and trace definitions, source systems, queries, filters, aggregation, and dimensions, time range, timezone, latency, freshness, and missing-data behavior, baseline, objective, threshold, alert, and uncertainty, and owner, access, privacy, runbook, escalation, and validation evidence.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, calculations, and owners.
5. Produce the smallest reviewable monitoring dashboard specification.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the evidenced reviewer, or `Needs verification`, and prohibited actions
- **Source note** with sources and limitations
