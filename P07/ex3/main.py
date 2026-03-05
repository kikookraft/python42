"""Exercise 3 - Game Engine demonstration."""

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    """Demonstrate Abstract Factory + Strategy patterns."""
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    engine.configure_engine(factory, strategy)

    print("\nSimulating aggressive turn...")
    turn_result = engine.simulate_turn()
    hand_str = ", ".join(turn_result["hand"])
    print(f"Hand: [{hand_str}]")
    print("\nTurn execution:")
    exec_data = turn_result["turn_execution"]
    print(f"Strategy: {exec_data.get('strategy', 'N/A')}")
    print(f"Actions: {exec_data.get('actions', {})}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )
    print(
        "\nHow do Abstract Factory and Strategy patterns work together? "
        "What makes this combination powerful for game engine systems?"
    )


if __name__ == "__main__":
    main()
