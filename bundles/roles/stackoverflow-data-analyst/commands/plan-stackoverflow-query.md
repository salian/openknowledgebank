---
type: Slash Command
command: /plan-stackoverflow-query
title: Plan Stack Overflow Query
description: Create a source-grounded SQL/API query plan.
okb_bundle_id: stackoverflow-data-analyst
inputs: [question, source, schema evidence, output dimensions, metrics]
outputs: [query plan]
requires_confirmation: false
timestamp: 2026-06-24T00:00:00Z
---

# /plan-stackoverflow-query

Use [design query plan](../workflows/design-query-plan.md) and [query-shape self-check](../frameworks/query-shape-self-check.md).

## Required Behavior

- State plan vs execution.
- Ground source objects.
- Define output row.
- Include query-shape self-check.
- Ask for confirmation before execution or export.
