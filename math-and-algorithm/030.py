# https://atcoder.jp/contests/math-and-algorithm/tasks/dp_d

n, w = map(int, input().split())
ww = [0] * n
vv = [0] * n
dp = [[0] * (w + 1) for _ in range(n)]

for i in range(n):
    ww[i], vv[i] = map(int, input().split())

for i in range(n):
    for j in range(w + 1):
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j - ww[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - ww[i]] + vv[i])
        else:
            if j - ww[i] >= 0:
                dp[i][j] = vv[i]
print(max(dp[-1]))