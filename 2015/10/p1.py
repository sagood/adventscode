from itertools import groupby


def look_and_say(s):
    return ''.join(str(len(list(v))) + k for k, v in groupby(s))


def main():
    cities = set()
    distances = dict()
    with open('in.txt') as f:
        num = f.readline()
        p1 = num
        for _ in range(40):
            p1 = look_and_say(p1)
        print(len(p1))

        p2 = num
        for _ in range(50):
            p2 = look_and_say(p2)
        print(len(p2))


if __name__ == '__main__':
    main()
