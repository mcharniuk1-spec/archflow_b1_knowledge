# Contributing

Thank you for helping improve ArchFlow's public reference implementation.

## Before a pull request

1. Keep the change scoped and public-safe.
2. Do not add private source material, credentials, local paths, customer data, or unreviewed skills.
3. Update the relevant contract and documentation when behavior or a public claim changes.
4. Regenerate dashboard data when a source it indexes changes.
5. Run the smallest relevant checks from the [quickstart](docs/quickstart.md#verify-a-checkout).

Changes to roles, requirements, validation, promotion, or adapters must preserve the unified Knowledge Case contract and add or update a provider-disabled fixture. Do not reintroduce PRD/ICP and agent control as separate top-level architectures.

## Contributions involving skills, retrieval, or agents

New skills must pass provenance, license, portability, path/secret safety, sanitized fixture, independent-review, and catalog-entry gates. Do not bulk-copy a private local skill library. Role names are functional contracts; a contribution must state the role's sources, tools, output, reviewer, and forbidden actions.

Structural tools such as Orbit or Graphify provide generated evidence, not requirements authority. Any local index must use an explicit corpus, remain ignored/private, expose read-only bounded operations by default, and return sanitized repository-relative references.

## Pull request description

State the objective, changed files, source boundary, checks run, known gaps, and whether the change affects provider use, database access, deployment, Git, or external writeback. Those actions are not enabled by a code contribution alone.
