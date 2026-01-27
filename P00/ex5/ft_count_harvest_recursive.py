
def ft_count_harvest_recursive(remain: int = -1, max: int = 0):
    if remain < 0:
        max = int(input("Days until harvest: "))
        ft_count_harvest_recursive(max-1, max)
    elif remain == 0:
        print(f"Day {max-remain}\nHarvest time!")
        return
    else:
        print(f"Day {max-remain}")
        ft_count_harvest_recursive(remain-1, max)


# ft_count_harvest_recursive()
