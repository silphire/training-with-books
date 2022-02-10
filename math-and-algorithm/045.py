# https://atcoder.jp/contests/math-and-algorithm/tasks/typical90_bz

from collections import defaultdict

n, m = map(int, input().split())

ab = [None] * m
for i in range(m):
    ab[i] = tuple(sorted(map(int, input().split())))
ab.sort()

c = [0] * (n + 1)
for a, b in ab:
    c[b] += 1

ans = 0
for i in range(n):
    if c[i + 1] == 1:
        ans += 1
print(ans)