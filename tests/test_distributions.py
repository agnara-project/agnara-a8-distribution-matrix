import importlib.metadata

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

    # The __all__ declaration should be empty
    assert getattr(agnara_a2a, "__all__", None) == [], "agnara_a2a __all__ is not empty"
    # Ensure no hidden actual implementations are secretly exposed
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

    # The __all__ declaration should be empty
    assert getattr(agnara_events, "__all__", None) == [], (
        "agnara_events __all__ is not empty"
    )
    # Ensure no hidden actual implementations are secretly exposed
    public_attrs = [attr for attr in dir(agnara_events) if not attr.startswith("_")]
    assert len(public_attrs) == 0, (
        f"agnara_events exposed unexpected public attributes: {public_attrs}"
    )
