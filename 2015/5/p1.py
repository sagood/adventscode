

def is_vowel(c):
    if c in ['a', 'e', 'i', 'o', 'u']:
        return 1
    else:
        return 0


def is_nice_string(s):
    vowels = 0
    double_letter = 0
    prev = s[0]
    vowels += is_vowel(prev)
    for i in range(1, len(s)):
        cur = s[i]
        vowels += is_vowel(cur)

        if cur == prev:
            double_letter += 1

        if str(prev) + str(cur) in ['ab', 'cd', 'pq', 'xy']:
            return False

        prev = s[i]

    # print(f"{vowels}, {double_letter}")
    if vowels >= 3 and double_letter >= 1:
        return True
    else:
        return False


def main():
    with open('in.txt') as f:
        # print(is_nice_string("ugknbfddgicrmopn"))
        # print(is_nice_string("aaa"))
        # print(is_nice_string("jchzalrnumimnmhp"))
        # print(is_nice_string("haegwjzuvuyypxyu"))
        # print(is_nice_string("dvszwmarrgswjxmb"))
        res = 0
        for line in f:
            line = line.strip()
            if is_nice_string(line):
                res += 1
        print(res)



if __name__ == '__main__':
    main()
