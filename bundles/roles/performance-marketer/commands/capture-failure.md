---
type: Slash Command
command: /capture-failure
title: Capture Failure
description: Record a performance marketer agent failure or user correction as a private improvement note.
okb_bundle_id: performance-marketer
inputs:
  - observed_failure
  - user_correction
  - context
outputs:
  - feedback_note
  - classification
  - recommended_next_action
requires_confirmation: true
timestamp: 2026-06-20T00:00:00Z
---

# Capture Failure

Use this command to record a failure, weak output, or user correction as a possible bundle improvement.

Do not write private user context into the public bundle. Store feedback privately first and remove secrets, personal data, confidential business details, and copyrighted material.

## Classification

Classify the issue as one or more:

- personal preference
- missing role knowledge
- missing workflow
- missing tool guidance
- missing framework
- missing deliverable format
- missing evaluation
- bad or unsafe guidance
- source/reference gap
- terminology gap

## Next Action

Recommend one of:

- ignore
- record as local preference
- research further
- propose candidate bundle patch
- escalate as safety issue
