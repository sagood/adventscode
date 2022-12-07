cwd = root = {}
stack = []


def solve(dir = root):
    if type(dir) == int:
        return (dir, 0)
    size = 0
    ans = 0
    for child in dir.values():
        s, a = solve(child)
        size += s
        ans += a
    if size <= 100000:
        ans += size
    return (size, ans)


def main():
    with open('in.txt') as f:
        for line in f:
            line = line.strip()
            if line[0] == "$":
                if line[2] == "c":
                    dir = line[5:]
                    if dir == "/":
                        cwd = root
                        stack = []
                    elif dir == "..":
                        cwd = stack.pop()
                    else:
                        if dir not in cwd:
                            cwd[dir] = {}
                        stack.append(cwd)
                        cwd = cwd[dir]
            else:
                x, y = line.split()
                if x == "dir":
                    if y not in cwd:
                        cwd[y] = {}
                else:
                    cwd[y] = int(x)

        print(solve()[1])


if __name__ == '__main__':
    main()
