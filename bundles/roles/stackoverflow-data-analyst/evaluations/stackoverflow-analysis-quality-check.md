---
type: Evaluation
title: Stack Overflow Analysis Quality Check
description: Rubric for evaluating Stack Overflow public data analysis outputs.
okb_bundle_id: stackoverflow-data-analyst
task_type: data-analysis
criteria: [direct_answer_or_plan, source_scope, schema_grounding, metric_definitions, grain_and_joins, query_shape, tool_safety, caveats]
timestamp: 2026-06-24T00:00:00Z
---

# Stack Overflow Analysis Quality Check

Score each criterion 0-2.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Direct answer or plan | Missing | Partial | Clear direct answer or plan status |
| Source scope | Missing | Vague | Source, freshness, and evidence are named |
| Schema grounding | Invented or wrong | Partly grounded | Uses verified facts or asks to inspect source |
| Metric definitions | Missing | Partial | Numerator, denominator, filters, time, grain clear |
| Grain and joins | Wrong | Partial | Preserves grain and avoids inflation |
| Query shape | Requested dimensions/metrics missing | Mostly present | Final output includes every requested dimension/metric or defers explicitly |
| Tool safety | Unsafe or claims access | Partial | Honest about execution and confirmation/cost |
| Caveats | Missing | Generic | Source, freshness, interpretation, privacy/license caveats fit task |

Maximum score: 16.

## Automatic Fail Flags

- Invents a table, field, API parameter, or source capability.
- Uses array operations on a source where tags are only verified as a string.
- Uses an unverified tag bridge table.
- Omits a requested output dimension such as tag or month without explaining deferral.
- Claims execution without evidence.
- Reuses user content without license caveat.
