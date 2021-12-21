def get_next(dice_start, diff):
    return 100 if dice_start + diff == 100 else (dice_start + diff) % 100


def main():
    with open('in.txt') as f:
        player1_pos = int(f.readline().strip().split(':')[1])
        player2_pos = int(f.readline().strip().split(':')[1])

        player1_score = 0
        player2_score = 0
        player1_rolled = 0
        player2_rolled = 0
        player1_move = True
        dice_start = 1
        while True:
            if player1_score >= 1000 or player2_score >= 1000:
                loser_score = player1_score if player1_score < player2_score else player2_score
                rolled = player1_rolled + player2_rolled
                print(loser_score * rolled)
                print(f"loser_score={loser_score}, rolled={rolled}")
                exit(0)

            one = get_next(dice_start, 0)
            two = get_next(dice_start, 1)
            three = get_next(dice_start, 2)
            cur_move = one + two + three

            if player1_move:
                player1_pos = (player1_pos + cur_move) % 10
                if player1_pos == 0:
                    player1_pos = 10
                # print(f"player1_pos={player1_pos}")
                player1_score += player1_pos
                # print(f"Player 1 rolls {dice_start}+{dice_start+1}+{dice_start+2} and moves to "
                #       f"space {player1_pos} for a total score of {player1_score}.")

                player1_rolled += 3
            else:
                player2_pos = (player2_pos + cur_move) % 10
                if player2_pos == 0:
                    player2_pos = 10
                # print(f"player2_pos={player2_pos}")
                player2_score += player2_pos
                # print(f"Player 2 rolls {dice_start}+{dice_start + 1}+{dice_start + 2} and moves to "
                #       f"space {player2_pos} for a total score of {player2_score}.")
                player2_rolled += 3

            player1_move = not player1_move
            # print(f"player1_score={player1_score}, player2_score={player2_score}")
            # print(f"player1_rolled={player1_rolled}, player2_rolled={player2_rolled}")
            dice_start = get_next(dice_start, 3)


if __name__ == '__main__':
    main()
