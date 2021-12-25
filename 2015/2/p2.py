

def main():
    with open('in.txt') as f:
        total = 0
        for line in f:
            line = line.strip()
            parts = line.split('x')
            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])
            cur = x * y * z
            l = [x, y, z]
            l.sort()
            cur += 2 * (l[0] + l[1])
            total += cur
        print(total)


if __name__ == '__main__':
    main()