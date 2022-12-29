def solve(start, stop, step, grid, height, width):
    positions = set([start])

    while True:
        next_positions = set()
        for r, c in positions:
            for x, y in ((r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (x, y) == stop:
                    return step

                if 0 <= x < height and 0 <= y < width \
                   and grid[x][(y - step) % width] != ">" \
                   and grid[x][(y + step) % width] != "<" \
                   and grid[(x - step) % height][y] != "v" \
                   and grid[(x + step) % height][y] != "^":
                    next_positions.add((x, y))
        positions = next_positions
        if not positions:
            positions.add(start)
        step += 1


def main():
    with open("in.txt", "r") as f:
        grid = [row[1:-1] for row in f.read().splitlines()[1:-1]]
        height, width = len(grid), len(grid[0])
        start, stop = (-1, 0), (height, width - 1)

        res = solve(start, stop, 1, grid, height, width)
        print(res)


if __name__ == '__main__':
    main()
