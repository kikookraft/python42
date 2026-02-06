
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


def garden_operations(test: int) -> None:
    if test == 0:
        check_temperature("25")  # Valid temperature
        print("is ok")
    if test == 1:
        check_temperature("-5")  # Invalid temperature (below 0)
    if test == 2:
        check_temperature("45")  # Invalid temperature (above 40)
    if test == 3:
        check_temperature("abc")  # Invalid temperature (not a number)
    if test == 4:
        print(10 / 0)  # This will raise a ZeroDivisionError
    if test == 5:
        with open("non_existent_file.txt", "r") as f:
            content = f.read()
            print(content)
    if test == 6:
        baba: dict[str, str | int] = {"name": "Baba", "age": 5}
        print(baba["name"])  # Valid key
        print(baba["color"])  # This will raise a KeyError


def test_error_types():
    for i in range(7):
        try:
            garden_operations(i)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    test_error_types()
    print("💀💀💀💀")
