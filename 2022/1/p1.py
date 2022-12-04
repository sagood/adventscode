

def main():
    max_calories = 0
    current_calories = 0
    with open('in.txt') as f:
        for line in f:
            if line == '\n':
                if current_calories > max_calories:
                    max_calories = current_calories
                current_calories = 0
            else:
                number = int(line)
                current_calories += number

    print(max_calories)


if __name__ == '__main__':
    main()
