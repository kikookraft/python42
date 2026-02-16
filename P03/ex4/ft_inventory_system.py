import sys


def inv_add(dico: dict[str, int], name: str, qty: int = 1) -> dict[str, int]:
    """Add quantity for an item name into the inventory dictionary.

    If the item already exists, its quantity is increased by "qty".
    Returns the updated dictionary (same object for convenience).
    """
    if qty < 0:
        # For simplicity, disallow negative additions here.
        raise ValueError("qty must be non-negative")
    if not name:
        # Disallow empty names for simplicity.
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
    """Build inventory from command line arguments and print a
    simple listing.

    If no items are provided the program prints an informative
    message and exits.
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
            # skip empty names
            continue
        inv_add(dico, name, qty)

    # Demonstrate dict methods
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {len(dico)}")

    # Use keys() method
    if dico.keys():
        print(f"Unique item types: {len(dico.keys())}")

    print("\n=== Current Inventory ===")
    # Use items() method to iterate
    for name, qty in dico.items():
        print(f"{name}: {qty} units")

    # Use values() to find statistics
    if dico.values():
        print("\n=== Inventory Statistics ===")
        max_item = max(dico, key=lambda k: dico[k])
        min_item = min(dico, key=lambda k: dico[k])
        print(f"Most abundant: {max_item} "
              f"({dico[max_item]} units)")
        print(f"Least abundant: {min_item} "
              f"({dico[min_item]} units)")

    # Demonstrate get() method for safe access
    print("\n=== Dictionary Properties Demo ===")
    sample_items = ["potion", "shield", "nonexistent"]
    for item in sample_items:
        in_inventory = item in dico.keys()
        print(f"Sample lookup - '{item}' in inventory: {in_inventory}")


if __name__ == "__main__":
    main()
