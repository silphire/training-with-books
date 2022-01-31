# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_af

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
d = float('inf')
for i in range(n):
    for j in range(i + 1, n):
        d = min(d, ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5)
print(d)