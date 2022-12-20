

def solve(inputs):
    arrangement = inputs.copy()
    zero_index = 0
    arr = [[idx, a] for (idx, a) in enumerate(arrangement)]

    for i in range(len(arrangement)):
        for j in range(len(arrangement)):
            if arr[j][0] == i:
                cur = arr.pop(j)
                new_index = (j + cur[1]) % len(arr)
                arr.insert(new_index, (i, cur[1]))
                break

    for (idx, (_, val)) in enumerate(arr):
        if val == 0:
            zero_index = idx
            break

    return arr[(zero_index + 1000) % len(arr)][1] + arr[(zero_index + 2000) % len(arr)][1] + arr[(zero_index + 3000) % len(arr)][1]


def main():
    with open("in.txt", "r") as f:
        inputs = list(map(int, f.readlines()))
        res = solve(inputs)
        print(res)


if __name__ == '__main__':
    main()
