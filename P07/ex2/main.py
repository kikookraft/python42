try:
    from ex2.EliteCard import EliteCard
except ImportError:
    print(
        "WARNING: you are using the module wrongly.\n"
        "launch this using 'py -m ex2.main' in the root directory."
    )
    exit(1)


def main() -> None:
    """Demonstrate multiple interface inheritance with EliteCard."""
    print("=== DataDeck Ability System ===\n")

    warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 4)

    card_methods: list[str] = ["play", "get_card_info", "is_playable"]
    combat_methods: list[str] = ["attack", "defend", "get_combat_stats"]
    magic_methods: list[str] = ["cast_spell",
                                "channel_mana", "get_magic_stats"]

    print("EliteCard capabilities:")
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combat_methods}")
    print(f"- Magical: {magic_methods}")

    print(f"\nPlaying {warrior.name} (Elite Card):")
    warrior.play({"mana": 10})

    print("\nCombat phase:")

    class _Target:
        name: str = "Enemy"
    print(f"Attack result: {warrior.attack(_Target())}")
    print(f"Defense result: {warrior.defend(5)}")

    print("\nMagic phase:")
    print(
        f"Spell cast: "
        f"{warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
    )
    print(f"Mana channel: {warrior.channel_mana(3)}")


if __name__ == "__main__":
    main()
