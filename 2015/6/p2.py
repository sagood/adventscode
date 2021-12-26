

def process(grid, start_row, start_col, end_row, end_col, op):
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if op == 0:
                grid[i][j] += 1
            elif op == 1:
                if grid[i][j] > 0:
                    grid[i][j] -= 1
            elif op == 2:
                grid[i][j] += 2


def main():
    with open('in.txt') as f:
        grid = [[0 for _ in range(1000)] for _ in range(1000)]
        for line in f:
            line = line.strip()
            # op: 0: turn on, 1: turn off, 2: toggle
            if "toggle" in line:
                op = 2
                parts = line.split('toggle')
            elif "turn on" in line:
                op = 0
                parts = line.split('turn on')
            elif "turn off" in line:
                op = 1
                parts = line.split('turn off')
            parts = parts[1].split('through')
            start = parts[0].split(',')
            start_row = int(start[0].strip())
            start_col = int(start[1].strip())
            end = parts[1].split(',')
            end_row = int(end[0].strip())
            end_col = int(end[1].strip())

            process(grid, start_row, start_col, end_row, end_col, op)

        print(sum([grid[i][j] for i in range(0, 1000) for j in range(0, 1000)]))


if __name__ == '__main__':
    main()
