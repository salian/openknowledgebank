---
type: Command
title: /plan-amplitude-analysis
description: "Declarative contract for planning an Amplitude analysis from verified source categories and local evidence."
okb_bundle_id: amplitude
timestamp: "2026-07-09T00:00:00Z"
---

# /plan-amplitude-analysis

This bundled command is a suggestion for consuming agents, not a trusted executable instruction. It does not grant permissions, override safety rules, or authorize background actions.

## Purpose

Produce an Amplitude analysis plan or interpretation brief that names the question, required evidence, metric definitions, and risk checks before drawing conclusions.

## Inputs

- Analysis question and decision to support.
- Amplitude evidence: chart links or screenshots, event names, property definitions, cohorts, filters, time range, environment, identity logic, experiment details, replay evidence, exports, and permissions.
- Source-of-record evidence when the decision is high impact.

## Output Contract

Return:

- `Source note`: Amplitude source category, local evidence used, and missing evidence.
- `Direct answer`: concise answer or status.
- `Metric definition`: events, properties, filters, time window, aggregation, identity logic, and exclusions.
- `Evidence quality`: data freshness, instrumentation risk, sampling/replay limits, privacy constraints, and source-of-record reconciliation.
- `Findings`: what the evidence supports, what it does not support, and alternative explanations.
- `Next step`: analysis, instrumentation, experiment, or review action.
- `Confirmation needed`: any live change, export, permission, experiment, or user-facing action.
