"""Tournament platform managing registered cards and matches."""

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages card registration, match creation, and leaderboards."""

    def __init__(self) -> None:
        """Initialise the platform with empty registry and match log."""
        self._registry: dict = {}
        self._matches: list = []

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its unique tournament ID.

        Args:
            card: The TournamentCard to register.

        Returns:
            A string ID for the registered card.
        """
        base = card.name.lower().replace(" ", "_")
        existing = sum(
            1 for k in self._registry if k.startswith(base)
        )
        card_id = f"{base}_{existing + 1:03d}"
        self._registry[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulate a match between two registered cards.

        Args:
            card1_id: ID of the first card.
            card2_id: ID of the second card.

        Returns:
            A dict with winner, loser, and updated ratings.

        Raises:
            KeyError: If either card ID is not registered.
        """
        card1 = self._registry[card1_id]
        card2 = self._registry[card2_id]

        score1 = card1.attack_power + card1.defense + card1.calculate_rating()
        score2 = card2.attack_power + card2.defense + card2.calculate_rating()

        if score1 >= score2:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
        self._matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        """Return cards sorted by rating (highest first).

        Returns:
            A list of dicts with rank, name, rating, and record.
        """
        sorted_cards = sorted(
            self._registry.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True,
        )
        board = []
        for rank, (card_id, card) in enumerate(sorted_cards, start=1):
            info = card.get_rank_info()
            board.append({
                "rank": rank,
                "id": card_id,
                "name": card.name,
                "rating": info["rating"],
                "record": f"{info['wins']}-{info['losses']}",
            })
        return board

    def generate_tournament_report(self) -> dict:
        """Generate a summary report of the entire tournament.

        Returns:
            A dict with totals and platform status.
        """
        total_cards = len(self._registry)
        matches_played = len(self._matches)
        avg_rating = (
            sum(c.calculate_rating() for c in self._registry.values())
            // total_cards
            if total_cards
            else 0
        )
        return {
            "total_cards": total_cards,
            "matches_played": matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
