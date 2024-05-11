def get_number_from_line(line: str) -> int:
    num = 0
    for c in line:
        if c.isdigit():
            num = int(c) * 10
            break

    for c in reversed(line):
        if c.isdigit():
            num += int(c)
            break

    return num


def main():
    res = 0
    with open('in.txt') as f:
        for line in f:
            res += get_number_from_line(line)

    print(res)


if __name__ == '__main__':
    main()
