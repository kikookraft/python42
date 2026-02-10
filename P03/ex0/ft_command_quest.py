import sys


def main() -> None:
    """Test the main function
    """
    # check arguments
    if len(sys.argv) == 1:
        print("No args, what do you want ??")
        return
    print(f"Okay, got {len(sys.argv)} arguments into {sys.argv[0]}, sooo...")
    i: int = 0
    for arg in sys.argv[1:]:
        i += 1
        print(f"{i} > {arg}")


if __name__ == "__main__":
    main()
