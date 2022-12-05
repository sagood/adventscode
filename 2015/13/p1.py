import re
from collections import defaultdict
from itertools import permutations


def find_max_happiness(d):
    res = 0
    for ordering in permutations(d.keys()):
        happiness = sum(d[a][b] + d[b][a] for a, b in zip(ordering, ordering[1:]))
        happiness += d[ordering[0]][ordering[-1]] + d[ordering[-1]][ordering[0]]
        res = max(res, happiness)
    return res


def main():
    d = defaultdict(dict)
    with open('in.txt') as f:
        for line in f:
            line = line.strip()
            x = re.match(r'(\S+) would (\S+) (\d+) happiness units by sitting next to (\S+).', line)
            p1, op, ch, p2 = x.group(1, 2, 3, 4)
            d[p1][p2] = int(ch) if op == 'gain' else -int(ch)

        print(find_max_happiness(d))


if __name__ == '__main__':
    main()
