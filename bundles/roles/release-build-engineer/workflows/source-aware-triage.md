---
type: Workflow
title: Release / Build Engineer Source-Aware Triage
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: source revision and branch policy, build definition, dependency lock state, artifact digest and provenance, test and scan results, environment promotion policy, change approvals, rollback procedure.
3. Label each item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, scopes, and sources.
5. Produce the smallest reviewable Build and release readiness brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification` entries
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the reviewer and prohibited unapproved actions
- **Source note** with sources and limitations

## Source Note

Name the authoritative source category, local evidence used, assumptions, and
missing facts. A polished draft is not proof that its claims are true.
