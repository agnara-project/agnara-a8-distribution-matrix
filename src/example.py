import importlib.metadata
import sys


def main():
    print("=== Validation of Agnara 0.1.0a8 ===")
    distributions = [
        "agnara",
        "agnara-a2a",
        "agnara-cli",
        "agnara-events",
        "agnara-http",
        "agnara-mcp",
        "agnara-telemetry",
    ]

    print("\n[1] Checking installed versions...")
    for dist in distributions:
        try:
            version = importlib.metadata.version(dist)
            print(f"  {dist}: {version}")
        except importlib.metadata.PackageNotFoundError:
            print(f"  {dist}: NOT INSTALLED")
            sys.exit(1)

    print("\n[2] Checking gap in API (agnara_a2a and agnara_events)...")
    import agnara_a2a
    import agnara_events

    print("  agnara_a2a __all__:", getattr(agnara_a2a, "__all__", None))
    print("  agnara_events __all__:", getattr(agnara_events, "__all__", None))

    print("\n  This script explicitly demonstrates that agnara_a2a and agnara_events")
    print(
        "  do not expose any public APIs in 0.1.0a8. They act as reserved namespaces."
    )
    print(
        "  Attempting to import implementations like 'agnara.events.Broker' will fail."
    )

    try:
        from agnara.events import Broker

        _ = Broker  # Prevent F401
    except ImportError as e:
        print(f"  [Expected Gap] ImportError: {e}")


if __name__ == "__main__":
    main()
