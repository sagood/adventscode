def evaluate(gate, commands, values):
    try:
        val = int(gate)
        values[gate] = val
        return
    except ValueError:
        pass
    command = commands[gate]
    if len(command) == 1:
        try:
            values[gate] = int(command[0])
        except ValueError:
            evaluate(command[0], commands, values)
            values[gate] = values[command[0]]
    elif len(command) == 2:
        if command[0] == "NOT":
            lhs = command[1]
            if values.get(lhs) is None:
                evaluate(lhs, commands, values)
            values[gate] = 0xffff - values[lhs]
    elif len(command) == 3:
        lhs = command[0]
        rhs = command[2]
        op = command[1]
        if values.get(lhs) is None:
            evaluate(lhs, commands, values)
        if values.get(rhs) is None:
            evaluate(rhs, commands, values)
        if op == "AND":
            values[gate] = values[lhs] & values[rhs]
        elif op == "OR":
            values[gate] = values[lhs] | values[rhs]
        elif op == "RSHIFT":
            values[gate] = 0xffff & (values[lhs] >> int(rhs))
        elif op == "LSHIFT":
            values[gate] = 0xffff & (values[lhs] << int(rhs))


def solve(instructions):
    commands = {tokens[-1]: tokens[:-2]
                for tokens in map(str.split, instructions)}
    values = {'b': 16076}
    evaluate('a', commands, values)
    print(values['a'])


def main():
    with open('in.txt') as f:
        instructions = f.readlines()
        solve(instructions)


if __name__ == '__main__':
    main()
