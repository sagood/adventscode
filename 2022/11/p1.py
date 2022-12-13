from math import lcm, prod

monkey_id = 0


class Monkey:
    def __init__(self, line):
        _, a, b, c, d, e = line.split('\n')
        global monkey_id
        self.id = monkey_id
        monkey_id += 1
        self.items = [int(i) for i in a[18:].split(',')]
        self.op = lambda old, b=b[19:]: eval(b)
        self.div = int(c[20:])
        self.true = int(d[28:])
        self.false = int(e[29:])
        self.act = 0


def main():
    with open('in.txt') as f:
        monkeys = [*map(Monkey, f.read().split('\n\n'))]
        p = lcm(*[m.div for m in monkeys])

        for _ in range(20):
            for monkey in monkeys:
                for worry in monkey.items:
                    worry = monkey.op(worry) % p
                    next_worry = worry // 3
                    dest = monkey.false if next_worry % monkey.div else monkey.true
                    monkeys[dest].items.append(next_worry)
                    monkey.act += 1
                monkey.items = []
    print(prod(sorted(-monkey.act for monkey in monkeys)[:2]))


if __name__ == '__main__':
    main()
