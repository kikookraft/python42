import alchemy
import time

elem_names: list[str] = ["Fire", "Water", "Earth", "Air"]


def up() -> None:
    print(" " * 30 + "\033[F", end="")  # Clear the previous line


def test_direct_import() -> None:
    print("Testing direct import...")
    for name in elem_names:
        time.sleep(.5)
        if name == "Fire":
            element: str = alchemy.elements.create_fire()
        elif name == "Water":
            element: str = alchemy.elements.create_water()
        elif name == "Earth":
            element: str = alchemy.elements.create_earth()
        elif name == "Air":
            element: str = alchemy.elements.create_air()
        else:
            print(f"wat??\ngot {name}")
            continue
        print(f"{name}: {element}")


def test_from_import() -> None:
    print("Testing from import...")
    for name in elem_names:
        time.sleep(.5)
        if name == "Fire":
            element: str = alchemy.create_fire()
        elif name == "Water":
            element: str = alchemy.create_water()
        elif name == "Earth":
            try:
                element: str = alchemy.create_earth()  # type: ignore
            except AttributeError:
                print("⚠️⚠️⚠️ F**ck, no earth in alchemy.__init__.py")
                continue
        elif name == "Air":
            try:
                element: str = alchemy.create_air()  # type: ignore
            except AttributeError:
                print(
                    "WHAT?? NO MORE AIR IN alchemy.__init__.py ❌🚨⛔🚫 !!!!!!\n")
                continue
        else:
            print(f"wat??\ngot {name}")
            continue
        print(f"{name}: {element}")


def main() -> None:
    print("Welcome to the Alchemy Lab!")
    test_direct_import()
    up()
    print("\n" + "="*30 + "\n")
    test_from_import()
    up()
    print("\n" + "="*30 + "\n")
    print("Anyway, package info:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
