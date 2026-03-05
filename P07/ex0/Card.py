"""Abstract base class for all DataDeck cards."""

from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):
    """Abstract base class that defines the universal card blueprint."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialise base card attributes."""
        if cost < 0:
            raise ValueError(f"Cost of the card {name} must be positive.")
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict[Any, Any]) -> dict[Any, Any]:
        pass

    def get_card_info(self) -> dict[str, Any]:
        """Return info of the cards

        returns:\n
        - name: str
        - cost: int
        - rarity: str
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card is playable based on cost and available mana"""
        return available_mana >= self.cost
