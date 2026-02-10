import sys
import math


def coords_dist(
        p1: tuple[float, float, float],
        p2: tuple[float, float, float]
        ) -> float:
    """Calculate distance between two point in space

    Args:
        p1 (tuple[float, float, float]): first pos
        p2 (tuple[float, float, float]): second pos

    Returns:
        float: the distance between the two points
    """
    return (
        math.sqrt(
            (p2[0]-p1[0])**2 +
            (p2[1]-p1[1])**2 +
            (p2[2]-p1[2])**2
        )
    )


def check_coord(co: tuple[str, str, str]) -> tuple[float, float, float]:
    """Check if the coord is correct

    Args:
        co (tuple[str, str, str]): coordinates

    Raises:
        Exception: error if its not number

    Returns:
        tuple[float, float, float]: tuple of float
    """
    coord: list[float] = []
    for i in range(3):
        coord.append(float(co[i]))
    return (coord[0], coord[1], coord[2])


def main() -> None:
    """Test the main function
    """
    coords: list[str] = []
    final_co: list[tuple[float, float, float]] = []
    # check arguments
    if len(sys.argv) == 1:
        print("there is nothing...")
        return
    if len(sys.argv[1:]) % 3 != 0:
        print("It seems you have messed up the coordinates")
        return
    for i in range(len(sys.argv[1:])):
        if len(coords) < 3:
            coords.append(sys.argv[i+1])
        else:
            co: tuple[str, str, str] = (
                coords[0],
                coords[1],
                coords[2]
            )
            coords.clear()
            try:
                co2: tuple[float, float, float] = check_coord(co)
            except Exception as e:
                print(f"Error: {e}")
                return
            final_co.append(co2)
    if len(final_co) == 0:
        try:
            good_cord: tuple[float, float, float] = check_coord(
                (coords[0], coords[1], coords[2]))
        except Exception as e:
            print(f"Error: {e}")
            return
        print(f"Distance to origin: {coords_dist(good_cord, (0, 0, 0))}")
    else:
        print(f"Distace between {final_co[0]} and {final_co[1]}:",
              coords_dist(final_co[0], final_co[1]))


if __name__ == "__main__":
    main()
