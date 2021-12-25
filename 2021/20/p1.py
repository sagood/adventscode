

def print_image(image):
    for row in range(len(image)):
        s = ''
        for col in range(len(image[0])):
            s += image[row][col]
        print(s)


def do_count(image):
    res = 0
    for row in range(len(image)):
        for col in range(len(image[0])):
            if image[row][col] == '#':
                res += 1

    return res


def process(image, enhancement, i):
    m = len(image)
    n = len(image[0])
    new_m = m + 2
    new_n = n + 2
    new_image = [['.' for _ in range(new_n)] for _ in range(new_m)]

    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    for row in range(new_m):
        for col in range(new_n):
            cur_str = ''
            # print(f"row={row}, col={col}")
            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                # print(f"new_row = {new_row}, new_col = {new_col}")
                if new_row < 1 or new_row >= m+1 or new_col < 1 or new_col >= n+1:
                    if i == 0:
                        cur_str += '0'
                    else:
                        cur_str += '0' if enhancement[0] == '.' else '1'
                else:
                    cur_str += '0' if image[new_row-1][new_col-1] == '.' else '1'
                # print(f"new_row={new_row}, new_col={new_col}, cur_str={cur_str}")
            # print(cur_str)
            cur = int(cur_str, base=2)
            # print(cur)
            enhanced_cur = enhancement[cur]
            new_image[row][col] = enhanced_cur
            # print(enhanced_cur)

    return new_image


def main():
    with open('in.txt') as f:
        enhancement = f.readline().strip()

        f.readline()

        image = []
        line = 'dd'
        while line:
            line = f.readline().strip()
            if line:
                image.append(line)

        for i in range(2):
            enhanced_image = process(image, enhancement, i)
            # print_image(enhanced_image)
            light_cnt = do_count(enhanced_image)
            print(light_cnt)
            image = enhanced_image


if __name__ == '__main__':
    main()
