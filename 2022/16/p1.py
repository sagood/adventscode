import re
from collections import defaultdict


def main():
    g = {}
    scores = {}
    with open("in.txt", "r") as f:
        for line in f:
            line = line.strip()
            parts = re.split(r"; tunnels? leads? to valves? ", line)
            v = parts[0].split(" ")[1]
            scores[v] = int(parts[0].split("=")[-1])
            g[v] = parts[1].split(", ")

        node_id = defaultdict(lambda: len(node_id))
        [node_id[u] for u in scores if scores[u]]
        ALLMASK = (1 << len(node_id)) - 1

        d = defaultdict(lambda: [[-1 for mask in range(ALLMASK + 1)] for t in range(31)])

        def dp(u, t, mask):
            if t == 0:
                return 0
            if d[u][t][mask] == -1:
                best = max(dp(v, t - 1, mask) for v in g[u])
                bit = 1 << node_id[u]
                if bit & mask:
                    best = max(best, dp(u, t - 1, mask - bit) + scores[u] * (t - 1))
                d[u][t][mask] = best
            return d[u][t][mask]

        print(dp("AA", 30, ALLMASK))




if __name__ == '__main__':
    main()