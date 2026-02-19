import sys


def inv_add(dico: dict[str, int], name: str, qty: int = 1) -> dict[str, int]:
    """Add quantity for an item name into the inventory dictionary.

    If the item already exists, its quantity is increased by "qty".
    Returns the updated dictionary (same object for convenience).
    """
    if qty < 0:
        raise ValueError("qty must be non-negative")
    if not name:
        raise ValueError("name must be non-empty")

    if name in dico:
        dico[name] += qty
    else:
        dico[name] = qty
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


def main() -> None:
    """Build inventory from command line arguments and print detailed
    analytics demonstrating dictionary operations.
    """
    args = sys.argv[1:]
    if not args:
        print("where inventory ??")
        return

    # Use dict() constructor to create inventory
    dico: dict[str, int] = dict()
    for item in args:
        name: str
        qty: int
        name, qty = _parse_arg(item)
        if not name:
            continue
        inv_add(dico, name, qty)

    # Calculate total items
    total_items: int = sum(dico.values())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(dico)}")

    # Display inventory sorted by quantity (descending)
    print("\n=== Current Inventory ===")
    sorted_items = sorted(dico.items(), key=lambda x: x[1], reverse=True)
    for name, qty in sorted_items:
        percentage = (qty / total_items) * 100
        unit_str = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit_str} ({percentage:.1f}%)")

    # Statistics
    print("\n=== Inventory Statistics ===")
    max_item = max(dico, key=lambda k: dico[k])
    min_item = min(dico, key=lambda k: dico[k])
    print(f"Most abundant: {max_item} ({dico[max_item]} units)")
    print(f"Least abundant: {min_item} ({dico[min_item]} unit)")

    # Categorize items (Moderate: >3, Scarce: <=3)
    print("\n=== Item Categories ===")
    moderate: dict[str, int] = {k: v for k, v in dico.items() if v > 3}
    scarce: dict[str, int] = {k: v for k, v in dico.items() if v <= 3}
    
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")

    # Management suggestions (restock items with quantity == 1)
    print("\n=== Management Suggestions ===")
    restock_needed = [name for name, qty in dico.items() if qty == 1]
    print(f"Restock needed: {restock_needed}")

    # Demonstrate dictionary methods
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(dico.keys())}")
    print(f"Dictionary values: {', '.join(str(v) for v in dico.values())}")
    
    # Demonstrate get() and membership test
    sample_item = list(dico.keys())[0] if dico else "none"
    in_inventory = sample_item in dico.keys()
    print(f"Sample lookup - '{sample_item}' in inventory: {in_inventory}")


if __name__ == "__main__":
    main()
