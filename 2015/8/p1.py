

def main():
    with open('in.txt') as f:
        res = 0
        for line in f:
            line = line.strip()
            res += len(line)
            s = line.encode('ascii', 'ignore').decode('unicode_escape')
            res -= (len(s) - 2)
            # print(line, s, len(line), len(s))
        print(res)


if __name__ == '__main__':
    main()
