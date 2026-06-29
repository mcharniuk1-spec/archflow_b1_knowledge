# Anti-Looping Review

## Adopted Controls

- L1 report-only default.
- State schema added under `project/loops/`.
- `max_revision_loops` remains 2.
- Item retry cap set to 3.
- Maker/checker split required.
- External writes blocked by default.
- Cloud model use blocked by default.

## Parallel Execution Rule

Allowed in E2:

- account universe collection
- company website parsing
- job-signal extraction
- review mining
- social-language mining
- competitor gap mapping

Sequential only:

- synthesis
- role verification
- message approval
- memory promotion
- Notion updates
- outreach
- payment verdict
