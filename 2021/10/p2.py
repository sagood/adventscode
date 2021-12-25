

def get_score(line):
    print(f"line is {line}")
    stack = []
    m = {'{': '}', '[': ']', '(': ')', '<': '>'}
    m2 = {'}': '{', ']': '[', ')': '(', '>': '<'}
    v = {'}': 3, ')': 1, ']': 2, '>': 4}
    for c in line:
        if c == '{' or c == '(' or c == '[' or c == '<':
            stack.append(c)
        else:
            top = stack.pop()
            if top != m2[c]:
                return 0
    score = 0
    stack.reverse()
    for c in stack:
        print(c)
        score *= 5
        score += v[m[c]]
    print(f"score is {score}")
    return score

def main():
    with open('in.txt') as f:
        res = []
        line = "sdd"
        while line:
            line = f.readline().strip()
            v = get_score(line)
            if v != 0:
                res.append(v)
        res.sort()
        print(res)
        print(res[(len(res) + 1) // 2 - 1])


if __name__ == '__main__':
    main()
