# Security Policy

## Supported Versions

This repository is a validation matrix specifically frozen at `0.1.0a8`. 

| Version | Supported          |
| ------- | ------------------ |
| 0.1.0a8 | :white_check_mark: |
| Other   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability within this validation suite or the specific distributions it tests, please report it via the GitHub private Security Advisory path or email `security@agnara.dev`.

DO NOT open public issues for security vulnerabilities.

## Project-Specific Threat Surface

This repository acts as an installation and API boundary validator. The primary security concerns are:
1. **Supply Chain Attacks**: Ensuring that the packages installed are exactly the versions specified and are fetched from the official PyPI registry.
2. **Environment Contamination**: Ensuring the CI environment is ephemeral and does not leak tokens or execution context.

We enforce clean-room installations (`python -m venv venv`) precisely to mitigate local contamination.
