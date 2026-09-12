# Public API Boundary

This document records the exact public API surfaces and verified limits of Agnara `0.1.0a8`.

## Verified Public Imports

The following distributions install successfully and expose standard functionality:
- `agnara`: The core package.
- `agnara_cli`: Command-line interface utilities.
- `agnara_http`: HTTP abstractions and servers.
- `agnara_mcp`: Model Context Protocol implementations.
- `agnara_telemetry`: Tracing and metrics.

## Intentionally Absent APIs

The following distributions install successfully but act as **reserved namespaces** in `0.1.0a8`:
- `agnara_a2a`
- `agnara_events`

**Expected Behavior**:
Both modules explicitly declare `__all__ = []`. They do not contain any implementation code for adapters, tasks, or event brokers.

**Prohibited Usage**:
Attempting to import nested namespaces (e.g., `from agnara.events import Broker` or `from agnara.a2a import Adapter`) will result in an `ImportError`. This behavior is expected and MUST NOT be mocked or bypassed in the validation suite.

## Version Constraints

All tests and validation examples are strictly bound to version `0.1.0a8`. Do not attempt to test APIs introduced in subsequent versions.
