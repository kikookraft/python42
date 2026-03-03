import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


def main() -> None:
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    result: str = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {result}\n")

    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}\n")

    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}\n")

    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}\n")

    print("Mamacita tengo fuego y agua, dame tierra y "
          "aire para hacer la pócima de la vida eterna!!!")


if __name__ == "__main__":
    main()
