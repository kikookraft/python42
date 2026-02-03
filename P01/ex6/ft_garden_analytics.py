
class Plant():
    def __init__(self, seed: int = 1) -> None:
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
        self.__die_age: int = int((seed % 10 + 4.2) * 10 + 0.5 * (seed / 10))
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

    def get_die_age(self) -> int:
        """Return die age
        """
        return self.__die_age

    def is_alive(self) -> bool:
        """return if the plant is alive

        Returns:
            bool: true if plant alive
        """
        return self.__alive

    def get_grow_ratio(self) -> float:
        """Return grow ratio
        """
        return self.__grow_ratio

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


class FloweringPlant(Plant):
    def __init__(self, seed: int = 2, name: str = "Flower") -> None:
        """Init the object
        """
        super().__init__(seed=seed)
        self.set_name(name)
        self.set_height(10.0)
        self.set_die_age(30)
        self.__color: str = "Red"
        self.__bloomed: bool = False
        self.__bloom_time: int = 5  # days to bloom

    def __repr__(self) -> str:
        """String representation"""
        return super().__repr__() + \
            f"\n Color: {self.__color} \n Bloomed: {self.__bloomed}"

    def bloom(self) -> None:
        """Make the flower bloom
        """
        if self.is_alive() and not self.__bloomed:
            self.__bloomed = True
            print(f"The {self.get_name()} has bloomed in \
{self.__color} color!")

    def age(self) -> None:
        """Increase the age of the flower and check for blooming
        """
        super().age()
        if self.is_alive() and not self.__bloomed and \
                self.get_age() >= self.__bloom_time:
            self.bloom()


class PrizeFlower(FloweringPlant):
    def __init__(self, seed: int = 8, name: str = "Flower") -> None:
        """Init class"""
        super().__init__(seed, name)
        self.__prize = seed % 3 * 9 / seed * (10/len(name))


class Tree(Plant):
    def __init__(self, seed: int = 3) -> None:
        """Init the object
        """
        super().__init__(seed)
        self.set_name("Tree")
        self.set_height(100.0)
        self.set_die_age(3650)  # 10 years
        self.__trunk_diameter: float = 1.0  # in cm

    def __repr__(self) -> str:
        """String representation"""
        return super().__repr__() + \
            f"\n Trunk Diameter: {self.__trunk_diameter} cm"

    def get_trunk_diameter(self) -> float:
        """Return trunk diameter
        """
        return self.__trunk_diameter

    def _Plant__grow(self) -> None:
        """Make the tree grow if alive
        """
        if not self.get_age() > self.get_die_age():
            self.set_height(self.get_height()
                            + self.get_height() * 2 * self.get_grow_ratio())
            self.__trunk_diameter += 0.1  # grows 0.1 cm per aging

    def produce_shade(self) -> None:
        """Produce shade
        """
        if self.is_alive():
            print(f"The {self.get_name()} is producing shade.")

    def age(self) -> None:
        """Increase the age of the tree
        """
        super().age()
        if self.is_alive():
            self.produce_shade()


class Vegetable(Plant):
    def __init__(self, seed: int = 4) -> None:
        """Init the object
        """
        super().__init__(seed)
        self.set_name("Vegetable")
        self.set_height(5.0)
        self.set_die_age(60)
        self.__nutritional_value: float = 10.0  # arbitrary units
        self.__harvest_season: int = 20  # days to harvest
        self.__harvested: bool = False

    def __repr__(self) -> str:
        """String representation"""
        return super().__repr__() + \
            f"\n Nutritional Value: {self.__nutritional_value} \n \
Harvested: {self.__harvested}"

    def harvest(self) -> None:
        """Harvest the vegetable
        """
        if self.is_alive() and not self.__harvested:
            self.__harvested = True
            print(f"The {self.get_name()} has been harvested with \
nutritional value {self.__nutritional_value}.")

    def age(self) -> None:
        """Increase the age of the vegetable and check for harvesting
        """
        super().age()
        if self.is_alive() and not self.__harvested and \
                self.get_age() >= self.__harvest_season:
            self.harvest()

    def get_nutritional_value(self) -> float:
        """Return nutritional value
        """
        return self.__nutritional_value

    def get_harvest_season(self) -> int:
        """Return harvest season
        """
        return self.__harvest_season

    def is_harvested(self) -> bool:
        """Return if harvested
        """
        return self.__harvested

    def set_nutritional_value(self, value: float) -> None:
        """Set nutritional value

        Args:
            value (float): nutritional value
        """
        if value >= 0:
            self.__nutritional_value = value
        else:
            print("Nutritional value must be positive")

    def set_harvest_season(self, season: int) -> None:
        """Set harvest season

        Args:
            season (int): harvest season
        """
        if season > 0:
            self.__harvest_season = season
        else:
            print("Harvest season must be positive")


class Garden:
    def __init__(
            self,
            plants: list[Plant] = [],
            name: str = "Garden"
            ) -> None:
        """Init the function"""
        self.__plants: list[Plant] = plants
        self.__name: str = name

    def set_name(self, name: str) -> None:
        """Set name of the garden

        Args:
            name (name): the name of the garden
        """
        if name != "":
            self.__name = name

    def age(self) -> None:
        """Make the plant age
        """
        p: Plant
        for p in self.__plants:
            if p.is_alive():
                p.age()
            else:
                print(p.get_name() + " has died 🥀🥀")
                self.__plants.remove(p)

    def __repr__(self) -> str:
        """String representation of the object
        """
        return f"=== {self.__name} ===\n{[p for p in self.__plants]}"

    def add_plants(self, p: Plant) -> None:
        """Add a plants to the garden"""
        self.__plants.append(p)

    def get_name(self) -> str:
        """get the name"""
        return self.__name




# TODO ex6
