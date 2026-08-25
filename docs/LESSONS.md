# Lessons Learned

This document records lessons learned from experiments, failures,
successes, and observations during the development of this project.

The purpose is to convert practical experience into reusable knowledge.

A lesson is not automatically a permanent rule.

Lessons may later become candidate rules and, after evaluation,
may be promoted into the project's AI engineering standards.

---

# Learning Process

EXPERIMENT
    ↓
OBSERVATION
    ↓
LESSON
    ↓
CLASSIFICATION
    ↓
CANDIDATE RULE
    ↓
DECISION
    ↓
PROMOTE / MODIFY / REJECT

---

# Lesson Entry Format

## LESSON-XXX - Lesson Title

**Date:**
YYYY-MM-DD

**Status:**
OBSERVED / CONFIRMED / REJECTED / PROMOTED

**Type:**
GENERAL / SPECIFIC

**Experiment:**
What were we testing?

**Expected Behavior:**
What did we expect the AI agent to do?

**Observed Behavior:**
What actually happened?

**Lesson:**
What did we learn?

**Candidate Rule:**
What possible rule can be derived from this lesson?

**Evidence:**
What evidence supports this lesson?

**Related Research:**
Relevant `RESEARCH.md` entry.

**Related Decision:**
Relevant `DECISIONS.md` entry.

**Next Action:**
What should be tested or changed next?

---

# Lessons

No AI coding experiments have been completed yet.

The first lessons will be recorded after the initial Claude Code
experiment.

---

# Lesson Classification

## SPECIFIC LESSON

A lesson that applies only to:

- one task,
- one project,
- one technology,
- one AI model,
- or one unusual situation.

Specific lessons should normally remain in this document.

---

## GENERAL LESSON

A lesson that appears useful across:

- multiple tasks,
- multiple projects,
- multiple AI agents,
- or multiple experiments.

General lessons may become candidate rules.

---

# Rule Promotion

A lesson should not become a permanent rule after a single observation
unless the evidence is especially strong.

Prefer repeated evidence.

Example:

Experiment 1:
Agent modified unrelated code.

Experiment 2:
Agent modified unrelated code again.

Experiment 3:
Explicit scope instructions prevented unrelated changes.

Possible general lesson:
Explicit scope boundaries improve change discipline.

Possible candidate rule:
Before implementation, identify which files and behaviors are inside
and outside the requested scope.

---

# Failed Experiments

Failed experiments must also be documented.

A failed experiment can provide valuable information about:

- unclear instructions,
- ineffective rules,
- model limitations,
- missing context,
- verification problems,
- tool limitations,
- or incorrect assumptions.

Do not delete or hide negative results.

---

# Evidence Levels

Lessons may use the following evidence levels:

## LOW

Observed once.

Not enough evidence for a general rule.

## MEDIUM

Observed repeatedly or supported by multiple related experiments.

May justify a candidate rule.

## HIGH

Observed consistently across different tasks, agents, or environments.

Strong candidate for becoming a general rule.

---

# Example Future Lesson

## LESSON-001 - Explicit Scope Reduces Unrelated Changes

**Status:**
OBSERVED

**Type:**
GENERAL

**Experiment:**
Ask an AI agent to modify only the `greet_user()` function.

**Expected Behavior:**
Only code required for the requested behavior should change.

**Observed Behavior:**
To be recorded after the experiment.

**Lesson:**
To be determined.

**Candidate Rule:**
To be determined.

**Evidence:**
LOW

**Related Research:**
RES-001
RES-002

**Related Decision:**
DEC-007

**Next Action:**
Repeat the experiment with multiple agents.
## Lesson: Documentation paths must be consistent

During the first live agent evaluation, the evaluation command expected
`docs/DECISIONS.md`, but the actual file was named `docs/DESICIONS.md`.

This caused part of the project context to be unavailable to the agent.

### Learning

Agent infrastructure depends on consistent file names and documentation paths.
A small naming mismatch can prevent an agent from receiving important project context.

### Action

The file was renamed from `DESICIONS.md` to `DECISIONS.md`.

Future evaluation runs should verify that all required context files exist
before invoking the agent.