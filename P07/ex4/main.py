try:
    from ex4.TournamentCard import TournamentCard
    from ex4.TournamentPlatform import TournamentPlatform
    from ex2.Combatable import Combatable
    from ex4.Rankable import Rankable
    from ex0.Card import Card
except ImportError:
    print(
        "WARNING: you are using the module wrongly.\n"
        "launch this using 'py -m ex4.main' in the root directory."
    )
    exit(1)


def main() -> None:
    """Demonstrate the full tournament platform."""
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 3, 6)

    dragon_id: str = platform.register_card(dragon)
    wizard_id: str = platform.register_card(wizard)

    interfaces: list[str] = [
        Card.__name__, Combatable.__name__, Rankable.__name__
    ]
    for card, card_id in [(dragon, dragon_id), (wizard, wizard_id)]:
        rank_info: dict[str, int | str] = card.get_rank_info()
        record: str = f"{rank_info['wins']}-{rank_info['losses']}"
        print(f"\n{card.name} (ID: {card_id}):")
        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {card.calculate_rating()}")
        print(f"- Record: {record}")

    print("\nCreating tournament match...")
    match_result: dict[str, str | int] = platform.create_match(
        dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament is over! ===")


if __name__ == "__main__":
    main()
