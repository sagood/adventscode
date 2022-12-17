from itertools import cycle

ACTION = {">": 1, "<": -1}
ROCKS = [
    (2 + 3j, 3 + 3j, 4 + 3j, 5 + 3j),  # -
    (3 + 3j, 2 + 4j, 3 + 4j, 4 + 4j, 3 + 5j),  # +
    (2 + 3j, 3 + 3j, 4 + 3j, 4 + 4j, 4 + 5j),  # _|
    (2 + 3j, 2 + 4j, 2 + 5j, 2 + 6j),  # |
    (2 + 3j, 3 + 3j, 3 + 4j, 2 + 4j)  # []
]


def main():
    with open("in.txt", "r") as f:
        for line in f:
            line = line.strip()
            jet_cycle = cycle(map(ACTION.get, line))
            rock_cycle = cycle(ROCKS)
            floor = 0
            filled = {i - 1j for i in range(7)}
            height = {}
            for i, rock in zip(range(1, 10001), rock_cycle):
                rock = tuple(r + floor*1j for r in rock)
                while True:
                    jet = next(jet_cycle)
                    new_rock = tuple(r + jet for r in rock)
                    if all(0 <= z.real < 7 for z in new_rock) and not filled & set(new_rock):
                        rock = new_rock
                    new_rock = tuple(r - 1j for r in rock)
                    if filled & set(new_rock):
                        filled.update(rock)
                        floor = max(floor, *(int(z.imag) + 1 for z in rock))
                        break
                    else:
                        rock = new_rock
                height[i] = floor

    print(height[2022])


if __name__ == '__main__':
    main()
