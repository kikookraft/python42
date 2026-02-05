
def check_temperature(temp_str: str) -> float | None:
    """Function that check if the given temperture is valid
      and return it as a float.
    """
    try:
        temp = float(temp_str)
        if temp < 0:
            raise ValueError("Temperature cannot be below 0.C")
        if temp > 40:
            raise ValueError("Temperature cannot be above 40.C")
        return temp
    except ValueError as e:
        print(f"Invalid temperature: {e}")
        return None


if __name__ == "__main__":
    while True:
        try:
            temp_str = input(
                "\nEnter a temperature in Celsius (or 'exit' to quit):\n> ")
            if temp_str.lower() == "exit":
                break
            temp = check_temperature(temp_str)
            if temp is not None:
                print(f"Valid temperature: {temp}°C")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break
