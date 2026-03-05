from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract interface defining magical capabilities."""

    @abstractmethod
    def cast_spell(
            self,
            spell_name: str,
            targets: list[str]) -> dict[str, str | int | list[str]]:
        """Cast a spell at the specified targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[str, str | int]:
        """Channel additional mana."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict[str, str | int]:
        """Return current magic statistics."""
        pass
