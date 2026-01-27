
def ft_count_harvest_recursive(remain: int = -1):
    if remain < 0:
        ft_count_harvest_recursive(int(input("Days until harvest: ")))
    elif remain == 0:
        print("Harvest time!")
        return
    print("Day {remain}")
    ft_count_harvest_recursive(remain-1)
