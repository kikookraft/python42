import functools
import time
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


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Time execution decorator"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(Color.cyan(f"Casting {func.__name__}..."))
        start_time: float = time.time()
        result: Any = func(*args, **kwargs)
        end_time: float = time.time()
        msg = f"Spell completed in {end_time - start_time:.3f} seconds"
        print(Color.green(msg))
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    """Decorator factory that validates power levels."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power: Any = kwargs.get("power")
            if power is None:  # search for power
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break
            # Validate power level
            if power is not None and isinstance(power, int):
                if power >= min_power:
                    return func(*args, **kwargs)
            return Color.red("Insufficient power for this spell")
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    """Decorator that retries failed spells."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    msg: str = "Spell failed, retrying... " \
                        f"(attempt {attempt}/{max_attempts})"
                    print(Color.yellow(msg))
            fail_msg = f"Spell casting failed after {max_attempts} attempts"
            return Color.red(fail_msg)
        return wrapper
    return decorator


class MageGuild:
    """Master the Ancient Arts of Functional Programming"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Name is valid if it's at least 3 characters
        and contains only letters/spaces"""
        return (len(name) >= 3) and all(c.isalpha()
                                        or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with a specific power"""
        msg = f"Successfully cast {spell_name} with {power} power"
        return Color.green(msg)


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))

    print("\nTesting retry_spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise ValueError("Fizzle!")

    print(unstable_spell())
