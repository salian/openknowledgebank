---
type: Framework
title: Source Selection Matrix
description: Selects the right Stack Overflow data source for the user's decision.
tags: [sources, freshness, reconciliation]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Source Selection Matrix

| Need | Prefer | Caveat |
| --- | --- | --- |
| Historical reproducible SQL | BigQuery public data or SEDE | Verify freshness and schema. |
| Shared public SQL query | SEDE | SQL dialect/schema may differ from BigQuery. |
| API-backed workflow | Stack Exchange API | Endpoint filters differ from SQL sources. |
| Current visible count | Live site/search or API output | Interface and ranking behavior can affect counts. |
| Customer-specific source of record | User export/warehouse | Inspect local schema first. |

## Rule

Choose the source that matches the decision. Do not declare a count "right" until definitions, filters, freshness, and source behavior are aligned.
