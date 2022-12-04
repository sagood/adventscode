

def draw(opp, you):
    return (opp == 'A' and you == 'X') or (opp == 'B' and you == 'Y') or (
                opp == 'C' and you == 'Z')


def win(opp, you):
    return (you == 'X' and opp == 'C') or (you == 'Y' and opp == 'A') or (
                you == 'Z' and opp == 'B')


def get_score(opp, you):
    base_score_map = {'Y': 2, 'X': 1, 'Z': 3}
    if draw(opp, you):
        extra_score = 3
    elif win(opp, you):
        extra_score = 6
    else:
        extra_score = 0

    return base_score_map[you] + extra_score


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