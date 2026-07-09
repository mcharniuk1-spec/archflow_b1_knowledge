# Final Publish Plan

Status: prepared only. No external action is approved or executed by this file.

## Preconditions

- Implementation files exist.
- Validation checks pass or gaps are recorded.
- Final QA reviewer approves or required fixes are completed.
- Owner explicitly approves the specific side effect.

## Approval-Gated Sequence

1. Show `git status` and diff summary.
2. Run final validation:
   - public safety scan;
   - dashboard data regeneration and JSON parse;
   - YAML/JSON parse checks;
   - Python compile for changed Python files;
   - `git diff --check`.
3. Update run handout, KB/log candidates, and validation results.
4. Commit with message: `founder-method hermes-cag-rag architecture update`.
5. Push to Git only after owner approval.
6. Deploy or promote website only after owner approval.
7. Perform Notion update only after owner approval and connector/writeback access.
8. Perform Railway, Telegram, Linear, Figma, or provider actions only after explicit approval for that specific target.

## Blocked By Default

- Git push.
- Website deployment.
- Production promotion.
- Provider calls.
- Notion mutation.
- Linear mirror.
- Telegram send.
- Railway action.
- Figma sync.
- Durable external writeback.
