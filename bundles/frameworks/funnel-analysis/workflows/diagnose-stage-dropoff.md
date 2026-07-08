---
type: Workflow
title: Diagnose Stage Drop-Off
description: "Analyze where funnel progression changes while separating measurement findings from causal hypotheses."
okb_bundle_id: funnel-analysis
timestamp: "2026-07-09T00:00:00Z"
---

# Diagnose Stage Drop-Off

## Steps

1. Confirm that the funnel definition and denominator basis are verified.
2. Identify the largest absolute and relative changes by stage, using the provided comparison period.
3. Check whether the change is concentrated in a segment, channel, device, geography, cohort, experiment variant, or source.
4. Review measurement-health risks: event firing, tag releases, consent mode, schema changes, filters, data freshness, and report sampling or thresholds when relevant.
5. Separate expected differences from unresolved discrepancies.
6. Generate hypotheses only from observed patterns and known changes.
7. Define the validation needed for each hypothesis before recommending live changes.

## Output

Use [Funnel Analysis Brief](../deliverables/funnel-analysis-brief.md).

## Do Not Claim

- Do not say a step caused the drop-off unless corroborating evidence supports it.
- Do not compare rates with different denominators as if they are the same metric.
- Do not assume that "no next action" always means user abandonment; tool and dimension behavior can affect that interpretation.
