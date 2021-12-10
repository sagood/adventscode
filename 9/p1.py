

def main():
    with open('in.txt') as f:
        lines = f.readlines()
        m = len(lines)
        n = len(lines[0]) - 1
        heightmap = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                heightmap[i][j] = int(lines[i][j])

        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        # process
        res = 0
        for i in range(m):
            for j in range(n):
                cur = heightmap[i][j]
                ok = True
                for d in dirs:
                    r = i + d[0]
                    c = j + d[1]
                    if r < 0 or c < 0 or r >= m or c >= n:
                        continue
                    else:
                        if heightmap[r][c] <= cur:
                            ok = False
                            break
                if ok:
                    print(f"[{i}][{j}] = {cur}")
                    res += (1+cur)

        print(res)


if __name__ == '__main__':
    main()
