from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    gold_result: str = lead_to_gold()
    potion_result: str = healing_potion()
    return (f"Philosopher's stone created using {gold_result} "
            f"and {potion_result}")


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
