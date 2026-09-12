# Distribution Validation Guide

This document explains the methodology used to validate Agnara distributions for this matrix.

## Methodology

The validation operates under a "clean-room" assumption:
1. **No Monorepo Context**: The validation runs entirely outside the `Blandskron/agnara` monorepo.
2. **Fresh Environment**: Every test run provisions a completely new Python virtual environment (`python -m venv venv`).
3. **PyPI Sole Source**: Dependencies are resolved exclusively from PyPI, using the exact pin `==0.1.0a8`. Local wheels or editable installs (`pip install -e`) are prohibited.
4. **Platform Matrix**: The process is verified simultaneously on Ubuntu, Windows, and macOS via GitHub Actions.

## Validation Steps

1. **Installation Check**: Pip must be able to resolve and install the 7 distributions without missing dependencies.
2. **Metadata Verification**: Programmatic tests (`importlib.metadata.version`) confirm that the exact version installed is `0.1.0a8`.
3. **Importability Check**: The distributions must be importable in Python without raising `ImportError` for missing system libraries.
4. **Surface Area Inspection**: For modules known to be placeholders (`agnara_a2a`, `agnara_events`), the test suite inspects the module's `__all__` attribute and public symbol list to ensure no hidden implementations are accidentally exposed.

## Execution

See `AGENTS.md` and `README.md` for the exact commands used to run the validation suite.
