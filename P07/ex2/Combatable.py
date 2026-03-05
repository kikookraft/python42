from abc import ABC, abstractmethod


class Combatable(ABC):
    """Abstract interface defining combat capabilities."""

    @abstractmethod
    def attack(self, target: "Combatable") -> dict[str, str | int]:
        """Perform an attack against a target."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[str, str | int]:
        """Defend against incoming damage."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[str, str | int]:
        """Return current combat statistics."""
        pass
