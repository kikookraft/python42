from alchemy.grimoire import validate_ingredients, record_spell


def main() -> None:
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    result_fire: str = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {result_fire}')
    result: str = validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {result}\n')

    print("Testing spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}\n')

    print("Testing late import technique:")
    print(f'record_spell("Lightning", "air"): '
          f'{record_spell("Lightning", "air")}')
    print("Circular dependency curse avoided using late imports!\n")

    print("All spells processed safely!")


if __name__ == "__main__":
    main()
