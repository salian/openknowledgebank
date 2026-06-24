---
type: Workflow
title: Answer Stack Overflow Data Question
description: General workflow for Stack Overflow public data requests.
tags: [workflow, analysis]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Answer Stack Overflow Data Question

## Steps

1. Restate the user's decision and requested output.
2. Choose source with [source selection matrix](../frameworks/source-selection-matrix.md).
3. Ground exact facts with [schema grounding protocol](../frameworks/schema-grounding-protocol.md).
4. Define metrics and row grain.
5. Draft plan using [design query plan](design-query-plan.md) when a query is needed.
6. Run [query-shape self-check](../frameworks/query-shape-self-check.md).
7. Report caveats, validation checks, and missing evidence.

## Output Contract

- Direct answer or plan status
- Source note
- Schema assumptions
- Metrics and output shape
- Query/API/report plan
- Validation and limitations
