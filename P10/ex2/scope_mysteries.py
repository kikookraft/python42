from typing import Callable, Dict, Any

try:
    from data_generator import FuncMageDataGenerator as fmg
except ImportError:
    print("Error importing FuncMageDataGenerator. "
          "Please ensure data_generator.py is in the same directory.")


class Color:
    """ANSI color codes for terminal output."""
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    @staticmethod
    def red(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.RED}{text}{Color.RESET}"

    @staticmethod
    def green(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.GREEN}{text}{Color.RESET}"

    @staticmethod
    def yellow(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.YELLOW}{text}{Color.RESET}"

    @staticmethod
    def blue(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.BLUE}{text}{Color.RESET}"

    @staticmethod
    def magenta(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.MAGENTA}{text}{Color.RESET}"

    @staticmethod
    def cyan(text: str) -> str:
        """Wrap text in color codes."""
        return f"{Color.CYAN}{text}{Color.RESET}"


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
    spells: list[str] = fmg.generate_spells(5)
    items: list[str] = fmg.generate_enchantment_items(5)
    print(Color.cyan("=== Generated Data ==="))
    print(Color.cyan(f"Spells: {spells}"))
    print(Color.cyan(f"Items : {items}"))
    print()

    print(Color.cyan("Testing mage counter..."))
    counter_func: Callable[[], int] = mage_counter()
    for i in range(3):
        print(Color.green(f"Call {i+1}: {counter_func()}"))

    print()
    print(Color.cyan("Testing enchantment factory..."))
    for i in range(len(spells)):
        enchant_func: Callable[[str], str] = enchantment_factory(spells[i])
        print(Color.yellow(enchant_func(items[i])))
