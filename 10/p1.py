

def get_score(line):
    stack = []
    m = {'}': '{', ']': '[', ')': '(', '>': '<'}
    v = {'}': 1197, ')': 3, ']': 57, '>': 25137}
    for c in line:
        if c == '{' or c == '(' or c == '[' or c == '<':
            stack.append(c)
        else:
            top = stack.pop()
            if top != m[c]:
                return v[c]
    return 0


def main():
    with open('in.txt') as f:
        res = 0
        line = "sdd"
        while line:
            line = f.readline().strip()
            v = get_score(line)
            res += v
        print(res)


if __name__ == '__main__':
    main()
