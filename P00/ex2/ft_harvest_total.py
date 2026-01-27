
def ft_harvest_total():
    total: int = 0
    for i in [1, 2, 3]:
        total += int(input(f"Day {i} harvest: "))
    print(f"Total harvest: {total}")
