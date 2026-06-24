---
type: Framework
title: Schema Grounding Protocol
description: Protocol for using exact source objects without inventing them.
tags: [schema, grounding, source-discipline]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Schema Grounding Protocol

## Steps

1. Identify the active source.
2. Locate verified schema evidence.
3. Mark every exact object as verified, user-provided, illustrative, or unknown.
4. Write query sketches only with verified objects.
5. Ask for source inspection when facts are unknown.
6. Validate before execution with dry run, sample rows, and row counts.

## Do Not Invent

- Tables or bridge tables
- Array fields
- Enum values
- API parameters
- Current live counts
- License conclusions
