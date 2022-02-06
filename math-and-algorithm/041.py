# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_al

from collections import defaultdict
t = int(input())
n = int(input())
d = defaultdict(int)
for _ in range(n):
    l, r = map(int, input().split())
    d[l] += 1
    d[r] -= 1
a = 0
for tt in range(t):
    a += d[tt]
    print(a)
    