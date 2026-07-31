---
type: Workflow
title: "GitHub source-aware triage"
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: repository and organization scope, commit, branch, tag, and default-branch state, pull requests, reviews, issues, and discussions, checks, workflow runs, logs, and artifacts, rulesets, environments, secrets, and permissions, release and deployment evidence, and security and audit evidence.
3. Label every item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, versions, scopes, filters, states, and owners.
5. Produce the smallest reviewable github repository change brief.
6. Require accountable confirmation before consequential action.

## Required Output Sections

- **Direct answer**
- **Evidence status** with separate `Verified`, `Provided`, `Assumed`, and `Needs verification`
- **Verification plan** naming source category, scope, date or version, and conflict checks
- **Confirmation boundary** naming the reviewer and prohibited unapproved actions
- **Source note** with sources and limitations
