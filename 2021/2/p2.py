

def main():
    horizontal = 0
    depth = 0
    aim = 0
    with open('in.txt') as f:
        for line in f:
            content = line.split(' ')
            direction = content[0]
            amount = int(content[1])
            if direction == 'forward':
                horizontal += amount
                depth += amount * aim
            elif direction == 'down':
                aim += amount
            elif direction == 'up':
                aim -= amount

    print(horizontal * depth)


if __name__ == '__main__':
    main()