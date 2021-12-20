import fileinput, re, functools


def tokenize(expr):
    return [int(token) if '0' <= token[0] <= '9' else token
            for token in re.findall("\[|\]|\d+", expr)]


def explode(tokens):
    depth = 0
    for index in range(len(tokens) - 4):
        if (depth >= 4 and
            tokens[index + 0] == '[' and
            tokens[index + 3] == ']'):
            for left in range(index - 1, -1, -1):
                if isinstance(tokens[left], int):
                    tokens[left] += tokens[index + 1]
                    break
            for right in range(index + 4, len(tokens)):
                if isinstance(tokens[right], int):
                    tokens[right] += tokens[index + 2]
                    break
            tokens[index : index + 4] = [0]
            return True
        elif tokens[index] == '[':
            depth += 1
        elif tokens[index] == ']':
            depth -= 1
    return False


def split(tokens):
    for index in range(len(tokens)):
        if isinstance(tokens[index], int) and tokens[index] >= 10:
            tokens[index : index + 1] = ['[',
                                         (tokens[index] + 0) // 2,
                                         (tokens[index] + 1) // 2,
                                         ']']
            return True
    return False


def reduct(tokens):
    while explode(tokens) or split(tokens):
        pass
    return tokens


def magnitude(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
        elif token == ']':
            stack[-2 :] = [3 * stack[-2] + 2 * stack[-1]]
    return stack[-1]


def main():
    with open('small.txt') as f:
        numbers = [tokenize(line.strip()) for line in f.readlines()]
        # print(numbers)

        total = functools.reduce(
            lambda left, right: reduct(['['] + left + right + [']']),
            numbers)
        print("Part 1:", magnitude(total))

        largest = 0
        for left in numbers:
            for right in numbers:
                total = reduct(['['] + left + right + [']'])
                largest = max(largest, magnitude(total))
        print("Part 2:", largest)


if __name__ == '__main__':
    main()
