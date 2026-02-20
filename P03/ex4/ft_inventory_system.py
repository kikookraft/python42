import sys

cat: dict[str, list[str]] = {
        "armor": ["helmet", "chestplate", "leggings", "boots"],
        "weapon": ["sword", "bow", "axe"],
        "potion": ["healing", "mana", "strength"]}


def inv_add(dico: dict[str, int], name: str, qty: int = 1) -> dict[str, int]:
    """Add quantity for an item name into the inventory dictionary.
    """
    if qty < 0:
        raise ValueError("qty must be non-negative")
    if not name:
        raise ValueError("name must be non-empty")

    if name in dico:
        dico.update({name: dico[name] + qty})
    else:
        dico.update({name: qty})
    return dico


def _parse_arg(arg: str) -> tuple[str, int]:
    """Parse a single argv entry.

    Expected formats:
    - "name" -> returns (name, 1)
    - "name:qty" -> returns (name, int(qty)) with fallback to 1 on parse error
    """
    if ":" in arg:
        name: str
        qty_str: str
        name, qty_str = arg.split(":", 1)
        try:
            qty = int(qty_str)
        except ValueError:
            qty = 1
    else:
        name = arg
        qty = 1
    return name, qty


def make_rarity_dict(dico: dict[str, int]) -> dict[str, dict[str, int | str]]:
    """Categorize items into rarity levels based on quantity."""
    # find the most present item quantity to set thresholds
    max_qty: int = max(dico.values()) if dico else 0
    result: dict[str, dict[str, int | str]] = {}
    for name, qty in dico.items():
        if qty > max_qty * 0.5:
            result[name] = {"quantity": qty,
                            "rarity": "common",
                            "value": max_qty - qty}
        elif qty > max_qty * 0.2:
            result[name] = {"quantity": qty,
                            "rarity": "uncommon",
                            "value": max_qty - qty}
        else:
            result[name] = {"quantity": qty,
                            "rarity": "rare",
                            "value": max_qty - qty}
    return result


def detect_categories(
        better_dico: dict[str, dict[str, int | str]]
        ) -> dict[str, dict[str, int]]:  # idk why pylance is doing shit
    """Detect item categories based on predefined catalog."""
    category_counts: dict[str, dict[str, int]] = {}
    for name, info in better_dico.items():
        category: str = "unknown"
        for cat_name, items in cat.items():  # search for category
            if name in items:
                category = cat_name
                break
            if category not in category_counts:
                category_counts[category] = {}
            category_counts[category][name] = int(info["quantity"])
        return category_counts


def main() -> None:
    """Build inventory from command line arguments and print detailed
    analytics demonstrating dictionary operations.
    """
    args = sys.argv[1:]
    if not args:
        print("where inventory ??")
        return

    dico: dict[str, int] = dict()  # inventory
    for item in args:  # parse things
        name: str
        qty: int
        name, qty = _parse_arg(item)
        if not name:
            continue
        inv_add(dico, name, qty)

    # this one is better
    better_dico: dict[str, dict[str, int | str]] = make_rarity_dict(dico)
    print("\n=== Inventory with Rarity ===")
    for name, info in better_dico.items():
        print(f"{name}: {info['quantity']} units, Rarity: {info['rarity']}")

    # Calculate total items
    total_items: int = sum(dico.values())

    print("\n=== Da inventory ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(dico)}")

    # Display inventory sorted by quantity (descending)
    print("\n=== Current Inventory ===")
    sorted_items: list[tuple[str, int]] = sorted(
        dico.items(), key=lambda x: x[1], reverse=True
    )
    for name, qty in sorted_items:
        percentage: float = (qty / total_items) * 100
        unit_str: str = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit_str} ({percentage:.1f}%)")

    # Statistics
    print("\n=== Inventory Statistics ===")
    max_item: str = max(dico, key=lambda k: dico[k])
    min_item: str = min(dico, key=lambda k: dico[k])
    print(f"Most abundant: {max_item} ({dico[max_item]} units)")
    print(f"Least abundant: {min_item} ({dico[min_item]} unit)")

    print("\n=== Item Categories ===")
    moderate: dict[str, int] = {k: v for k, v in dico.items() if v > 3}
    scarce: dict[str, int] = {k: v for k, v in dico.items() if v <= 3}

    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")

    # Management suggestions
    print("\n=== Management Suggestions ===")
    restock_needed: list[str] = [
        name for name, qty in dico.items() if qty == 1
    ]
    print(f"Restock needed: {restock_needed}")
    if dico.get("test", 0) == 0:
        print("You should buy some 'test' it is very yummy !")
    else:
        print("Yay you now have some 'test' in your inventory ! Good job !")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(dico.keys())}")
    print(f"Dictionary values: {', '.join(str(v) for v in dico.values())}")


if __name__ == "__main__":
    main()
