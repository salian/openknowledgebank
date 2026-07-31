---
type: Workflow
title: Data Scientist source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: question, population, decision, and success criteria; data provenance, consent, lineage, definitions, and access; code, environment, methods, assumptions, train-test split, and leakage controls; metrics, uncertainty, subgroup analysis, privacy, security, deployment, and monitoring evidence.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, calculations, methods, and owners.
5. Produce the smallest reviewable data science analysis brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`; record explicit request facts as `Prompt-provided request` under `Provided`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the evidenced reviewer, or `Needs verification`, and prohibited actions
- **Source note** with sources and limitations
