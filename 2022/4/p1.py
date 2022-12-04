def fully_overlaps(range1, range2):
    first_start = int(range1[0])
    first_end = int(range1[1])
    second_start = int(range2[0])
    second_end = int(range2[1])

    if (first_start <= second_start <= first_end) and (
            first_start <= second_end <= first_end):
        return True
    elif (second_start <= first_start <= second_end) and (
            second_start <= first_end <= second_end):
        return True
    else:
        return False


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