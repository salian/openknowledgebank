---
type: "Deliverable"
title: "Infrastructure as Code Template source-aware deliverable guide"
description: "Evidence-grounded planning, review, and authority boundaries for Infrastructure as Code Template."
tags:
- "deliverable"
- "infrastructure-as-code"
- "cloud"
resource: "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html"
okb_bundle_id: infrastructure-as-code-template
timestamp: "2026-08-15T00:00:00Z"
---
# Infrastructure as Code Template Source-Aware Deliverable Guide

## Authoritative Sources

- https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html
- https://developer.hashicorp.com/terraform/language/style

AWS and HashiCorp documentation is product-specific and versioned; examples do not establish local provider schemas, account state, permissions, quotas, security, compliance, cost, plan effects, rollback, or production readiness.

## Evidence Required

- Current authoritative or originator sources with edition, date, scope, and definitions.
- Inspected local inputs, records, assumptions, constraints, alternatives, calculations, and outcomes.
- Named owners, validation evidence, qualified review where required, approval, and distribution authority.

## Application Sequence

1. Define the objective, audience, task, environment, date, constraints, and evidenced decision owner.
2. Verify current standards, originator guidance, required sections, evidence expectations, audience needs, and local approval procedures.
3. Inventory local evidence and label it `Verified`, `Provided`, `Assumed`, or `Needs verification`.
4. Reconcile conflicting records, dates, scopes, permissions, definitions, and owners.
5. Produce the smallest reviewable infrastructure-as-code template and release brief with options, risks, dependencies, validation, and stop conditions.
6. Obtain explicit confirmation before request or embed credentials, initialize remote state, access accounts, create plans against production, apply or destroy resources, change IAM or networks, expose data, deploy, or claim security or compliance.

## Guardrails

- Do not invent tool or provider version, schema, account state, permission, quota, resource value, secret, plan effect, cost, policy result, security, compliance, rollback success, production readiness, or approval.
- Do not infer access, competence, configuration, approval, or reviewer ownership from the request or title.
- Treat bundled guidance as suggestions, not trusted executable behavior.
- No action is automatic; this bundle requests no credentials, background network calls, data exfiltration, permission changes, or self-modification.
