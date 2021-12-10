

def main():
    with open('in.txt') as f:
        line = f.readline().strip()
        numbers = line.split(',')
        boards = []

        # empty line
        line = f.readline()
        while line:
            # 5x5 grid
            board = [[0 for i in range(5)] for j in range(5)]
            for i in range(5):
                line = f.readline().strip()
                nums = line.split()
                for j in range(5):
                    board[i][j] = nums[j]

            boards.append(board)

            # empty line
            line = f.readline()

        # prepare to process
        visited = [[[False for i in range(5)] for j in range(5)] for k in range(len(boards))]
        wins = [False for i in range(len(boards))]

        # process
        for num in numbers:
            for i in range(len(boards)):
                if wins[i]:
                    continue

                board = boards[i]
                for j in range(5):
                    for k in range(5):
                        if board[j][k] == num:
                            visited[i][j][k] = True

                win = does_win(visited[i])
                if win:
                    if sum(wins) == len(boards) - 1:
                        accu = 0
                        for j in range(5):
                            for k in range(5):
                                if not visited[i][j][k]:
                                    accu += int(boards[i][j][k])
                        print(accu)
                        print(num)
                        print(accu * int(num))
                        exit(0)
                    else:
                        wins[i] = True


def does_win(board):

    win = False
    m = len(board)
    n = len(board[0])
    for i in range(m):
        row = True
        for j in range(n):
            if not board[i][j]:
                row = False
                break
        if row:
            return True

    for j in range(n):
        col = True
        for i in range(m):
            if board[i][j] == False:
                col = False
                break
        if col == True:
            return True

    return False

if __name__ == '__main__':
    main()
