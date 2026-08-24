# Agent Evaluation System

This directory contains evaluation scenarios used to test whether an AI coding agent follows the rules defined in AGENTS.md and the project's documentation system.

## Purpose

The goal of these evaluations is to measure whether the agent:

- follows project instructions,
- documents important changes,
- records architectural decisions,
- uses project terminology consistently,
- reports verification honestly,
- follows the Definition of Done,
- and preserves useful knowledge for future tasks.

## Evaluation Principle

An agent should not only produce working code.

A successful agent should also leave the project in a state where another developer or agent can understand:

- what changed,
- why it changed,
- what decisions were made,
- what was learned,
- and whether the work was actually verified.

## Evaluation Areas

1. Code Changes
2. Documentation
3. Decision Recording
4. Knowledge Preservation
5. Verification
6. Definition of Done Compliance

## Result States

Each evaluation can end with:

- PASS
- FAIL
- PARTIAL
- BLOCKED