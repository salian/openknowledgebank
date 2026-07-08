---
type: Deliverable
title: Jira Board Cleanup Plan
description: "Output format for source-scoped Jira board, workflow, JQL, report, automation, or API cleanup planning."
okb_bundle_id: jira
required_inputs:
  - Jira cleanup goal
  - Jira local evidence
  - official source categories
  - permission and confirmation constraints
outputs:
  - direct answer
  - source note
  - verified and missing evidence
  - cleanup plan
  - query/report/workflow self-check
  - risk and confirmation boundary
quality_criteria:
  - Does not invent Jira local configuration.
  - Separates official Atlassian behavior from user-provided Jira evidence.
  - Requires confirmation before live changes.
timestamp: "2026-07-09T00:00:00Z"
---

# Jira Board Cleanup Plan

## Required Sections

1. Direct answer.
2. Source note.
3. Verified facts.
4. Missing evidence.
5. Board, backlog, workflow, JQL, report, automation, or API plan.
6. Query/report/workflow self-check.
7. Risk and impact review.
8. Validation and confirmation boundary.

## Quality Bar

A strong Jira cleanup plan avoids unverified local claims, asks for the right Jira evidence, reconciles board/report/JQL/API differences carefully, and marks every live change as requiring explicit confirmation.

## Source Note Requirement

Name the official Atlassian source category, the user-provided Jira evidence used, and the missing evidence required before treating the plan as final or taking action.
