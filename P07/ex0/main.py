from typing import Any, Dict
try:
    from ex0.CreatureCard import CreatureCard
except ImportError:
    # Fallback if card_generator is not available
    print(
        "WARNING: you are using the module wrongly.\n"
        "launch this using 'py -m ex0.main' in the root directory."
    )
    exit(1)
try:
    from card_generator import CardGenerator  # type: ignore[import]
except ImportError:
    # Fallback if card_generator is not available
    print(
        "WARNING: card_generator module not found. "
        "Using built-in sample data."
    )

    import random

    class CardGenerator:  # type: ignore[no-redef]
        """Fallback CardGenerator with hardcoded sample creature data."""

        _SAMPLE_CREATURES: list[Dict[str, Any]] = [
            {"name": "Fire Dragon", "cost": 5,
             "rarity": "Legendary", "attack": 7, "health": 5},
            {"name": "Goblin Warrior", "cost": 2,
             "rarity": "Common", "attack": 2, "health": 1},
            {"name": "Ice Wizard", "cost": 4,
             "rarity": "Rare", "attack": 3, "health": 4},
            {"name": "Lightning Elemental", "cost": 3,
             "rarity": "Uncommon", "attack": 4, "health": 2},
            {"name": "Stone Golem", "cost": 6,
             "rarity": "Rare", "attack": 5, "health": 8},
            {"name": "Shadow Assassin", "cost": 3,
             "rarity": "Uncommon", "attack": 5, "health": 2},
            {"name": "Healing Angel", "cost": 4,
             "rarity": "Rare", "attack": 2, "health": 6},
            {"name": "Forest Sprite", "cost": 1,
             "rarity": "Common", "attack": 1, "health": 1},
        ]

        def get_random_creature(self) -> Dict[str, Any]:
            return random.choice(self._SAMPLE_CREATURES).copy()


def get_random_creature() -> CreatureCard:
    """Return a random CreatureCard built from CardGenerator data."""
    generator = CardGenerator()
    data: Dict[str, Any] = generator.get_random_creature()
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

    available_mana = 5
    for creature in random_creature:
        print(
            f"\nPlaying {creature.name} with {available_mana} mana available:")
        print(f"Playable: {creature.is_playable(available_mana)}")
        print(f"Play result: {creature.play({'mana': available_mana})}")
        if creature.is_playable(available_mana):
            available_mana -= creature.cost

    print(f"\nMana remaining after playing creatures: {available_mana}")


if __name__ == "__main__":
    main()
