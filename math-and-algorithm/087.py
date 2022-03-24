# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bq

MOD = 10 ** 9 + 7
n = int(input())
# {n(n+1)/2}^2
# n^2(n+1)^2 / 4
# n^2(n^2 + 2n + 1) / 4
# n^4 + 2n^3 + n^2 / 4
ans = pow(n, 4, MOD) + 2 * pow(n, 3, MOD) + pow(n, 2, MOD)
ans %= MOD
ans *= pow(4, MOD - 2, MOD)
ans %= MOD
print(ans)