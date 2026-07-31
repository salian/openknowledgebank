---
type: Workflow
title: Machine Learning Engineer source-aware triage
---
# Source-Aware Triage

1. State the requested decision or artifact.
2. Inventory evidence: use case, affected users, decision stakes, owners, and acceptance criteria; datasets, provenance, consent, licenses, lineage, splits, and representativeness; model, code, features, dependencies, configurations, and environment versions; evaluation design, baselines, metrics, uncertainty, subgroup and robustness tests; security, privacy, human oversight, deployment, monitoring, rollback, incidents, and approvals.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, calculations, and owners.
5. Produce the smallest reviewable machine-learning delivery brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the evidenced reviewer, or `Needs verification`, and prohibited actions
- **Source note** with sources and limitations
