

def main():
    with open('in.txt') as f:
        lines = f.readlines()
        res = sum(2 + line.count('\\') + line.count('"') for line in lines)
        print(res)


if __name__ == '__main__':
    main()
