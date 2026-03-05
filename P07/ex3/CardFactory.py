"""Abstract factory interface for creating DataDeck cards."""

from abc import ABC, abstractmethod
from typing import Optional
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory defining how themed card sets are created."""

    @abstractmethod
    def create_creature(
        self,
        name_or_power: Optional[str | int] = None,
    ) -> Card:
        """Create a creature card.

        Args:
            name_or_power: Optional name or power level hint.

        Returns:
            A concrete Card instance representing a creature.
        """
        pass

    @abstractmethod
    def create_spell(
        self,
        name_or_power: Optional[str | int] = None,
    ) -> Card:
        """Create a spell card.

        Args:
            name_or_power: Optional name or power level hint.

        Returns:
            A concrete Card instance representing a spell.
        """
        pass

    @abstractmethod
    def create_artifact(
        self,
        name_or_power: Optional[str | int] = None,
    ) -> Card:
        """Create an artifact card.

        Args:
            name_or_power: Optional name or power level hint.

        Returns:
            A concrete Card instance representing an artifact.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck of cards.

        Args:
            size: Number of cards to include.

        Returns:
            A dict mapping card types to lists of created cards.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return the card types supported by this factory.

        Returns:
            A dict listing supported creature, spell, and artifact names.
        """
        pass
