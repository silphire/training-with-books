# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ab

n = int(input())
dp = [0] * (n + 10)
dp[0] = 1
for i in range(n):
    dp[i + 2] += dp[i]
    dp[i + 1] += dp[i]
print(dp[n])