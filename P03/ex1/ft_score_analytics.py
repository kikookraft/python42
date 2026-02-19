import sys


def main() -> None:
    """Test the main function
    """
    print("=== Player Score Analytics ===")
    
    # Check no arguments
    if len(sys.argv) == 1:
        print("where is the score ??")
        return
    
    scores: list[int] = []
    
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"tf is the number {arg} ??")
    
    if not scores: # in case scores are messed up
        print("No valid scores provided.")
        return
    
    # stats
    total_players: int = len(scores)
    total_score: int = sum(scores)
    average_score: float = total_score / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score
    
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
