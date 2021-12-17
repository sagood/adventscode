

def main():
    with open('in.txt') as f:
        line = f.readline().strip()
        parts = line.split(',')
        x_parts = parts[0].split('x=')[1].split('..')
        x_start, x_end = int(x_parts[0]), int(x_parts[1])
        y_parts = parts[1].split('y=')[1].split('..')
        y_start, y_end = int(y_parts[0]), int(y_parts[1])
        y_max = -y_start-1
        print(y_max * (y_max + 1) // 2)


if __name__ == '__main__':
    main()
