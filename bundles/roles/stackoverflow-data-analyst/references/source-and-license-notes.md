---
type: Reference
title: Source and License Notes
description: Source freshness, tool, and licensing notes for Stack Overflow public data.
tags: [sources, licensing, freshness]
okb_bundle_id: stackoverflow-data-analyst
source_quality: grounded-summary
timestamp: 2026-06-24T00:00:00Z
---

# Source and License Notes

## BigQuery

Use for reproducible SQL planning over public historical data. Confirm project, permissions, billing/sandbox status, and dry-run expectations before execution.

## SEDE

Use for public SQL exploration and shared queries. SEDE can differ from BigQuery by schema, SQL dialect, refresh cadence, and inclusion rules.

## API

The `/questions` endpoint's `tagged` parameter is semicolon-delimited AND logic. More than five tags returns zero for that method.

## Live Site/Search

Use for current visible counts when the user provides output or authorizes access. Live search behavior can differ from SQL/API sources.

## Licensing

Stack Overflow public user contributions are CC BY-SA licensed with date-specific license eras. Do not copy substantial content without attribution/share-alike review.

## Source Note Template

```text
Source note:
- Source category:
- Exact source/evidence:
- Time period and freshness:
- Schema assumptions:
- Missing evidence:
- License/privacy caveat:
```
