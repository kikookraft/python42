"""Exercise 1 - Deck Builder demonstration."""

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    """Demonstrate polymorphism with different card types in a deck."""
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(ArtifactCard(
        "Mana Crystal", 2, "Uncommon", 5, "+1 mana per turn"
    ))

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    game_state: dict = {"mana": 10}
    for _ in range(3):
        card = deck.draw_card()
        if card is None:
            break
        card_type = card.get_card_info().get("type", "Unknown")
        print(f"\nDrew: {card.name} ({card_type})")
        print(f"Play result: {card.play(game_state)}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )
    print(
        "\nHow does polymorphism enable the Deck to work with any card type? "
        "What are the benefits of this design pattern for card game systems?"
    )


if __name__ == "__main__":
    main()
