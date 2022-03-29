# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bs

n = int(input())

ans = float('inf')
for x in range(1, int(n ** 0.5) + 2):
    if n % x == 0:
        ans = min(ans, (x + n // x) * 2)
print(ans)