---
type: Workflow
title: "Jenkins source-aware triage"
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: Jenkins version and controller scope, agents, labels, executors, and node state, job, pipeline, multibranch, and Jenkinsfile definitions, plugins, dependencies, and compatibility evidence, credentials references and permission boundaries, build parameters, logs, artifacts, and test results, and environment, deployment, rollback, and approval evidence.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, and owners.
5. Produce the smallest reviewable jenkins pipeline and change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the reviewer and prohibited unapproved actions
- **Source note** with sources and limitations
