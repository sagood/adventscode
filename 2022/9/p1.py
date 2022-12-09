
def main():
    with open('in.txt') as f:
        DIRS = {"L": -1 + 0j, "R": 1 + 0j, "U": 0 - 1j, "D": 0 + 1j}
        for l in (2, 10):
            knots = [0 + 0j for _ in range(l)]
            visited = set([0 + 0j])
            for line in f:
                direction, num = line.split()
                knots[0] += int(num) * DIRS[direction]
                while True:
                    for i in range(1, len(knots)):
                        dist = knots[i - 1] - knots[i]
                        if abs(dist) < 2:
                            break
                        knots[i] += complex(dist.real // abs(dist.real) if dist.real else 0,
                                            dist.imag // abs(dist.imag) if dist.imag else 0)
                    else:
                        visited.add(knots[-1])
                        continue
                    break
            print(len(visited))


if __name__ == '__main__':
    main()
