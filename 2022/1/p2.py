import queue


def main():
    q = queue.PriorityQueue()
    current_calories = 0
    with open('in.txt') as f:
        for line in f:
            if line == '\n':
                q.put(-current_calories)
                current_calories = 0
            else:
                number = int(line)
                current_calories += number

    q.put(-current_calories)
    print(-(q.get() + q.get() + q.get()))


if __name__ == '__main__':
    main()