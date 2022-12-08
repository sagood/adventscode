
def main():
    with open('in.txt') as f:
        trees = [[(x, y, int(z)) for x, z in enumerate(line.strip())] for (y, line) in enumerate(
            f.readlines())]
        scenic_score = {}

        for _ in range(4):
            for line in trees:
                for (i, (x, y, z)) in enumerate(line):
                    distance = 0
                    for (x_, y_, z_) in line[i + 1:]:
                        distance += 1
                        if z_ >= z:
                            break

                    scenic_score[(x, y)] = scenic_score.get((x, y), 1) * distance

            trees = list(zip(*reversed(trees)))

        print(max(scenic_score.values()))


if __name__ == '__main__':
    main()
