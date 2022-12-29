from itertools import accumulate, zip_longest, starmap, chain, tee


def main():
    with open("in.txt", "r") as f:
        parse = lambda x: -2 if x == "=" else (-1 if x == "-" else int(x))
        snafus = [[parse(ch) for ch in reversed(line)] for line in f.read().split()]
        snafu = list(map(sum, (zip_longest(*snafus, fillvalue=0))))

        divisors = accumulate([0] + snafu, lambda acc, el: (acc + el + 2) // 5)
        snafu = starmap(lambda a, b: ((a + b + 2) % 5) - 2, zip(snafu, divisors))

        unparse = lambda x: "=" if x == -2 else ("-" if x == -1 else str(x))
        print("".join(reversed(list(map(unparse, snafu)))))


if __name__ == '__main__':
    main()
