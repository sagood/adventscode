

def main():
    prev_sum = 0
    cur_sum = 0
    num1 = 0
    num2 = 0
    res = 0
    cnt = 1
    with open('in.txt') as f:
        for line in f:
            number = int(line)

            if cnt == 1:
                cur_sum += number
                num1 = number
            elif cnt == 2:
                cur_sum += number
                num2 = number
            else:
                cur_sum += number
                if cur_sum > prev_sum:
                    res += 1

                prev_sum = cur_sum
                cur_sum -= num1
                num1 = num2
                num2 = number

            cnt += 1

    print(res-1)


if __name__ == '__main__':
    main()