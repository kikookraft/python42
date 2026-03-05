"""Concrete CreatureCard implementation."""

from typing import Any
from ex0.Card import Card


class CreatureCard(Card):
    """Card for creatures that implement the abstract method"""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        """Initialize a creature card.

        Args:
            name: The card's name.
            cost: The mana cost to play the card.
            rarity: The card's rarity tier.
            attack: Attack power of the creature (must be positive).
            health: Health points of the creature (must be positive).

        Raises:
            ValueError: If attack or health are not positive integers.
        """
        if attack < 0:
            raise ValueError(f"Attack of {name} must be positive integer.")
        if health < 0:
            raise ValueError(f"Health of {name} must be positive integer.")
        if cost < 0:
            raise ValueError(f"Cost of {name} must be positive integer.")
        super().__init__(name, cost, rarity)
        self.attack: int = attack
        self.health: int = health

    def get_card_info(self) -> dict[str, int | str]:
        """Return a dictionary with the creature card's full information."""
        info: dict[str, Any] = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Summon card on the battlefield.

        returns:
        - card_played: str
        - mana_used: int
        - effect: str
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: "CreatureCard") -> dict[str, Any]:
        """Attack another thing.

        returns:
        - attacker: str
        - target: str
        - damage_dealt: int
        - combat_resolved: bool
        """
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
