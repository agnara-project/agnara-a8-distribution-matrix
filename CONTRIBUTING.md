# Contributing

Thank you for your interest in contributing to the Agnara Distribution Matrix.

## Project Status

This repository is **Frozen** against Agnara version `0.1.0a8`. Its primary purpose is historical and architectural validation of that specific release. 

**We DO NOT accept PRs that:**
- Upgrade the Agnara dependency versions.
- Introduce mocked APIs for `agnara_a2a` or `agnara_events`.
- Remove the clean-room validation requirements.

We **DO** accept PRs that:
- Fix bugs in the validation suite.
- Improve documentation clarity without changing the historical facts.
- Improve the CI/CD pipeline reliability.

## Setup

Requires Python `>=3.14`.

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
python -m pip install -e ".[dev]"
```

## Branching and Commits

- We use the `feature/`, `fix/`, `docs/` branch naming convention.
- All branches merge directly into `main` via Pull Request.
- We strictly enforce Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, etc.).

## Quality Gates

Before submitting a PR, ensure all gates pass:

```bash
python -m pip check
ruff format --check .
ruff check .
pytest -v
python src/example.py
python -m build
```

## Pull Request Process

1. Use the provided Pull Request template.
2. Ensure CI passes on all operating systems (Linux, Windows, macOS).
3. Update documentation if you change how validation is performed.
