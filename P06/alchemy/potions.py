from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    fire_result: str = create_fire()
    water_result: str = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion() -> str:
    earth_result: str = create_earth()
    fire_result: str = create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion() -> str:
    air_result: str = create_air()
    water_result: str = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion() -> str:
    fire_result: str = create_fire()
    water_result: str = create_water()
    earth_result: str = create_earth()
    air_result: str = create_air()
    return (f"Wisdom potion brewed with all elements: {fire_result}, "
            f"{water_result}, {earth_result}, and {air_result}")
