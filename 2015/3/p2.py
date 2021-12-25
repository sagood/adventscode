

def main():
    with open('in.txt') as f:
        line = f.readline().strip()
        houses = set()
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        houses.add((0, 0))
        robot = False
        for c in line:
            if not robot:
                if c == '^':
                    y1 = y1 + 1
                elif c == 'v':
                    y1 = y1 - 1
                elif c == '>':
                    x1 += 1
                elif c == '<':
                    x1 -= 1

                if (x1, y1) not in houses:
                    houses.add((x1, y1))
            else:
                if c == '^':
                    y2 = y2 + 1
                elif c == 'v':
                    y2 = y2 - 1
                elif c == '>':
                    x2 += 1
                elif c == '<':
                    x2 -= 1

                if (x2, y2) not in houses:
                    houses.add((x2, y2))

            robot = not robot

        print(len(houses))


if __name__ == '__main__':
    main()
