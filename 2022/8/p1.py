
def main():
    with open('in.txt') as f:
        trees = [[(x, y, int(z)) for x, z in enumerate(line.strip())] for (y, line) in enumerate(
            f.readlines())]
        visible = set()

        for _ in range(4):
            for line in trees:
                candidates = []
                for (i, (x, y, z)) in enumerate(line):
                    candidates = [(x_, y_, z_) for (x_, y_, z_) in candidates if z < z_]
                    candidates.append((x, y, z))

                visible = visible | set((x, y) for (x, y, z) in candidates)

            trees = list(zip(*reversed(trees)))

        print(len(visible))


if __name__ == '__main__':
    main()
