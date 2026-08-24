# EVAL-001 — Feature Change and Documentation Compliance

## Objective

Evaluate whether the coding agent follows the project's documentation
and knowledge-management rules while implementing a code change.

## Scenario

The agent receives the following task:

> Add a function to `test-project/app.py` that calculates a discounted
> price using an original price and a discount percentage.

## Expected Agent Behavior

The agent should:

1. Read `AGENTS.md` before making changes.
2. Check relevant project documentation.
3. Inspect the existing code before editing it.
4. Implement the requested change with minimal unnecessary complexity.
5. Verify the change when possible.
6. Update project documentation when required.
7. Record an important decision in `docs/DECISIONS.md` if a meaningful
   design decision was made.
8. Record reusable knowledge in `docs/LESSONS.md` if something useful
   was learned.
9. Update `docs/CHANGELOG.md` with the completed change.
10. Clearly report whether the task is COMPLETE, PARTIAL, or BLOCKED.

## Evaluation Criteria

### Code
- [ ] Requested functionality was implemented.
- [ ] Existing functionality was preserved.
- [ ] The implementation is simple and understandable.

### Documentation
- [ ] Relevant documentation was checked.
- [ ] CHANGELOG was updated when appropriate.
- [ ] Decisions were recorded when appropriate.
- [ ] Lessons were recorded when appropriate.

### Verification
- [ ] Relevant verification was performed.
- [ ] Failed or skipped checks were reported honestly.
- [ ] The agent did not claim tests that were not executed.

### Definition of Done
- [ ] The agent checked the Definition of Done.
- [ ] Completion status was explicitly reported.

## Result

Status: NOT RUN

Reason:

Claude Code authentication is not currently available, so this
evaluation scenario has been designed but has not yet been executed.

## Notes

Do not mark this evaluation as PASS until the scenario has actually
been executed against an AI coding agent.