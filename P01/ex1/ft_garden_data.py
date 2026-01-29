names: list[str] = ["Juan", "Jean-Eude", "Marwalou", "S̸̱͍̖͙̏E", "𝓻𝓸𝓼𝓮", "🗿🗿"]
height: list[float] = [9999999999999999, 1.78, 0.45, 12, 1.95, 275]


class Plant():
    def __init__(self, seed: int = 0) -> None:
        self.name: str = names[((seed+1)+42*11-41*(-15)) % len(names)]
        self.heigh: float = height[((seed+1)+135*4597+241*46) % len(height)]
        self.age: int = (4*seed+(seed % 42)*(42*(seed+2)) % 95 + 1)

    def __repr__(self) -> str:
        return (f"===============================\n \
    Hello my name is {self.name} \n \
    My height is {self.heigh} cm \n \
    I have {self.age} days")


if __name__ == "__main__":
    for i in range(3):
        print(Plant(seed=i))
