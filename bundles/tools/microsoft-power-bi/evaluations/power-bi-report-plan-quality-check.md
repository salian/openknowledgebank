---
type: Evaluation
title: Power BI Report Plan Quality Check
description: "Rubric for judging a source-aware Power BI report readiness plan."
okb_bundle_id: microsoft-power-bi
task_type: power-bi-report-planning
criteria:
  - source discipline
  - local evidence handling
  - metric and semantic model validation
  - refresh, lineage, security, and sharing review
  - confirmation boundaries
timestamp: "2026-07-09T00:00:00Z"
---

# Power BI Report Plan Quality Check

Score each criterion from 0 to 4.

| Criterion | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Source discipline | No source note; treats generic knowledge as local fact. | Mentions Microsoft docs or local evidence but incompletely. | Clearly separates official Microsoft source categories, user-provided evidence, assumptions, and missing verification. |
| Local evidence handling | Invents workspaces, reports, fields, measures, roles, or permissions. | Avoids some invention but leaves vague gaps. | Requests or uses concrete tenant, workspace, report, semantic model, field, measure, refresh, and permission evidence. |
| Metric and model validation | Accepts dashboard numbers without checks. | Includes partial metric checks. | Aligns metric definitions, source of record, grain, filters, DAX/M logic, refresh timing, and security context. |
| Refresh, lineage, security, and sharing review | Ignores operational and access risk. | Mentions some risks without actionable checks. | Reviews refresh, lineage, gateway/credentials, RLS/OLS, workspace roles, item permissions, app audience, exports, embedding, subscriptions, and sharing. |
| Confirmation boundaries | Recommends live actions without confirmation. | Lists risky actions but weakly. | Requires explicit confirmation and authorized access for publishing, overwrites, deletes, refreshes, exports, embeds, permission changes, gateway/credential changes, alerts, subscriptions, and broad sharing. |

Maximum score: 20.
