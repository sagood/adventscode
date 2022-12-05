import re


def main():
    with open('in.txt') as f:
        inputs = f.read().split('\n')

    s = [[] for _ in range(9)]
    while not inputs[0].startswith(' 1'):
        for i in range(9):
            if inputs[0][1 + 4 * i] != ' ':
                s[i].append(inputs[0][1 + 4 * i])
        inputs.pop(0)

    inputs = inputs[2:]
    for c, f, t in [map(int, re.findall('\d+', l)) for l in inputs]:
        s[t-1], s[f-1] = s[f-1][:c][::-1] + s[t-1], s[f-1][c:]

    print(''.join(x[0] for x in s))


if __name__ == '__main__':
    main()