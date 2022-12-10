def calc(current_cycle, current_register):
    if current_cycle in [20, 60, 100, 140, 180, 220]:
        print(f'****************{current_cycle=}, {current_register=}')
        return current_cycle * current_register
    else:
        return 0


def main():
    with open('in.txt') as f:
        current_cycle = 1
        previous_instruction = 'noop'
        current_register = 1
        res = 0
        for line in f:
            parts = line.strip().split(' ')
            if previous_instruction == 'addx':
                current_cycle += 1
                res += calc(current_cycle, current_register)

            if parts[0] == 'noop':
                current_cycle += 1
                previous_instruction = 'noop'
                res += calc(current_cycle, current_register)
            elif parts[0] == 'addx':
                # print(f'{current_cycle=}, {current_register=}, {current_number=}')
                current_cycle += 1
                res += calc(current_cycle, current_register)
                current_number = int(parts[1])
                current_register += current_number
                previous_instruction = 'addx'

            print(f'{current_cycle=}, {current_register=}')

    print(res)


if __name__ == '__main__':
    main()
