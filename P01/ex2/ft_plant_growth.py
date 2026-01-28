names = ["Juan", "Jean-Eude", "Marwalou", "S̸̱͍̖͙̏È̷̡̧͚̅G̷͌͆̀̕", "𝓻𝓸𝓼𝓮", "🗿🗿"]
height = [9999999999999999, 1.78, 0.45, 12, 1.95, 275]


class Plant():
    def __init__(self, seed: int = 0) -> None:
        self.name: str = names[((seed+1)+42*11-41*(-15)) % len(names)]
        self.heigh: float = height[((seed+1)+135*4597+241*46) % len(height)]
        self.aging: int = (4*seed+(seed % 42)*(42*(seed+2)) % 95 + 1)
        self.grow_ratio: float = .42

    def __repr__(self) -> str:
        return (f"===============================\n \
    Hello my name is {self.name} \n \
    My height is {self.heigh} cm \n \
    I have {self.aging} days")

    def grow(self) -> None:
        self.heigh += self.heigh * self.grow_ratio

    def age(self) -> None:
        self.aging += 1

    def die(self) -> None:
        self.heigh = 0
        self.name = f"{self.name} - dead"

    def get_info(self) -> tuple:
        return (self.heigh, self.age)
