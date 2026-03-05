"""Concrete SpellCard implementation."""

from ex0.Card import Card


class SpellCard(Card):
    """magic (not the card game) initialisation"""

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
        if effect_type not in {"damage", "heal", "buff", "debuff"}:
            raise ValueError(f"Invalid effect_type: {effect_type}. "
                             "Must be one of: damage, heal, buff, debuff.")
        self.effect_type: str = effect_type
        self._used: bool = False

    def get_card_info(self) -> dict[str, str | int]:
        """Return a dictionary with the spell card's full information.
        returns:
        - type: "Spell"
        - effect_type: The type of effect (damage, heal, buff, debuff)
        - other info from the base Card class (name, cost, rarity)
        """
        info: dict[str, str | int] = super().get_card_info()
        info["type"] = "Spell"
        info["effect_type"] = self.effect_type
        return info

    def play(self, game_state: dict[str, int]) -> dict[str, str | int]:
        """Play the spell, consuming it in the process.
        returns:
        - card_played: The name of the card played
        - mana_used: The mana cost of the card
        - effect: A description of the effect applied (based on effect_type)
        """
        # check if the spell has already been used or enough mana is available
        if self._used:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect":
                "Spell has already been used and cannot be played again.",
            }
        if game_state.get("mana", 0) < self.cost:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to play the spell.",
            }
        self._used = True
        effect_map: dict[str, str] = {
            "damage": f"Deal {self.cost} damage to target",
            "heal": f"Restore {self.cost * 2} health",
            "buff": f"Grant +{self.cost} attack to a creature",
            "debuff": f"Reduce target attack by {self.cost}",
        }
        effect: str = effect_map.get(
            self.effect_type,
            f"Apply {self.effect_type} effect",
        )
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect,
        }

    def resolve_effect(
            self,
            targets: list[str]
            ) -> dict[str, str | int | list[str]]:
        """Apply the spell's effect to the specified targets."""
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True,
        }
