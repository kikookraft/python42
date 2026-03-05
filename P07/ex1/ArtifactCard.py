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
        self.durability = durability
        self.effect = effect
        self._active = False

    def get_card_info(self) -> dict:
        """Return a dictionary with the artifact card's full information."""
        info = super().get_card_info()
        info["type"] = "Artifact"
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info

    def play(self, game_state: dict) -> dict:
        """Play the artifact, placing it into the active area.

        Args:
            game_state: Current game state dictionary.

        Returns:
            A dict describing the result of playing the card.
        """
        self._active = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict:
        """Activate the artifact's ongoing ability.

        Returns:
            A dict describing the activated ability result.
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
