import re


def main():
    with open("in.txt", "r") as f:
        lines = f.readlines()

        maze = {}
        current_pos = None

        for y, l in enumerate(lines, 1):
            if not l:
                break

            for x, c in enumerate(l, 1):
                if c == '.':
                    maze[x + y * 1j] = True
                    if not current_pos:
                        current_pos = x + y * 1j
                elif c == '#':
                    maze[x + y * 1j] = False

        moves = re.findall('(\d+|[LR])', lines[-1])
        facing = 1

        for m in moves:
            if m in 'RL':
                facing *= 1j if m == 'R' else -1j
            else:
                for i in range(int(m)):
                    match maze.get(current_pos + facing, None):
                        case True:
                            current_pos += facing
                        case False:
                            break
                        case None:
                            match facing:
                                case 1:
                                    candidate = complex(min(pos.real for pos in maze.keys() if
                                                            pos.imag == current_pos.imag),
                                                        current_pos.imag)
                                case -1:
                                    candidate = complex(max(pos.real for pos in maze.keys() if
                                                            pos.imag == current_pos.imag),
                                                        current_pos.imag)
                                case 1j:
                                    candidate = complex(current_pos.real, min(
                                        pos.imag for pos in maze.keys() if
                                        pos.real == current_pos.real))
                                case -1j:
                                    candidate = complex(current_pos.real, max(
                                        pos.imag for pos in maze.keys() if
                                        pos.real == current_pos.real))

                            if maze[candidate]:
                                current_pos = candidate
                            else:
                                break

        directions = [1j ** i for i in range(4)]
        print(1000 * int(current_pos.imag) + 4 * int(current_pos.real) + directions.index(facing))


if __name__ == '__main__':
    main()
