import sys
import os

# some magic to import from parent directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ex0.CreatureCard import CreatureCard  # noqa: E402
from card_generator import CardGenerator  # noqa: E402


def get_random_creature() -> CreatureCard:
    """Return a random CreatureCard built from CardGenerator data."""
    generator = CardGenerator()
    data = generator.get_random_creature()
    return CreatureCard(
        data["name"],
        data["cost"],
        data["rarity"],
        data["attack"],
        data["health"],
    )


def main() -> None:
    """Demonstrate the abstract base class and CreatureCard."""
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    random_creature: list[CreatureCard] = [
        get_random_creature() for _ in range(3)
    ]

    print("CreatureCard Info:")
    for creature in random_creature:
        print(creature.get_card_info())

    available_mana = 6
    for creature in random_creature:
        print(
            f"\nPlaying {creature.name} with {available_mana} mana available:")
        print(f"Playable: {creature.is_playable(available_mana)}")
        print(f"Play result: {creature.play({'mana': available_mana})}")
        available_mana -= creature.cost


if __name__ == "__main__":
    main()
