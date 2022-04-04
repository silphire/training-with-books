# https://atcoder.jp/contests/math-and-algorithm/tasks/abc204_d

import math

n = int(input())
tt = list(map(int, input().split()))
sm = sum(tt)
s = math.ceil(sm / 2)
dp = [[False] * (10 ** 5 + 10 ** 3 + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(n):
    t = tt[i]
    for x in range(10 ** 5 + 1):
        dp[i + 1][x + t] |= dp[i][x]
        dp[i + 1][x] |= dp[i][x]

for x in range(s, sm + 1):
    if dp[n][x]:
        print(x)
        exit()