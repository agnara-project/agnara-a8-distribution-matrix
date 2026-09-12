---
name: documentation
description: How documentation is structured and synchronized.
---

# Documentation Skill

## Structure
- `README.md`: Human entry point. Explains why the project exists and how to run it.
- `AGENTS.md`: Machine instructions and inviolable constraints.
- `ARCHITECTURE.md`: Technical flow of the validation.
- `docs/`: Granular documentation (e.g. `public-api-boundary.md`, `distribution-validation.md`).

## Synchronization
- When commands change, update `README.md` and `AGENTS.md`.
- When the API boundary changes, update `docs/public-api-boundary.md` and tests.
- Documentation must reflect the code's ACTUAL state, not future aspirations.
