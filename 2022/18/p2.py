def main():
    cubes = []
    with open("in.txt", "r") as f:
        cubes = {tuple(map(int, l.split(','))) for l in f}

        sides = lambda x, y, z: {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z),
                                 (x, y, z + 1), (x, y, z - 1)}

        print(sum((s not in cubes) for c in cubes for s in sides(*c)))

        seen = set()
        todo = [(0, 0, 0)]

        while todo:
            here = todo.pop()
            seen |= {here}
            todo += [s for s in (sides(*here) - cubes - seen) if all(-1 <= c <= 25 for c in s)]

        print(sum((s in seen) for c in cubes for s in sides(*c)))


if __name__ == '__main__':
    main()
