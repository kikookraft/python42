from typing import Dict, List, Any
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


def artifact_sorter(artifacts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Sort by power level"""
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(
        mages: List[Dict[str, Any]],
        min_power: int
        ) -> List[Dict[str, Any]]:
    """Filter mages by minimum power level"""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    """Transform spells by adding asterisks"""
    return list(map(lambda s: '*' + s + '*', spells))


def mage_stats(mages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate :
    most powerfull mage
    least powerfull mage level
    averagre power level
    return {’max_power’: int, ’min_power’: int, ’avg_power’: float}
    """
    if not mages:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0.0
        }
    most_powerful: Dict[str, Any] = max(mages, key=lambda x: x["power"])
    least_powerful: Dict[str, Any] = min(mages, key=lambda x: x["power"])
    total_power: int = sum(mage["power"] for mage in mages)
    average_power: float = total_power / len(mages)
    return {
        "max_power": most_powerful["power"],
        "min_power": least_powerful["power"],
        "avg_power": average_power
    }


def main() -> None:
    """Demonstrate the use of lambda functions for mage data processing.
    """
    # Generate test data
    artifacts: List[Dict[str,
                         Any]] = fmg.generate_artifacts(4)  # type: ignore
    mages: List[Dict[str, Any]] = fmg.generate_mages(5)  # type: ignore
    spells: List[str] = fmg.generate_spells(4)  # type: ignore

    print(Color.cyan("=== Original Artifacts ==="))
    for artifact in artifacts:
        print(artifact)

    print(Color.cyan("\n=== Sorted Artifacts by Power ==="))
    sorted_artifacts: List[Dict[str, Any]] = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(artifact)

    print(Color.cyan("\n=== Original Mages ==="))
    for mage in mages:
        print(mage)

    min_power_threshold = 70
    print(Color.cyan(f"\n=== Mages with Power >= {min_power_threshold} ==="))
    powerful_mages: List[Dict[str, Any]] = power_filter(
        mages,
        min_power_threshold)
    for mage in powerful_mages:
        print(mage)

    print(Color.cyan("\n=== Original Spells ==="))
    for spell in spells:
        print(spell)

    print(Color.cyan("\n=== Transformed Spells ==="))
    transformed_spells: List[str] = spell_transformer(spells)
    for spell in transformed_spells:
        print(spell)

    print(Color.cyan("\n=== Mage Power Stats ==="))
    stats: Dict[str, Any] = mage_stats(mages)
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Average Power: {stats['avg_power']:.2f}")


if __name__ == "__main__":
    main()
