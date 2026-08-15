---
type: "Bundle Overview"
title: "Model Performance and Drift Report overview"
description: "Scope, evidence, and authority boundaries for Model Performance and Drift Report."
---
# Model Performance and Drift Report Overview

Verify model, version, owner, use and risk tier; inspect training and production data lineage, labels and ground truth; define metrics, windows, baselines, thresholds and uncertainty; analyze data, prediction, performance and concept drift plus subgroup behavior; investigate causes and incidents; document limitations, reproducibility, decisions, escalation, rollback, review, and approval.

## Evidence Contract

Relevant evidence includes model card and approved use, version and deployment records, training and production data lineage, feature and prediction distributions, labels and ground truth, monitoring definitions and code, baselines and thresholds, uncertainty and sample sizes, subgroup analysis, incidents and changes, validation, rollback, owners, and approvals. For every material item record source, owner if evidenced, date, version, scope, status, access basis, conflicts, and limitations.

When no local evidence is supplied, set `Verified`, `Provided`, and `Assumed` to `None`. Put exact missing artifacts under `Needs verification`. A general disclaimer is not a substitute for requesting evidence.

## Boundary

Analysis and drafting do not establish model identity, data lineage or quality, ground truth, baseline, threshold, drift, causal explanation, performance, subgroup effect, fairness, validity, incident, fitness for use, or approval. Stop before taking any action to consequential action without evidenced authority and explicit confirmation.
