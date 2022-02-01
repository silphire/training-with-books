# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ag

import math

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

if r1 < r2:
    x1, x2 = x2, x1
    y1, y2 = y2, y1
    r1, r2 = r2, r1

d = (x1 - x2) ** 2 + (y1 - y2) ** 2
if d == (r1 + r2) ** 2:
    print(4)
elif d > (r1 + r2) ** 2:
    print(5)
else:
    if d < (r1 - r2) ** 2:
        print(1)
    elif d > (r1 - r2) ** 2:
        print(3)
    else:
        print(2)