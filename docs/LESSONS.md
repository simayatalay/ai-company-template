# Lessons Learned

This document records reusable lessons discovered during development,
testing, review, and maintenance.

The purpose is to convert practical experience into reusable engineering
knowledge.

A lesson is not automatically a permanent project rule.

Lessons may later become candidate rules and, after sufficient evidence,
may be promoted into project standards.

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

**Context:**
What situation produced this lesson?

**Expected Behavior:**
What was expected to happen?

**Observed Behavior:**
What actually happened?

**Lesson:**
What reusable knowledge was learned?

**Candidate Rule:**
What possible engineering rule could be derived?

**Evidence:**
What evidence supports this lesson?

**Related Research:**
Relevant `RESEARCH.md` entry, if any.

**Related Decision:**
Relevant `DECISIONS.md` entry, if any.

**Next Action:**
What should be tested, changed, or investigated next?

---

# Lesson Classification

## Specific Lesson

A specific lesson applies only to a limited context, such as:

- one task,
- one project,
- one technology,
- one tool,
- or one unusual environment.

Specific lessons should normally remain observations until there is
evidence that they apply more broadly.

## General Lesson

A general lesson appears useful across:

- multiple tasks,
- multiple projects,
- multiple tools or agents,
- or multiple environments.

General lessons may become candidate engineering rules.

---

# Rule Promotion

A lesson should not become a permanent rule after a single observation
unless the evidence is especially strong.

Prefer repeated and independent evidence.

Before promoting a lesson, ask:

- Has the behavior been observed more than once?
- Does the lesson apply beyond one specific project?
- Would the rule improve consistency or reliability?
- Could the rule create unnecessary restrictions?

---

# Failed Experiments

Failed experiments should also be documented.

They may reveal problems such as:

- unclear instructions,
- missing context,
- ineffective rules,
- tool limitations,
- verification problems,
- environment dependencies,
- or incorrect assumptions.

Negative results should not be hidden or discarded.

---

# Evidence Levels

## LOW

Observed once.

Not enough evidence for a general rule.

## MEDIUM

Observed repeatedly or supported by multiple related experiments.

May justify a candidate rule.

## HIGH

Observed consistently across different tasks, tools, agents, or
environments.

Strong candidate for becoming a general engineering rule.

---

# Lessons

Add validated project lessons below this section as they are discovered.

The base template should remain general.
Project-specific lessons may be added only after the template is adopted
for a particular project.