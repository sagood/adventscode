def eval(inputs, ops, expr):
    if type(expr) is tuple:
        return expr
    elif expr.isdigit():
        return (int(expr), 0)
    elif expr.isalpha():
        return eval(inputs, ops, inputs[expr])
    else:
        a, op, b = expr.split()
        return ops[op](eval(inputs, ops, a), eval(inputs, ops, b))


def main():
    with open("in.txt", "r") as f:
        inputs = {a: b for a, b in [line.strip().split(': ') for line in f]}
        ops = {
            '+': lambda a, b: (a[0] + b[0], a[1] + b[1]),
            '-': lambda a, b: (a[0] - b[0], a[1] - b[1]),
            '*': lambda a, b: (a[0] * b[0], a[1] * b[0] + a[0] * b[1]),
            '/': lambda a, b: (a[0] / b[0], (a[1] * b[0] - a[0] * b[1]) / b[0] ** 2)
        }

        inputs['humn'] = (0, 1)
        a, b = inputs['root'].split(' + ')
        c, d = eval(inputs, ops, f"{a} - {b}")
        print(-c / d)


if __name__ == '__main__':
    main()
