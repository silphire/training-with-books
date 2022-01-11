# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_p

import functools
import math
input()
print(functools.reduce(lambda x, y: math.gcd(x, y), map(int, input().split())))
