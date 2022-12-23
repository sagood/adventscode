moves = [({-1j, 1 - 1j, -1 - 1j}, -1j), ({1j, 1 + 1j, -1 + 1j}, 1j), ({-1, -1 - 1j, -1 + 1j}, -1),
         ({1, 1 - 1j, 1 + 1j}, 1)]


def move(elf):
    if any(elf + delta in board for delta in [1, 1j, -1, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]):
        for c, d in moves:
            if not any(elf + e in board for e in c):
                props[elf + d] = None if (elf + d) in props else elf
                return 1
    return 0


def main():
    with open("in.txt", "r") as f:
        data = f.readlines()
        global board
        board = {complex(x, y) for y, row in enumerate(data) for x, elf in enumerate(row) if
                    elf in '#'}
        round = 1
        while True:
            global props
            props = {}
            if sum(map(move, board)) == 0: break
            moves.append(moves.pop(0))
            for prop, elf in props.items():
                if elf is not None: board = board - {elf} | {prop}
            if round == 10:
                width = int(max(a.real for a in board)) + 1 - int(min(a.real for a in board))
                height = int(max(a.imag for a in board)) + 1 - int(min(a.imag for a in board))
            round += 1

    print(width * height - len(board))


if __name__ == '__main__':
    main()
