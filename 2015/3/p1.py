

def main():
    with open('in.txt') as f:
        line = f.readline().strip()
        houses = set()
        x, y = 0, 0
        houses.add((x, y))
        for c in line:
            if c == '^':
                y = y + 1
            elif c == 'v':
                y = y - 1
            elif c == '>':
                x += 1
            elif c == '<':
                x -= 1

            if (x, y) not in houses:
                houses.add((x, y))

        print(len(houses))


if __name__ == '__main__':
    main()