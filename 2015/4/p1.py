import hashlib


def main():
    with open('in.txt') as f:
        line = f.readline().strip()
        # line = "abcdef"
        # line = "pqrstuv"
        cur = 100000
        while True:
            cur_text = line + str(cur)
            h = hashlib.md5(cur_text.encode("utf-8")).hexdigest()
            if h[0:5] == '00000':
                print(cur)
                exit(0)
            cur += 1


if __name__ == '__main__':
    main()
