---
type: Role
title: Machine Learning Engineer Source-Aware Guide
description: Defines source-aware machine-learning engineering and model operations, evidence handling, and action boundaries.
tags:
- machine-learning-engineer
- machine-learning
- role
resource: https://www.onetcenter.org/dl_files/database/db_27_2_text/Alternate%20Titles.txt
okb_bundle_id: machine-learning-engineer
timestamp: '2026-07-31T00:00:00Z'
---
# Machine Learning Engineer Source-Aware Guide

Source-aware role bundle for machine-learning engineering and model operations, evidence reconciliation, reviewable recommendations, and controlled consequential actions.

Apply this guidance as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- use case, affected users, decision stakes, owners, and acceptance criteria
- datasets, provenance, consent, licenses, lineage, splits, and representativeness
- model, code, features, dependencies, configurations, and environment versions
- evaluation design, baselines, metrics, uncertainty, subgroup and robustness tests
- security, privacy, human oversight, deployment, monitoring, rollback, incidents, and approvals

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
- Do not infer data fitness, model performance, fairness, robustness, causality, production behavior, risk acceptance, or approval.
- Do not invent an artifact owner, author, date, or version.
- Require accountable confirmation before training on sensitive data, deploying models, changing decision thresholds, exposing endpoints, or claiming safety, fairness, or compliance.
