---
type: Workflow
title: Software Developer / Software Engineer Source-Aware Triage
---

# Source-Aware Triage

1. State the requested decision or deliverable.
2. Inventory evidence: requirements and acceptance criteria, repository and revision state, architecture and interface contracts, dependency versions, tests and static analysis, runtime telemetry, deployment and rollback controls.
3. Label each item as verified, provided, assumed, or needs verification.
4. Reconcile conflicting definitions, dates, scopes, and sources.
5. Produce the smallest reviewable Software change implementation and review brief.
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
