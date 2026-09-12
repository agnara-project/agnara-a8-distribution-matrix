# PyPI Validation and Metadata Drift

During the clean-room validation of the Agnara ecosystem release `0.1.0a8`, a historical metadata drift was documented. This document records the real state of the packages fetched from PyPI without attempting to false or alter the historical artifact.

## Findings

Some distributions published under `0.1.0a8` contain legacy references within their `long_description` (README texts), maintaining textual references to older versions such as `0.1.0a4`. This is purely a documentary drift on PyPI and does not affect the functional execution or the explicit dependency boundaries (`Requires-Dist`) of the artifacts.

### Validation Matrix

| Distribution       | PyPI Version | Requires Python | Core Dependency | Public/Import Status | Metadata Notes                                        |
|--------------------|--------------|-----------------|-----------------|----------------------|-------------------------------------------------------|
| `agnara`           | `0.1.0a8`    | `>=3.14`        | N/A             | Fully Functional     | Clean.                                                |
| `agnara-a2a`       | `0.1.0a8`    | `>=3.14`        | `==0.1.0a8`     | Placeholder Module   | May contain historical `0.1.0a4` references in text.  |
| `agnara-cli`       | `0.1.0a8`    | `>=3.14`        | `==0.1.0a8`     | Fully Functional     | Clean.                                                |
| `agnara-events`    | `0.1.0a8`    | `>=3.14`        | `==0.1.0a8`     | Placeholder Module   | May contain historical `0.1.0a4` references in text.  |
| `agnara-http`      | `0.1.0a8`    | `>=3.14`        | `==0.1.0a8`     | Fully Functional     | Clean.                                                |
| `agnara-mcp`       | `0.1.0a8`    | `>=3.14`        | `==0.1.0a8`     | Fully Functional     | Clean.                                                |
| `agnara-telemetry` | `0.1.0a8`    | `>=3.14`        | `==0.1.0a8`     | Fully Functional     | Clean.                                                |

## Architectural Decision

We treat PyPI artifacts as immutable. The discrepancy between the textual descriptions inside the wheel and the actual functional version code (`0.1.0a8`) is acknowledged as a non-blocking documentary issue upstream. We **DO NOT** attempt to mock, rebuild, or disguise this drift within the validation matrix. This matrix accurately reflects the state of the PyPI registry for `0.1.0a8`.
