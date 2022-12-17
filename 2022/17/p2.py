from collections import Counter, defaultdict
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

    rows_number = 10
    z = [x + y * 1j for x in range(7) for y in range(floor- rows_number - 1, floor)]
    bools = [x in filled for x in z]
    offset = 0
    while True:
        offset += 1
        if all(((x - offset * 1j) in filled) ==b for x, b in zip(z, bools)):
            cycle_height = offset
            break

    height2i = defaultdict(list)
    loop_size = Counter()
    prev_height = 0
    for i, h in height.items():
        h %= cycle_height
        if h != prev_height:
            if height2i[h]:
                loop_size[i - height2i[h][-1]] += 1
            height2i[h].append(i)
        prev_height = h
    cycle_length = max(loop_size, key=loop_size.get)

    iterations, offset = divmod(1000000000000, cycle_length)
    print(height[offset] + cycle_height * iterations)


if __name__ == '__main__':
    main()
