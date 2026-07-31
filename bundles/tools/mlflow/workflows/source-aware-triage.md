---
type: Workflow
title: "MLflow source-aware triage"
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: MLflow version, deployment, and tracking URI, experiments, runs, metrics, parameters, artifacts, and datasets, model registry records, versions, aliases, and deployment references, backend and artifact stores, authentication and access controls, and promotion, deployment, and deletion approvals.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, calculations, and owners.
5. Produce the smallest reviewable mlflow experiment and model-governance brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the evidenced reviewer, or `Needs verification` when no reviewer evidence is provided, and prohibited unapproved actions
- **Source note** with sources and limitations
