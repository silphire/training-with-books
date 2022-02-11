# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ao

from collections import defaultdict
import sys
sys.setrecursionlimit(400000)

n, m = map(int, input().split())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

color = [None] * n

def dfs(p, c):
    global g, color
    if color[p] is None:
        color[p] = c
        for x in g[p]:
            if not dfs(x, 1 - c):
                return False
        return True
    else:
        return color[p] == c

for p in range(n):
    if color[p] is None:
        if not dfs(p, 0):
            print('No')
            exit()
print('Yes')