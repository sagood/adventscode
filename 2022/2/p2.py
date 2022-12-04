def get_score(opp, res):
    if res == 'X':
        # lose
        extra_score = 0
        if opp == 'A':
            base_score = 3
        elif opp == 'B':
            base_score = 1
        else:
            base_score = 2
    elif res == 'Y':
        # draw
        extra_score = 3
        if opp == 'A':
            base_score = 1
        elif opp == 'B':
            base_score = 2
        else:
            base_score = 3
    elif res == 'Z':
        # win
        extra_score = 6
        if opp == 'A':
            base_score = 2
        elif opp == 'B':
            base_score = 3
        else:
            base_score = 1

    return base_score + extra_score


def main():
    score = 0
    with open('in.txt') as f:
        for line in f:
            inputs = line.strip().split(' ')
            current_score = get_score(inputs[0], inputs[1])
            score += current_score

    print(score)


if __name__ == '__main__':
    main()