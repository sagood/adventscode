from collections import defaultdict


def solve(part, neighbours, seen=set(), cave='start'):
    if cave == 'end':
        return 1
    if cave in seen:
        if cave == 'start':
            return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1

    return sum(solve(part, neighbours, seen | {cave}, n) for n in neighbours[cave])


def main():
    with open('in.txt') as f:
        neighbours = defaultdict(list)
        line = f.readline()
        while line:
            v1, v2 = line.strip().split('-')
            neighbours[v1] += [v2]
            neighbours[v2] += [v1]
            line = f.readline()

    print(solve(part=1, neighbours=neighbours))
    print(solve(part=2, neighbours=neighbours))


if __name__ == '__main__':
    main()

