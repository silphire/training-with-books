# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_n
import math
n = int(input())
f = []
for x in range(2, math.ceil(n ** 0.5) + 1):
    while n % x == 0:
        f.append(x)
        n //= x
if n > 1:
    f.append(n)
print(' '.join(map(str, f)))