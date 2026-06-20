# Tindex Core

## Purpose

`tindex-core` is the reference implementation of the Tindex Canonical Domain Model.

Its responsibility is to implement the canonical specifications defined in the `tindex-specifications` repository as executable software.

The core is technology-independent in its design but implemented using Python.

## Responsibilities

* Implement canonical domain objects.
* Enforce canonical business rules.
* Execute reasoning workflows.
* Provide domain services.
* Remain independent of user interfaces and deployment concerns.

## Out of Scope

The following do **not** belong in `tindex-core`:

* Web frontend
* Website
* Authentication UI
* Deployment scripts
* Infrastructure
* Monitoring
* Marketing pages

These belong to other repositories.

## Guiding Principle

Every implementation in this repository must remain consistent with the canonical specifications.

When implementation reveals weaknesses in the specifications, the specifications are revised through evidence rather than bypassed in code.
