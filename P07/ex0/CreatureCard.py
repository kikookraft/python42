"""Concrete CreatureCard implementation."""

from ex0.Card import Card


class CreatureCard(Card):
    """A concrete card representing a creature on the battlefield."""

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
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer.")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer.")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        """Return a dictionary with the creature card's full information."""
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info

    def play(self, game_state: dict) -> dict:
        """Summon the creature to the battlefield.

        Args:
            game_state: Current game state dictionary.

        Returns:
            A dict describing the result of playing the card.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: "CreatureCard") -> dict:
        """Attack another creature.

        Args:
            target: The creature being attacked.

        Returns:
            A dict describing the combat result.
        """
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }
