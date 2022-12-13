

def solve(a, b):
    max_len = max(len(a), len(b))
    for index in range(max_len):
        if index == len(a) and index < len(b):
            return True
        if index < len(a) and index == len(b):
            return False

        val_a = a[index]
        val_b = b[index]
        if isinstance(val_a, int) and isinstance(val_b, int):
            if val_a < val_b:
                return True
            if val_a > val_b:
                return False
        elif isinstance(val_a, list) and isinstance(val_b, list):
            ret = solve(val_a, val_b)
            if ret is not None:
                return ret
        elif isinstance(val_a, int) and isinstance(val_b, list):
            ret = solve([val_a], val_b)
            if ret is not None:
                return ret
        elif isinstance(val_a, list) and isinstance(val_b, int):
            ret = solve(val_a, [val_b])
            if ret is not None:
                return ret

    return None


with open("in.txt", "r") as file:
    data = file.read()
    pairs = [pair.split('\n') for pair in data.split('\n\n')]

    res = 0
    for pair_index, pair in enumerate(pairs):
        a = eval(pair[0])
        b = eval(pair[1])
        if solve(a, b):
            res += pair_index + 1

    print(res)