import typing
from typing import Generator


def rnd(seed: int) -> Generator[int, None, None]:
    """Simple linear congruential generator (LCG) for pseudo-random numbers."""
    a, c, m = 1664525, 1013904223, 2**32
    while True:
        seed = (a * seed + c) % m
        yield seed


def rnd_int(seed: int, low: int, high: int) -> Generator[int, None, None]:
    """Generate pseudo-random integers in a range [low, high]."""
    for num in rnd(seed):
        yield low + (num % (high - low + 1))


def count(start: int = 0) -> Generator[int, None, None]:
    """Generate an infinite sequence of integers starting from 'start'."""
    n = start
    while True:
        yield n
        n += 1


def game_event_generator(event_count: int) -> Generator[
        typing.Dict[str, typing.Any], None, None]:
    """Generate random game events
    """
    players = ['philippe', 'bob', 'squid game',
               'Queen Elizabeth II', 'spiderman', 'Jean Eude', "tobesson"]
    actions = ['killed creeper', 'pressed F to pay respect',
               'leveled up', 'died', 'was the impostor']

    gen: Generator[int, None, None] = rnd_int(42, 1, 1000000)
    ct: Generator[int, None, None] = count(1)

    for _ in range(event_count):
        yield {
            'id': next(ct),
            'player': players[next(gen) % len(players)],
            'action': actions[next(gen) % len(actions)],
            'level': (next(gen) % 20) + 1
        }


def fibonacci_generator(count: int) -> Generator[int, None, None]:
    """this good old fibonacci buddy is back"""
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def stream_gen() -> Generator[str, None, None]:
    """Example of a simple string stream generator."""
    messages = [
        "Hello",
        "I",
        "am",
        "under",
        "water, ",
        "please",
        "help",
        "me",
        "and",
        "nice",
        "to",
        "meet",
        "you",
        "hihihihihi :)"
    ]
    for msg in messages:
        yield msg


def main() -> None:
    """print data flowing like piss yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
    print("=== indian meme moment ===")
    for msg in stream_gen():
        print(msg, end=' ')
    print("")

    print("\n=== and now some maths ===")
    for num in fibonacci_generator(20):
        print(f"Fibonacci number: {num}")

    print("\n=== random game events ===")
    try:
        input("Press Enter to start the big mess...")
        for event in game_event_generator(100000):
            if event['action'] == 'died':
                print(
                    f"skipping die event because we dont care about "
                    f"{event['player']} dying")
            print(f"Event ID: {event['id']}, Player: {event['player']}, "
                f"Action: {event['action']}, Level: {event['level']}")
    except (KeyboardInterrupt, EOFError):
        print("\n💀💀💀")


if __name__ == "__main__":
    main()
