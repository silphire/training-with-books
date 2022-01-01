# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_g
import math
n, x, y = map(int, input().split())
z = x * y // math.gcd(x, y)
print(n // x + n // y - n // z)