from functools import cmp_to_key


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
    lines = [line.strip() for line in data.replace('\n\n', '\n').split('\n')]
    lines.append('[[2]]')
    lines.append('[[6]]')
    packets = [eval(line) for line in lines]
    sorted_packets = sorted(packets, key=cmp_to_key(lambda a, b: -1 if solve(a, b) else 1))
    index2 = sorted_packets.index([[2]]) + 1
    index6 = sorted_packets.index([[6]]) + 1

    print(index2 * index6)