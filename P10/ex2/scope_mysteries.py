from typing import Callable, Dict, Any


def mage_counter() -> Callable[[], int]:
    """Create counter"""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Create spell accumulator"""
    power: int = initial_power

    def add_power(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Create enchantment factory"""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> Dict[str, Callable[..., Any]]:
    memory: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_func: Callable[[], int] = mage_counter()
    print(f"Call 1: {counter_func()}")
    print(f"Call 2: {counter_func()}")
    print(f"Call 3: {counter_func()}")

    print("Testing enchantment factory...")
    flaming: Callable[[str], str] = enchantment_factory("Flaming")
    frozen: Callable[[str], str] = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
