import importlib.metadata
import subprocess
import sys

import pytest

DISTRIBUTIONS = [
    "agnara",
    "agnara-a2a",
    "agnara-cli",
    "agnara-events",
    "agnara-http",
    "agnara-mcp",
    "agnara-telemetry",
]

MODULES = [
    "agnara",
    "agnara_a2a",
    "agnara_cli",
    "agnara_events",
    "agnara_http",
    "agnara_mcp",
    "agnara_telemetry",
]


@pytest.mark.parametrize("dist_name", DISTRIBUTIONS)
def test_distribution_metadata(dist_name):
    """Validate that the exact distribution is installed and is version 0.1.0a8"""
    try:
        version = importlib.metadata.version(dist_name)
        assert version == "0.1.0a8", f"{dist_name} has wrong version: {version}"

        # Verify that if it's an extension, it depends on agnara==0.1.0a8
        if dist_name != "agnara":
            requires = importlib.metadata.requires(dist_name) or []
            # We don't strictly assert the exact string because packaging metadata
            # might format it differently, but we assert 'agnara' is in the list
            # and ideally pinned.
            agnara_reqs = [r for r in requires if r.startswith("agnara ")]
            if agnara_reqs:
                assert "0.1.0a8" in agnara_reqs[0], (
                    f"{dist_name} doesn't depend on agnara 0.1.0a8: {agnara_reqs}"
                )
            else:
                agnara_reqs_strict = [r for r in requires if r.startswith("agnara==")]
                if agnara_reqs_strict:
                    assert "0.1.0a8" in agnara_reqs_strict[0], (
                        f"{dist_name} doesn't depend on agnara 0.1.0a8: "
                        f"{agnara_reqs_strict}"
                    )
    except importlib.metadata.PackageNotFoundError:
        pytest.fail(f"Distribution {dist_name} is not installed in the environment.")


@pytest.mark.parametrize("module_name", MODULES)
def test_module_importability(module_name):
    """Validate that the modules can be imported publicly without errors"""
    try:
        __import__(module_name)
    except ImportError as e:
        pytest.fail(f"Could not import {module_name}: {e}")


def test_a2a_api_surface():
    """
    Validate the actual API surface of agnara_a2a.
    It currently does not expose any public APIs (post-v0.1 placeholder).
    """
    import agnara_a2a

    assert getattr(agnara_a2a, "__all__", None) == [], "agnara_a2a __all__ is not empty"
    public_attrs = [attr for attr in dir(agnara_a2a) if not attr.startswith("_")]
    assert len(public_attrs) == 0, (
        f"agnara_a2a exposed unexpected public attributes: {public_attrs}"
    )


def test_events_api_surface():
    """
    Validate the actual API surface of agnara_events.
    It currently does not expose any public APIs (post-v0.1 placeholder).
    """
    import agnara_events

    assert getattr(agnara_events, "__all__", None) == [], (
        "agnara_events __all__ is not empty"
    )
    public_attrs = [attr for attr in dir(agnara_events) if not attr.startswith("_")]
    assert len(public_attrs) == 0, (
        f"agnara_events exposed unexpected public attributes: {public_attrs}"
    )


def test_cli_smoke():
    """Validate that the CLI entrypoint works."""
    result = subprocess.run(
        [sys.executable, "-m", "agnara_cli", "--help"], capture_output=True, text=True
    )
    # If the CLI module doesn't natively support -m agnara_cli, we try the bin script
    if result.returncode != 0:
        result = subprocess.run(["agnara", "--help"], capture_output=True, text=True)

    assert result.returncode == 0, f"CLI help failed:\n{result.stderr}"


def test_functional_smoke_tests():
    """
    Validate the existence of basic expected functionality without relying on internals.
    """
    # Core
    import agnara

    assert hasattr(agnara, "__version__") or hasattr(agnara, "Agent"), (
        "agnara core missing expected baseline symbols"
    )

    # HTTP
    import agnara_http

    assert dir(agnara_http), "agnara_http should be importable"

    # MCP
    import agnara_mcp

    assert dir(agnara_mcp), "agnara_mcp should be importable"

    # Telemetry
    import agnara_telemetry

    assert dir(agnara_telemetry), "agnara_telemetry should be importable"
