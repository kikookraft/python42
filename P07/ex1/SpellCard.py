"""Concrete SpellCard implementation."""

from ex0.Card import Card


class SpellCard(Card):
    """A concrete card representing an instant magical effect."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        """Initialize a spell card.

        Args:
            name: The card's name.
            cost: The mana cost to play the card.
            rarity: The card's rarity tier.
            effect_type: The type of effect (damage, heal, buff, debuff).
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self._used = False

    def get_card_info(self) -> dict:
        """Return a dictionary with the spell card's full information."""
        info = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info

    def play(self, game_state: dict) -> dict:
        """Play the spell, consuming it in the process.

        Args:
            game_state: Current game state dictionary.

        Returns:
            A dict describing the result of playing the card.
        """
        self._used = True
        effect_map = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Restore {self.cost * 2} health",
            "buff": f"Grant +{self.cost} attack to a creature",
            "debuff": f"Reduce target attack by {self.cost}",
        }
        effect = effect_map.get(
            self.effect_type,
            f"Apply {self.effect_type} effect",
        )
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect,
        }

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell's effect against targets.

        Args:
            targets: List of target names to apply the effect to.

        Returns:
            A dict describing the resolved effect.
        """
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
