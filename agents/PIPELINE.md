# Multi-Agent Engineering Pipeline

## Purpose

Execute software tasks through a controlled sequence of specialized roles.

The pipeline should separate implementation, testing, review, and repository
operations whenever possible.

The goal is to make software changes traceable, verifiable, and reproducible.

---

## Core Workflow

1. Read project instructions and task context.
2. Create or link the work to an issue or ticket.
3. Run the Coding Agent.
4. Run required verification and tests.
5. Run the Test Agent.
6. Run the Code Review Agent.
7. If review is approved, run the Git Agent.
8. Update the issue or ticket with progress and evidence.
9. Close the issue only when all required quality gates have passed.

---

## Role Responsibilities

### Coding Agent

Responsible for:

- understanding the requested change,
- modifying only the required code,
- keeping the implementation simple and focused.

The Coding Agent should not perform final approval or repository publishing.

### Test Agent

Responsible for:

- checking expected behavior,
- evaluating available test evidence,
- reporting PASS, FAIL, or BLOCKED.

Testing may include different environments such as browser, desktop, CLI,
API, unit, integration, or project-specific tests.

### Code Review Agent

Responsible for:

- reviewing the resulting implementation,
- identifying correctness, scope, maintainability, or quality issues,
- returning APPROVE, REQUEST CHANGES, or BLOCKED.

The reviewer should not approve work when required verification evidence is
missing.

### Git Agent

Responsible for:

- staging intended changes,
- creating focused commits,
- pushing changes when allowed,
- updating repository-related issue or ticket status.

The Git Agent must not proceed before required testing and review gates pass.

### Orchestrator

Responsible for:

- running roles in the correct order,
- passing relevant context between stages,
- stopping the pipeline when a blocking condition occurs,
- routing failed work back to the appropriate stage.

---

## Quality Gates

The pipeline must stop when:

- required verification fails,
- a required test fails,
- the Test Agent returns FAIL or BLOCKED,
- the Code Review Agent returns REQUEST CHANGES or BLOCKED,
- repository operations fail,
- required context is unavailable.

No later stage should override an earlier failed quality gate.

---

## Retry and Feedback Flow

If implementation-related verification fails:

Coding Agent
↓
Verification / Test
↓
FAIL
↓
Return to Coding Agent

If review requests changes:

Code Review Agent
↓
REQUEST CHANGES
↓
Return to Coding Agent
↓
Re-run verification and testing
↓
Re-run review

Previously passed checks should be repeated when the implementation changes
in a way that may invalidate them.

---

## Issue / Ticket Lifecycle

Each significant task should be traceable through an issue or ticket.

The issue may record:

- original problem or request,
- current status,
- implementation progress,
- verification results,
- test results,
- review decision,
- commit or repository status,
- final resolution.

An issue should not be closed while required work remains blocked or
unverified.

---

## Rules

- Do not skip required testing or review.
- Do not report tests as executed when they were not run.
- Keep changes focused on the requested task.
- Preserve role boundaries.
- Record blocking failures clearly.
- Use evidence rather than agent confidence as the basis for completion.
- Do not commit or push changes before required quality gates pass.
- Re-run relevant checks after implementation changes.
- Keep the workflow independent of a specific model, vendor, or tool.

---

## Final Status

The pipeline should finish with exactly one of:

- COMPLETE
- PARTIAL
- BLOCKED
- FAILED

`COMPLETE` should be used only when the Definition of Done is satisfied.