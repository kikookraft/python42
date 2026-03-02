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
