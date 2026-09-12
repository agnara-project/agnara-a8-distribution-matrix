---
name: repository-maintenance
description: How an agent should safely inspect, modify and verify this repository.
---

# Repository Maintenance Skill

## Inspection
- Always read `AGENTS.md` and `pyproject.toml` to understand the version boundaries.
- Inspect `tests/test_distributions.py` to understand how the project asserts package presence.

## Modification
- If modifying validation code, ensure NO mocked APIs are used. Gaps must be validated exactly as they appear in `0.1.0a8`.
- If modifying dependencies, only add development dependencies under `[project.optional-dependencies]`.
- NEVER change the Agnara pins from `0.1.0a8` unless specifically instructed to pivot the entire repository.

## Verification
1. Run `pytest -v` to ensure the version and API assertions hold.
2. Run `ruff format --check .` and `ruff check .`.
3. Check `src/example.py` for successful execution of the demonstration.
