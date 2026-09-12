# Autonomous Agent Operations

This document (`AGENTS.md`) is the **single operational source of truth for autonomous coding agents** (such as OpenAI Codex, Claude Code, and other compatible machine maintainers).

README is for humans. AGENTS is for machine execution and repository maintenance.

## 1. Project Identity

- **Repository**: `agnara-a8-distribution-matrix`
- **Purpose**: Validation from outside the monorepo that the 7 distributions of Agnara 0.1.0a8 install from PyPI without git/path dependencies, expose correct public surfaces, and can be verified correctly.
- **Target Agnara Version**: `0.1.0a8` (Strict boundary)
- **Python Version**: `>=3.14`
- **Status**: Historical / Frozen / Complete. Validation complete. Frozen for `0.1.0a8`.
- **Mission**: Ensure a clean-room installation works properly, revealing actual gaps without mocking APIs.

## 2. Inviolable Architectural Constraints

- **Dependency Boundaries**: Agnara dependencies MUST be pinned strictly to `==0.1.0a8`.
- **Installation Requirements**: Must be installed purely from PyPI. No Git references, no local monorepo paths, no editable (`-e`) installs for Agnara packages.
- **No Speculative APIs**: Do not invent APIs for `agnara_a2a` and `agnara_events` if they are not exposed.
- **Reproducible Execution**: Must be reproducible in isolated environments across Linux, Windows, and macOS.
- **Frozen Version Constraint**: Do NOT upgrade Agnara versions. This project's identity is intrinsically tied to validating `0.1.0a8`.

## 3. Codebase Structure and Ownership

```text
agnara-a8-distribution-matrix/
├── .agents/                 # Machine-readable agent skills
├── .github/                 # CI workflows and issue/PR templates
├── docs/                    # Detailed technical documentation
├── src/
│   └── example.py           # Reproducible demonstration script
├── tests/
│   └── test_distributions.py # Validation test suite
├── AGENTS.md                # Agent operational truth
├── ARCHITECTURE.md          # Architectural validation strategy
├── CHANGELOG.md             # Project history
├── CONTRIBUTING.md          # Contribution guidelines
├── LICENSE                  # Repository License
├── pyproject.toml           # Project metadata and dependencies
├── README.md                # Human entry point
└── SECURITY.md              # Security policy
```

- **`tests/`**: Owns programmatic validation of the public API and versions.
- **`src/`**: Owns reproducible executable demonstrations of the project state.

## 4. Environment and Command Palette

**Environment Creation & Installation (Requires Python 3.14+)**:
```bash
python -m venv venv
# On Unix: source venv/bin/activate
# On Windows: venv\Scripts\activate
python -m pip install -e ".[dev]"
```

**Quality Gates**:
```bash
python -m pip check
ruff format --check .
ruff check .
pytest -v
python src/example.py
python -m build
```

## 5. Public API / Integration Boundary

- **Verified Public API**: `agnara`, `agnara-cli`, `agnara-http`, `agnara-mcp`, `agnara-telemetry`.
- **Intentionally Excluded/Placeholder**: `agnara_a2a`, `agnara_events`. These act as reserved namespaces with `__all__ = []` in 0.1.0a8. Importing implementations (e.g. `from agnara.events import Broker`) will raise `ImportError`.

## 6. Negative Constraints

- DO NOT upgrade Agnara dependencies beyond `0.1.0a8`.
- DO NOT use private internals of Agnara.
- DO NOT invent future APIs or mock the gaps.
- DO NOT replace PyPI dependencies with local paths.
- DO NOT suppress failing tests to make CI green; document actual behavior instead.

## 7. Git and Contribution Protocol

Branching model:
```text
feature/fix/docs branch -> main
```
Commit convention: Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).

## 8. Documentation Synchronization Contract

Any change to commands, architecture, or behavior must be synchronously updated in `README.md`, `AGENTS.md`, and `ARCHITECTURE.md`. These files must NEVER contradict each other.

## 9. Definition of Done

Work is complete when all of the following quality gates pass:
```bash
python -m pip check
ruff format --check .
ruff check .
pytest -v
python src/example.py
python -m build
```

5. All documentation matches the behavior.
6. The GitHub Actions matrix is completely green on Ubuntu, Windows, macOS using CPython 3.14.
