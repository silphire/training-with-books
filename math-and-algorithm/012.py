# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_l

import math
n = int(input())
fin = math.ceil(n ** 0.5) + 1
primes = [True] * fin
primes[0] = primes[1] = False
for x in range(2, fin):
    if not primes[x]:
        continue
    for y in range(x + x, fin, x):
        primes[y] = False
for x, p in enumerate(primes):
    if p and n % x == 0:
            print('No')
            exit()
print('Yes')