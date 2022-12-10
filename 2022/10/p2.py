def draw(current_register, current_cycle, res):
    crt_pos = current_cycle % 40
    if crt_pos == 0:
        crt_pos = 40
    current_column_index = current_cycle % 40
    if current_column_index == 0:
        current_column_index = 40
    current_column_index -= 1

    if current_register <= crt_pos <= current_register + 2:
        res[current_cycle // 41][current_column_index] = '█'
    else:
        print(f'current_register: {current_register}, current_cycle: {current_cycle}, crt_pos: {crt_pos}')
        res[current_cycle // 41][current_column_index] = '.'


def main():
    with open('in.txt') as f:
        current_cycle = 1
        previous_instruction = 'noop'
        current_register = 1
        res = [[ '█' for x in range(40)] for y in range(6)]
        for line in f:
            parts = line.strip().split(' ')
            if previous_instruction == 'addx':
                current_cycle += 1
                draw(current_register, current_cycle, res)

            if parts[0] == 'noop':
                current_cycle += 1
                draw(current_register, current_cycle, res)
                previous_instruction = 'noop'
            elif parts[0] == 'addx':
                current_cycle += 1
                current_number = int(parts[1])
                draw(current_register, current_cycle, res)
                current_register += current_number
                previous_instruction = 'addx'

    for i in range(len(res)):
        print(''.join(res[i]))


if __name__ == '__main__':
    main()
