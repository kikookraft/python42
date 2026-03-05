"""Exercise 0 - Card Foundation demonstration."""

from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Demonstrate the abstract base class and CreatureCard."""
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    available_mana = 6
    print(f"\nPlaying {dragon.name} with {available_mana} mana available:")
    print(f"Playable: {dragon.is_playable(available_mana)}")
    print(f"Play result: {dragon.play({'mana': available_mana})}")

    print(f"\n{dragon.name} attacks {goblin.name}:")
    print(f"Attack result: {dragon.attack_target(goblin)}")

    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {dragon.is_playable(low_mana)}")

    print("\nAbstract pattern successfully demonstrated!")
    print(
        "\nHow do abstract base classes ensure consistency across different "
        "card types? What happens if you try to create a Card directly "
        "without implementing required methods?"
    )


if __name__ == "__main__":
    main()
