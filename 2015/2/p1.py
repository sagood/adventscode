

def main():
    with open('in.txt') as f:
        total = 0
        for line in f:
            line = line.strip()
            parts = line.split('x')
            x = int(parts[0])
            y = int(parts[1])
            z = int(parts[2])
            cur = 2 * x * y + 2 * x * z + 2 * y * z
            cur += min(x * y, y * z, x * z)
            total += cur
        print(total)


if __name__ == '__main__':
    main()