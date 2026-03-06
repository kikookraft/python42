from typing import Any


try:
    from ex3.FantasyCardFactory import FantasyCardFactory
    from ex3.AggressiveStrategy import AggressiveStrategy
    from ex3.GameEngine import GameEngine
except ImportError:
    print(
        "WARNING: you are using the module wrongly.\n"
        "launch this using 'py -m ex3.main' in the root directory."
    )
    exit(1)


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
    turn_result: dict[str, Any] = engine.simulate_turn()
    hand_str: str = ", ".join(turn_result["hand"])
    print(f"Hand: [{hand_str}]")
    print("\nTurn execution:")
    exec_data: dict[str, Any] = turn_result["turn_execution"]
    print(f"Strategy: {exec_data.get('strategy', 'N/A')}")
    print(f"Actions: {exec_data.get('actions', {})}")

    print("\nGame Report:")
    print(engine.get_engine_status())


if __name__ == "__main__":
    main()
