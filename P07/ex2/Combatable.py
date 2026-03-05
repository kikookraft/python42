"""Abstract combat interface for DataDeck cards."""

from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract interface defining combat capabilities."""

    @abstractmethod
    def attack(self, target) -> dict:
        """Perform an attack against a target.

        Args:
            target: The target being attacked.

        Returns:
            A dict describing the attack result.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage.

        Args:
            incoming_damage: The amount of damage coming in.

        Returns:
            A dict describing the defense result.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return current combat statistics.

        Returns:
            A dict with combat stat values.
        """
        pass
