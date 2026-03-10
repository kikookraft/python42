import sys


def print_red(text: str, end: str = "\n") -> None:
    print("\033[91m {}\033[00m"              .format(text), end=end)


def print_green(text: str, end: str = "\n") -> None:
    print("\033[92m {}\033[00m"              .format(text), end=end)


def print_blue(text: str, end: str = "\n") -> None:
    print("\033[94m {}\033[00m"              .format(text), end=end)


def print_yellow(text: str, end: str = "\n") -> None:
    print("\033[93m {}\033[00m"              .format(text), end=end)


def print_purple(text: str, end: str = "\n") -> None:
    print("\033[95m {}\033[00m"              .format(text), end=end)


if __name__ == "__main__":
    import os
    import site

    venv: str | None = os.environ.get("VIRTUAL_ENV")

    if venv is None:
        print_red("MATRIX STATUS: You're still plugged in")
        print("Current Python:", end=" ")
        print_purple(sys.executable)
        print("Virtual Environment: None detected")
        print()
        print_yellow("WARNING: You're in the global environment!")
        print_yellow("The machines can see everything you install booooo.")
        print()
        print("To enter the construct, run:")
        print_blue("    py -m venv .venv && source .venv/bin/activate.fish")
        print()
        print("Then run this program again.")
    else:
        venv_name: str = os.path.basename(venv)
        print_green("MATRIX STATUS: Welcome to the construct")
        print("Current Python:", end=" ")
        print_purple(sys.executable)
        print("Virtual Environment:", end=" ")
        print_purple(venv_name)
        print("Environment Path:", end=" ")
        print_purple(venv)
        print()
        print_green("SUCCESS: You're in an isolated environment!")
        print_green("Safe to install packages without affecting")
        print_green("the global system.")
        print()
        print("Package installation path:")
        print_blue("    " + site.getsitepackages()[0])
