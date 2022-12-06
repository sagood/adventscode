def is_word_ok(word):
    return len(set(word)) == len(word)


def main():
    with open('in.txt') as f:
        line = f.readline().strip()
        for i in range(14, len(line)):
            word = line[i-14:i]
            if is_word_ok(word):
                print(i)
                exit(0)


if __name__ == '__main__':
    main()
