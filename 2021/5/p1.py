import collections


def main():
    with open('in.txt') as f:
        lines = f.readlines()
        s = collections.defaultdict(int)
        for line in lines:
            line = line.strip()
            parts = line.split('->')
            part1 = parts[0].split(',')
            part2 = parts[1].split(',')
            x1 = int(part1[0].strip())
            y1 = int(part1[1].strip())
            x2 = int(part2[0].strip())
            y2 = int(part2[1].strip())

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2)+1):
                    s[(x1, y)] += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2)+1):
                    s[(x, y1)] += 1

        res = {k: v for k, v in s.items() if v >= 2}
        print(len(res))


if __name__ == '__main__':
    main()