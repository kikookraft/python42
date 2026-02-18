from typing import Generator


def base() -> Generator[str, None, None]:
    """A simple base generator
    """
    yield "Hello"
    yield "World"
    yield "feur"


def count(start: int = 0, step: int = 1) -> Generator[int, None, None]:
    """A simple count generator

    This generator yields an infinite sequence of integers, starting from
    `start` and incrementing by `step` each time.
    """
    n = start
    while True:
        yield n
        n += step


def rnd(
        seed: int = 0,
        mini: int = 0,
        maxi: int = 2**32 - 1
        ) -> Generator[int, None, None]:
    """A simple pseudo-random number generator using a linear congruential
    generator (LCG) algorithm.

    The LCG is defined by the formula:
        X_{n+1} = (a * X_n + c) % m

    where:
        - X is the sequence of pseudo-random values
        - a, c, and m are constants
        - X_0 is the seed
    """
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    while True:
        x: int = (a * x + c) % m
        yield mini + (x % (maxi - mini + 1))


def demo_count() -> None:
    """Demonstrate the count generator"""
    print("Counting from 5 with step 2:")
    for i, num in enumerate(count(5, 2)):
        print(num)
        if i >= 9:  # Limit to 10 numbers
            print("... (and more counting it goes)")
            break


def demo_random() -> None:
    """Demonstrate the rnd generator"""
    print("Random numbers from 1 to 100:")
    for i, num in enumerate(rnd(seed=42, mini=1, maxi=100)):
        print(num)
        if i >= 9:  # Limit to 10 numbers
            print("... (and more random it goes)")
            break


def demo_interactive() -> None:
    """Demonstrate interactive use of generators"""
    try:
        conter_input: int = int(
            input("Enter starting number for count generator\n> "))
    except ValueError:
        print("Invalid input. Using default starting number 0.")
        conter_input = 0
    print("Counting:")
    counting: Generator[int, None, None] = count(conter_input)
    for i, num in enumerate(counting):
        print(num)
        if i >= 9:  # Limit to 10 numbers
            print("... (and blablablaaaa)")
            break

    print("\nRandom numbers:")
    try:
        max_random: int = int(
            input("Enter maximum number for random generator\n> "))
    except ValueError:
        print("Invalid input. Using default maximum number 100.")
        max_random = 100
    for i, num in enumerate(rnd(seed=42, mini=1, maxi=max_random)):
        print(num)
        if i >= 9:  # Limit to 10 numbers
            print("... (and more random it goes)")
            break


def go_next() -> None:
    try:
        input("Press Enter to get the next value from the generator...\n")
    except (KeyboardInterrupt, EOFError):
        print("\nGenerator stopped by user.")
        return
    print("\n" + "=" * 40 + "\n")


def main() -> None:
    """Demonstrate the generators"""
    demo: Generator[str, None, None] = base()
    print("Base generator output:")
    print(next(demo))  # Hello
    print(next(demo))  # World
    print(next(demo))  # feur
    go_next()
    demo_count()
    go_next()
    demo_random()
    go_next()
    demo_interactive()


if __name__ == "__main__":
    main()
