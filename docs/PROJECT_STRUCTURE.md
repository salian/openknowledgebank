# Public Repository Structure

This repository is the public source for OpenKnowledgeBank bundles.

## What Belongs Here

- Publishable OpenKnowledge bundles.
- Public registry files.
- Bundle schemas and validators.
- Contribution guidance.
- Public examples.
- Public documentation for users and contributors.

## What Does Not Belong Here

- Private strategy.
- Roadmaps that are not ready to publish.
- Monetization plans.
- Internal operating notes.
- Raw research notes with licensing uncertainty.
- Website application code.
- Secrets, API keys, credentials, personal data, or private source material.

## Security Note

This is a public repository. Assume anything committed here can become visible on GitHub and reused by others.

Before committing or pushing, review changes for accidental private context, credentials, unpublished strategy, source material with unclear rights, and internal planning notes.

## Directory Layout

```text
bundles/
  roles/
  industries/
  capabilities/
  tools/
  frameworks/
  compliance/
  jurisdictions/
  deliverables/
  datasets/
registry/
schemas/
tools/
examples/
docs/
```

## Agent Discovery

Agents and LLMs should use:

- `AGENT_USAGE.md`
- `registry/bundles.json`
- `registry/external-repos.json`
- `registry/suggestions.json`

These files help agents discover bundles, understand trust tiers, recommend adjacent bundles, install bundle content locally, and suggest missing bundles.

## Bundle Rule

Each bundle should be a downloadable knowledge module. A role bundle should include enough concepts, workflows, metrics, examples, and references for an LLM agent to perform useful work in that role. Non-role bundles should model their category directly rather than pretending to be a role.

Examples:

- compliance: AVETMISS compliance
- tool: HubSpot
- framework: Minto's Pyramid Principle
- deliverable: target persona
- jurisdiction: Australia
- dataset: GA4 sample ecommerce dataset

## Agent Affordances

Bundles may include optional agent affordances that help agents act, not just understand.

Recommended optional directories:

- `frameworks/`: reusable thinking structures and role-specific frameworks.
- `tools/`: safe and useful tool guidance.
- `workflows/`: repeatable processes.
- `deliverables/`: output templates and quality criteria.
- `commands/`: suggested slash commands or user-facing actions.
- `skills/`: reusable runtime-compatible capabilities, where supported.
- `evaluations/`: checks and rubrics for judging agent performance.

Affordance files are still bundle content and must follow the same safety and review expectations as other concepts.

## Public Positioning

This repository should present OpenKnowledgeBank as a free, open, inspectable, and remixable library for AI agent knowledge.

Public copy should prioritize:

- View on GitHub.
- Download.
- Use with your agent.
- Contribute.

Avoid ads, gated downloads, premium bundle messaging, and commercial CTAs in Phase 1.
