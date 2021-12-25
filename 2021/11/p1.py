def increase(grid, r, c):
    for i in range(r):
        for j in range(c):
            grid[i][j] += 1


def contains_flash(grid, r, c):
    for i in range(r):
        for j in range(c):
            if grid[i][j] >= 9:
                return True
    return False


def flash(grid, r, c):
    dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    has_flash = False
    for i in range(r):
        for j in range(c):
            if grid[i][j] >= 9:
                for d in dirs:
                    next_r = i + dir[0]
                    next_c = j + dir[1]
                    if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                        continue
                    else:
                        grid[next_r][next_c] += 1
                        if grid[next_r][next_c] >= 9:
                            has_flash = True


def main():
    with open('in.txt') as f:
        lines = f.readlines()
        r = len(lines)
        c = len(lines[0]) - 1
        grid = [[0 for _ in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                grid[i][j] = int(lines[i][j])

        # process
        res = 0
        dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

        for _ in range(100):
            increase(grid, r, c)
            stack = []
            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 10:
                        for d in dirs:
                            next_r = i + d[0]
                            next_c = j + d[1]
                            if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                                continue
                            else:
                                stack.append((next_r, next_c))

            while len(stack) > 0:
                i, j = stack.pop()
                grid[i][j] += 1
                if grid[i][j] == 10:
                    for d in dirs:
                        next_r = i + d[0]
                        next_c = j + d[1]
                        if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                            continue
                        else:
                            stack.append((next_r, next_c))

            for i in range(r):
                for j in range(c):
                    if grid[i][j] > 9:
                        res += 1
                        grid[i][j] = 0

        print(res)
        print(grid)


if __name__ == '__main__':
    main()
