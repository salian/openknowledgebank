---
type: Slash Command
command: /prepare-improvement-pr
title: Prepare Improvement PR
description: Prepare a reviewed public PR for a bundle improvement.
inputs:
  - approved improvement proposal
  - changed files
  - test results
outputs:
  - PR summary
  - test notes
  - privacy check
requires_confirmation: true
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# /prepare-improvement-pr

Confirm the change is generalizable and contains no private data, secrets, account IDs, user identifiers, proprietary artifacts, or confidential strategy. Ask for final confirmation before public PR activity.
