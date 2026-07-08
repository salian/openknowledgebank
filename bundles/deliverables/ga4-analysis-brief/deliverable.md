---
type: Deliverable
title: GA4 Analysis Brief
description: "A decision-ready brief for GA4 reports, explorations, and export-based analysis."
okb_bundle_id: ga4-analysis-brief
required_inputs:
  - user question and decision context
  - GA4 report, exploration, export, or schema evidence
  - date range and comparison period
  - metric and dimension definitions
  - filters, segments, comparisons, and attribution context
outputs:
  - direct answer
  - source scope
  - findings
  - caveats
  - hypotheses
  - recommended next actions
quality_criteria:
  - Does not invent access, events, schemas, metrics, or causes.
  - Names source scope, date range, filters, and definitions.
  - Separates observations from hypotheses.
  - Includes a visible source note.
timestamp: "2026-07-09T00:00:00Z"
---

# GA4 Analysis Brief

## Required Sections

1. **Direct answer**: the best answer supported by the current evidence, plus what cannot be concluded yet.
2. **Source scope**: GA4 property/report/exploration/export source, date range, timezone, comparison period, filters, segments, attribution, and data freshness.
3. **Metric and dimension definitions**: names, definitions, grain, entity logic, and any differences between GA4 UI and export/warehouse data.
4. **Findings**: verified observations, sized where data is provided, with expected differences separated from unresolved discrepancies.
5. **Caveats and missing evidence**: settings, implementation, schema, consent, thresholding, sampling, source-of-record, or business context still needed.
6. **Hypotheses**: possible explanations, each tied to evidence and required validation.
7. **Recommended next actions**: analysis and verification first; live changes only after explicit confirmation.
8. **Source note**: official source category, user evidence, and missing verification.

## Quality Bar

A good brief lets a decision-maker act on what is known while preserving enough source detail for an analyst to reproduce or challenge the conclusion.
