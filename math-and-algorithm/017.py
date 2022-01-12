# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_q

import functools
import math
n = int(input())
aa = list(map(int, input().split()))

def lcm(a, b):
    return a * b // math.gcd(a, b)

print(functools.reduce(lambda a, b: lcm(a, b), aa))