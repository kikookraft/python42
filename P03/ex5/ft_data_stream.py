import typing
from typing import Generator


def game_event_generator(count: int) -> Generator[dict[str, typing.Any], None, None]:
    """Generate game events using a pseudo-random generator.
    
    Args:
        count: Number of events to generate
        
    Yields:
        Dictionary containing event data
    """
    players = ['alice', 'bob', 'charlie', 'diana', 'eve']
    actions = ['killed monster', 'found treasure', 'leveled up']
    
    # Simple LCG for randomness
    seed = 42
    a, c, m = 1664525, 1013904223, 2**32
    
    for i in range(count):
        # Generate pseudo-random values
        seed = (a * seed + c) % m
        player_idx = seed % len(players)
        
        seed = (a * seed + c) % m
        action_idx = seed % len(actions)
        
        seed = (a * seed + c) % m
        level = 1 + (seed % 20)  # Level between 1 and 20
        
        yield {
            'id': i + 1,
            'player': players[player_idx],
            'level': level,
            'action': actions[action_idx]
        }


def fibonacci_generator(count: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence.
    
    Args:
        count: Number of Fibonacci numbers to generate
        
    Yields:
        Next Fibonacci number
    """
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_generator(count: int) -> Generator[int, None, None]:
    """Generate prime numbers.
    
    Args:
        count: Number of primes to generate
        
    Yields:
        Next prime number
    """
    num = 2
    generated = 0
    while generated < count:
        if is_prime(num):
            yield num
            generated += 1
        num += 1


def main() -> None:
    """Demonstrate generator usage with game data streaming."""
    print("=== Game Data Stream Processor ===")
    
    # Generate and process game events
    event_count = 1000
    print(f"Processing {event_count} game events...")
    
    # Process events using generator (memory efficient)
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    
    event_stream = game_event_generator(event_count)
    
    # Show first few events
    for event in event_stream:
        if event['id'] <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")
        
        # Collect statistics
        if event['level'] >= 10:
            high_level_count += 1
        if event['action'] == 'found treasure':
            treasure_count += 1
        if event['action'] == 'leveled up':
            levelup_count += 1
        
        if event['id'] == 3:
            print("...")
    
    # Display analytics
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: [depends on system]")
    
    # Demonstrate other generators
    print("\n=== Generator Demonstration ===")
    
    # Fibonacci
    fib_count = 10
    fib_numbers = list(fibonacci_generator(fib_count))
    print(f"Fibonacci sequence (first {fib_count}): "
          f"{', '.join(map(str, fib_numbers))}")
    
    # Primes
    prime_count = 5
    prime_numbers = list(prime_generator(prime_count))
    print(f"Prime numbers (first {prime_count}): "
          f"{', '.join(map(str, prime_numbers))}")


if __name__ == "__main__":
    main()
