---
type: Slash Command
command: /prepare-improvement-pr
title: Prepare Improvement PR
description: Prepare a reviewed bundle improvement for contribution back to OpenKnowledgeBank.
okb_bundle_id: performance-marketer
inputs:
  - approved_candidate_patch
  - reviewer_notes
outputs:
  - pr_summary
  - changed_files
  - safety_notes
  - source_notes
requires_confirmation: true
timestamp: 2026-06-20T00:00:00Z
---

# Prepare Improvement PR

Use this command only after a human has reviewed and approved a candidate improvement.

Do not create or submit a PR silently.

## PR Notes

The PR should explain:

- what failed or was missing
- why the improvement is generally useful
- which files changed
- what sources or rationale support the change
- safety, privacy, and licensing considerations
