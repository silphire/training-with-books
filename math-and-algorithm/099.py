from collections import defaultdict
import sys
sys.setrecursionlimit(100001)
n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

dp = [0] * n

def dfs(x, p):
    dp[x] = 1
    for y in g[x]:
        if y == p:
            continue
        dfs(y, x)
        dp[x] += dp[y]

dfs(0, -1)
ans = 0
for i in range(1, n):
    ans += dp[i] * (n - dp[i])
print(ans)