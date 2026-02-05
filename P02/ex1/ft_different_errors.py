
def check_temperature(temp_str: str) -> int | None:
    """Function that check if the given temperture is valid
      and return it as a float.
    """
    try:
        temp = int(temp_str)
        if temp < 0:
            raise ValueError("Temperature cannot be below 0.C")
        if temp > 40:
            raise ValueError("Temperature cannot be above 40.C")
        return temp
    except ValueError as e:
        print(f"Invalid temperature: {e}")
        return None


def garden_operations() -> None:
    check_temperature("25")  # Valid temperature
    check_temperature("-5")  # Invalid temperature (below 0)
    check_temperature("45")  # Invalid temperature (above 40)
    check_temperature("abc")  # Invalid temperature (not a number)
    print(10 / 0)  # This will raise a ZeroDivisionError
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
        print(content)
    baba: dict[str, str | int] = {"name": "Baba", "age": 5}
    print(baba["name"])  # Valid key
    print(baba["color"])  # This will raise a KeyError


def test_error_types():
    try:
        garden_operations()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    test_error_types()
    print("💀💀💀💀")
