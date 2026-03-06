from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages card registration, match creation, and leaderboards."""

    def __init__(self) -> None:
        """Initialise the platform with empty registry and match log."""
        self._registry: dict[str, TournamentCard] = {}
        self._matches: list[dict[str, str | int]] = []

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its unique tournament ID."""
        base: str = card.name.lower().replace(" ", "_")
        existing: int = sum(
            1 for k in self._registry if k.startswith(base)
        )
        card_id: str = f"{base}_{existing + 1:03d}"
        self._registry[card_id] = card
        return card_id

    def create_match(
        self, card1_id: str, card2_id: str
    ) -> dict[str, str | int]:
        """Simulate a match between two registered cards.
        returns:
        - winner: ID of the winning card
        - loser: ID of the losing card
        - winner_rating: Updated rating of the winner
        - loser_rating: Updated rating of the loser

        Raises:
            KeyError: If either card ID is not registered.
        """
        card1: TournamentCard = self._registry[card1_id]
        card2: TournamentCard = self._registry[card2_id]

        score1: int = card1.attack_power + \
            card1.defense + card1.calculate_rating()
        score2: int = card2.attack_power + \
            card2.defense + card2.calculate_rating()

        if score1 >= score2:
            winner: TournamentCard = card1
            loser: TournamentCard = card2
            winner_id: str = card1_id
            loser_id: str = card2_id
        else:
            winner: TournamentCard = card2
            loser: TournamentCard = card1
            winner_id: str = card2_id
            loser_id: str = card1_id
        winner.update_wins(1)
        loser.update_losses(1)

        result: dict[str, str | int] = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }
        self._matches.append(result)
        return result

    def get_leaderboard(self) -> list[dict[str, str | int]]:
        """Return cards sorted by rating (highest first).
        returns:
        - rank: Position on the leaderboard
        - id: The card's tournament ID
        - name: The card's name
        - rating: Current rating
        - record: Win-loss record as "W-L"
        """
        sorted_cards: list[tuple[str, TournamentCard]] = sorted(
            self._registry.items(),
            key=lambda item: item[1].calculate_rating(),
            reverse=True,
        )
        board: list[dict[str, str | int]] = []
        for rank, (card_id, card) in enumerate(sorted_cards, start=1):
            info: dict[str, str | int] = card.get_rank_info()
            board.append({
                "rank": rank,
                "id": card_id,
                "name": card.name,
                "rating": info["rating"],
                "record": f"{info['wins']}-{info['losses']}",
            })
        return board

    def generate_tournament_report(self) -> dict[str, str | int]:
        """Generate a summary report of the entire tournament.
        returns:
        - total_cards: Number of registered cards
        - matches_played: Total matches simulated
        - avg_rating: Average rating across all cards
        - platform_status: Current platform status string
        """
        total_cards: int = len(self._registry)
        matches_played: int = len(self._matches)
        avg_rating: int = (
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
