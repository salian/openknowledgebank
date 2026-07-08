---
type: Reference
title: Funnel Analysis Source Checks
description: "Official and local source categories to inspect before funnel-analysis claims or actions."
okb_bundle_id: funnel-analysis
timestamp: "2026-07-09T00:00:00Z"
---

# Funnel Analysis Source Checks

## Official Source Categories

- Analytics-tool documentation for funnel settings, counting behavior, segments, breakdowns, filters, and reporting limits.
- Tool-specific documentation for open/closed funnels, sequence requirements, elapsed time, next actions, and conversion-basis settings.
- Warehouse, event, CRM, or BI documentation when the funnel is rebuilt outside the analytics UI.
- Privacy, consent, and data-governance guidance when user-level analysis or exports are involved.

## Local Evidence Categories

- Report, exploration, dashboard, query, or export used for the funnel.
- Event names, parameters, dimensions, schema excerpts, and source-of-record definitions.
- Date range, timezone, filters, attribution, comparison period, and data freshness.
- Segment, cohort, channel, experiment, and breakdown definitions.
- Known product releases, tag changes, campaign changes, consent changes, and instrumentation incidents.

## Rule

If an exact funnel fact is not in official documentation or local evidence, do not present it as authoritative. Ask for inspection or mark the item as an assumption.
