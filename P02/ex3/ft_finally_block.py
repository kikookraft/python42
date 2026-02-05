
def water_plants(plant_list: list[str]) -> None:
    """Water the plants and handle any errors."""
    print("Starting to water the plants...")
    try:
        if not plant_list:
            raise ValueError("No plants to water.")
        for plant in plant_list:
            if plant == "cactus":
                raise ValueError("Cacti require very little water.")
            print(f"Watering {plant}...")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Finished watering the plants, even if there were errors.")


def test_watering_system():
    plants = ["rose", "tulip", "cactus", "daisy"]
    water_plants(plants)


if __name__ == "__main__":
    test_watering_system()
    water_plants(["cactus"])
    water_plants([])
    print("💀💀💀💀")
