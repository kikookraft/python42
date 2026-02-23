

import os


def crisis_handler(filename: str) -> None:
    """
    Handle archive access with crisis response protocols.
    """
    display_name: str = os.path.basename(filename)
    try:
        with open(filename, 'r') as file:
            content: str = file.read()
            print(f"ROUTINE ACCESS: Attempting access to '{display_name}'...")
            print(f"SUCCESS: Archive recovered - ``{content.strip()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{display_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{display_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{display_name}'...")
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis contained, system recovering")


def main() -> None:
    """Run crisis response system tests."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()

    # Test 1: Non-existent archive (FileNotFoundError)
    crisis_handler("lost_archive.txt")
    print()

    # Test 2: Security-restricted vault (PermissionError)
    crisis_handler("classified_vault.txt")
    print()

    # Test 3: Standard archive recovery (Success)
    crisis_handler("standard_archive.txt")
    print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
