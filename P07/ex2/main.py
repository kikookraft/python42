"""Exercise 2 - Ability System demonstration."""

from ex2.EliteCard import EliteCard


def main() -> None:
    """Demonstrate multiple interface inheritance with EliteCard."""
    print("=== DataDeck Ability System ===\n")

    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 4)

    card_methods = ["play", "get_card_info", "is_playable"]
    combat_methods = ["attack", "defend", "get_combat_stats"]
    magic_methods = ["cast_spell", "channel_mana", "get_magic_stats"]

    print("EliteCard capabilities:")
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    print(f"\nPlaying {warrior.name} (Elite Card):")
    warrior.play({"mana": 10})

    print("\nCombat phase:")

    class _Target:
        name = "Enemy"
    print(f"Attack result: {warrior.attack(_Target())}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    print(
        f"Spell cast: "
        f"{warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
    )
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")
    print(
        "\nHow do multiple interfaces enable flexible card design? "
        "What are the advantages of separating combat and magic concerns?"
    )


if __name__ == "__main__":
    main()
