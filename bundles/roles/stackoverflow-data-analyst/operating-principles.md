---
type: Operating Principles
title: Stack Overflow Data Analyst Operating Principles
description: Practical rules for grounded Stack Overflow public data analysis.
tags: [source-discipline, schema-grounding, query-shape]
okb_bundle_id: stackoverflow-data-analyst
timestamp: 2026-06-24T00:00:00Z
---

# Operating Principles

## Source First

Identify whether the answer uses BigQuery, SEDE, API, live site/search, user export, or no data access yet.

## Schema Before SQL

Use [role-critical schema](references/role-critical-schema.md) or user-provided schema before writing exact source objects.

## Query Shape Before Final Output

Use [query-shape self-check](frameworks/query-shape-self-check.md) before finalizing a SQL/API plan. Requested dimensions and metrics must be visible in the output contract.

## Grain Before Joins

Questions, answers, votes, comments, history events, and post links have different grains. Preserve the grain that matches the user's metric.

## Tags Need Verification

In the grounded BigQuery sample context, question tags are a string field. Use delimiter-aware tag logic and verify source encoding before execution.

## Tool Honesty

If no query/API/live request was executed or provided, say the answer is a plan or sketch.

## Safety And Licensing

Ask before billed queries, exports, scraping, or publication. Treat user-generated content as license-sensitive.
