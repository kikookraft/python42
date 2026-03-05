"""Abstract ranking interface for tournament participants."""

from abc import ABC, abstractmethod


class Rankable(ABC):
    """Abstract interface for cards that can be ranked in tournaments."""

    @abstractmethod
    def calculate_rating(self) -> int:
        """Calculate and return the current rating.

        Returns:
            The computed rating as an integer.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """Update the win count.

        Args:
            wins: Number of wins to add.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """Update the loss count.

        Args:
            losses: Number of losses to add.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """Return ranking information.

        Returns:
            A dict with ranking data.
        """
        pass
