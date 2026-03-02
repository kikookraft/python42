import time


def create_fire() -> str:
    print("FIRE   \n🔥🔥🔥", end="\033[F")
    time.sleep(.5)
    return "Fire Element created"


def create_water() -> str:
    print("WATER   \n💧💧💧", end="\033[F")
    time.sleep(.5)
    return "Water Element created"


def create_earth() -> str:
    print("EARTH   \n🌍🌍🌍", end="\033[F")
    time.sleep(.5)
    return "Earth Element created"


def create_air() -> str:
    print("AIR   \n💨💨💨", end="\033[F")
    time.sleep(.5)
    return "Air Element created"


if __name__ == "__main__":
    print("Creating elements...")
    print(create_fire())
    print(create_water())
    print(create_earth())
    print(create_air())
