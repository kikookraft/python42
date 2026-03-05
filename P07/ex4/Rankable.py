from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract interface for cards that can be ranked in tournaments."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current rating."""
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the win count."""
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the loss count."""
        pass

    @abstractmethod
    def get_rank_info(self) -> dict[str, str | int]:
        """Return ranking information."""
        pass
