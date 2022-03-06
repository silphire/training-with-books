# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bd

n, k = map(int, input().split())

x = 0
for a in range(1, n + 1):
    for b in range(max(a - (k - 1), 1), min(a + k, n + 1)):
        for c in range(max(a - (k - 1), 1), min(a + k, n + 1)):
            if abs(b - c) < k:
                x += 1
print(n ** 3 - x)