def get_common_char(first_component: str, second_component: str):
    for c1 in first_component:
        for c2 in second_component:
            if c1 == c2:
                return c1
    return ''



def main():
    with open('in.txt') as f:
        res = 0
        for line in f:
            inputs = line.strip()
            length = len(inputs)
            first_component = inputs[0:length // 2]
            second_component = inputs[length // 2:length]
            common_char = get_common_char(first_component, second_component)

            if 'a' <= common_char <= 'z':
                res += ord(common_char) - ord('a') + 1
            elif 'A' <= common_char <= 'Z':
                res += ord(common_char) - ord('A') + 27

    print(res)


if __name__ == '__main__':
    main()