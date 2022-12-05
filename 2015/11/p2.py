def meets_requirements(current_pw):
    return meets_requirement1(current_pw) and meets_requirement2(current_pw) and meets_requirement3(current_pw)


def meets_requirement1(current_pw):
    for i in range(len(current_pw) - 2):
        if ord(current_pw[i]) == ord(current_pw[i + 1]) - 1 == ord(current_pw[i + 2]) - 2:
            return True

    return False


def meets_requirement2(current_pw):
    forbidden = ['i', 'o', 'l']
    for c in current_pw:
        if c in forbidden:
            return False

    return True


def meets_requirement3(current_pw):
    pairs = set()
    for i in range(len(current_pw) - 1):
        if current_pw[i] == current_pw[i + 1]:
            pairs.add(current_pw[i])

    return len(pairs) >= 2


def increment(current_pw):
    current_pw = list(current_pw)
    for i in range(len(current_pw) - 1, -1, -1):
        if current_pw[i] == 'z':
            current_pw[i] = 'a'
        else:
            current_pw[i] = chr(ord(current_pw[i]) + 1)
            break

    return ''.join(current_pw)


def main():
    current_pw = 'cqjxxzaa'
    while not meets_requirements(current_pw):
        current_pw = increment(current_pw)

    print(current_pw)


if __name__ == '__main__':
    main()
