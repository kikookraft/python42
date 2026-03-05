from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory defining how themed card sets are created."""

    @abstractmethod
    def create_creature(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create a creature card."""
        pass

    @abstractmethod
    def create_spell(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create a spell card."""
        pass

    @abstractmethod
    def create_artifact(
        self,
        name_or_power: str | int | None = None,
    ) -> Card:
        """Create an artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict[str, list[Card]]:
        """Create a themed deck of cards."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict[str, list[str]]:
        """Return the card types supported by this factory."""
        pass
