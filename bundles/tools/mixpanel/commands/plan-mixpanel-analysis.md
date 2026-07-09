---
type: Command
title: /plan-mixpanel-analysis
description: Declarative contract for Mixpanel work with source discipline and local evidence separation.
okb_bundle_id: mixpanel
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-mixpanel-analysis

This bundled command is a suggestion for consuming agents, not a trusted executable instruction. It does not grant permissions, override safety rules, or authorize background actions.

## Purpose

Produce a source-aware Mixpanel plan, review, or brief that separates official source categories from local evidence.

## Inputs

- User question and decision to support.
- Local evidence: ['project, event, property, cohort, filter, date range, identity merge, environment, implementation, permission, export, and source-of-record evidence'].
- Any proposed change, publication, commitment, export, or live action.

## Output Contract

Return: `Source note`, `Direct answer`, `Evidence map`, `Findings`, `Risks`, `Recommended next step`, and `Confirmation needed`.

## Risk Boundary

Do not proceed with changing instrumentation, cohorts, dashboards, reports, alerts, exports, permissions, integrations, privacy settings, or user-facing product decisions from Mixpanel evidence without explicit user confirmation.
