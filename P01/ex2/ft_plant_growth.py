names = ["Juan", "Jean-Eude", "Marwalou", "S̸̱͍̖͙̏È̷̡̧͚̅G̷͌͆̀̕", "𝓻𝓸𝓼𝓮", "🗿🗿"]
height = [42, 1.78, 0.45, 12, 1.95, 275]


class Plant():
    def __init__(self, seed: int = 0) -> None:
        """
        Init the object
        Args:
            seed (int, optional): the seed for the random number generation.
              Defaults to 0.
        """
        self.name: str = names[((seed+1)+42*11-41*(-15)) % len(names)]
        self.heigh: float = height[((seed+1)+135*4597+241*46) % len(height)]
        self.aging: int = (4*seed+(seed % 42)*(42*(seed+2)) % 32 + 1)
        self.grow_ratio: float = .0042
        self.die_age: int = int(15000 * self.grow_ratio -
                                (self.aging * 23215 * self.grow_ratio) % 95)
        self.alive = True

    def __repr__(self) -> str:
        """
        Represent the object as a string
        Returns:
            str: _object_
        """
        return (f"===============================\n \
    Hello my name is {self.name} \n \
    My height is {self.heigh} cm \n \
    I have {self.aging} days")

    def grow(self) -> None:
        """
        Make the plant grow if alive
        """
        if not self.aging > self.die_age:
            self.heigh += self.heigh * self.grow_ratio

    def age(self) -> None:
        """
        Increase the age og the plant
        """
        if self.aging > self.die_age:
            self.die()
        else:
            self.aging += 1
            self.grow()

    def die(self) -> None:
        """Make the plant die
        """
        self.alive = False

    def get_info(self) -> tuple:
        """get info

        Returns:
            tuple: info
        """
        return (self.heigh, self.age, self.name, self.alive)

    def get_name(self):
        """Return name
        """
        return self.name

    def get_height(self):
        """Return height
        """
        return self.heigh

    def get_age(self):
        """Return age
        """
        return self.aging

    def is_alive(self) -> bool:
        """return if the plant is alive

        Returns:
            bool: true if plant alive
        """
        return self.alive


def ft_any(iterable) -> bool:
    """Custom any function

    Args:
        iterable: An iterable to check

    Returns:
        bool: True if any element is truthy
    """
    for element in iterable:
        if element:
            return True
    return False


if __name__ == "__main__":
    plants = [Plant(i) for i in range(5)]
    day = 0
    prev_s = [plant.get_height() for plant in plants]

    while ft_any(plant.is_alive() for plant in plants):
        if day % 7 == 0:
            print(f"--- Day {day} ---")
        for plant in plants:
            if plant.is_alive():
                plant.age()
                if day % 7 == 0:
                    print(plant.get_name(), ": \
", plant.get_height(), "cm, \
", plant.get_age(), "days old.")
                    grow = plant.get_height() - prev_s[plants.index(plant)]
                    print("  Grown +", grow, "\
cm since last week.")
                prev_s[plants.index(plant)] = plant.get_height()
            else:
                if day % 7 == 0:
                    print(plant.get_name(), "is dead at", plant.get_age(), "\
days old.")
                    plants.remove(plant)
        day += 1
    for plant in plants:
        print(plant.get_name(), "is dead at", plant.get_age(), "days old.")
    print("All plants are dead.")
