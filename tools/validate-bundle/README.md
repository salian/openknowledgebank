# Bundle Validator

Planned validator for OpenKnowledgeBank bundles.

Initial checks should include:

- every markdown concept has YAML frontmatter
- every concept has a `type`
- each bundle has `index.md`
- each bundle has `log.md`
- registry entries point to existing bundle paths
- bundle IDs and paths match naming rules
