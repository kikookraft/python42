"""Abstract strategy interface for DataDeck game engine."""

from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract interface defining a game strategy."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a turn based on the current hand and battlefield.

        Args:
            hand: Cards currently in hand.
            battlefield: Cards currently on the battlefield.

        Returns:
            A dict describing the turn actions taken.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of this strategy.

        Returns:
            The strategy name string.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Order available targets by strategic priority.

        Args:
            available_targets: List of possible targets.

        Returns:
            Ordered list of targets.
        """
        pass
