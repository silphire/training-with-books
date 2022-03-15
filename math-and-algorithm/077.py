# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bj

n = int(input())
xx = [0] * n
yy = [0] * n
for i in range(n):
    xx[i], yy[i] = map(int, input().split())
xx.sort()
yy.sort()

ax = 0
ay = 0
cx = 0
cy = 0
for i in range(n):
    ax += xx[i] * i - cx
    cx += xx[i]
    ay += yy[i] * i - cy
    cy += yy[i]
print(ax + ay)