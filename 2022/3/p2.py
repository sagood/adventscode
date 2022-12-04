def get_common_char(first_component: str, second_component: str):
    for c1 in first_component:
        for c2 in second_component:
            if c1 == c2:
                return c1
    return ''



def main():
    with open('in.txt') as f:
        res = 0
        i = 0
        string = ["", "", ""]
        for line in f:
            if i <= 2:
                string[i] = line.strip()
                i += 1
                if i == 3:
                    first, second, third = string[0], string[1], string[2]
                    common_char = (set(first) & set(second) & set(third)).pop()

                    if 'a' <= common_char <= 'z':
                        res += ord(common_char) - ord('a') + 1
                    elif 'A' <= common_char <= 'Z':
                        res += ord(common_char) - ord('A') + 27
                    i = 0
                    string = ["", "", ""]

    print(res)


if __name__ == '__main__':
    main()