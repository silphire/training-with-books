# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_k
import math
n = int(input())
primes = [True] * (n + 1)
primes[0] = primes[1] = False
for x in range(2, math.ceil(n ** 0.5) + 1):
    if not primes[x]:
        continue
    for y in range(x + x, n + 1, x):
        primes[y] = False
print(' '.join([str(x) for x, f in enumerate(primes) if f]))