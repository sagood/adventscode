class Kind:
    AIR = 0
    ROCK = 1
    SAND = 2


def main():
    with open("in.txt", "r") as f:
        points = {}
        lowest_rock = 0
        for line in f:
            raw_points = [tuple(map(int, point.split(","))) for point in line.split("->")]
            for i in range(len(raw_points) - 1):
                x1, y1, x2, y2 = *raw_points[i], *raw_points[i + 1]
                lowest_rock = max(y1, y2, lowest_rock)
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        points[(x, y)] = Kind.ROCK

    total = 0
    res = 0
    floor = lowest_rock + 2
    sand = None
    while sand != (500, 0):
        sand = 500, 0
        while True:
            y = sand[1] + 1
            for dx in 0, -1, 1:
                x = sand[0] + dx
                if y < floor and points.get((x,y), Kind.AIR) == Kind.AIR:
                    sand = x, y
                    break
            else:
                if not res and sand[1] > lowest_rock:
                    res = total
                points[sand] = Kind.SAND
                break
        total += 1

    print(total)


if __name__ == '__main__':
    main()