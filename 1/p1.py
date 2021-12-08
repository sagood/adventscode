

def main():
    prev = 0
    res = 0
    is_first = True
    with open('in.txt') as f:
        for line in f:
            number = int(line)
            if is_first:
                prev = number
                is_first = False
            else:
                if number > prev:
                    res += 1
                prev = number

    print(res)


if __name__ == '__main__':
    main()