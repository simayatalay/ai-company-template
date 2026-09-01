# Engineering Influences

This document records external ideas, practices, and engineering principles
that may influence the template.

The purpose is not to copy sources directly into project rules.

Instead, useful ideas should be:

1. identified,
2. understood,
3. interpreted,
4. tested when practical,
5. integrated only when they improve the template.

---

# Influence Entry Format

## INF-XXX - Influence Title

**Source:**
Person, organization, article, documentation, talk, or project.

**Main Idea:**
What engineering idea is being proposed?

**General Interpretation:**
What reusable principle can be extracted?

**Potential Template Impact:**
Which part of the template could be influenced?

Examples:

- `AGENTS.md`
- agent role definitions
- testing rules
- review rules
- repository workflow
- documentation structure
- orchestration
- verification requirements

**Status:**
OBSERVED / RESEARCHING / TESTING / ADOPTED / REJECTED

**Evidence:**
What supports the decision to adopt or reject the idea?

---

# General Influence Areas

External ideas may influence areas such as:

## Context Before Action

Agents should understand the relevant task, files, constraints, and expected
outcome before making changes.

Possible template impact:

- Think Before Coding
- scope control
- planning requirements
- context gathering

---

## Simplicity

Prefer the simplest implementation that correctly solves the requested
problem.

Avoid unnecessary abstractions, dependencies, or premature optimization.

Possible template impact:

- Simplicity First
- code review criteria
- coding agent instructions

---

## Small and Verifiable Changes

Prefer small changes that can be independently understood, tested, and
reviewed.

Possible template impact:

- Surgical Changes
- testing
- review
- commit discipline

---

## Independent Verification

Generated code should not be considered correct only because it appears
plausible.

Use executable tests, observable evidence, or independent review whenever
possible.

Possible template impact:

- Test Agent
- Code Review Agent
- pipeline quality gates

---

## Separation of Responsibilities

Implementation, testing, review, and repository operations should be
separated when practical.

Possible template impact:

- specialized agents
- orchestration
- clearer failure ownership
- safer repository operations

---

## Traceable Work

Important work should leave a trace that explains:

- what problem was addressed,
- what changed,
- how it was tested,
- how it was reviewed,
- and how it was resolved.

Possible template impact:

- issue-driven development
- Git history
- progress comments
- decision records

---

# Influence Integration Process

INFLUENCE
    ↓
RESEARCH
    ↓
INTERPRETATION
    ↓
CANDIDATE PRACTICE
    ↓
EXPERIMENT
    ↓
LESSON
    ↓
DECISION
    ↓
TEMPLATE INTEGRATION

Not every external idea should become a permanent rule.

An idea may be:

- adopted,
- modified,
- rejected,
- or kept for further research.

---

# Promotion Criteria

Before integrating an external idea into the base template, ask:

1. Does it solve a recurring engineering problem?
2. Is it useful beyond one specific project?
3. Can different developers or agents understand it?
4. Does it improve reliability, clarity, or maintainability?
5. Can its usefulness be supported by evidence?
6. Does it avoid unnecessary tool or vendor dependence?

If the answers are sufficiently positive, the idea may be integrated into
the appropriate template component.

---

# Template Principle

The base template should contain reusable engineering principles rather than
person-specific or tool-specific instructions.

Sources may inspire the template, but the final rule should stand on its own.