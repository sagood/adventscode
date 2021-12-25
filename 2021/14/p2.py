from collections import Counter, defaultdict


def main():
    with open('small.txt') as f:
        line = f.readline().strip()
        start = line

        f.readline()

        rules = dict()
        while line:
            line = f.readline().strip()
            if '->' in line:
                parts = line.split('->')
                left = parts[0].strip()
                right = parts[1].strip()
                rules[left] = right

        pairs = defaultdict(int)
        for a, b in zip(start, start[1:]):
            pairs[a+b] += 1
        # print(pairs)

        # process
        chars = defaultdict(int)
        for c in start:
            chars[c] += 1
        # print(chars)

        for _ in range(40):
            for (a, b), c in pairs.copy().items():
                # print(f"a = {a}, b = {b}, c = {c}")
                x = rules[a + b]
                pairs[a + b] -= c
                pairs[a + x] += c
                pairs[x + b] += c
                chars[x] += c

        print(max(chars.values()) - min(chars.values()))


if __name__ == '__main__':
    main()
