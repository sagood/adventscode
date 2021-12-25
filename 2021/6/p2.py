from collections import Counter


def main():
    with open('in.txt') as f:
        line = f.readline()
        fishes = list(map(int, line.split(',')))
        lives = dict(Counter(fishes))

        for _ in range(256):
            lives = {l: (0 if lives.get(l + 1) is None else lives.get(l + 1)) for l in range(-1, 8)}
            lives[8] = lives[-1]
            lives[6] += lives[-1]
            lives[-1] = 0

        print(sum(lives.values()))


if __name__ == '__main__':
    main()
