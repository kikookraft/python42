"""Abstract base class for all DataDeck cards."""

from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract base class that defines the universal card blueprint."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize base card attributes.

        Args:
            name: The card's name.
            cost: The mana cost to play the card.
            rarity: The card's rarity tier.
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play this card and apply its effect to the game state.

        Args:
            game_state: Current state of the game.

        Returns:
            A dict describing the result of playing the card.
        """
        pass

    def get_card_info(self) -> dict:
        """Return a dictionary with the card's information.

        Returns:
            A dict containing name, cost, and rarity.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check whether the card can be played with available mana.

        Args:
            available_mana: The amount of mana currently available.

        Returns:
            True if the card's cost is covered, False otherwise.
        """
        return available_mana >= self.cost
