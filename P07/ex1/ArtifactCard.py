"""Concrete ArtifactCard implementation."""

from ex0.Card import Card


class ArtifactCard(Card):
    """A concrete card representing a permanent game modifier."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        """Initialize an artifact card.
        Args:
            name: The card's name.
            cost: The mana cost to play the card.
            rarity: The card's rarity tier.
            durability: Number of turns the artifact lasts.
            effect: Description of the permanent ability.
        """
        super().__init__(name, cost, rarity)
        if durability < 0:
            raise ValueError(f"Durability of {durability} is invalid."
                             "Must be non-negative.")
        self.durability: int = durability
        self.effect: str = effect
        self._active: bool = False

    def get_card_info(self) -> dict[str, str | int | bool]:
        """Return a dictionary with the artifact card's full information."""
        info: dict[str, str | int | bool] = super().get_card_info()
        info["type"] = "Artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info

    def play(self, game_state: dict[str, int]) -> dict[str, str | int]:
        """Play the artifact, placing it into the active area.

        returns:
        - card_played: The name of the card played
        - mana_used: The mana cost of the card
        - effect: A description of the effect applied (based on effect_type)
        """
        if game_state.get("mana", 0) < self.cost:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to play this card.",
            }
        if self._active:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect":
                "This artifact is already active and cannot be played again.",
            }
        self._active = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict[str, str | int | bool]:
        """Activate the artifact's ongoing ability.

        returns:
        - artifact: The name of the artifact
        - ability: The effect of the artifact
        - durability_remaining: The remaining durability of the artifact
        - activated: Whether the ability was successfully activated
        """
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "reason": "No durability",
            }
        self.durability -= 1
        return {
            "artifact": self.name,
            "ability": self.effect,
            "durability_remaining": self.durability,
            "activated": True,
        }
