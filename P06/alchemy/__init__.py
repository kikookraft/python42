__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .elements import create_fire, create_water


def main() -> None:
    print("Welcome to the Alchemy Lab!")
    print(create_fire())
    print(create_water())


# if __name__ == "__main__": # broken
#     main()
