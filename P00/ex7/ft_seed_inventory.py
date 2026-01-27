
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit.lower() in ["packets", "grams"]:
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
    elif unit == "area":
        print(f"{seed_type.capitalize()} seeds: covers {quantity} m²")
    else:
        print("Unknown unit type")


# ft_seed_inventory("a", 1, "f")
