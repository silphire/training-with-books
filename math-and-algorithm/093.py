# https://atcoder.jp/contests/math-and-algorithm/tasks/typical90_al
import math
a, b = map(int, input().split())
lcm = a // math.gcd(a, b) * b
if lcm > 10 ** 18:
    print('Large')
else:
    print(lcm)