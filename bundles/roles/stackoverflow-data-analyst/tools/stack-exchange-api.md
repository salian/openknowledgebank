---
type: Tool Guide
title: Stack Exchange API
description: Guide for Stack Exchange API source use.
tool_category: web-api
okb_bundle_id: stackoverflow-data-analyst
integration_notes:
  mcp_candidate: false
  requires_user_auth: false
safe_operations: [draft request plan, explain endpoint behavior]
confirmation_required: [make authenticated requests, store response data]
timestamp: 2026-06-24T00:00:00Z
---

# Stack Exchange API

Use when the user needs API-backed source behavior rather than SQL.

## Grounded Behavior

For `/questions`, `tagged` is semicolon-delimited AND logic and more than five tags returns zero.

## Caveat

API filters and output fields are not the same as BigQuery or SEDE schemas.
