"""Concrete aggressive game strategy."""

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """A strategy that prioritises attacking and dealing damage fast."""

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Sort targets: enemy player first, then enemy creatures.

        Args:
            available_targets: List of possible targets.

        Returns:
            Ordered list of targets.
        """
        player_targets = [
            t for t in available_targets if "Player" in str(t)
        ]
        other_targets = [
            t for t in available_targets if "Player" not in str(t)
        ]
        return player_targets + other_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Play low-cost cards first and attack aggressively.

        Args:
            hand: Cards currently in hand.
            battlefield: Cards currently on the battlefield.

        Returns:
            A dict describing the turn actions taken.
        """
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        mana_budget = sum(c.cost for c in sorted_hand)
        mana_used = 0
        cards_played = []
        for card in sorted_hand:
            if mana_used + card.cost <= mana_budget:
                cards_played.append(card.name)
                mana_used += card.cost

        targets = self.prioritize_targets(["Enemy Player"])
        damage = sum(c.cost for c in hand)
        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets,
                "damage_dealt": damage,
            },
        }
