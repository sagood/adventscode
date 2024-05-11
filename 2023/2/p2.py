import numpy as np


def main():
    colors = {'red': 0, 'green': 1, 'blue': 2}
    with open('in.txt') as f:
        lines = f.readlines()
        cubes = np.zeros((len(lines), 3, 10), dtype=int)
        for i, line in enumerate(lines):
            _, p = line.split(':')
            for j, c in enumerate(p.split(';')):
                for pair in c.split(','):
                    count, color = pair.split()
                    cubes[i, colors[color], j] = count

    res = cubes.max(2).prod(1).sum()

    print(res)


if __name__ == '__main__':
    main()
