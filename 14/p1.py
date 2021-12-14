from collections import Counter


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

        # process
        for _ in range(10):
            res = ''
            for i in range(len(start) - 1):
                cur = start[i:i+2]
                tmp = rules[cur]
                res += cur[0] + tmp
                if i == len(start) - 2:
                    res += cur[1]
            # print(res)
            start = res

        c = dict(Counter(start))
        low = 1e9
        high = -1e9
        for (k, v) in c.items():
            low = min(low, v)
            high = max(high, v)
        print(high - low)


if __name__ == '__main__':
    main()
