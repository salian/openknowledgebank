# OpenKnowledgeBank

OpenKnowledgeBank is a public collection of downloadable knowledge bundles for LLM agents.

Each bundle is designed to help an AI agent perform serious work in a specific role, industry, or capability area. The project follows the spirit of Open Knowledge Format: simple markdown files with YAML frontmatter, organized into portable directories.

Bundles can also represent tools, frameworks, compliance regimes, jurisdictions, deliverables, and datasets.

OpenKnowledgeBank is free to use, inspect, remix, and contribute to.

## Repository Structure

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

## Bundle Types

- `roles/`: job-like agent roles, such as `performance-marketer`.
- `industries/`: domain context that can enrich role bundles.
- `capabilities/`: reusable skill or workflow knowledge, such as analytics or market research.
- `tools/`: platform, API, or product knowledge.
- `frameworks/`: reusable thinking models and methodologies.
- `compliance/`: rules, standards, and regulatory regimes.
- `jurisdictions/`: reusable legal, geographic, or regulatory context.
- `deliverables/`: output types and quality standards.
- `datasets/`: data/catalog style knowledge bundles.

## Current Status

This repository is being bootstrapped. The first seed bundle is:

- `bundles/roles/performance-marketer`

## Use and Contribute

- Browse the bundle folders.
- Download or fork the repository.
- Use bundles with your own agents.
- Contribute improvements or new bundles.

See `docs/BUNDLE_CREATION_PROCESS.md` for the recommended process for creating a new bundle.

Agents and LLMs should start with `AGENT_USAGE.md` and `registry/bundles.json`.

See `docs/BUNDLE_SCHEMA.md` for the current working canonical bundle schema.

## License

Knowledge bundles are licensed under Creative Commons Attribution 4.0 International.

Code and tooling are licensed under MIT.

See `LICENSE.md` and `LICENSE-CODE.md`.
