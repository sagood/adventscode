

def main():
    with open('in.txt') as f:
        line = f.readline().strip()
        parts = line.split(',')
        x_parts = parts[0].split('x=')[1].split('..')
        x_start, x_end = int(x_parts[0]), int(x_parts[1])
        y_parts = parts[1].split('y=')[1].split('..')
        y_start, y_end = int(y_parts[0]), int(y_parts[1])

        res = 0
        for v_y in range(y_start, 1 - y_start):
            y, i, v_x = 0, 0, set()
            while y_start <= y:
                x, j = 0, 0
                if y <= y_end:
                    while x <= x_end:
                        if x_start <= x: v_x.add(j)
                        j, x = j + 1, x + min(j, i)
                i, y, v_y = i+1, y + v_y, v_y - 1
            res += len(v_x)
        print(res)



if __name__ == '__main__':
    main()
