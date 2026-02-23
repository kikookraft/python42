
def secure_extraction(filename: str) -> list[str]:
    """
    extract everything from a vault file securely.
    """
    lines: list[str] = []
    with open(filename, 'r') as vault:
        lines = vault.read().splitlines()
    return lines


def secure_preservation(filename: str, data: str) -> None:
    """
    write data to a vault file securely
    """
    with open(filename, 'w') as vault:
        vault.write(data)


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()

    print("SECURE EXTRACTION:")
    try:
        classified_lines: list[str] = secure_extraction("classified_data.txt")
        for line in classified_lines:
            print(line)
    except Exception as e:
        print(f"An error occurred during secure extraction: {e}")
    print()

    print("SECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", 'w') as vault:
            vault.write("[CLASSIFIED] New security protocols archived")
    except Exception as e:
        print(f"An error occurred during secure preservation: {e}")
    print()

    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
