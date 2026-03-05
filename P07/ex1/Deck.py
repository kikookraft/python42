"""Deck management system for DataDeck."""

import random
from typing import Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    """Manages a collection of cards as a playable deck."""

    def __init__(self) -> None:
        """Initialize an empty deck."""
        self._cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck.

        Args:
            card: The card to add.
        """
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card from the deck by name.

        Args:
            card_name: The name of the card to remove.

        Returns:
            True if the card was found and removed, False otherwise.
        """
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck in place."""
        random.shuffle(self._cards)

    def draw_card(self) -> Optional[Card]:
        """Draw the top card from the deck.

        Returns:
            The drawn card, or None if the deck is empty.
        """
        if not self._cards:
            return None
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict[str, int | float]:
        """Return statistics about the current deck contents.

        returns:
        - total_cards: Total number of cards in the deck
        - creatures: Number of creature cards
        - spells: Number of spell cards
        - artifacts: Number of artifact cards
        - avg_cost: Average mana cost of cards in the deck
        """
        total: int = len(self._cards)
        creatures: int = sum(
            1 for c in self._cards if isinstance(c, CreatureCard))
        spells: int = sum(
            1 for c in self._cards if isinstance(c, SpellCard))
        artifacts: int = sum(
            1 for c in self._cards if isinstance(c, ArtifactCard))
        total_cost: int = sum(c.cost for c in self._cards)
        avg_cost: float = round(total_cost / total, 1) if total else 0.0
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
