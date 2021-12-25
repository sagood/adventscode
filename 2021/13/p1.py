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
                break
            elif 'x=' in line:
                x = int(line.split('=')[1])
                fold_x(dots, x)
                break

        print(len(dots))


if __name__ == '__main__':
    main()
