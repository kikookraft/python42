from typing import Dict, List, Set, Any


def filter_high_scores(
    sessions: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Filter sessions with scores above 1800
    """
    return [
        session for session in sessions
        if session.get('score', 0) > 1800
    ]


def transform_player_scores(
    sessions: List[Dict[str, Any]]
) -> List[int]:
    """
    Extract just the scores from sessions
    """
    return [
        session['score']
        for session in sessions
        if 'score' in session
    ]


def group_by_category(
    players: Dict[str, Dict[str, Any]]
) -> Dict[str, List[str]]:
    """
    Group players by their favorite mode
    """
    modes: Set[str] = {
        player_data['favorite_mode']
        for player_data in players.values()
        if 'favorite_mode' in player_data
    }

    return {
        mode: [
            player_name
            for player_name, player_data in players.items()
            if player_data.get('favorite_mode') == mode
        ]
        for mode in modes
    }


def count_occurrences(
    sessions: List[Dict[str, Any]]
) -> Dict[str, int]:
    """
    Count session occurrences by mode
    """
    modes: Set[str] = {
        session['mode']
        for session in sessions
        if 'mode' in session
    }

    return {
        mode: sum(
            1 for session in sessions
            if session.get('mode') == mode
        )
        for mode in modes
    }


def create_mappings(
    players: Dict[str, Dict[str, Any]]
) -> Dict[str, int]:
    """
    Map player names to achievement counts
    """
    return {
        player_name: player_data.get('achievements_count', 0)
        for player_name, player_data in players.items()
    }


def find_unique_players(
    sessions: List[Dict[str, Any]]
) -> Set[str]:
    """
    Find all unique players
    """
    return {
        session['player']
        for session in sessions
        if 'player' in session
    }


def find_unique_achievements(
    players: Dict[str, Dict[str, Any]],
    achievements: List[str]
) -> Set[str]:
    """
    Find unique achievements
    """
    return {
        achievement
        for achievement in achievements
        if any(
            player_data.get('achievements_count', 0) > 0
            for player_data in players.values()
        )
    }


def deduplicate_data(
    sessions: List[Dict[str, Any]]
) -> Set[str]:
    """
    Deduplicate player names
    """
    return {
        session.get('player', 'unknown')
        for session in sessions
    }


def combined_analysis(
    data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    full analysis thing
    """
    players: Dict[str, Dict[str, Any]] = data.get('players', {})
    sessions: List[Dict[str, Any]] = data.get('sessions', [])

    # List comprehension: Filter high scores
    high_score_sessions: List[Dict[str, Any]] = [
        session for session in sessions
        if session.get('score', 0) > 1800
    ]

    # Dict comprehension: Group players by mode
    mode_groups: Dict[str, List[str]] = group_by_category(players)

    # Set comprehension: Find unique players
    unique_players: Set[str] = find_unique_players(sessions)

    # Combined analysis
    total_players: int = len(players)
    total_sessions: int = len(sessions)
    high_score_count: int = len(high_score_sessions)

    return {
        'total_players': total_players,
        'total_sessions': total_sessions,
        'high_score_sessions': high_score_count,
        'unique_active_players': len(unique_players),
        'mode_distribution': mode_groups,
        'score_categories': count_occurrences(sessions),
        'achievement_counts': create_mappings(players)
    }


def main() -> None:
    """
    Demonstrate all comprehension types with gaming data.
    """
    # Sample gaming data
    players: Dict[str, Dict[str, Any]] = {
        'alice': {
            'level': 42,
            'total_score': 5200,
            'sessions_played': 50,
            'favorite_mode': 'competitive',
            'achievements_count': 8
        },
        'bob': {
            'level': 28,
            'total_score': 2800,
            'sessions_played': 35,
            'favorite_mode': 'casual',
            'achievements_count': 5
        },
        'charlie': {
            'level': 35,
            'total_score': 3900,
            'sessions_played': 42,
            'favorite_mode': 'competitive',
            'achievements_count': 7
        },
        'diana': {
            'level': 50,
            'total_score': 8100,
            'sessions_played': 68,
            'favorite_mode': 'ranked',
            'achievements_count': 12
        }
    }

    sessions: List[Dict[str, Any]] = [
        {'player': 'alice', 'score': 2100, 'mode': 'competitive'},
        {'player': 'bob', 'score': 1200, 'mode': 'casual'},
        {'player': 'charlie', 'score': 1900, 'mode': 'competitive'},
        {'player': 'diana', 'score': 2500, 'mode': 'ranked'},
        {'player': 'alice', 'score': 1850, 'mode': 'competitive'},
        {'player': 'bob', 'score': 900, 'mode': 'casual'},
        {'player': 'charlie', 'score': 2100, 'mode': 'ranked'},
        {'player': 'diana', 'score': 2800, 'mode': 'ranked'},
    ]

    achievements: List[str] = [
        'first_kill', 'level_10', 'speedrun', 'boss_slayer'
    ]

    print("=== Analytics Dashboard Example ===\n")

    # List Comprehension Example
    print(">>> List Comprehension Example >>>")
    high_scores: List[Dict[str, Any]] = filter_high_scores(sessions)
    print(f"High scores (>1800): {len(high_scores)} sessions")
    for session in high_scores:
        print(f"  - {session['player']}: {session['score']} "
              f"({session['mode']})")
    print()

    # Dict Comprehension Example
    print(">>> Dict Comprehension Example >>>")
    score_categories: Dict[str, int] = count_occurrences(sessions)
    print("Score categories by mode:")
    for mode, count in score_categories.items():
        print(f"  - {mode}: {count} sessions")
    print()

    # Set Comprehension Example
    print(">>> Set Comprehension Example >>>")
    unique_players: Set[str] = find_unique_players(sessions)
    print(f"Unique players: {sorted(unique_players)}")
    print()

    # Combined Analysis
    print(">>> Combined Analysis >>>")
    data: Dict[str, Any] = {
        'players': players,
        'sessions': sessions,
        'achievements': achievements
    }
    analysis: Dict[str, Any] = combined_analysis(data)

    print(f"Total players: {analysis['total_players']}")
    print(f"Total sessions: {analysis['total_sessions']}")
    print(f"High score sessions: {analysis['high_score_sessions']}")
    print(
        f"Unique active players: {analysis['unique_active_players']}")
    print()

    print("Player distribution by mode:")
    for mode, player_list in analysis['mode_distribution'].items():
        print(f"  - {mode}: {len(player_list)} "
              f"players {player_list}")
    print()

    print("Achievement counts:")
    for player, count in analysis['achievement_counts'].items():
        print(f"  - {player}: {count} achievements")


if __name__ == "__main__":
    main()
