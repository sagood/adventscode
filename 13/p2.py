def fold_x(dots, x):
    candidates = list(dots)
    for candidate in candidates:
        c_x, c_y = candidate
        if c_x > x:
            p_x, p_y = 2 * x - c_x, c_y
            if (p_x, p_y) in dots:
                dots.remove((c_x, c_y))
            else:
                dots.remove((c_x, c_y))
                dots.add((p_x, p_y))


def fold_y(dots, y):
    candidates = list(dots)
    for candidate in candidates:
        c_x, c_y = candidate
        if c_y > y:
            p_x, p_y = c_x, 2 * y - c_y
            if (p_x, p_y) in dots:
                dots.remove((c_x, c_y))
            else:
                dots.remove((c_x, c_y))
                dots.add((p_x, p_y))


def main():
    with open('in.txt') as f:
        dots = set()
        line = f.readline().strip()
        while line:
            if ',' in line:
                parts = line.split(',')
                x = int(parts[0])
                y = int(parts[1])
                dots.add((x, y))
            else:
                break
            line = f.readline()

        while line:
            line = f.readline().strip()
            if 'y=' in line:
                y = int(line.split('=')[1])
                fold_y(dots, y)
            elif 'x=' in line:
                x = int(line.split('=')[1])
                fold_x(dots, x)

        # process dots
        min_x = min_y = 1e9
        max_x = max_y = -1e9
        for (dot_x, dot_y) in dots:
            min_x = min(min_x, dot_x)
            max_x = max(max_x, dot_x)
            min_y = min(min_y, dot_y)
            max_y = max(max_y, dot_y)

        for i in range(max_y+1):
            s = ''
            for j in range(max_x+1):
                if (j, i) in dots:
                    s += '#'
                else:
                    s += ' '
            print(s)


if __name__ == '__main__':
    main()
