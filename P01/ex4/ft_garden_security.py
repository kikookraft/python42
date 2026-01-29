
class SecurePlant():
    def __init__(self) -> None:
        """
        Init the object
        Args:
            seed (int, optional): the seed for the random number generation.
              Defaults to 0.
        """
        self.__name: str = ""
        self.__heigh: float = 0.0
        self.__aging: int = 0
        self.__grow_ratio: float = .0042
        self.__die_age: int = 90
        self.__alive = True

    def __repr__(self) -> str:
        """
        Represent the object as a string
        Returns:
            str: _object_
        """
        return (f"===============================\n \
    Hello my name is {self.__name} \n \
    My height is {self.__heigh} cm \n \
    I have {self.__aging} days")

    def __grow(self) -> None:
        """
        Make the plant grow if alive
        """
        if not self.__aging > self.__die_age:
            self.__heigh += self.__heigh * self.__grow_ratio

    def age(self) -> None:
        """
        Increase the age og the plant
        """
        if self.__aging > self.__die_age:
            self.__die()
        else:
            self.__aging += 1
            self.__grow()

    def __die(self) -> None:
        """Make the plant die
        """
        self.__alive = False

    def get_info(self) -> tuple[float, int, str, bool]:
        """get info

        Returns:
            tuple: info
        """
        return (self.__heigh, self.__aging, self.__name, self.__alive)

    def get_name(self) -> str:
        """Return name
        """
        return self.__name

    def get_height(self) -> float:
        """Return height
        """
        return self.__heigh

    def get_age(self) -> int:
        """Return age
        """
        return self.__aging

    def is_alive(self) -> bool:
        """return if the plant is alive

        Returns:
            bool: true if plant alive
        """
        return self.__alive

    #######################
    #   SECURE METHODS   #
    #######################

    def set_height(self, height: float) -> None:
        """Set height

        Args:
            height (float): height
        """
        if height >= 0:
            self.__heigh = height
        else:
            print("Height must be positive")

    def set_age(self, age: int) -> None:
        """Set age

        Args:
            age (int): age
        """
        if age >= 0:
            self.__aging = age
        else:
            print("Age must be positive")

    def set_name(self, name: str) -> None:
        """Set name

        Args:
            name (str): name
        """
        if len(name) > 0:
            self.__name = name
        else:
            print("Name must be non empty")

    def set_die_age(self, die_age: int) -> None:
        """Set die age

        Args:
            die_age (int): die age
        """
        if die_age > 0:
            self.__die_age = die_age


if __name__ == "__main__":
    plants: list[SecurePlant] = [SecurePlant() for _ in range(5)]

    for plant in plants:
        plant.set_name("Fern")
        plant.set_height(10.0)
        plant.set_age(5)
        plant.set_die_age(100)
        print(plant)
