---
type: Workflow
title: Plan Sales Process and Pipeline
description: "Plan HubSpot Sales Hub CRM, pipeline, deal, owner, and reporting work with verified source and portal evidence."
okb_bundle_id: hubspot-sales-hub
timestamp: "2026-07-09T00:00:00Z"
---

# Plan Sales Process and Pipeline

## Purpose

Create a reviewable plan for how contacts, companies, deals, leads, tasks, meetings, owners, stages, forecasts, reports, and dashboards should support a sales process in HubSpot Sales Hub.

## Evidence to Inspect First

- Current HubSpot product, Knowledge Base, Developers, or commercial source category for the relevant Sales Hub, CRM object, pipeline, forecast, report, permission, or API behavior.
- User-provided portal evidence for objects, properties, associations, pipelines, stages, lifecycle/lead statuses, owners, teams, required fields, views, imports, permissions, and seat/edition details.
- Report or dashboard definitions for pipeline, deal velocity, activity, conversion, forecast, goal, owner/team performance, source, currency, time zone, and data freshness.
- Test records, sandbox evidence, or limited-scope validation evidence when a change could affect live CRM data.

## Output Shape

1. Source note.
2. Current-state map: objects, properties, pipelines, stages, ownership, activities, reports, dashboards, permissions, and integration touchpoints actually verified.
3. Gap list: missing evidence and unsupported assumptions.
4. Proposed process or pipeline plan: source, criteria, stage logic, owner/team logic, required data, exception handling, and fallback owner.
5. Reporting and reconciliation logic: filters, date fields, owner/team scope, currency, stage definitions, attribution/source logic, deduplication, and data freshness.
6. Impact assessment: customer impact, rep impact, data impact, reporting impact, permission impact, and integration impact.
7. Validation and rollout plan: sample records, test views/reports, owner review, monitoring, explicit confirmation, rollback trigger, and rollback steps.

## Reconciliation Pattern

When two HubSpot reports, dashboards, forecasts, exports, APIs, or external tools disagree, do not choose a winner until definitions align. Compare object scope, filters, owner/team scope, date field, time zone, pipeline/stage definitions, lifecycle or lead status, currency, attribution/source logic, association logic, deduplication, permissions, snapshots, and data freshness. Separate expected differences from unresolved discrepancies.
