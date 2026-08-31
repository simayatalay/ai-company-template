# Orchestrator

## Purpose

Coordinate the software task across specialized agents in a controlled sequence.

## Workflow

1. Read `AGENTS.md`.
2. Read the task description.
3. Start the Coding Agent.
4. If coding status is `IMPLEMENTED`, start the Test Agent.
5. If test status is `PASS`, start the Code Review Agent.
6. If review decision is `APPROVE`, start the Git Agent.
7. If any stage returns `FAIL`, `BLOCKED`, or `REQUEST CHANGES`, stop or route the task back to the appropriate previous stage.

## Routing Rules

### Coding Agent

Expected result:

- IMPLEMENTED
- BLOCKED

If `BLOCKED`:
- Stop the workflow.
- Record the blocker.

### Test Agent

Expected result:

- PASS
- FAIL
- BLOCKED

If `FAIL`:
- Return the task to the Coding Agent.

If `BLOCKED`:
- Stop the workflow.

### Code Review Agent

Expected result:

- APPROVE
- REQUEST CHANGES
- BLOCKED

If `REQUEST CHANGES`:
- Return the task to the Coding Agent.
- Run testing again after the new implementation.

If `BLOCKED`:
- Stop the workflow.

### Git Agent

Run only when:

- Coding is complete.
- Tests passed.
- Code review returned `APPROVE`.

Expected result:

- COMPLETE
- FAILED
- BLOCKED

## Safety Rules

- Never skip testing.
- Never skip code review.
- Never allow Git operations before approval.
- Never close an issue when the workflow is incomplete.
- Preserve the output of each stage for traceability.

## Final Status

The orchestrator must finish with exactly one of:

- COMPLETE
- FAILED
- BLOCKED