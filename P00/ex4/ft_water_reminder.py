
def ft_water_reminder():
    wtdays: int = int(input("How much days since last water ?\n> "))
    if wtdays > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


# ft_water_reminder()
