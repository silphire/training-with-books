# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_ac

n = int(input())
aa = list(map(int, input().split()))

dp = [0] * n
dp[0] = aa[0]
dp[1] = max(aa[0], aa[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + aa[i])
print(dp[n - 1])
