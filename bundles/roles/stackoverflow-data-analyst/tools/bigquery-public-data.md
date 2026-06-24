---
type: Tool Guide
title: BigQuery Public Data
description: Safe-use guide for Stack Overflow public BigQuery planning.
tool_category: data-warehouse
okb_bundle_id: stackoverflow-data-analyst
integration_notes:
  mcp_candidate: false
  requires_user_auth: true
safe_operations: [draft query plan, review SQL, explain schema assumptions, request dry run]
confirmation_required: [execute query, export results, use billed project]
timestamp: 2026-06-24T00:00:00Z
---

# BigQuery Public Data

Use for reproducible SQL planning over the public Stack Overflow dataset.

## Safe Use

- Draft query plans.
- Identify source objects from [role-critical schema](../references/role-critical-schema.md).
- Recommend dry runs.
- Explain cost and freshness caveats.

## Confirmation Required

- Query execution
- Exporting data
- Using a billed project
- User-level analysis
