
class Plant():
    """Base Plant class"""
    def __init__(self, seed: int = 1) -> None:
        self.__name: str = ""
        self.__heigh: float = 0.0
        self.__aging: int = 0
        self.__grow_ratio: float = .0042
        self.__die_age: int = int((seed % 10 + 4.2) * 10 + 0.5 * (seed / 10))
        self.__alive = True

    def __repr__(self) -> str:
        if self.__alive:
            return (f"\n===============================\n \
    Hello my name is {self.__name} \n \
    My height is {self.__heigh} cm \n \
    I have {self.__aging} days\n")
        else:
            return (f"\n===============================\n \
    {self.__name} is dead. \n \
    It lived for {self.__aging} days \n")

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
        return (self.__heigh, self.__aging, self.__name, self.__alive)

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__heigh

    def get_age(self) -> int:
        return self.__aging

    def get_die_age(self) -> int:
        return self.__die_age

    def is_alive(self) -> bool:
        return self.__alive

    def get_grow_ratio(self) -> float:
        return self.__grow_ratio

    #######################
    #   SECURE METHODS   #
    #######################

    def set_height(self, height: float) -> None:
        if height >= 0:
            self.__heigh = height
        else:
            print("Height must be positive")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__aging = age
        else:
            print("Age must be positive")

    def set_name(self, name: str) -> None:
        if len(name) > 0:
            self.__name = name
        else:
            print("Name must be non empty")

    def set_die_age(self, die_age: int) -> None:
        if die_age > 0:
            self.__die_age = die_age


class FloweringPlant(Plant):
    """Plant that can flower"""
    def __init__(self, seed: int = 2, name: str = "Flower") -> None:
        super().__init__(seed=seed)
        self.set_name(name)
        self.set_height(10.0)
        self.set_die_age(30)
        self.__color: str = "Red"
        self.__bloomed: bool = False
        self.__bloom_time: int = 5  # days to bloom

    def __repr__(self) -> str:
        return super().__repr__() + \
            f"Color: {self.__color} \nBloomed: {self.__bloomed}\n"

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
    """Flower that has a prize value"""
    def __init__(self, seed: int = 8, name: str = "Flower") -> None:
        super().__init__(seed, name)
        self.__prize = seed % 3 * 9 / seed * (10/len(name))

    def __repr__(self) -> str:
        return super().__repr__() + \
            f"Prize: {self.__prize}\n"

    def get_prize(self) -> float:
        return self.__prize


class Tree(Plant):
    """Tree class that extends Plant"""
    def __init__(self, seed: int = 3) -> None:
        super().__init__(seed)
        self.set_name("Tree")
        self.set_height(100.0)
        self.set_die_age(3650)  # 10 years
        self.__trunk_diameter: float = 1.0  # in cm

    def __repr__(self) -> str:
        return super().__repr__() + \
            f"Trunk Diameter: {self.__trunk_diameter} cm\n"

    def get_trunk_diameter(self) -> float:
        return self.__trunk_diameter

    def _Plant__grow(self) -> None:
        if not self.get_age() > self.get_die_age():
            self.set_height(self.get_height()
                            + self.get_height() * 2 * self.get_grow_ratio())
            self.__trunk_diameter += 0.1  # grows 0.1 cm per aging

    def produce_shade(self) -> None:
        if self.is_alive():
            # print(f"The {self.get_name()} is producing shade.")
            pass

    def age(self) -> None:
        """Increase the age of the tree
        """
        super().age()
        if self.is_alive():
            self.produce_shade()


class Vegetable(Plant):
    def __init__(self, seed: int = 4) -> None:
        super().__init__(seed)
        self.set_name("Vegetable")
        self.set_height(5.0)
        self.set_die_age(60)
        self.__nutritional_value: float = 10.0  # arbitrary units
        self.__harvest_season: int = 20  # days to harvest
        self.__harvested: bool = False

    def __repr__(self) -> str:
        return super().__repr__() + \
            f"Nutritional Value: {self.__nutritional_value} \n\
Harvested: {self.__harvested}\n"

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
        return self.__nutritional_value

    def get_harvest_season(self) -> int:
        return self.__harvest_season

    def is_harvested(self) -> bool:
        return self.__harvested

    def set_nutritional_value(self, value: float) -> None:
        if value >= 0:
            self.__nutritional_value = value
        else:
            print("Nutritional value must be positive")

    def set_harvest_season(self, season: int) -> None:
        if season > 0:
            self.__harvest_season = season
        else:
            print("Harvest season must be positive")


