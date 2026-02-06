
class GardenError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message: str = message


class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    pass


class WaterError(GardenError):
    """Exception raised for errors related to watering."""
    pass


class Plant:
    def __init__(self,
                 name: str,
                 water_level: float = 1.0
                 ) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty.")
        self.__name: str = name
        self.__last_watered: int = 0
        self.__water_level: float = water_level

    def name(self) -> str:
        """Returns the name of the plant.
        """
        return self.__name

    def check_health(self, current_day: int) -> bool:
        """Checks if the plant is healthy based on
        the last watered day and water requirement.
        """
        if current_day < 0:
            raise ValueError("Current day cannot be negative.")
        return self.__water_level > 0.3

    def water(self, current_day: int, water_amount: float = 1.0) -> None:
        if current_day < 0:
            raise ValueError("Current day cannot be negative.")
        if water_amount <= 0:
            raise WaterError("Water amount must be a positive number.")
        if water_amount > 10.0:
            raise WaterError("Water amount cannot exceed 10.0.")
        """Waters the plant and updates the last watered day.
        """
        self.__last_watered = current_day
        self.__water_level = water_amount

    def last_watered(self) -> int:
        """Returns the last watered day of the plant.
        """
        return self.__last_watered

    def age(self) -> None:
        """Make the time pass, increasing the last watered day by 1.
        and decreasing the water level by 0.1.
        """
        self.__last_watered += 1
        self.__water_level -= 0.3
        if self.__water_level < 0:
            self.__water_level = 0.0

    def __repr__(self) -> str:
        return f"Plant(name={self.__name}, \
last_watered={self.__last_watered}, \
water_level={self.__water_level})"

    def get_water_level(self) -> float:
        """Returns the current water level of the plant.
        """
        return self.__water_level


class GardenManager:
    def __init__(self) -> None:
        self.__plants: list[Plant] = []
        self.__current_day: int = 0

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant to the garden.
        """
        self.__plants.append(plant)

    def water_plants(self, water_amount: float = 1.0) -> None:
        """Waters all plants in the garden.
        """
        if water_amount <= 0:
            raise WaterError("Water amount must be a positive number.")
        if water_amount > 10.0:
            raise WaterError("Water amount cannot exceed 10.0.")
        for plant in self.__plants:
            plant.water(self.__current_day, water_amount)

    def age_plants(self) -> None:
        """Ages all plants in the garden by one day.
        """
        for plant in self.__plants:
            plant.age()
        self.__current_day += 1

    def check_plants_health(self) -> list[bool]:
        """Checks the health of all plants in the garden.
        Returns a list of booleans indicating the health of each plant.
        """
        return [
            plant.check_health(self.__current_day) for plant in self.__plants
            ]

    def get_plants(self) -> list[Plant]:
        """Returns the list of plants in the garden.
        """
        return self.__plants

    def get_current_day(self) -> int:
        """Returns the current day in the garden.
        """
        return self.__current_day

    def __repr__(self) -> str:
        tmp: str = ""
        for plant in self.__plants:
            tmp += repr(plant) + "\n"
        return f"GardenManager(current_day={self.__current_day},\
plants=[\n{tmp}])"


if __name__ == "__main__":
    garden = GardenManager()
    plant1 = Plant("Rose", 3)
    plant2 = Plant("Tulip", 2)
    try:
        plant3 = Plant("", 1)
    except PlantError as e:
        print(f"Error creating plant: {e}")
    garden.add_plant(plant1)
    garden.add_plant(plant2)

    for day in range(20):
        print(f"Day {garden.get_current_day()}:")
        print(garden)
        garden.age_plants()
        print(garden.check_plants_health())
        for plant in garden.get_plants():
            if not plant.check_health(garden.get_current_day()):
                print(f"{plant.name()} is unhealthy, watering it.")
                try:
                    plant.water(garden.get_current_day(), day*2)
                except WaterError as e:
                    print(f"Error watering plant: {e}")
                    plant.water(garden.get_current_day(), 1.0)
        if day < 9:
            try:
                input(f"Press Enter to continue to the day {day + 1}...")
            except EOFError:
                pass
