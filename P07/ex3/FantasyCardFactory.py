import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Creates fantasy-themed cards: dragons, spells, and magical items."""

    _CREATURES: list[dict[str, str | int]] = [
        {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
         "attack": 7, "health": 5},
        {"name": "Goblin Warrior", "cost": 2, "rarity": "Common",
         "attack": 2, "health": 1},
        {"name": "Ice Wizard", "cost": 4, "rarity": "Rare",
         "attack": 3, "health": 4},
    ]

    _SPELLS: list[dict[str, str | int]] = [
        {"name": "Fireball", "cost": 4, "rarity": "Uncommon",
         "effect_type": "damage"},
        {"name": "Ice Shard", "cost": 2, "rarity": "Common",
         "effect_type": "damage"},
        {"name": "Divine Light", "cost": 3, "rarity": "Rare",
         "effect_type": "heal"},
    ]

    _ARTIFACTS: list[dict[str, str | int]] = [
        {"name": "Mana Ring", "cost": 2, "rarity": "Uncommon",
         "durability": 5, "effect": "+1 mana per turn"},
        {"name": "Dragon Staff", "cost": 4, "rarity": "Rare",
         "durability": 3, "effect": "+2 attack to all creatures"},
        {"name": "Mana Crystal", "cost": 3, "rarity": "Uncommon",
         "durability": 4, "effect": "+1 mana per turn"},
    ]

    def get_supported_types(self) -> dict[str, list[str]]:
        """Return the card types supported by the fantasy factory."""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create a fantasy creature card."""
        if isinstance(name_or_power, str):
            data: dict[str, str | int] | None = next(
                (c for c in self._CREATURES if c["name"] == name_or_power),
                None,
            )
        else:
            data = None
        if data is None:
            data = random.choice(self._CREATURES)
        return CreatureCard(
            str(data["name"]),
            int(data["cost"]),
            str(data["rarity"]),
            int(data["attack"]),
            int(data["health"]),
        )

    def create_spell(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create a fantasy spell card."""
        if isinstance(name_or_power, str):
            data: dict[str, str | int] | None = next(
                (s for s in self._SPELLS if s["name"] == name_or_power),
                None,
            )
        else:
            data = None
        if data is None:
            data = random.choice(self._SPELLS)
        return SpellCard(
            str(data["name"]),
            int(data["cost"]),
            str(data["rarity"]),
            str(data["effect_type"]),
        )

    def create_artifact(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create a fantasy artifact card."""
        if isinstance(name_or_power, str):
            data: dict[str, str | int] | None = next(
                (a for a in self._ARTIFACTS if a["name"] == name_or_power),
                None,
            )
        else:
            data = None
        if data is None:
            data = random.choice(self._ARTIFACTS)
        return ArtifactCard(
            str(data["name"]),
            int(data["cost"]),
            str(data["rarity"]),
            int(data["durability"]),
            str(data["effect"]),
        )

    def create_themed_deck(self, size: int) -> dict[str, list[Card]]:
        """Create a themed deck split evenly across card types.
        returns:
        - creatures: list of CreatureCard instances
        - spells: list of SpellCard instances
        - artifacts: list of ArtifactCard instances
        """
        third: int = size // 3
        remainder: int = size - third * 3
        creatures: list[Card] = [self.create_creature() for _ in range(third + remainder)]
        spells: list[Card] = [self.create_spell() for _ in range(third)]
        artifacts: list[Card] = [self.create_artifact() for _ in range(third)]
        return {
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
        }
