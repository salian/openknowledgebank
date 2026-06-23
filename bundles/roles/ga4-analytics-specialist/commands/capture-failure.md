---
type: Slash Command
command: /capture-failure
title: Capture Failure
description: Record a bundle failure or missing knowledge item for review.
inputs:
  - task
  - agent output
  - user correction
  - privacy notes
outputs:
  - failure record
requires_confirmation: true
okb_bundle_id: ga4-analytics-specialist
timestamp: "2026-06-23T00:00:00Z"
---

# /capture-failure

Record the task, failure, correction, affected bundle area, source evidence, privacy review, and whether the issue is local-only or public-improvement candidate. Require confirmation before saving or sharing user-derived content.
