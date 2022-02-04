# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ak

from collections import defaultdict

n = int(input())
aa = list(map(int, input().split()))
m = int(input())
d = defaultdict(int)
pb = None
for _ in range(m):
    b = int(input())
    if pb is None:
        pb = b
        continue
    minb = min(pb, b)
    maxb = max(pb, b)
    d[minb - 1] += 1
    d[maxb - 1] -= 1
    pb = b
ans = 0
nt = 0
for i in range(n - 1):
    nt += d[i]
    ans += nt * aa[i]
print(ans)