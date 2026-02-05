
class GardenError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    pass


class WaterError(GardenError):
    """Exception raised for errors related to watering."""
    pass


def check_plant(plant_name: str) -> None:
    """Check if the plant is valid."""
    valid_plants = ["rose", "tulip", "daisy"]
    if plant_name not in valid_plants:
        raise PlantError(
            f"Invalid plant: {plant_name}. Valid plants are: "
            f"{', '.join(valid_plants)}.")


def check_water_amount(amount: int) -> None:
    """Check if the water amount is valid."""
    if amount < 0:
        raise WaterError("Water amount cannot be negative.")
    if amount > 100:
        raise WaterError("Water amount cannot exceed 100 liters.")


if __name__ == "__main__":
    try:
        check_plant("cactus")
    except PlantError as e:
        print(f"Plant error: {e.message}")

    try:
        check_water_amount(-10)
    except WaterError as e:
        print(f"Water error: {e.message}")

    try:
        check_water_amount(150)
    except WaterError as e:
        print(f"Water error: {e.message}")
