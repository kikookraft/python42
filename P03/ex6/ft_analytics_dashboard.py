def main() -> None:
    """Demonstrate comprehension mastery with gaming data yooohooo
    """

    # Sample gaming data - hardcoded because we're not savages
    game_data: dict[str, dict[str, int | str]] = {
        'alice': {'score': 2300, 'level': 42, 'region': 'north',
                  'achievements': 5, 'status': 'active'},
        'bob': {'score': 1800, 'level': 28, 'region': 'east',
                'achievements': 3, 'status': 'active'},
        'charlie': {'score': 2150, 'level': 35, 'region': 'central',
                    'achievements': 7, 'status': 'active'},
        'diana': {'score': 2050, 'level': 30, 'region': 'north',
                  'achievements': 4, 'status': 'inactive'},
        'eve': {'score': 1500, 'level': 20, 'region': 'east',
                'achievements': 2, 'status': 'inactive'},
        'frank': {'score': 950, 'level': 15, 'region': 'Auvergne Rhone Alpes',
                  'achievements': 1, 'status': 'active'}
    }

    all_achievements: list[str] = [
        'first_kill', 'level_10', 'boss_slayer',
        'first_kill', 'speedrun', 'level_10',
        'boss_slayer', 'collector', 'speedrun',
        'first_kill', 'collector', 'level_10'
    ]

    print("\n=== jdhdjshggfdhgdshgffshgdfjhds ===")

    # high sscores
    high_scorers: list[str] = [
        name for name, data in game_data.items()
        if isinstance(data['score'], int) and data['score'] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    # transform scores
    scores_doubled: list[int] = [
        data['score'] * 2 for data in game_data.values()
        if isinstance(data['score'], int)
    ]
    # data = map(lambda x: x * 2,
    #            [data['score'] for data in game_data.values()])
    # print(f"Scores doubled (map): {list(data)}")
    print(f"Scores doubled: {scores_doubled}")

    # actives players
    active_players: list[str] = [
        name for name, data in game_data.items()
        if data['status'] == 'active'
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict ===")

    # scores carabistouilles
    player_scores: dict[str, int] = {
        name: data['score'] for name, data in game_data.items()
        if isinstance(data['score'], int)
    }
    print(f"Player scores: {player_scores}")

    # scores
    score_categories: dict[str, int] = {
        'high': sum(1 for d in game_data.values()
                    if isinstance(d['score'], int) and d['score'] > 2000),
        'medium': sum(1 for d in game_data.values()
                      if isinstance(d['score'], int)
                      and 1500 <= d['score'] <= 2000),
        'low': sum(1 for d in game_data.values()
                   if isinstance(d['score'], int) and d['score'] < 1500)
    }
    print(f"Score categories: {score_categories}")

    # count achievements
    achievement_counts: dict[str, int] = {
        name: data['achievements'] for name, data in game_data.items()
        if isinstance(data['achievements'], int)
    }
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set ===")

    # unique players
    unique_players: set[str] = {
        name for name in game_data.keys()
    }
    print(f"Unique players: {unique_players}")

    # uniques achievments
    unique_achievements: set[str] = {
        achievement for achievement in all_achievements
    }
    print(f"Unique achievements: {unique_achievements}")

    # LA REGION
    active_regions: set[str] = {
        data['region'] for data in game_data.values()
        if data['status'] == 'active' and isinstance(data['region'], str)
    }
    print(f"Active regions: {active_regions}")

    print("\n=== Combined ===")

    # mess
    total_players: int = len(unique_players)
    total_unique_achievements: int = len(unique_achievements)

    scores: list[int] = [
        data['score'] for data in game_data.values()
        if isinstance(data['score'], int)
    ]
    average_score: float = sum(scores) / len(scores) if scores else 0

    # find top performer
    top_player: str = max(
        game_data.keys(),
        key=lambda name: (
            game_data[name]['score']
            if isinstance(game_data[name]['score'], int) else 0
        )
    )
    top_score: int | str = game_data[top_player]['score']
    top_achievements: int = int(game_data[top_player]['achievements']) + 1

    # add achievements to top player
    game_data[top_player].update({'achievements': top_achievements})

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.2f}")
    print(f"Top performer: {top_player} ({top_score} points, "
          f"{top_achievements} achievements)")


if __name__ == "__main__":
    main()
