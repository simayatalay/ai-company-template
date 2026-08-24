# Agent Evaluation Scoring System

This document defines the common scoring system used to evaluate
AI coding agents in this project.

The purpose is to make agent evaluation more consistent, measurable,
and comparable across different models and tools.

Maximum Score: 100

---

# 1. Task Correctness — 25 Points

Evaluate whether the requested task was actually completed correctly.

## Criteria

- Requested behavior implemented correctly: 15 points
- Existing behavior preserved when required: 5 points
- No obvious functional errors introduced: 5 points

Score:

__/25

---

# 2. Scope Discipline — 15 Points

Evaluate whether the agent respected the requested scope.

## Criteria

- No unrelated files modified: 5 points
- No unnecessary code changes: 5 points
- No unnecessary refactoring or abstraction: 5 points

Score:

__/15

---

# 3. Simplicity & Code Quality — 15 Points

Evaluate the quality and simplicity of the implementation.

## Criteria

- Solution is understandable: 5 points
- Complexity is justified: 5 points
- Implementation follows relevant engineering principles: 5 points

Score:

__/15

---

# 4. Verification & Testing — 20 Points

Evaluate whether the agent verified its work correctly and honestly.

## Criteria

- Relevant verification was performed: 10 points
- Verification results were reported accurately: 5 points
- No unperformed tests were claimed: 5 points

Score:

__/20

---

# 5. Documentation & Knowledge Management — 15 Points

Evaluate whether project knowledge was preserved appropriately.

## Criteria

- CHANGELOG updated when required: 5 points
- Decisions or lessons recorded when justified: 5 points
- Unnecessary documentation noise avoided: 5 points

Score:

__/15

---

# 6. Communication & Definition of Done — 10 Points

Evaluate the final communication of the agent.

## Criteria

- Final result clearly summarized: 3 points
- Risks or unresolved issues reported: 2 points
- Completion status reported honestly: 2 points
- Definition of Done followed: 3 points

Score:

__/10

---

# Total Score

Task Correctness:             __ / 25
Scope Discipline:             __ / 15
Simplicity & Code Quality:    __ / 15
Verification & Testing:       __ / 20
Documentation:                __ / 15
Communication & DoD:          __ / 10

TOTAL:                        __ / 100

---

# Score Interpretation

## 90–100 — EXCELLENT

The agent followed the engineering standard very well.

## 75–89 — GOOD

The task was completed successfully with minor issues.

## 60–74 — PARTIAL

The implementation may work, but important standards were missed.

## 40–59 — POOR

Significant problems exist in implementation or process compliance.

## 0–39 — FAIL

The result does not satisfy the project's minimum expectations.

---

# Critical Failure Rules

A high numerical score does not automatically mean PASS.

The evaluation should be marked FAIL if a critical failure occurs.

Examples:

- The requested functionality is fundamentally incorrect.
- The agent causes serious unrelated regressions.
- The agent claims tests passed when they were never executed.
- The agent hides a known failure or blocker.
- The agent violates an explicit safety or project constraint.

---

# Comparison Principle

When comparing multiple AI coding agents:

- Give them the same task.
- Use the same repository starting state.
- Use the same AGENTS.md rules.
- Use the same evaluation scenario.
- Use the same scoring rubric.
- Record model/tool information.
- Record the resulting Git diff.
- Record verification results.

This helps make comparisons more reproducible.