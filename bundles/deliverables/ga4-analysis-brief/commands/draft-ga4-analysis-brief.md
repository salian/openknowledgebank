---
type: Slash Command
command: /draft-ga4-analysis-brief
title: Draft GA4 Analysis Brief
description: "Draft a source-scoped GA4 analysis brief without inventing access, metric definitions, or causes."
okb_bundle_id: ga4-analysis-brief
inputs:
  - user question
  - GA4 report, exploration, export, or schema evidence
  - date range and comparison period
  - metrics, dimensions, filters, and segments
outputs:
  - GA4 analysis brief
  - missing evidence
  - validation plan
  - next actions
requires_confirmation: true
timestamp: "2026-07-09T00:00:00Z"
---

# /draft-ga4-analysis-brief

Purpose: produce a decision-ready GA4 analysis brief that is explicit about source scope, definitions, uncertainty, and action boundaries.

Bundled commands are suggestions, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## Output Contract

Return:

1. Direct answer.
2. Source scope.
3. Metric and dimension definitions.
4. Findings.
5. Caveats and missing evidence.
6. Hypotheses.
7. Recommended next actions.
8. Source note.

## Confirmation Boundary

Do not modify GA4, GTM, dashboards, reports, audiences, campaigns, experiments, exports, warehouse tables, or permissions without explicit user confirmation and authorized tool access.
