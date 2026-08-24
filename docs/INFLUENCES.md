# Engineering Influences

This document records engineering ideas, methods, and principles
that may influence the AI coding standards developed in this project.

The goal is not to copy every idea directly into `AGENTS.md`.

Instead, external ideas should be:

1. Collected
2. Understood
3. Converted into candidate rules
4. Tested when possible
5. Promoted only if they improve AI coding behavior

---

# 1. Andrej Karpathy

## Main Ideas

Relevant ideas include:

- Keep AI instructions clear and explicit.
- Give AI enough context to understand the task.
- Break complex problems into smaller steps.
- Review AI-generated code rather than accepting it blindly.
- Use verification as part of AI-assisted development.

## Relevance to This Project

These ideas support the project's existing principles:

- Think Before Coding
- Goal-Driven Execution
- Verification
- Human review

## Candidate Rules

### KARPATHY-CR-001

Before implementing a complex task, the agent should first understand
the relevant context and create a short plan.

Status: CANDIDATE

### KARPATHY-CR-002

AI-generated code should not be considered correct solely because
it appears plausible.

Relevant verification should be performed.

Status: CANDIDATE

---

# 2. Rob Pike

## Main Ideas

Relevant engineering themes include:

- Simplicity is preferable to unnecessary complexity.
- Clear code is more valuable than clever code.
- Abstractions should have a real purpose.
- Understand the problem before introducing complexity.

## Relevance to This Project

These ideas strongly support the existing `Simplicity First` principle.

## Candidate Rules

### PIKE-CR-001

Prefer the simplest implementation that correctly solves the requested
problem.

Status: CANDIDATE

### PIKE-CR-002

Do not introduce an abstraction unless it provides a clear benefit.

Status: CANDIDATE

---

# 3. Rich Hickey

## Main Ideas

Relevant engineering themes include:

- Simple and easy are not the same thing.
- Complexity often comes from unnecessary coupling.
- Systems should avoid mixing unrelated responsibilities.
- Good design attempts to keep concepts independent.

## Relevance to This Project

These ideas can help AI agents avoid creating unnecessary dependencies
between parts of a codebase.

## Candidate Rules

### HICKEY-CR-001

Avoid unnecessarily coupling independent responsibilities.

Status: CANDIDATE

### HICKEY-CR-002

When evaluating a solution, consider structural simplicity rather than
only ease of implementation.

Status: CANDIDATE

---

# 4. Kent Beck

## Main Ideas

Relevant engineering themes include:

- Make changes in small steps.
- Use tests to create confidence.
- Keep feedback loops short.
- Improve design incrementally.
- Prefer changes that are easy to verify.

## Relevance to This Project

These ideas support:

- Surgical Changes
- Verification
- Testing
- Incremental implementation

## Candidate Rules

### BECK-CR-001

Prefer small, independently verifiable changes over large changes.

Status: CANDIDATE

### BECK-CR-002

When behavior changes, determine whether an appropriate test should
also be added or updated.

Status: CANDIDATE

---

# 5. Alican Kiraz

## Research Status

Research on Alican Kiraz's engineering and AI-assisted development
practices will be collected separately before creating permanent rules.

Ideas attributed to an individual should not become project rules
without sufficient evidence or a reliable source.

## Candidate Rules

No rule has been promoted yet.

Status: RESEARCH REQUIRED

---

# Influence Evaluation Process

An external idea should move through the following process:

INFLUENCE
    ↓
RESEARCH
    ↓
CANDIDATE RULE
    ↓
EXPERIMENT
    ↓
LESSON
    ↓
DECISION
    ↓
PROMOTED RULE
    ↓
AGENTS.md

Not every candidate rule should reach the final stage.

A candidate may be:

- accepted,
- modified,
- rejected,
- kept for further testing.

---

# Promotion Criteria

Before an external idea becomes a general rule, ask:

1. Does the rule solve a recurring problem?
2. Is it useful beyond one specific task?
3. Can the agent understand and follow it?
4. Does it improve the resulting code or workflow?
5. Does it conflict with another rule?
6. Can its usefulness be demonstrated through experiments?

If the answer is sufficiently positive, the rule may be considered
for promotion into `AGENTS.md`.