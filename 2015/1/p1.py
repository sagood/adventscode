

def main():
    with open('in.txt') as f:
        floor = 0
        line = f.readline().strip()
        for c in line:
            if c == '(':
                floor += 1
            elif c == ')':
                floor -= 1

        print(floor)


if __name__ == '__main__':
    main()