class Garden:
    """Garden class that contains plants"""
    def __init__(
            self,
            plants: list[Plant | Vegetable |
                         Tree | FloweringPlant | PrizeFlower] = [],
            name: str = "Garden"
            ) -> None:
        self.__plants: list[Plant | Vegetable |
                            Tree | FloweringPlant | PrizeFlower] = plants
        self.__name: str = name

    def set_name(self, name: str) -> None:
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

    def __repr__(self) -> str:
        return f"=== {self.__name} ===\n{[p for p in self.__plants]}\n"

    def add_plants(self, p: list[Plant | Vegetable |
                   Tree | FloweringPlant | PrizeFlower]) -> None:
        """Add a plants to the garden"""
        self.__plants.extend(p)

    @classmethod
    def add_plant(cls,
                  garden: 'Garden',
                  p: Plant | Vegetable |
                  Tree | FloweringPlant | PrizeFlower) -> None:
        """Add a plant to the garden"""
        garden.__plants.append(p)

    def get_name(self) -> str:
        return self.__name

    def get_plants(self) -> list[Plant | Vegetable |
                                 Tree | FloweringPlant | PrizeFlower]:
        """Get the list of plants

        Returns:
            list: the plants in the garden
        """
        return self.__plants


class GardenManager:
    """Garden Manager class that manages multiple gardens"""
    def __init__(self) -> None:
        self.__gardens: list[Garden] = []

    def age(self):
        """make the plant age
        """
        g: Garden
        for g in self.__gardens:
            g.age()

    def create_garden_network(self) -> None:
        """Create a network of gardens with plants
        """
        for i in range(6):
            p: Plant | Vegetable | Tree | FloweringPlant | PrizeFlower
            for j in range(12):
                seed = i * 10 + j
                if j % 4 == 0:
                    p = Tree(seed)
                elif j % 4 == 1:
                    p = FloweringPlant(seed, f"Flower{seed}")
                elif j % 4 == 2:
                    p = PrizeFlower(seed, f"PrizeFlower{seed}")
                else:
                    p = Vegetable(seed)
                if j == 0:
                    garden = Garden([p], f"Garden{i}")
                    self.__gardens.append(garden)
                    print(
                        f"Adding {p.get_name()} to garden {garden.get_name()}")
                else:
                    self.__gardens[i].add_plants([p])

    def run(self, verbose: bool = False) -> None:
        """run the time and age plants
        """
        if self.__gardens == []:
            return
        for i in range(150):
            print(f"--- Day {i} ---")
            for g in self.__gardens:
                g.age()
                if verbose:
                    print(f"{g}")

    def __repr__(self) -> str:
        return f"=== Garden Network ===\n{[g for g in self.__gardens]}"

    def get_gardens(self) -> list[Garden]:
        return self.__gardens

    class GardenStats:
        """Class to compute garden statistics"""
        @staticmethod
        def mean(nb: list[int | float]) -> float:
            """Compute the mean of a list of numbers"""
            moy: float = 0
            for i in nb:
                moy += i
            return (moy / len(nb))

        @classmethod
        def garden_analytics(cls,
                             manager: 'GardenManager'
                             ) -> dict[str, float]:
            """Compute garden analytics

            Args:
                manager (GardenManager): the garden manager"""
            total_plants: int = 0
            total_alive: int = 0
            ages: list[float] = []
            heights: list[float] = []

            g: Garden
            for g in manager.get_gardens():
                p: Plant | Vegetable | Tree | FloweringPlant | PrizeFlower
                for p in g.get_plants():
                    total_plants += 1
                    if p.is_alive():
                        total_alive += 1
                    ages.append(p.get_age())
                    heights.append(p.get_height())

            analytics: dict[str, float] = {
                "total_plants": total_plants,
                "total_alive": total_alive,
                "mean_age": cls.mean(ages) if ages else 0,
                "mean_height": cls.mean(heights) if heights else 0,
                "total_gardens": len(manager.get_gardens())
            }
            return analytics


if __name__ == "__main__":
    manager = GardenManager()
    manager.create_garden_network()
    print(manager)
    manager.run(verbose=False)
    print(manager)

    stats = GardenManager.GardenStats.garden_analytics(manager)
    print("Garden Analytics:")
    for key, value in stats.items():
        print(f"{key}: {value}")
