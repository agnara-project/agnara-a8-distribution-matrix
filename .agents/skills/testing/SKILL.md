---
name: testing
description: How to run the project's validation gates.
---

# Testing Skill

## Executing Gates
Run standard quality gates:
```bash
ruff format --check .
ruff check .
pytest -v
```

## Interpreting Failures
- If a test fails because `0.1.0a8` behaves differently than expected, DO NOT change the test to mock the behavior. The purpose of this project is to expose the truth. Document the gap and potentially adjust the test to assert the *actual* failing or limited behavior.
- Ensure all distributions are tested for version match (`==0.1.0a8`).
