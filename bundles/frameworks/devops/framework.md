---
type: Framework
title: "DevOps Source-Aware Application Framework"
description: "Defines source-aware software delivery and operational performance, evidence handling, and action boundaries."
tags:
  - "devops"
  - "software-delivery"
  - "reliability"
  - "framework"
resource: https://dora.dev/
okb_bundle_id: devops
timestamp: "2026-07-31T00:00:00Z"
---

# DevOps Source-Aware Application Framework

Source-aware framework bundle for improving software delivery and operations through value-stream, delivery, reliability, security, telemetry, and controlled-change evidence.

Apply the framework as a decision aid, not as proof of local facts, outcomes, compliance, professional judgment, or authorization.

## Evidence Required

- product and value-stream scope
- repositories, pipelines, environments, and deployment process
- change, release, and rollback evidence
- reliability, incident, recovery, and service telemetry
- security, access, secrets, and supply-chain controls
- metric definitions, source systems, periods, and current DORA guidance

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
- Do not infer deployment state, pipeline result, metric definition, incident cause, reliability impact, and change authorization.
- Require accountable confirmation before deploying or rolling back production, changing pipelines or infrastructure, handling credentials, changing access, or declaring performance improvements without comparable evidence.
