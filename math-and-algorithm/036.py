# https://atcoder.jp/contests/math-and-algorithm/tasks/abc168_c

import math

a, b, h, m = map(int, input().split())
hm = h * 60 + m
ax = a * math.cos(2 * math.pi * hm / 720)
ay = a * math.sin(2 * math.pi * hm / 720)
bx = b * math.cos(2 * math.pi * m  / 60)
by = b * math.sin(2 * math.pi * m  / 60)

print(math.dist((ax, ay), (bx, by)))