from abc import ABC, abstractmethod
from typing import Any


class GameStrategy(ABC):
    """Abstract interface defining a game strategy."""

    @abstractmethod
    def execute_turn(
        self,
        hand: list[Any],
        battlefield: list[Any],
    ) -> dict[str, Any]:
        """Execute a turn based on the current hand and battlefield."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of this strategy."""
        pass

    @abstractmethod
    def prioritize_targets(
        self,
        available_targets: list[Any],
    ) -> list[Any]:
        """Order available targets by strategic priority."""
        pass
