from typing import Any
from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Orchestrates a card game using a factory and a strategy."""

    def __init__(self) -> None:
        """Initialise the engine with no factory or strategy set."""
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._hand: list[Any] = []
        self._battlefield: list[Any] = []
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        """Configure the engine with a factory and strategy."""
        self._factory = factory
        self._strategy = strategy

        creature: Card = factory.create_creature()
        spell: Card = factory.create_spell()
        artifact: Card = factory.create_artifact()
        self._hand = [creature, spell, artifact]
        self._cards_created = len(self._hand)

    def simulate_turn(self) -> dict[str, Any]:
        """Simulate one game turn using the configured strategy.
        returns:
        - hand: list of card summaries as strings
        - turn_execution: the strategy result dict

        Raises:
            RuntimeError: If the engine has not been configured.
        """
        if self._factory is None or self._strategy is None:
            raise RuntimeError(
                "Engine not configured. Call configure_engine first."
            )

        hand_summary: list[str] = [
            f"{c.name} ({c.cost})" for c in self._hand
        ]
        result: dict[str, Any] = self._strategy.execute_turn(
            self._hand, self._battlefield)
        actions: dict[str, Any] = result.get("actions", {})
        damage: int = actions.get("damage_dealt", 0)
        self._total_damage += damage
        self._turns_simulated += 1

        return {
            "hand": hand_summary,
            "turn_execution": result,
        }

    def get_engine_status(self) -> dict[str, str | int]:
        """Return a summary report of the engine's activity.
        returns:
        - turns_simulated: number of turns run
        - strategy_used: name of the active strategy
        - total_damage: cumulative damage dealt
        - cards_created: number of cards in the starting hand
        """
        strategy_name: str = (
            self._strategy.get_strategy_name()
            if self._strategy
            else "None"
        )
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self._total_damage,
            "cards_created": self._cards_created,
        }
