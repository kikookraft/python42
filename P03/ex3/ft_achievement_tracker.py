from typing import Dict, Set, List


def track_achievements(
    player_data: Dict[str, List[str]]
) -> Dict[str, Set[str]]:
    """
    Convert player achievement lists to sets
    """
    result: Dict[str, Set[str]] = {}
    for player, achievements in player_data.items():
        result[player] = set(achievements)
    return result


def find_all_unique_achievements(
    achievement_sets: Dict[str, Set[str]]
) -> Set[str]:
    """
    Find all unique achievements across all players using union operation.
    """
    if not achievement_sets:
        return set()

    all_achievements: Set[str] = set()
    for achievements in achievement_sets.values():
        all_achievements = all_achievements.union(achievements)

    return all_achievements


def find_common_achievements(
    achievement_sets: Dict[str, Set[str]]
) -> Set[str]:
    """
    Find achievements common to all players using intersection operation.
    """
    if not achievement_sets:
        return set()

    achievement_list = list(achievement_sets.values())
    common: Set[str] = achievement_list[0].copy()

    for achievements in achievement_list[1:]:
        common = common.intersection(achievements)

    return common


def find_rare_achievements(
    achievement_sets: Dict[str, Set[str]]
) -> Dict[str, Set[str]]:
    """
    Find rare achievements that only one player has.
    """
    rare_achievements: Dict[str, Set[str]] = {}
    all_players = list(achievement_sets.keys())

    for player in all_players:
        player_achievements = achievement_sets[player]
        other_players_achievements: Set[str] = set()

        for other_player in all_players:
            if other_player != player:
                other_players_achievements = other_players_achievements.union(
                    achievement_sets[other_player]
                )

        unique_to_player = player_achievements.difference(
            other_players_achievements
        )

        if unique_to_player:
            rare_achievements[player] = unique_to_player

    return rare_achievements


def find_player_differences(
    achievement_sets: Dict[str, Set[str]],
    player1: str,
    player2: str
) -> Dict[str, Set[str]]:
    """
    Find unique achievements for each of two players using difference.
    """
    if player1 not in achievement_sets or player2 not in achievement_sets:
        return {
            'common': set(),
            f'{player1}_unique': set(),
            f'{player2}_unique': set()
        }

    set1 = achievement_sets[player1]
    set2 = achievement_sets[player2]

    return {
        'common': set1.intersection(set2),
        f'{player1}_unique': set1.difference(set2),
        f'{player2}_unique': set2.difference(set1)
    }


def main() -> None:
    """Main function to demonstrate the achievement tracker system."""
    print("dgvfhsfdshgfdghsdjfhgfgdkjshhjgkfd")

    # Sample player data
    player_data: Dict[str, List[str]] = {
        'alice': [
            'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
        ],
        'bob': [
            'first_kill', 'level_10', 'boss_slayer', 'collector', 'test'
        ],
        'charlie': [
            'level_10', 'treasure_hunter', 'boss_slayer',
            'speed_demon', 'perfectionist'
        ]
    }

    # Track achievements using sets
    achievement_sets = track_achievements(player_data)

    # Display player achievements
    for player, achievements in achievement_sets.items():
        print(f"Player {player} achievements: {achievements}")

    print("\n=== Achievement Analytics ===")

    # Find all unique achievements
    all_unique = find_all_unique_achievements(achievement_sets)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")

    # Find common achievements
    common = find_common_achievements(achievement_sets)
    print(f"\nCommon to all players: {common}")

    # Find rare achievements
    rare = find_rare_achievements(achievement_sets)
    # Collect all rare achievements into one set
    all_rare: Set[str] = set()
    for player_rare in rare.values():
        all_rare = all_rare.union(player_rare)
    print(f"Rare achievements (1 player): {all_rare}")

    # Compare two players
    alice_bob_diff = find_player_differences(
        achievement_sets, 'alice', 'bob'
    )
    print(f"\nAlice vs Bob common: {alice_bob_diff['common']}")
    print(f"Alice unique: {alice_bob_diff['alice_unique']}")
    print(f"Bob unique: {alice_bob_diff['bob_unique']}")


if __name__ == "__main__":
    main()
