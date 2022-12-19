import collections
import re
import sys


def solve(oo, co, Oo, Oc, go, gO, T=24):
    q = collections.deque()
    q.append((0, (0, 0, 0, 0, 1, 0, 0, 0)))
    s = set()

    res = 0
    while len(q) > 0:
        t, (o, c, O, g, No, Nc, NO, Ng) = q.popleft()
        res = max(res, g)

        if t == T or (o, c, O, g, No, Nc, NO, Ng) in s:
            continue
        s.add((o, c, O, g, No, Nc, NO, Ng))

        if (g + Ng * (T - t) + (T - t) * (T - t + 1) // 2) <= res:
            continue

        if (
                o >= oo
                and No < max(oo, co, Oo, go)
                and o + (T - t) * No < (T - t) * max(oo, co, Oo, go)  # (*)
        ):
            q.append((t + 1, (o - oo + No, c + Nc, O + NO, g + Ng, No + 1, Nc, NO, Ng)))
        if (
                o >= co
                and Nc < Oc
                and c + (T - t) * Nc < (T - t) * Oc  # (*)
        ):
            q.append((t + 1, (o - co + No, c + Nc, O + NO, g + Ng, No, Nc + 1, NO, Ng)))
        if (
                o >= Oo and c >= Oc
                and NO < gO
                and O + (T - t) * NO < (T - t) * gO  # (*)
        ):
            q.append((t + 1, (o - Oo + No, c - Oc + Nc, O + NO, g + Ng, No, Nc, NO + 1, Ng)))
        if o >= go and O >= gO:
            q.append((t + 1, (o - go + No, c + Nc, O - gO + NO, g + Ng, No, Nc, NO, Ng + 1)))
        else:
            q.append((t + 1, (o + No, c + Nc, O + NO, g + Ng, No, Nc, NO, Ng)))

    return res


def main():
    with open("in.txt", "r") as f:
        blueprints = [tuple(map(int, re.findall(r"\d+", blueprint))) for blueprint in
                      f.read().strip().split("\n")]
        res = solve(*blueprints[0][1:], T=32) * solve(*blueprints[1][1:], T=32) * solve(
            *blueprints[2][1:], T=32)
        print(res)


if __name__ == '__main__':
    main()
