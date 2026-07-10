# Jarvis Closeout Task Contracts

## Actor Contract

Goal: inspect the current dashboard and Jarvis implementation, identify stale or defective behavior, and propose or implement only the smallest evidence-backed corrections.

Evidence required:

- file and line references;
- generation/runtime/browser commands and results;
- explicit browser-local versus external-save classification;
- changed-file list and diff summary when edits are justified.

Forbidden:

- provider activation;
- secret handling in public output;
- deployment or Telegram action;
- unsupported always-online, persistence, or writeback claims.

## Reviewer Contract

Goal: independently audit dashboard/Jarvis proof, hosted-state evidence, PDF publication safety, public-link availability, and Telegram sender/target readiness.

Evidence required:

- pass/fail/block per proof lane;
- exact commands or connector checks;
- public-safe PDF inclusion/exclusion rationale;
- Telegram send recommendation: approve, revise, or block.

Forbidden:

- file edits;
- deployment;
- Telegram send;
- disclosure of private targets, URLs, identifiers, or credentials.

## Integrator Contract

Goal: review both outputs, apply justified fixes, run the complete validation set, publish only public-safe artifacts, push verified changes, then send Telegram once all sender/target/link gates pass.

The integrator owns final claims, commit/push, external-action ordering, durable run notes, and rollback evidence.
