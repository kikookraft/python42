"""Fantasy-themed concrete card factory."""

import random
from typing import Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Creates fantasy-themed cards: dragons, spells, and magical items."""

    _CREATURES = [
        {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary",
         "attack": 7, "health": 5},
        {"name": "Goblin Warrior", "cost": 2, "rarity": "Common",
         "attack": 2, "health": 1},
        {"name": "Ice Wizard", "cost": 4, "rarity": "Rare",
         "attack": 3, "health": 4},
    ]

    _SPELLS = [
        {"name": "Fireball", "cost": 4, "rarity": "Uncommon",
         "effect_type": "damage"},
        {"name": "Ice Shard", "cost": 2, "rarity": "Common",
         "effect_type": "damage"},
        {"name": "Divine Light", "cost": 3, "rarity": "Rare",
         "effect_type": "heal"},
    ]

    _ARTIFACTS = [
        {"name": "Mana Ring", "cost": 2, "rarity": "Uncommon",
         "durability": 5, "effect": "+1 mana per turn"},
        {"name": "Dragon Staff", "cost": 4, "rarity": "Rare",
         "durability": 3, "effect": "+2 attack to all creatures"},
        {"name": "Mana Crystal", "cost": 3, "rarity": "Uncommon",
         "durability": 4, "effect": "+1 mana per turn"},
    ]

    def get_supported_types(self) -> dict:
        """Return the card types supported by the fantasy factory."""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(
        self,
        name_or_power: Optional[str | int] = None,
    ) -> Card:
        """Create a fantasy creature card.

        Args:
            name_or_power: Optional creature name or power level.

        Returns:
            A CreatureCard instance.
        """
        if isinstance(name_or_power, str):
            data = next(
                (c for c in self._CREATURES if c["name"] == name_or_power),
                None,
            )
        else:
            data = None
        if data is None:
            data = random.choice(self._CREATURES)
        return CreatureCard(
            data["name"],
            data["cost"],
            data["rarity"],
            data["attack"],
            data["health"],
        )

    def create_spell(
        self,
        name_or_power: Optional[str | int] = None,
    ) -> Card:
        """Create a fantasy spell card.

        Args:
            name_or_power: Optional spell name or power level.

        Returns:
            A SpellCard instance.
        """
        if isinstance(name_or_power, str):
            data = next(
                (s for s in self._SPELLS if s["name"] == name_or_power),
                None,
            )
        else:
            data = None
        if data is None:
            data = random.choice(self._SPELLS)
        return SpellCard(
            data["name"],
            data["cost"],
            data["rarity"],
            data["effect_type"],
        )

    def create_artifact(
        self,
        name_or_power: Optional[str | int] = None,
    ) -> Card:
        """Create a fantasy artifact card.

        Args:
            name_or_power: Optional artifact name or power level.

        Returns:
            An ArtifactCard instance.
        """
        if isinstance(name_or_power, str):
            data = next(
                (a for a in self._ARTIFACTS if a["name"] == name_or_power),
                None,
            )
        else:
            data = None
        if data is None:
            data = random.choice(self._ARTIFACTS)
        return ArtifactCard(
            data["name"],
            data["cost"],
            data["rarity"],
            data["durability"],
            data["effect"],
        )

    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck split evenly across card types.

        Args:
            size: Total number of cards to create.

        Returns:
            A dict mapping 'creatures', 'spells', 'artifacts' to card lists.
        """
        third = size // 3
        remainder = size - third * 3
        creatures = [self.create_creature() for _ in range(third + remainder)]
        spells = [self.create_spell() for _ in range(third)]
        artifacts = [self.create_artifact() for _ in range(third)]
        return {
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
        }
