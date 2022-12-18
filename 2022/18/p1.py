

offsets = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
]


def main():
    cubes = []
    with open("in.txt", "r") as f:
        for line in f:
            line = line.strip()
            x, y, z = [int(i) for i in line.split(",")]
            cubes.append([x, y, z])

            res = 0
            for cube in cubes:
                for offset in offsets:
                    adjacent = False
                    for cube2 in cubes:
                        if cube2[0] == cube[0] + offset[0] and cube2[1] == cube[1] + offset[1] and \
                                cube2[2] == cube[2] + offset[2]:
                            adjacent = True
                            break
                    if not adjacent:
                        res += 1

        print(res)


if __name__ == '__main__':
    main()
