import sys


def main() -> None:
    """Test the main function
    """
    i: int = 0
    scores: list[int] = []
    # check arguments
    if len(sys.argv) == 1:
        print("where score?")
        return
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
            if i == 0:
                print(f"Added {arg} to the list of scores")
            elif i < 2:
                print(f"Ok now {arg} is a number!")
        except ValueError:
            i += 1
            if i == 1:
                print(f"since when {arg} is a number ???")
            elif i == 2:
                print("what ?!")
            elif i >= 3 and i < 6:
                print(f"noo{'o'*i}!")
            else:
                print(f"ST{'O'*i}PPP {'!'*i}")
    if i > 3:
        print("I see the subject make you crazy too...")
    print("")
    try:
        print(f"Statistic time !\n\
            Total score: {sum(scores)}\n\
            Best score: {max(scores)}\n\
            Looser: {min(scores)}\n\
            Average score: {sum(scores)/len(scores)}\n\
            ")
    except ValueError:
        print("No valid scores to analyze.")


if __name__ == "__main__":
    main()
