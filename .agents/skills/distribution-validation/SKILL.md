---
name: distribution-validation
description: How to perform isolated clean-room validation of Agnara distributions.
---

# Distribution Validation Skill

## Core Concept
This project verifies that Agnara distributions can be installed and executed from PyPI in a completely isolated environment, independent of the source monorepo.

## Rules
- NEVER use `-e` (editable) installs for validation targets.
- NEVER point dependencies to a local path or git URL.
- Always use a fresh virtual environment (`python -m venv venv`) when validating a matrix.
- Test across all supported OS runners (Linux, macOS, Windows) in GitHub Actions.
- Ensure that the imported modules match the expected public API. If a namespace is empty or acts as a placeholder, assert that it is empty explicitly.
