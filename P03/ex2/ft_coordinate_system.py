import sys
import math


def calculate_distance(
    pos1: tuple[float, float, float],
    pos2: tuple[float, float, float]
) -> float:
    """calculate distance between two position in 3d dimension

    Args:
        pos1: First position (x, y, z)
        pos2: Second position (x, y, z)

    Returns:
        The distance between the two positions
    """
    return math.sqrt(
        (pos2[0] - pos1[0]) ** 2 +
        (pos2[1] - pos1[1]) ** 2 +
        (pos2[2] - pos1[2]) ** 2
    )


def parse_coordinates(coord_string: str) -> tuple[int, int, int]:
    """parse coord like "x,y,z" into tuple.

    Args:
        coord_string: String in format "x,y,z"

    Returns:
        Tuple of (x, y, z)

    Raises:
        ValueError: If parsing fails
    """
    parts = coord_string.split(",")
    if len(parts) != 3:
        raise ValueError(
            "Coordinate string must have exactly 3 values, got : "
            + coord_string)

    x, y, z = 0, 0, 0
    try:
        x = int(parts[0].strip())
        y = int(parts[1].strip())
        z = int(parts[2].strip())
    except ValueError as e:
        raise ValueError(f"Invalid coordinate value: {e}")

    return (x, y, z)


def main() -> None:
    """Demonstrate tuple usage for 3D coordinate systems
    """
    print("=== 😭 ===")

    coords: list[tuple[int, int, int]] = []

    # take argument as "x,y,z x2,y2,z2"
    for coordinate in sys.argv[1:]:
        try:
            x, y, z = parse_coordinates(coordinate)
            coords.append((x, y, z))
        except Exception as e:
            print(f"An error occured: {e}")

    origin = (0, 0, 0)
    if len(coords) < 2:
        # calculate distance between point and origin
        if len(coords) == 1:
            distance = calculate_distance(origin, coords[0])
            print(
                f"Distance from origin to point {coords[0]} is {distance:.2f}")
        else:
            print("Not enough coordinates to calculate distance.")
    else:
        for i in range(len(coords) - 1):
            distance = calculate_distance(origin, coords[i])
            print(
                f"Distance from origin to point {coords[i]} is {distance:.2f}")
        distance = calculate_distance(origin, coords[-1])
        print(
            f"Distance from origin to last point {coords[-1]} is"
            + f" {distance:.2f}")


if __name__ == "__main__":
    main()
