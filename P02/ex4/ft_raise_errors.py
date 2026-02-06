
def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int) -> None:
    """Check the health of a plant based on its name, water level,
      and sunlight hours."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty.")
    if plant_name not in ["rose", "tulip", "daisy"]:
        raise ValueError(f"Unknown plant: {plant_name}")
    if water_level < 0:
        raise ValueError("Water level cannot be negative.")
    if water_level > 10:
        raise ValueError("Water level cannot exceed 10 liters.")
    if sunlight_hours < 2:
        raise ValueError("Sunlight hours cannot be less than 2.")
    if sunlight_hours > 12:
        raise ValueError("Sunlight hours cannot exceed 12.")
    print(f"{plant_name} is healthy with {water_level} liters of water and "
          f"{sunlight_hours} hours of sunlight.")


def test_plant_checks(
        plant_name: str,
        water_level: int,
        sunlight_hours: int) -> None:
    try:
        check_plant_health(plant_name, water_level, sunlight_hours)
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    test_plant_checks("rose", 5, 6)  # Valid case
    test_plant_checks("", 5, 6)  # Invalid plant name
    test_plant_checks("cactus", 5, 6)  # Unknown plant
    test_plant_checks("tulip", -1, 6)  # Negative water level
    test_plant_checks("daisy", 11, 6)  # Excessive water level
    test_plant_checks("rose", 5, 1)  # Insufficient sunlight
    test_plant_checks("tulip", 5, 13)  # Excessive sunlight
    print("💀💀💀💀")
