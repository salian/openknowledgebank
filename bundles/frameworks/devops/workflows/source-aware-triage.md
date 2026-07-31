---
type: Workflow
title: "DevOps source-aware triage"
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: product and value-stream scope, repositories, pipelines, environments, and deployment process, change, release, and rollback evidence, reliability, incident, recovery, and service telemetry, security, access, secrets, and supply-chain controls, and metric definitions, source systems, periods, and current DORA guidance.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, calculations, and owners.
5. Produce the smallest reviewable devops delivery and reliability brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the evidenced reviewer, or `Needs verification` when no reviewer evidence is provided, and prohibited unapproved actions
- **Source note** with sources and limitations
