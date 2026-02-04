names: list[str] = ["Juan", "Jean-Eude", "Marwalou", "S̸̱͍̖͙̏È", "𝓻𝓸𝓼𝓮", "🗿🗿"]
height: list[float] = [42, 1.78, 0.45, 12, 1.95, 275]


class Plant():
    """Plants class
    """
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

    def get_info(self) -> tuple[float, int, str, bool]:
        """get info

        Returns:
            tuple: info
        """
        return (self.heigh, self.aging, self.name, self.alive)

    def get_name(self) -> str:
        """Return name
        """
        return self.name

    def get_height(self) -> float:
        """Return height
        """
        return self.heigh

    def get_age(self) -> int:
        """Return age
        """
        return self.aging

    def is_alive(self) -> bool:
        """return if the plant is alive

        Returns:
            bool: true if plant alive
        """
        return self.alive


if __name__ == "__main__":
    plants: list[Plant] = [Plant(i) for i in range(5)]

    for plant in plants:
        print(plant)
