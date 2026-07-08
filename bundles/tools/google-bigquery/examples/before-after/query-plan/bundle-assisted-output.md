---
type: Example Output
title: Bundle-Assisted Output
okb_bundle_id: google-bigquery
timestamp: "2026-07-08T00:00:00Z"
---

# Bundle-Assisted Output

I can plan the query, but I should not invent the table or field names.

Needed evidence:

- project, dataset, and table names;
- schema fields for acquisition channel, revenue, event/order date, and order identity;
- definition of "revenue" and "last month";
- timezone and attribution model;
- source-of-record or dashboard total to validate against;
- permission and cost context for running the query.

Query shape:

- select acquisition channel and revenue metric;
- filter to the agreed date range and timezone;
- group by channel at the requested grain;
- validate totals against the source-of-record report;
- run a dry run before live execution and avoid selecting unnecessary columns.

Source note: BigQuery guidance should use official BigQuery SQL and cost/performance docs plus user-provided schema and business definitions. Missing before executable SQL: table/schema evidence, metric definition, timezone, validation target, and dry-run estimate.
