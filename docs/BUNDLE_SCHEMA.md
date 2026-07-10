# Bundle Schema

Status: v0.1 working canonical

OpenKnowledgeBank bundles follow the spirit of OKF: markdown files with YAML frontmatter, organized into portable directories.

This schema is intentionally expected to evolve after the first few bundles.

## Required Bundle Files

Role bundles must include:

```text
index.md
log.md
role.md
```

Non-role bundles should include a category-specific equivalent:

- compliance: `overview.md`
- tools: `tool.md`
- frameworks: `framework.md`
- deliverables: `deliverable.md`
- jurisdictions: `jurisdiction.md`
- datasets: `dataset.md`

## Recommended Directories

```text
responsibilities/
workflows/
playbooks/
metrics/
tools/
frameworks/
deliverables/
commands/
skills/
evaluations/
examples/
references/
```

## Concept Frontmatter

Every markdown concept file must include `type`.

Recommended:

```yaml
---
type: Workflow
title: Diagnose Conversion Drop
description: ""
tags: []
okb_bundle_id: ga4-analytics-specialist
timestamp: 2026-06-21T00:00:00Z
---
```

## Bundle Index Frontmatter

`index.md` should include:

```yaml
---
type: Bundle Index
title: GA4 Analytics Specialist
description: Entry point for the GA4 Analytics Specialist OpenKnowledge bundle.
okb_bundle_id: ga4-analytics-specialist
okb_bundle_version: "0.1.0"
status: draft
trust_tier: trusted
license: CC-BY-4.0
timestamp: 2026-06-21T00:00:00Z
---
```

## Registry Metadata

The website and agents use:

```text
registry/bundles.json
```

Required registry fields:

- `id`
- `title`
- `description`
- `category`
- `path`
- `repo`
- `license`
- `trust_tier`
- `status`
- `version`
- `source_url`
- `download_url`

Recommended fields:

- `tags`
- `aliases`
- `problems_solved`
- `industries`
- `tools`
- `frameworks`
- `deliverables`
- `commands`
- `skills`
- `evaluations`
- `related_bundles`
- `adjacent_bundles`
- `jurisdictions`
- `authorities`
- `contributors`
- `maintainers`
- `standard_mappings`
- `limitations`
- `safety_notes`

## Trust Tiers

- `trusted`: reviewed and maintained by OpenKnowledgeBank.
- `community`: external repository or contribution that passed basic review.
- `unverified`: submitted or discovered resource that has not been reviewed.
- `rejected`: unsafe, spam, malicious, noncompliant, or unsuitable.

## Status Values

- `draft`
- `beta`
- `stable`
- `deprecated`

## Validation

Phase 1 validation should use:

- errors for broken required structure
- warnings for missing recommended metadata
- info messages for improvement suggestions
