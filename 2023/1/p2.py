s = {'one': 1, 'two': 2, 'three': 3,
     'four': 4, 'five': 5, 'six': 6,
     'seven': 7, 'eight': 8, 'nine': 9}


def get_number_from_line(line: str) -> int:
    min_index = len(line)
    num = 0
    for n in s.keys():
        index = line.find(n)
        if index != -1 and index < min_index:
            min_index = index
            num = s[n] * 10

    for i in range(len(line)):
        if line[i].isdigit() and i < min_index:
            num = int(line[i]) * 10
            break

    num2 = 0
    max_index = -1
    for n in s.keys():
        index = line.rfind(n)
        if index != -1 and index > max_index:
            max_index = index
            num2 = s[n]

    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit() and i > max_index:
            num2 = int(line[i])
            break

    num = num + num2
    return num


def main():
    res = 0
    with open('in.txt') as f:
        for line in f:
            res += get_number_from_line(line)

    print(res)


if __name__ == '__main__':
    main()
