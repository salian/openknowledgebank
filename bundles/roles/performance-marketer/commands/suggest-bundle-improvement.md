---
type: Slash Command
command: /suggest-bundle-improvement
title: Suggest Bundle Improvement
description: Convert reviewed feedback into a candidate performance marketer bundle improvement.
okb_bundle_id: performance-marketer
inputs:
  - feedback_note
  - classification
  - source_or_rationale
outputs:
  - proposed_change
  - affected_files
  - review_checklist
requires_confirmation: true
timestamp: 2026-06-20T00:00:00Z
---

# Suggest Bundle Improvement

Use this command to turn a reviewed feedback note into a candidate bundle improvement.

Before proposing a public change, confirm that the improvement is generalizable, safe, free of private data, and consistent with the bundle structure.

## Required Review

- Is this useful beyond one user?
- Does it contain private or confidential context?
- Does it require a source?
- Does it affect tool safety?
- Which bundle files should change?
- Should it remain local instead of becoming public?
