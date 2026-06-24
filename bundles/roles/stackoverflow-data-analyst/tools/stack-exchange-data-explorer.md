---
type: Tool Guide
title: Stack Exchange Data Explorer
description: Guide for SEDE source use and reconciliation.
tool_category: public-sql-interface
okb_bundle_id: stackoverflow-data-analyst
integration_notes:
  mcp_candidate: false
  requires_user_auth: false
safe_operations: [draft query, compare source behavior, request query URL]
confirmation_required: [publish query, rely on as source of record]
timestamp: 2026-06-24T00:00:00Z
---

# Stack Exchange Data Explorer

Use SEDE for public SQL exploration and shareable queries.

## Required Evidence

- Query SQL or URL
- Site/database
- Run date
- Filters and output

## Caveat

Do not assume SEDE and BigQuery schemas or freshness match.
