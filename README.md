# Agnara 0.1.0a8 Distribution Matrix

Agnara distribution and compatibility validation matrix for release `0.1.0a8`.

**Ecosystem Role**: Distribution Validator  
**Target Agnara Release**: `0.1.0a8` (Frozen)  
**Python Requirement**: `>=3.14`  
**Status**: Validation Complete

## Mission

This repository exists separately from Agnara Core to validate that the 7 distributions of `0.1.0a8` install cleanly from PyPI in an isolated environment, without depending on Git repositories, editable installs, or local paths. It documents the actual public API surface exposed by these packages, specifically highlighting missing implementations without inventing or mocking APIs.

## Scope

**In Scope**:
- Validating PyPI installation of `0.1.0a8` distributions.
- Asserting correct package versions and metadata.
- Documenting the real public API surface of placeholder packages (`agnara_a2a`, `agnara_events`).
- Cross-platform verification (Linux, Windows, macOS).

**Out of Scope**:
- Providing functional A2A or Event broker capabilities.
- Modifying or extending Agnara core features.
- Testing any version other than `0.1.0a8`.

## Release / Compatibility Baseline

- **Agnara Core**: `==0.1.0a8`
- **Distributions**: `agnara-a2a`, `agnara-cli`, `agnara-events`, `agnara-http`, `agnara-mcp`, `agnara-telemetry` (all pinned to `0.1.0a8`)
- **Python**: `3.14`

## Prerequisites

- Python `>=3.14`

## Quick Start

```bash
# Clone the repository
git clone https://github.com/agnara-project/agnara-a8-distribution-matrix.git
cd agnara-a8-distribution-matrix

# Create a clean virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install the validation matrix
python -m pip install -e ".[dev]"

# Run the validation suite
pytest -v
python src/example.py
```

## Architecture and Conceptual Flow

This project executes a programmatic validation pipeline. It fetches distributions directly from PyPI into a pristine environment, then asserts via `tests/` that the structural metadata matches expected boundaries. 

For a complete breakdown, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Project Structure

- `tests/`: Programmatic validation of package presence, metadata, and API gaps.
- `src/`: Executable scripts demonstrating the actual API state.
- `docs/`: Technical documentation regarding API boundaries and methodology.
- `.agents/`: Agent instructions and skills for autonomous maintenance.
- `.github/`: CI workflows and governance templates.

## Testing and Verification

Ensure code quality and validation integrity by running:

```bash
ruff format --check .
ruff check .
pytest -v
```

To see the live demonstration of the API state:
```bash
python src/example.py
```

## Known Limitations

During validation of `0.1.0a8`, the following true gaps were documented:
- `agnara-a2a` and `agnara-events` install successfully but act strictly as reserved namespaces. 
- They intentionally expose an empty public surface (`__all__ = []`).
- No namespace packages (`agnara.a2a` or `agnara.events`) exist; attempting to import implementations (e.g., `from agnara.events import Broker`) will correctly raise an `ImportError`.

These limitations are asserted by the test suite and deliberately not mocked.

## Relationship to Agnara

This project is a standalone downstream validator for Agnara Core. It does not track `main` or development branches; it is forever historically frozen against the `0.1.0a8` alpha release.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on our branch model and quality gates. Note that we do not accept PRs that attempt to mock missing APIs or upgrade the Agnara dependency.

## Security

Please report vulnerabilities following our [Security Policy](SECURITY.md).

## License

This project is licensed under the [MIT License](LICENSE).