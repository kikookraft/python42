# import sys

def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    filename: str = "ancient_fragment.txt"

    try:
        with open(filename, 'r') as file:
            content: str = file.read()
            print(f"\n--- Contents of '{filename}' ---\n")
            i: int = 1
            for line in content.splitlines():
                print(f"{i}> {line}")
                i += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found, humanity is fucked up.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    print("\n=== END OF ARCHIVES ===")


if __name__ == "__main__":
    main()
