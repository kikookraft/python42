from typing import Any, Callable


try:
    from data_generator import FuncMageDataGenerator as fmg
except ImportError:
    print("Error importing FuncMageDataGenerator. "
          "Please ensure data_generator.py is in the same directory.")
    exit(1)


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


def spell_combiner(
        spell1: Callable[..., Any],
        spell2: Callable[..., Any]) -> Callable[..., Any]:
    def combined_spell(*args: Any, **kwargs: Any) -> tuple[Any, ...]:
        result1: Any = spell1(*args, **kwargs)
        result2: Any = spell2(*args, **kwargs)
        return (result1, result2)
    return combined_spell


def power_amplifier(
        base_spell: Callable[..., Any],
        multiplier: int) -> Callable[..., Any]:
    """Amplify the power of a spell."""
    def amplified_spell(*args: Any, **kwargs: Any) -> Any:
        result: Any = base_spell(*args, **kwargs)
        return result * multiplier
    return amplified_spell


def conditional_caster(
        condition: Callable[..., Any],
        spell: Callable[..., Any]) -> Callable[..., Any]:
    """Cast a spell conditionally."""
    def conditional_spell(*args: Any, **kwargs: Any) -> Any | str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable[..., Any]]) -> Callable[..., Any]:
    """Execute a sequence of spells."""
    def sequence_spell(*args: Any, **kwargs: Any) -> list[Any]:
        results: list[Any] = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence_spell


if __name__ == "__main__":
    # Generate test data using FuncMageDataGenerator
    test_values: list[int] = fmg.generate_spell_powers(3)
    test_targets: list[str] = ["Dragon", "Goblin", "Wizard", "Knight"]
    spell_names: list[str] = fmg.generate_spells(4)

    print(Color.cyan("=== Exercise 1 Test Data ==="))
    print(Color.cyan(f"test_values  : {test_values}"))
    print(Color.cyan(f"test_targets : {test_targets}"))
    print(Color.cyan(f"spell_names  : {spell_names}"))
    print()

    # Spell factories built from generated data
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage(target: str) -> int:
        return test_values[0]

    def is_enemy(target: str) -> bool:
        return target.lower() in ("dragon", "goblin", "orc")

    print(Color.yellow("Testing spell combiner..."))
    combined: Any = spell_combiner(fireball, heal)
    for target in test_targets[:2]:
        result: tuple[Any, ...] = combined(target)
        res_str: str = f"  Combined spell result: {result[0]}, {result[1]}"
        print(Color.green(res_str))
    print()

    print(Color.yellow("Testing power amplifier..."))
    multiplier = 3
    mega_damage: Any = power_amplifier(damage, multiplier)
    for target in test_targets[:2]:
        original: int = damage(target)
        amplified: int = mega_damage(target)
        amp_str: str = f"  [{target}] Original: " + \
            f"{original}, Amplified: {amplified}"
        print(Color.green(amp_str))
    print()

    print(Color.yellow("Testing conditional caster..."))
    conditional_fireball: Any = conditional_caster(is_enemy, fireball)
    for target in test_targets:
        cond_str: str = f"  Against {target}: {conditional_fireball(target)}"
        print(Color.green(cond_str))
    print()

    print(Color.yellow("Testing spell sequence..."))

    def create_spell_func(s_name: str) -> Callable[[str], str]:
        return lambda t: f"{s_name.capitalize()} hits {t}"

    spell_funcs: list[Callable[..., Any]] = [
        create_spell_func(name) for name in spell_names
    ]
    sequence: Any = spell_sequence(spell_funcs)
    for target in test_targets[:2]:
        seq_str: str = f"  [{target}] Sequence: {sequence(target)}"
        print(Color.green(seq_str))
