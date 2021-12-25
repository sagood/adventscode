from collections import Counter
from functools import lru_cache
from itertools import product

dice_freq = Counter(sum(p) for p in product((1, 2, 3), repeat=3))


@lru_cache(maxsize=None)
def part2(p1, p2, sc1 = 0, sc2 = 0):
    if sc1 >= 21: return (1, 0)
    if sc2 >= 21: return (0, 1)
    result = (0, 0)
    for roll_sum, freq in dice_freq.items():
        new_pos = (p1 + roll_sum - 1) % 10 + 1
        new_score = sc1 + new_pos
        p2w, p1w = part2(p2, new_pos, sc2, new_score)
        result = (result[0] + freq * p1w, result[1] + freq * p2w)
    return result


def main():
    with open('in.txt') as f:
        player1_pos = int(f.readline().strip().split(':')[1])
        player2_pos = int(f.readline().strip().split(':')[1])
        print(max(part2(player1_pos, player2_pos)))


if __name__ == '__main__':
    main()
