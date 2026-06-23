---
type: Tool Guide
title: Google Analytics 4
description: "Safe-use guide for GA4 reports, Explorations, metrics, and settings."
tool_category: analytics
resource: "https://support.google.com/analytics"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - interpret user-provided reports
  - request settings
  - draft analysis plans
confirmation_required:
  - change settings
  - mark conversions/key events
  - change audiences
  - alter streams
  - export user data
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# Google Analytics 4

Ask for report surface, metric, dimensions, date range, comparison, filters, segments, timezone, currency, reporting identity, and visible data quality notices.

## Safe Use

The agent can interpret user-provided reports and request settings. It must not imply it inspected the property without evidence or authorization.

## Confirmation Required

Changing conversions/key events, audiences, reporting identity, data filters, attribution settings, streams, retention, exports, or user-data access requires explicit confirmation.
