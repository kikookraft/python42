import functools
import operator
from typing import Callable, Any


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


def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, Any] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if not spells:
        return 0
    return functools.reduce(ops[operation], spells)


def partial_enchanter(
        base_enchantment: Callable[..., Any]) -> dict[str, Callable[..., Any]]:
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, 'fire'),
        'ice_enchant': functools.partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': functools.partial(
            base_enchantment, 50, 'lightning'
        )
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[..., Any]:
    @functools.singledispatch
    def dispatcher(arg: Any) -> None:
        print(Color.red("Unknown spell type"))

    @dispatcher.register(int)
    def _(arg: int) -> None:
        print(Color.green(f"Damage spell: {arg}"))

    @dispatcher.register(str)
    def _(arg: str) -> None:
        print(Color.blue(f"Enchantment: {arg}"))

    @dispatcher.register(list)
    def _(arg: list[Any]) -> None:
        print(Color.magenta(f"Multi-cast: {arg}"))

    return dispatcher


if __name__ == "__main__":
    print(Color.cyan("Testing spell reducer..."))
    spells: list[int] = [10, 20, 30, 40]
    print(Color.yellow(f"Sum: {spell_reducer(spells, 'add')}"))
    print(Color.yellow(f"Product: {spell_reducer(spells, 'multiply')}"))
    print(Color.yellow(f"Max: {spell_reducer(spells, 'max')}"))

    print()
    print(Color.cyan("Testing partial enchanter..."))

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"Enchanting {target} with {element} magic (Power: {power})"

    enchanters: dict[str, Callable[..., Any]] = partial_enchanter(
        base_enchantment
    )
    print(Color.yellow(enchanters['fire_enchant']("Sword")))
    print(Color.yellow(enchanters['ice_enchant']("Shield")))
    print(Color.yellow(enchanters['lightning_enchant']("Amulet")))

    print()
    print(Color.cyan("Testing memoized fibonacci..."))
    print(Color.green(f"Fib(10): {memoized_fibonacci(10)}"))
    print(Color.green(f"Fib(15): {memoized_fibonacci(15)}"))

    print()
    print(Color.cyan("Testing spell dispatcher..."))
    dispatcher_func: Callable[..., Any] = spell_dispatcher()
    dispatcher_func(42)
    dispatcher_func("Flaming Sword")
    dispatcher_func([10, "Ice Shield", 20])
    dispatcher_func(3.14)
