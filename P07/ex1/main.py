from typing import Any, Dict


try:
    from ex0.Card import Card
    from ex0.CreatureCard import CreatureCard
    from ex1.SpellCard import SpellCard
    from ex1.ArtifactCard import ArtifactCard
    from ex1.Deck import Deck
except ImportError:
    print(
        "WARNING: you are using the module wrongly.\n"
        "launch this using 'py -m ex1.main' in the root directory."
    )
    exit(1)

try:
    from card_generator import CardGenerator  # type: ignore[import]
except ImportError:
    print(
        "WARNING: card_generator module not found. "
        "Using built-in sample data."
    )

    import random

    class CardGenerator:  # type: ignore[no-redef]
        """Fallback CardGenerator with hardcoded sample data."""

        _SAMPLE_CREATURES: list[dict[str, str | int]] = [
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
        _SAMPLE_SPELLS: list[Dict[str, Any]] = [
            {"name": "Lightning Bolt", "cost": 3,
             "rarity": "Common", "effect_type": "damage"},
            {"name": "Healing Potion", "cost": 2,
             "rarity": "Common", "effect_type": "heal"},
            {"name": "Fireball", "cost": 4,
             "rarity": "Uncommon", "effect_type": "damage"},
            {"name": "Shield Spell", "cost": 1,
             "rarity": "Common", "effect_type": "buff"},
            {"name": "Meteor", "cost": 8,
             "rarity": "Legendary", "effect_type": "damage"},
            {"name": "Ice Shard", "cost": 2,
             "rarity": "Common", "effect_type": "damage"},
            {"name": "Divine Light", "cost": 5,
             "rarity": "Rare", "effect_type": "heal"},
            {"name": "Magic Missile", "cost": 1,
             "rarity": "Common", "effect_type": "damage"},
        ]
        _SAMPLE_ARTIFACTS: list[Dict[str, Any]] = [
            {"name": "Mana Crystal", "cost": 2, "rarity": "Common",
             "durability": 5, "effect": "Permanent: +1 mana per turn"},
            {"name": "Sword of Power", "cost": 3, "rarity": "Uncommon",
             "durability": 3,
             "effect": "Permanent: +2 attack to equipped creature"},
            {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare",
             "durability": 4,
             "effect": "Permanent: Draw an extra card each turn"},
            {"name": "Shield of Defense", "cost": 5, "rarity": "Rare",
             "durability": 6,
             "effect": "Permanent: +3 health to all friendly creatures"},
            {"name": "Crown of Kings", "cost": 7, "rarity": "Legendary",
             "durability": 8,
             "effect": "Permanent: +1 cost reduction to all cards"},
            {"name": "Boots of Speed", "cost": 2, "rarity": "Uncommon",
             "durability": 2,
             "effect": "Permanent: Cards cost 1 less mana"},
            {"name": "Cloak of Shadows", "cost": 3, "rarity": "Uncommon",
             "durability": 3,
             "effect": "Permanent: Creatures have stealth"},
            {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary",
             "durability": 7,
             "effect": "Permanent: +1 spell damage"},
        ]

        def get_random_creature(self) -> Dict[str, Any]:
            return random.choice(self._SAMPLE_CREATURES).copy()

        def get_random_spell(self) -> Dict[str, Any]:
            return random.choice(self._SAMPLE_SPELLS).copy()

        def get_random_artifact(self) -> Dict[str, Any]:
            return random.choice(self._SAMPLE_ARTIFACTS).copy()


def main() -> None:
    """Demonstrate polymorphism with different card types in a deck."""
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    gen = CardGenerator()

    c_data: Dict[str, Any] = gen.get_random_creature()
    s_data: Dict[str, Any] = gen.get_random_spell()
    a_data: Dict[str, Any] = gen.get_random_artifact()

    deck = Deck()
    deck.add_card(CreatureCard(
        c_data["name"], c_data["cost"], c_data["rarity"],
        c_data["attack"], c_data["health"],
    ))
    deck.add_card(SpellCard(
        s_data["name"], s_data["cost"], s_data["rarity"],
        s_data["effect_type"],
    ))
    deck.add_card(ArtifactCard(
        a_data["name"], a_data["cost"], a_data["rarity"],
        a_data["durability"], a_data["effect"],
    ))
    deck.add_card(ArtifactCard(
        a_data["name"], a_data["cost"], a_data["rarity"],
        a_data["durability"], a_data["effect"],
    ))
    deck.add_card(SpellCard(
        s_data["name"], s_data["cost"], s_data["rarity"],
        s_data["effect_type"],
    ))

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    game_state: dict[str, int] = {"mana": 10}
    for _ in range(5):
        card: Card | None = deck.draw_card()
        if card is None:
            break
        card_type: Any = card.get_card_info().get("type", "Unknown")
        print(f"\nDrew: {card.name} ({card_type})")
        played_card: dict[str, str | int] = card.play(game_state)
        print(f"Play result: {played_card}")
        if int(played_card["mana_used"]) > 0:
            game_state["mana"] -= int(played_card["mana_used"])

    print(f"\nMana remaining after playing cards: {game_state['mana']}\n\n")


if __name__ == "__main__":
    main()
