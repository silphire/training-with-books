# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bn

n = int(input())
r = sorted([
    tuple(map(int, input().split()))
    for _ in range(n)
], key=lambda x: x[1])

t = 0
a = 0
for x, y in r:
    if t <= x:
        t = y
        a += 1
print(a)