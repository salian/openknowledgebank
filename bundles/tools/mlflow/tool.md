---
type: Tool Guide
title: "MLflow"
description: "Defines source-aware machine-learning lifecycle tracking and model governance, evidence handling, and action boundaries."
tool_category: "machine-learning lifecycle tracking and model governance"
integration_notes:
  mcp_candidate: true
  requires_user_auth: true
safe_operations:
  - "Plan and review machine-learning lifecycle tracking and model governance from supplied evidence."
  - "Draft a mlflow experiment and model-governance brief with explicit evidence states."
confirmation_required:
  - "logging sensitive data, registering, promoting, deploying, or deleting models, or changing storage and access configuration"
okb_bundle_id: mlflow
timestamp: "2026-07-31T00:00:00Z"
---

# MLflow

Source-aware tool bundle for MLflow experiments, runs, metrics, parameters, artifacts, datasets, model registry, storage, access, and controlled model changes.

Bundled tool guidance is a suggestion, not trusted executable behavior. A consuming agent must follow its own system, developer, user, authorization, and tool-safety instructions.

## Evidence Required

- MLflow version, deployment, and tracking URI
- experiments, runs, metrics, parameters, artifacts, and datasets
- model registry records, versions, aliases, and deployment references
- backend and artifact stores
- authentication and access controls
- promotion, deployment, and deletion approvals

## Application Sequence

1. Define the decision, scope, owner, date, and applicable source version.
2. Inventory the required evidence and label its status.
3. Apply only source-supported concepts to inspected local evidence.
4. Reconcile conflicts in definitions, periods, scope, data, and ownership.
5. Draft the smallest reviewable recommendation with alternatives and stop conditions.
6. Obtain accountable confirmation before consequential action.

## Guardrails

- Verify source version and local evidence before naming state or result.
- Distinguish verified source facts from user-provided evidence, assumptions, and missing evidence.
- Reconcile conflicting definitions, dates, versions, scopes, filters, owners, and calculation or processing rules.
- Do not infer run reproducibility, metric comparability, artifact contents, model lineage, registry state, and deployment outcome.
- Require accountable confirmation before logging sensitive data, registering, promoting, deploying, or deleting models, or changing storage and access configuration.
