"""Exercise 4 - Tournament Platform demonstration."""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Card


def main() -> None:
    """Demonstrate the full tournament platform."""
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 3, 6)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    interfaces = [Card.__name__, Combatable.__name__, Rankable.__name__]
    for card, card_id in [(dragon, dragon_id), (wizard, wizard_id)]:
        rank_info = card.get_rank_info()
        record = f"{rank_info['wins']}-{rank_info['losses']}"
        print(f"\n{card.name} (ID: {card_id}):")
        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {card.calculate_rating()}")
        print(f"- Record: {record}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(
            f"{entry['rank']}. {entry['name']} - "
            f"Rating: {entry['rating']} ({entry['record']})"
        )

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
    print(
        "\nHow does multiple inheritance allow a class to implement several "
        "interfaces? What are the benefits of combining ranking capabilities "
        "with card game mechanics?"
    )


if __name__ == "__main__":
    main()
