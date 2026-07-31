---
type: Tool Guide
title: "Google Search Console"
description: "Defines source-aware organic search monitoring and diagnosis, evidence handling, and action boundaries."
tool_category: "Organic search monitoring tool"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review organic search monitoring and diagnosis from supplied evidence."
  - "Draft a search console diagnosis brief with explicit evidence states."
confirmation_required:
  - "changing users, submitting removals or validation requests, modifying sitemaps or site configuration, or publishing unsupported ranking claims"
okb_bundle_id: google-search-console
timestamp: "2026-07-31T00:00:00Z"
---

# Google Search Console

Source-aware tool bundle for Google Search Console properties, performance, indexing, URL inspection, sitemaps, reports, and review-ready search briefs.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- property type, verified scope, and ownership
- report, date range, search type, country, device, query, and page filters
- metric definitions, freshness, and aggregation behavior
- URL inspection and live-test evidence
- indexing, canonical, robots, sitemap, and enhancement evidence
- site changes and deployment dates
- analytics, server, rank, and source-of-record comparisons

## Guardrails

- Verify official-source behavior and local configuration before naming state.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, scopes, filters, owners, and processing rules.
- Require accountable confirmation before changing users, submitting removals or validation requests, modifying sitemaps or site configuration, or publishing unsupported ranking claims.
