# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bt

import math

l, r = map(int, input().split())
l = max(l, 2)
s = r - l + 1
primes = [True] * s

for x in range(2, math.ceil(r ** 0.5) + 1):
    m = (l + x - 1) // x * x
    for y in range(m, r + 1, x):
        if y == x:
            continue
        primes[y - l] = False

ans = 0
for p in primes:
    if p:
        ans += 1
print(ans)
