"""Game engine that orchestrates card factories and strategies."""

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Orchestrates a card game using a factory and a strategy."""

    def __init__(self) -> None:
        """Initialise the engine with no factory or strategy set."""
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._hand: list = []
        self._battlefield: list = []
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        """Configure the engine with a factory and strategy.

        Args:
            factory: The card factory to use.
            strategy: The game strategy to apply.
        """
        self._factory = factory
        self._strategy = strategy

        creature = factory.create_creature()
        spell = factory.create_spell()
        artifact = factory.create_artifact()
        self._hand = [creature, spell, artifact]
        self._cards_created = len(self._hand)

    def simulate_turn(self) -> dict:
        """Simulate one game turn using the configured strategy.

        Returns:
            A dict summarising the turn outcome.

        Raises:
            RuntimeError: If the engine has not been configured.
        """
        if self._factory is None or self._strategy is None:
            raise RuntimeError(
                "Engine not configured. Call configure_engine first."
            )

        hand_summary = [
            f"{c.name} ({c.cost})" for c in self._hand
        ]
        result = self._strategy.execute_turn(self._hand, self._battlefield)
        actions = result.get("actions", {})
        damage = actions.get("damage_dealt", 0)
        self._total_damage += damage
        self._turns_simulated += 1

        return {
            "hand": hand_summary,
            "turn_execution": result,
        }

    def get_engine_status(self) -> dict:
        """Return a summary report of the engine's activity.

        Returns:
            A dict with turn count, strategy used, totals, and card count.
        """
        strategy_name = (
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
