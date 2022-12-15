def find(set_y, data, beacons):
    x_ranges = set()
    for sensor, beacon in data:
        manhattan = sum(abs(a - b) for a, b in zip(sensor, beacon))
        if (man_y := abs(sensor[1] - set_y)) <= manhattan:
            x_ranges.add((sensor[0] - (man_x := manhattan - man_y), sensor[0] + man_x))
    total_range = []
    ranges = sorted(x_ranges)
    start, end = ranges[0]
    for x, y in ranges[1:]:
        if x > end:
            total_range.append((start, end))
            start, end = x, y
            continue
        if y > end:
            end = y
    if (start, end) not in total_range:
        total_range.append((start, end))
    if len(total_range) > 1:
        return (total_range[0][1] + 1) * 4000000 + set_y
    return None


def main():
    with open("in.txt", "r") as f:
        set_y = 2000000
        data = [((z := [int(x.split(" ")[y].split("=")[1].strip(",").strip(":")) for y in
                        [2, 3, -2, -1]])[:2], z[2:]) for x in f.read().splitlines()]
    beacons = set(tuple(x[1]) for x in data)
    for y in range(4000000):
        if ret := find(y, data, beacons):
            print(ret)
            break


if __name__ == '__main__':
    main()