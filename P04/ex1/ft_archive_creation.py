data: list[str] = [
    "[ENTRY 001] New quantum algorithm discovered",
    "[ENTRY 002] Efficiency increased by 347%",
    "[ENTRY 003] Archived by Data Archivist trainee"
]


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    name: str = "new_discovery.txt"
    print(f"Initialising new storage unit: {name}")
    print("Storage unit created successfully...\n")

    try:
        with open(name, 'w') as file:
            for line in data:
                file.write(line + "\n")
                print(f"Writing to file: {line}")
            print("\nData inscription complete. Storage unit sealed")
            print(f"File '{name}' created successfully in the archives.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


if __name__ == "__main__":
    main()
