"""Abstract magic interface for DataDeck cards."""

from abc import ABC, abstractmethod


class Magical(ABC):
    """Abstract interface defining magical capabilities."""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Cast a spell at the specified targets.

        Args:
            spell_name: The name of the spell to cast.
            targets: A list of target names.

        Returns:
            A dict describing the spell cast result.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """Channel additional mana.

        Args:
            amount: The amount of mana to channel.

        Returns:
            A dict describing the channeling result.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """Return current magic statistics.

        Returns:
            A dict with magic stat values.
        """
        pass
