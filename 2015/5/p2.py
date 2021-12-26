import re


def main():
    with open('in.txt') as f:
        # print(is_nice_string("ugknbfddgicrmopn"))
        # print(is_nice_string("aaa"))
        # print(is_nice_string("jchzalrnumimnmhp"))
        # print(is_nice_string("haegwjzuvuyypxyu"))
        # print(is_nice_string("dvszwmarrgswjxmb"))
        lines = f.readlines()
        count = sum(
            1 for s in lines
            if len(re.findall(r"([a-z]{2}).*\1", s))
            and re.findall(r"([a-z]).\1", s)
        )
        print(count)


if __name__ == '__main__':
    main()
