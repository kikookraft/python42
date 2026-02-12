import sys


def inv_add(dico: dict[str, int], name: str, qty: int = 1) -> dict[str, int]:
    if name in dico.values():
        dico.update()
    else:
        dico[name] = qty
    return dico



def main():
    dico: dict[str, int] = {}
    if len(sys.argv) == 1:
        print("Empty inventory - exiting.")
        return
    for item in sys.argv[:1]:
        dico = inv_add(dico, item)


if __name__ == "__main__":
    pass