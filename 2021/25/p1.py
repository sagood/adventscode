import itertools


def main():
    with open('in.txt') as f:
        grid = [line.strip() for line in f]

        h, w = len(grid), len(grid[0])
        d = {(i, j): col for i, row in enumerate(grid) for j, col in enumerate(row) if col != '.'}

        for t in itertools.count(1):
            d1 = {p if c == '>' and (p := (i, (j + 1) % w)) not in d else (i, j): c for (i, j), c in
                  d.items()}
            d1 = {p if c == 'v' and (p := ((i + 1) % h, j)) not in d1 else (i, j): c for (i, j), c
                  in d1.items()}
            if d1 == d:
                print(t)
                break
            d = d1


if __name__ == '__main__':
    main()
