# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_m
import math
n = int(input())
a = set()
for x in range(1, math.ceil(n ** 0.5) + 1):
    if n % x == 0:
        d = n // x
        a.add(d)
        a.add(n // d)
for x in a:
    print(x)