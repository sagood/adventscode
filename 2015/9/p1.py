import sys
from itertools import permutations


def main():
    cities = set()
    distances = dict()
    with open('in.txt') as f:
        for line in f:
            (src, _, dest, _, dist) = line.split()
            cities.add(src)
            cities.add(dest)
            distances.setdefault(src, dict())[dest] = int(dist)
            distances.setdefault(dest, dict())[src] = int(dist)

    min_dist = sys.maxsize
    max_dist = 0
    for items in permutations(cities):
        dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
        min_dist = min(min_dist, dist)
        max_dist = max(max_dist, dist)

    print(f"min: {min_dist}")
    print(f"max: {max_dist}")


if __name__ == '__main__':
    main()
