
def main():
    with open('in.txt') as f:
        floor = 0
        line = f.readline().strip()
        for pos, c in enumerate(line):
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1

            if floor == -1:
                print(pos + 1)
                exit(0)


if __name__ == '__main__':
    main()