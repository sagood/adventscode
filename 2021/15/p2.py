import heapq


def print_grid(grid):
    for i in range(len(grid)):
        print(grid[i])
    print()


def neighbors(x, y, m, n):
    dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    res = []
    for d in dirs:
        next_x = x + d[0]
        next_y = y + d[1]
        if 0 <= next_x < m and 0 <= next_y < n:
            res.append((next_x, next_y))
    return res


def main():
    with open('in.txt') as f:
        lines = list(map(str.strip, f.readlines()))
        m = len(lines)
        n = len(lines[0])

        grid = [[0 for i in range(5*n)] for j in range(5*m)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = int(lines[i][j])

        for multi in range(1, 5):
            for j in range(multi * n, (multi + 1) * n):
                for i in range(0, m):
                    num = grid[i][j % n] + multi
                    grid[i][j] = 9 if num == 9 else num % 9

        for multi in range(1, 5):
            for i in range(multi * m, (multi + 1) * m):
                for j in range(0, 5 * n):
                    num = grid[i % m][j] + multi
                    grid[i][j] = 9 if num == 9 else num % 9

        print_grid(grid)

        # process
        q = []
        heapq.heappush(q, (0, 0, 0))
        visited = {(0, 0): 0}

        m = 5 * m
        n = 5 * n
        while q:
            cost, x, y = heapq.heappop(q)
            for (new_x, new_y) in neighbors(x, y, m, n):
                new_cost = cost + grid[new_x][new_y]
                if (new_x, new_y) == (m - 1, n - 1):
                    print(new_cost)
                    exit(0)

                if (new_x, new_y) in visited and visited[(new_x, new_y)] > new_cost:
                    visited[(new_x, new_y)] = new_cost

                if (new_x, new_y) not in visited:
                    heapq.heappush(q, (new_cost, new_x, new_y))
                    visited[(new_x, new_y)] = new_cost

        print(visited[m - 1][n - 1])


if __name__ == '__main__':
    main()
