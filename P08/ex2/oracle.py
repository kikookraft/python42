from typing import Dict
import dotenv
import os


KEYS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"


def get_all(data: dict[str, str | None]) -> int:
    good: int = 0
    for key in KEYS:
        try:
            value: str | None = data[key]
            match key:
                case "MATRIX_MODE":
                    if value not in ["development", "production"]:
                        print("Invalid value for "
                              f"{Color.RED}{key}{Color.RESET}: "
                              f"{Color.RED}{value}{Color.RESET}")
                        good -= 1
                    print(f"Mode: {Color.GREEN}{value}{Color.RESET}")
                case "DATABASE_URL":
                    if value and not value.startswith("https://"):
                        print("Database: "
                              f"{Color.RED}Disconnected{Color.RESET}")
                        good -= 1
                        continue
                    print(f"Database: {Color.BLUE}Connected{Color.RESET}")
                case "API_KEY":
                    if not value:
                        print(f"Key {Color.RED}{key}{Color.RESET} "
                              "not valid")
                        good -= 1
                        continue
                    print(
                        "API Key: "
                        f"{Color.YELLOW}{'*' * (len(value) - 3)}"
                        f"{value[-3:]}{Color.RESET}")
                case "LOG_LEVEL":
                    if value not in ["DEBUG", "INFO",
                                     "WARNING", "ERROR", "CRITICAL"]:
                        print("Invalid value for "
                              f"{Color.RED}{key}{Color.RESET}: "
                              f"{Color.RED}{value}{Color.RESET}")
                        good -= 1
                    print(f"Log level: {Color.CYAN}{value}{Color.RESET}")
                case "ZION_ENDPOINT":
                    if not value:
                        print(f"{Color.RED}Could not connect"
                              f"to Zion {Color.RESET}")
                        good -= 1
                    print("Zion endpoint: "
                          f"{Color.GREEN}Online{Color.RESET}")
                case _:
                    print(f"Unknown key: {Color.RED}{key}{Color.RESET}")
            good += 1
        except KeyError:
            match key:
                case "MATRIX_MODE":
                    print(f"Mode: {Color.RED}Disconnected{Color.RESET}")
                case "DATABASE_URL":
                    print(f"Database: {Color.RED}Disconnected{Color.RESET}")
                case "API_KEY":
                    print(f"Key {Color.RED}{key}{Color.RESET} missing")
                case "LOG_LEVEL":
                    print(f"{Color.RED}LOG_LEVEL{Color.RESET}"
                          " not found in the matrix")
                case "ZION_ENDPOINT":
                    print(f"{Color.RED}Could not connect"
                          f"to Zion {Color.RESET} (no endpoint)")
                case _:
                    print(f"Key {Color.RED}{key}{Color.RESET}"
                          " not found in the matrix")
    return good


if __name__ == "__main__":
    if not os.path.exists(".env"):
        print("No matrix detected\n  Have you taken a blue pill ??")
        exit(1)
    print("ORACLE STATUS: REading the matrix...\n")
    dotenv.load_dotenv(override=False)
    data: Dict[str, str | None] = {key: os.environ.get(key) for key in KEYS}
    if get_all(data) == len(KEYS):
        print(f"\n{Color.GREEN}.env Properly configured!{Color.RESET}")
    else:
        print(f"\n{Color.RED}.env is not properly configured!{Color.RESET}")
