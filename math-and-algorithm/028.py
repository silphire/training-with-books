# https://atcoder.jp/contests/math-and-algorithm/tasks/dp_a

n = int(input())
hh = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0
for i in range(n):
    if i + 1 < n:
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(hh[i + 1] - hh[i]))
    if i + 2 < n:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(hh[i + 2] - hh[i]))
print(dp[n - 1])