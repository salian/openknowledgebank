---
type: Workflow
title: HIPAA Eligibility and Claim Status Operating Rules Source-Aware Triage
description: Workflow for converting a sparse question into an evidence-backed brief.
okb_bundle_id: hipaa-eligibility-claim-status-operating-rules
timestamp: "2026-07-09T00:00:00Z"
---

# Source-Aware Triage

## Inputs

- User question and intended decision.
- Official source category already inspected, if any.
- Local evidence relevant to Eligibility and claim status operating rules.
- Missing documents, system records, transaction artifacts, contracts, policies, incident facts, or implementation guides.

## Steps

1. Classify the request as Eligibility and claim status operating rules work or route it back to the broader [HIPAA](../../hipaa/index.md) hub.
2. Identify the official source category using [source-map.md](../requirements/source-map.md).
3. Ask only for minimum necessary, redacted evidence; avoid collecting unnecessary PHI/ePHI.
4. Separate verified source facts, user-provided facts, assumptions, and missing evidence.
5. Draft the [source-aware brief](../deliverables/source-aware-brief.md).
6. Mark professional review and explicit confirmation requirements for any risky action.

## Output Contract

The final output should include: direct answer, source note, evidence matrix, missing evidence, risk boundary, and next steps.
