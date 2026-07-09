---
type: Tool Guide
title: Amplitude
description: "Defines safe, source-aware use of Amplitude in product analytics and product-management bundles."
tool_category: "Product analytics, experimentation, cohorts, funnels, and session replay platform"
okb_bundle_id: amplitude
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - Plan product analytics questions from user-provided Amplitude evidence.
  - Review event taxonomy, chart definitions, cohorts, funnels, experiments, and replay evidence.
  - Draft analysis briefs with source notes and data-quality caveats.
confirmation_required:
  - Change instrumentation, cohorts, experiments, dashboards, alerts, permissions, exports, integrations, privacy settings, or user-facing experiences.
timestamp: "2026-07-09T00:00:00Z"
---

# Amplitude Tool Guide

Amplitude is a product analytics platform used for event-based analysis, funnels, cohorts, experiments, and user-experience evidence such as session replay.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, and tool-safety instructions.

## What This Bundle Is For

- Planning product analytics questions and evidence requests.
- Reviewing event taxonomy and property definitions before analysis.
- Interpreting funnels, cohorts, experiments, dashboards, and replays with caveats.
- Helping product, growth, data, and analytics roles produce decision-ready briefs.

## What This Bundle Is Not

- A complete Amplitude product, SDK, API, billing, privacy, governance, or administrator reference.
- A substitute for data engineering, privacy, security, experimentation, product analytics, legal, or Amplitude administrator review.
- A claim that the agent has access to the user's Amplitude workspace.

## Guardrails

- Verify event names, property names, user identity logic, filters, cohorts, time ranges, environments, and chart definitions before interpreting results.
- Reconcile high-impact conclusions with source-of-record data or independent checks.
- Treat session replay as qualitative evidence that needs privacy and sampling review.
- Require confirmation before live changes, exports, experiments, or permission changes.
