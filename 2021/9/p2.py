import math


def dfs(r, c, m, n, groups, heightmap):
    if r < 0 or c < 0 or r >= m or c >= n or heightmap[r][c] == 9 or heightmap[r][c] == -1:
        return

    heightmap[r][c] = -1
    groups[len(groups) - 1] += 1
    dfs(r+1, c, m, n, groups, heightmap)
    dfs(r - 1, c, m, n, groups, heightmap)
    dfs(r, c + 1, m, n, groups, heightmap)
    dfs(r, c - 1, m, n, groups, heightmap)


def main():
    groups = []
    with open('in.txt') as f:
        lines = f.readlines()
        m = len(lines)
        n = len(lines[0]) - 1
        heightmap = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                heightmap[i][j] = int(lines[i][j])

        # process
        for i in range(m):
            for j in range(n):
                groups.append(0)
                dfs(i, j, m, n, groups, heightmap)

        print(groups)
        print(math.prod(sorted(groups, reverse=True)[:3]))


if __name__ == '__main__':
    main()
