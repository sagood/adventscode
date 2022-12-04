def fully_overlaps(range1, range2):
    first_start = int(range1[0])
    first_end = int(range1[1])
    second_start = int(range2[0])
    second_end = int(range2[1])

    if first_end < second_start or second_end < first_start:
        return False
    else:
        return True


def main():
    with open('in.txt') as f:
        res = 0
        for line in f:
            inputs = line.strip()
            inputs = inputs.split(',')
            range1 = inputs[0].split('-')
            range2 = inputs[1].split('-')
            if fully_overlaps(range1, range2):
                res += 1

    print(res)


if __name__ == '__main__':
    main()