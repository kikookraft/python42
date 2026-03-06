from typing import Any
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """A strategy that prioritises attacking and dealing damage fast."""

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return "AggressiveStrategy"

    def prioritize_targets(
        self,
        available_targets: list[Any],
    ) -> list[Any]:
        """Sort targets: enemy player first, then enemy creatures."""
        player_targets: list[Any] = [
            t for t in available_targets if "Player" in str(t)
        ]
        other_targets: list[Any] = [
            t for t in available_targets if "Player" not in str(t)
        ]
        return player_targets + other_targets

    def execute_turn(
        self,
        hand: list[Any],
        battlefield: list[Any],
    ) -> dict[str, Any]:
        """Play low-cost cards first and attack aggressively.
        returns:
        - strategy: The strategy name used
        - actions: dict with cards_played, mana_used, targets_attacked,
          damage_dealt
        """
        sorted_hand: list[Any] = sorted(hand, key=lambda c: c.cost)
        mana_budget: int = sum(c.cost for c in sorted_hand)
        mana_used = 0
        cards_played: list[str] = []
        for card in sorted_hand:
            if mana_used + card.cost <= mana_budget:
                cards_played.append(card.name)
                mana_used += card.cost

        targets: list[Any] = self.prioritize_targets(["Enemy Player"])
        damage: int = sum(c.cost for c in hand)
        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets,
                "damage_dealt": damage
            },
        }
