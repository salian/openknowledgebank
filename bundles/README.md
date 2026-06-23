# Bundles

OpenKnowledgeBank bundles are organized into multiple categories:

- `roles/`: job-like agent roles.
- `industries/`: domain bundles that provide business or sector context.
- `capabilities/`: reusable capability bundles that can support many roles.
- `tools/`: platform, API, and product knowledge.
- `frameworks/`: reusable thinking models and methodologies.
- `compliance/`: compliance regimes, reporting standards, rules, and regulations.
- `jurisdictions/`: reusable legal, geographic, or regulatory context.
- `deliverables/`: specific output types and quality standards.
- `datasets/`: data/catalog style knowledge bundles.

Each bundle is a directory of markdown concepts with YAML frontmatter.

## Optional Agent Affordances

Bundles may include directories that make the knowledge easier for agents to use:

- `frameworks/`
- `tools/`
- `workflows/`
- `deliverables/`
- `commands/`
- `skills/`
- `evaluations/`

These directories are optional, but high-quality bundles should include the ones that materially improve agent performance.
